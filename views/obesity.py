import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set the title of the app
st.title("Obesitas")

# Default state if first time running
if 'page' not in st.session_state:
    st.session_state.page = 'info'  # Default to showing information about obesity

# Create a horizontal layout for buttons with minimal spacing
col1, col2 = st.columns(2)  # Create two columns

with col1:
    if st.button("Informasi tentang Obesitas", key="info_button"):
        st.session_state.page = "info"  # Change state to obesity information page

with col2:
    if st.button("Hitung BMI", key="bmi_button"):
        st.session_state.page = "bmi"  # Change state to BMI calculation page

# Render the corresponding content based on the state
if st.session_state.page == "bmi":
    st.header("Hitung Indeks Massa Tubuh (BMI)")

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
    if st.button("Hitung BMI", key="calculate_bmi"):
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
                st.warning("Anda mengalami kekurangan berat badan, disarankan untuk berkonsultasi dengan profesional kesehatan.")
            elif 18.5 <= bmi < 24.9:
                kategori = "Normal"
            elif 25 <= bmi < 29.9:
                kategori = "Kelebihan berat badan"
                st.warning("Anda memiliki kelebihan berat badan, disarankan untuk berkonsultasi dengan profesional kesehatan.")
            else:
                kategori = "Obesitas"
                st.warning("Anda memiliki obesitas, disarankan untuk berkonsultasi dengan profesional kesehatan.")

            st.write(f"Kategori BMI Anda: **{kategori}**")

            # Recommendations for all categories
            if kategori == "Kekurangan berat badan":
                st.subheader("Rekomendasi")
                st.write("""
                    1. **Tingkatkan Asupan Kalori**: Cobalah untuk mengonsumsi lebih banyak makanan kaya kalori 
                    seperti kacang-kacangan, avokad, dan produk susu.
                    2. **Makan Lebih Sering**: Tambahkan makanan ringan antara waktu makan utama untuk meningkatkan asupan.
                    3. **Latihan Angkat Beban**: Latihan termasuk angkat beban dapat membantu menambah massa otot.
                    4. **Konsultasi dengan Profesional**: Bicaralah dengan dokter atau ahli gizi untuk mendapatkan bantuan yang tepat.
                """)
            elif kategori in ["Kelebihan berat badan", "Obesitas"]:
                st.subheader("Rekomendasi")
                st.write("""
                    1. **Perbaiki Pola Makan**: Cobalah untuk mengonsumsi lebih banyak buah, sayur, dan biji-bijian. 
                    2. **Olahraga Secara Teratur**: Targetkan setidaknya 150 menit aktivitas sedang setiap minggu.
                    3. **Konsultasi ```python
                    dengan Profesional**: Bicaralah dengan dokter atau ahli gizi untuk mendapatkan bantuan yang tepat.
                    4. **Pantau Berat Badan Anda**: Lakukan pemeriksaan berat badan secara berkala untuk memantau kemajuan.
                """)
        else:
            st.warning("Silakan masukkan berat dan tinggi yang valid.")

