import streamlit as st
import pandas as pd

# 1. Konfigurasi Halaman Web
st.set_page_config(
    page_title="Dashboard IPG Jawa Tengah", page_icon="📊", layout="wide"
)


# 2. Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("data/processed/ipg_jateng_clean.csv")
    return df


df = load_data()

# 3. Judul Dashboard
st.title("📊 Dashboard Indeks Pembangunan Gender (IPG)")
st.markdown("**Jawa Tengah Tahun 2025** | Fokus: Kabupaten Batang")

# 4. Sidebar untuk Filter
st.sidebar.header("Pengaturan Tampilan")
pilihan_grafik = st.sidebar.selectbox(
    "Pilih Analisis:", ["Peringkat IPG (Total)", "Selisih IPM (Laki-laki vs Perempuan)"]
)

# 5. Logika Grafik
if pilihan_grafik == "Peringkat IPG (Total)":
    st.subheader("Peringkat IPG Kabupaten/Kota di Jawa Tengah")
    st.write(
        "Grafik ini menunjukkan posisi Kabupaten Batang dibandingkan daerah lain. Semakin tinggi nilainya, semakin setara pembangunan gender di daerah tersebut."
    )

    # Siapkan data: Urutkan dari terendah ke tertinggi (agar di Streamlit yang tertinggi ada di atas)
    df_sorted = df.sort_values(by="IPG", ascending=True)

    # Set index agar nama kabupaten jadi sumbu Y
    df_chart = df_sorted.set_index("Kabupaten/Kota")["IPG"]

    # Tampilkan dengan Streamlit Native (Biru default)
    st.bar_chart(df_chart, color="#3498db", height=600)

else:
    st.subheader("Selisih Nilai IPM (Laki-laki vs Perempuan)")
    st.write(
        "Nilai positif besar menunjukkan ketimpangan (perempuan tertinggal). Nilai negatif menunjukkan IPM perempuan lebih tinggi dari laki-laki."
    )

    # Hitung selisih
    df["Selisih_IPM"] = df["IPM Laki-laki"] - df["IPM Perempuan"]
    df_gap = df.sort_values(by="Selisih_IPM", ascending=True)

    df_chart_gap = df_gap.set_index("Kabupaten/Kota")["Selisih_IPM"]

    # Tampilkan dengan Streamlit Native (Hijau)
    st.bar_chart(df_chart_gap, color="#2ecc71", height=600)

# 6. Menampilkan Data Mentah
with st.expander("Lihat Tabel Data Lengkap"):
    st.dataframe(df)

# 7. Menambahkan Insight / Kesimpulan
st.divider()
st.subheader("💡 Insight Menarik")

col1, col2 = st.columns(2)

with col1:
    st.info(
        "**Fenomena Menarik: Klaten & Karanganyar**\n\n"
        "Meskipun IPM total tinggi, kedua daerah ini memiliki nilai selisih **negatif** (IPM Perempuan > Laki-laki). "
        "Ini menunjukkan keberhasilan pemberdayaan perempuan di sektor formal (pendidikan & kesehatan)."
    )

with col2:
    st.warning(
        "**Tantangan: Grobogan & Cilacap**\n\n"
        "Kedua daerah ini memiliki selisih IPM positif paling besar (10 poin lebih). "
        "Artinya, masih ada ketimpangan yang signifikan di mana perempuan tertinggal jauh "
        "dibandingkan laki-laki."
    )

st.caption(
    "Sumber Data: BPS Kabupaten Batang (Publikasi IPG 2025). Diolah menggunakan Python & Streamlit."
)
