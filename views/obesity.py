import streamlit as st

st.title("Obesity")

st.title("Hitung Indeks Massa Tubuh (BMI)")

# Input data pengguna
st.header("Masukkan Data Anda")

# Menggunakan kolom untuk input
col1, col2 = st.columns(2)

with col1:
    umur = st.number_input("Umur (tahun)", min_value=0, format="%d")
    tinggi = st.number_input("Tinggi Badan (cm)", min_value=0.0, format="%.2f")

with col2:
    berat = st.number_input("Berat Badan (kg)", min_value=0.0, format="%.2f")
    jenis_kelamin = st.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])

# Tombol untuk menghitung BMI
if st.button("Hitung BMI"):
    if berat > 0 and tinggi > 0:
        # Fungsi untuk menghitung BMI
        tinggi_m = tinggi / 100  # Konversi tinggi dari cm ke m
        bmi = berat / (tinggi_m ** 2)

        # Menampilkan hasil
        st.subheader("Hasil")
        st.write(f"Indeks Massa Tubuh (BMI) Anda adalah: **{bmi:.2f}**")

        # Kategori BMI
        if bmi < 18.5:
            kategori = "Kekurangan berat badan"
        elif 18.5 <= bmi < 24.9:
            kategori = "Normal"
        elif 25 <= bmi < 29.9:
            kategori = "Kelebihan berat badan"
        else:
            kategori = "Obesitas"

        st.write(f"Kategori BMI Anda: **{kategori}**")
    else:
        st.warning("Silakan masukkan berat dan tinggi yang valid.")

# Fungsi untuk menghitung kalori harian
