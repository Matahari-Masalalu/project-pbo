import streamlit as st

st.title("Kalkulator Kebutuhan Kalori Harian")

st.header("Masukkan Data Anda")

# Input data pengguna
umur = st.number_input("Umur (tahun)", min_value=0, format="%d")
tinggi = st.number_input("Tinggi Badan (cm)", min_value=0.0, format="%.2f")
berat = st.number_input("Berat Badan (kg)", min_value=0.0
, format="%.2f")
jenis_kelamin = st.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])
tingkat_aktivitas = st.selectbox("Tingkat Aktivitas", ["Sedentari (tidak aktif)", "Ringan (olahraga ringan 1-3 hari/minggu)", 
                                                        "Sedang (olahraga sedang 3-5 hari/minggu)", "Tinggi (olahraga berat 6-7 hari/minggu)"])

# Tombol untuk menghitung kalori harian
if st.button("Hitung Kebutuhan Kalori Harian"):
    if berat > 0 and tinggi > 0 and umur > 0:
        # Menghitung BMR (Basal Metabolic Rate)
        if jenis_kelamin == "Laki-laki":
            bmr = 10 * berat + 6.25 * tinggi - 5 * umur + 5
        else:
            bmr = 10 * berat + 6.25 * tinggi - 5 * umur - 161

        # Menghitung Total Kalori Harian berdasarkan tingkat aktivitas
        if tingkat_aktivitas == "Sedentari (tidak aktif)":
            kalori_harian = bmr * 1.2
        elif tingkat_aktivitas == "Ringan (olahraga ringan 1-3 hari/minggu)":
            kalori_harian = bmr * 1.375
        elif tingkat_aktivitas == "Sedang (olahraga sedang 3-5 hari/minggu)":
            kalori_harian = bmr * 1.55
        else:  # Tinggi (olahraga berat 6-7 hari/minggu)
            kalori_harian = bmr * 1.725

        # Menampilkan hasil
        st.subheader("Hasil")
        st.write(f"Kebutuhan kalori harian Anda adalah: **{kalori_harian:.2f} kalori**")
    else:
        st.warning("Silakan masukkan data yang valid.")