elif st.session_state.page == "info":
    st.header("Apa itu Obesitas?")
    st.write("""
        Obesitas adalah kondisi medis yang ditandai dengan kelebihan lemak tubuh. 
        Ini dapat meningkatkan risiko berbagai penyakit, termasuk diabetes, penyakit jantung, dan beberapa jenis kanker.
    """)
    st.image("obesitas.png", use_container_width=True)  # Ganti dengan URL gambar yang sesuai

    # Indeks Massa Tubuh (BMI)
    st.subheader("Indeks Massa Tubuh (BMI) 📏")
    st.write("""
        BMI adalah ukuran yang digunakan untuk menilai berat badan seseorang berdasarkan tinggi badan. 
        Ini dihitung dengan rumus:

        $$ 
        BMI = \frac{berat \, (kg)}{(tinggi \, (m))^2} 
        $$

        *Kategori BMI:*
        - *Kekurangan berat badan*: BMI < 18.5
        - *Normal*: 18.5 ≤ BMI < 24.9
        - *Kelebihan berat badan*: 25 ≤ BMI < 29.9
        - *Obesitas*: BMI ≥ 30
    """)

    # Pentingnya Memantau BMI
    st.subheader("Mengapa Penting untuk Memantau BMI? 🩺")
    st.write("""
        Memantau BMI Anda dapat membantu Anda memahami status kesehatan Anda dan mengambil langkah-langkah yang diperlukan untuk 
        menjaga berat badan yang sehat. Jika Anda memiliki pertanyaan atau kekhawatiran tentang berat badan Anda, 
        disarankan untuk berkonsultasi dengan profesional kesehatan.
    """)

    # Faktor Penyebab Obesitas
    st.subheader("Faktor Penyebab Obesitas 🔍")
    st.write("""
        Beberapa faktor yang dapat menyebabkan obesitas meliputi:
        - *Genetik*: Riwayat keluarga dapat mempengaruhi kecenderungan seseorang untuk mengalami obesitas.
        - *Gaya Hidup*: Pola makan yang tidak sehat dan kurangnya aktivitas fisik dapat berkontribusi pada obesitas.
        - *Lingkungan*: Akses terbatas ke makanan sehat dan fasilitas olahraga dapat meningkatkan risiko obesitas.
        - *Faktor Psikologis*: Stres, depresi, dan masalah emosional lainnya dapat memicu kebiasaan makan yang tidak sehat.
    """)

    # Dampak Kesehatan dari Obesitas
    st.subheader("Dampak Kesehatan dari Obesitas")
    st.write("""
        Obesitas dapat menyebabkan berbagai masalah kesehatan, termasuk:
        - Penyakit jantung
        - Diabetes tipe 2
        - Hipertensi
        - Masalah tidur (sleep apnea)
        - Beberapa jenis kanker
    """)

    st.markdown("---")

    # Data prevalensi obesitas
    data = {
        'Tahun': [2007, 2013, 2016, 2018],
        'Perkotaan': [23.8, 30.7, 38.5, 39.7],
        'Perdesaan': [15.3, 21.5, 28.5, 30.0],
        'Perkotaan+Perdesaan': [19.1, 26.3, 33.5, 35.4]
    }

    df = pd.DataFrame(data)

    # Penjelasan tentang data
    st.subheader("Data Prevalensi Obesitas")
    st.write("""
        Berikut adalah data prevalensi obesitas pada penduduk berusia di atas 18 tahun berdasarkan klasifikasi 
        perkotaan dan perdesaan dari tahun 2007 hingga 2018. Data ini menunjukkan persentase populasi yang mengalami 
        obesitas di masing-masing kategori. 
        - *Perkotaan*: Persentase obesitas di daerah perkotaan.
        - *Perdesaan*: Persentase obesitas di daerah perdesaan.
        - *Perkotaan+Perdesaan*: Rata-rata prevalensi obesitas di seluruh populasi yang mencakup baik daerah perkotaan 
            maupun perdesaan.
    """)

    # Membuat visualisasi
    plt.figure(figsize=(10, 5))
    plt.plot(df['Tahun'], df['Perkotaan'], marker='o', label='Perkotaan', color='blue', linewidth=2)
    plt.plot(df['Tahun'], df['Perdesaan'], marker='o', label='Perdesaan', color='green', linewidth=2)
    plt.plot(df['Tahun'], df['Perkotaan+Perdesaan'], marker='o', label='Perkotaan+Perdesaan', color='orange', linewidth=2)

    plt.title('📊 Prevalensi Obesitas pada Penduduk Umur > 18 Tahun (2007-2018)', fontsize=16)
    plt.xlabel('Tahun', fontsize=12)
    plt.ylabel('Prevalensi Obesitas (%)', fontsize=12)
    plt.xticks(df['Tahun'])
    plt.legend()
    plt.grid()
    st.pyplot(plt)

    # Kesimpulan dari data
    st.subheader("Kesimpulan dari Data")
    st.write("""
        Dari data yang ditampilkan, kita dapat melihat tren peningkatan prevalensi obesitas di daerah perkotaan 
        dan perdesaan dari tahun 2007 hingga 2018. 
        - *Perkotaan* menunjukkan peningkatan yang lebih signifikan dibandingkan dengan *perdesaan*, 
            dengan prevalensi obesitas mencapai hampir 40% pada tahun 2018.
        - *Perdesaan* juga menunjukkan peningkatan, tetapi dengan angka yang lebih rendah, mencapai sekitar 30%.
        - Rata-rata prevalensi obesitas di seluruh populasi (Perkotaan+Perdesaan) juga menunjukkan tren yang meningkat, 
            dari 19.1% pada tahun 2007 menjadi 35.4% pada tahun 2018.

        Hal ini menunjukkan bahwa obesitas menjadi masalah kesehatan yang semakin serius di masyarakat, 
        baik di daerah perkotaan maupun perdesaan. Penting untuk meningkatkan kesadaran dan upaya pencegahan 
        terhadap obesitas melalui pendidikan kesehatan, akses ke makanan sehat, dan promosi gaya hidup aktif.
    """)
