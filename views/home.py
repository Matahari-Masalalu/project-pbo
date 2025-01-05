import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Home")


st.title("🌟 Selamat Datang di Kalkulator BMI 🌟")
st.image("https://example.com/your-image.jpg", use_column_width=True)  # Ganti dengan URL gambar yang sesuai

# Informasi tentang Obesitas
st.header("Apa itu Obesitas?")
st.write("""
    Obesitas adalah kondisi medis yang ditandai dengan kelebihan lemak tubuh. 
    Ini dapat meningkatkan risiko berbagai penyakit, termasuk diabetes, penyakit jantung, dan beberapa jenis kanker.
""")
st.image("https://example.com/obesity-image.jpg", use_column_width=True)  # Ganti dengan URL gambar yang sesuai

# Indeks Massa Tubuh (BMI)
st.subheader("Indeks Massa Tubuh (BMI) 📏")
st.write("""
    BMI adalah ukuran yang digunakan untuk menilai berat badan seseorang berdasarkan tinggi badan. 
    Ini dihitung dengan rumus:
    
    \[
    BMI = \frac{berat \, (kg)}{(tinggi \, (m))^2}
    \]

    **Kategori BMI:**
    - **Kekurangan berat badan**: BMI < 18.5
    - **Normal**: 18.5 ≤ BMI < 24.9
    - **Kelebihan berat badan**: 25 ≤ BMI < 29.9
    - **Obesitas**: BMI ≥ 30
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
    - **Genetik**: Riwayat keluarga dapat mempengaruhi kecenderungan seseorang untuk mengalami obesitas.
    - **Gaya Hidup**: Pola makan yang tidak sehat dan kurangnya aktivitas fisik dapat berkontribusi pada obesitas.
    - **Lingkungan**: Akses terbatas ke makanan sehat dan fasilitas olahraga dapat meningkatkan risiko obesitas.
    - **Faktor Psikologis**: Stres, depresi, dan masalah emosional lainnya dapat memicu kebiasaan makan yang tidak sehat.
""")

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
    - **Perkotaan**: Persentase obesitas di daerah perkotaan.
    - **Perdesaan**: Persentase obesitas di daerah perdesaan.
    - **Perkotaan+Perdesaan**: Rata-rata prevalensi obesitas di seluruh populasi yang mencakup baik daerah perkotaan 
        maupun perdesaan.
```python
""")

# Membuat visualisasi
plt.figure(figsize=(10, 5))
plt.plot(df['Tahun'], df['Perkotaan'], marker='o', label='Perkotaan', color='blue', linewidth=2)
plt.plot(df['Tahun'], df['Perdesaan'], marker ='o', label='Perdesaan', color='green', linewidth=2)
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
    - **Perkotaan** menunjukkan peningkatan yang lebih signifikan dibandingkan dengan **perdesaan**, 
        dengan prevalensi obesitas mencapai hampir 40% pada tahun 2018.
    - **Perdesaan** juga menunjukkan peningkatan, tetapi dengan angka yang lebih rendah, mencapai sekitar 30%.
    - Rata-rata prevalensi obesitas di seluruh populasi (Perkotaan+Perdesaan) juga menunjukkan tren yang meningkat, 
        dari 19.1% pada tahun 2007 menjadi 35.4% pada tahun 2018.
    
    Hal ini menunjukkan bahwa obesitas menjadi masalah kesehatan yang semakin serius di masyarakat, 
    baik di daerah perkotaan maupun perdesaan. Penting untuk meningkatkan kesadaran dan upaya pencegahan 
    terhadap obesitas melalui pendidikan kesehatan, akses ke makanan sehat, dan promosi gaya hidup aktif.
""")

st.write("Silakan pilih menu di samping untuk mulai menghitung BMI Anda. Mari kita jaga kesehatan bersama!")