import pandas as pd

class ModelKebijakanEkonomi:
    def predict(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()

        df["Provinsi"] = df["Provinsi"].str.upper().str.strip()

        df["Kategori Ekonomi"] = pd.qcut(
            df["Pertumbuhan PDRB"],
            q=3,
            labels=["RENDAH", "SEDANG", "TINGGI"]
        )

        df["Keputusan Pemerintah"] = df["Kategori Ekonomi"].map({
            "RENDAH": "STIMULUS EKONOMI & UMKM",
            "SEDANG": "PENGUATAN INDUSTRI DAERAH",
            "TINGGI": "EKSPANSI & INVESTASI"
        })

        return df
