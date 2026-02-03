import os
import pandas as pd
import geopandas as gpd
import folium

from django.shortcuts import render
from model.model_kebijakan_ekonomi import ModelKebijakanEkonomi

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model = ModelKebijakanEkonomi()

# =========================
# LOAD GEOJSON
# =========================
GEOJSON_PATH = os.path.join(
    BASE_DIR, "data", "gabungan_38_wilayah_batas_provinsi.geojson"
)

gdf = gpd.read_file(GEOJSON_PATH)
gdf["name"] = gdf["name"].str.upper().str.strip()

WARNA = {
    "RENDAH": "#d73027",
    "SEDANG": "#fee08b",
    "TINGGI": "#1a9850"
}

# =========================
# FUNGSI MAP
# =========================
def buat_map(data=None):
    peta = folium.Map(
        location=[-2.5, 118],
        zoom_start=5,
        tiles="cartodbpositron"
    )

    if data is not None:
        gabungan = gdf.merge(
            data,
            left_on="name",
            right_on="Provinsi",
            how="left"
        )

        folium.GeoJson(
            gabungan,
            style_function=lambda f: {
                "fillColor": WARNA.get(
                    f["properties"].get("Kategori Ekonomi"),
                    "#cccccc"
                ),
                "color": "black",
                "weight": 1,
                "fillOpacity": 0.8
            },

            # 🔍 HOVER (info cepat)
            tooltip=folium.GeoJsonTooltip(
                fields=[
                    "name",
                    "Pertumbuhan PDRB",
                    "Kategori Ekonomi"
                ],
                aliases=[
                    "Provinsi:",
                    "Pertumbuhan PDRB (%):",
                    "Kategori Ekonomi:"
                ],
                localize=True
            ),

            # 🖱️ KLIK (keputusan kebijakan)
            popup=folium.GeoJsonPopup(
                fields=["Keputusan Pemerintah"],
                aliases=["Rekomendasi Kebijakan Ekonomi:"],
                localize=True
            )
        ).add_to(peta)

    return peta._repr_html_()

# =========================
# VIEW UTAMA
# =========================
def index(request):
    map_html = buat_map()

    if request.method == "POST" and request.FILES.get("file"):
        df = pd.read_excel(request.FILES["file"])
        df = df.iloc[:, [0, 1]]
        df.columns = ["Provinsi", "Pertumbuhan PDRB"]

        df["Provinsi"] = df["Provinsi"].str.upper().str.strip()
        df["Pertumbuhan PDRB"] = pd.to_numeric(
            df["Pertumbuhan PDRB"], errors="coerce"
        ).fillna(0)

        hasil = model.predict(df)
        map_html = buat_map(hasil)

    return render(request, "index.html", {"map": map_html})
