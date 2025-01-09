import streamlit as st

# Judul Aplikasi
st.markdown("<h2 style='text-align: center; color: #00000;'>Selamat Datang di Aplikasi Kesehatan</h2>", unsafe_allow_html=True)

# Deskripsi Aplikasi
st.write("""
    Aplikasi ini dirancang untuk membantu Anda memahami dan mengelola kesehatan Anda dengan lebih baik. 
    Kami menyediakan berbagai fitur, termasuk:
""")
st.markdown("""
    <ul style='font-size: 18px;'>
        <li><strong>Kalkulator BMI</strong>: Menghitung Indeks Massa Tubuh Anda untuk menilai status berat badan.</li>
        <li><strong>Kalkulator Kalori Harian</strong>: Menghitung kebutuhan kalori harian berdasarkan berat badan, tinggi badan, usia, dan tingkat aktivitas.</li>
        <li><strong>Prediksi Penyakit Kulit</strong>: Menggunakan teknologi machine learning untuk mendiagnosis dan memprediksi penyakit kulit berdasarkan gambar.</li>
    </ul>
""", unsafe_allow_html=True)

# Informasi Tambahan
st.subheader("Mengapa Penting untuk Memantau Kesehatan Anda?")
st.write("""
    Memantau kesehatan Anda adalah langkah penting untuk mencegah penyakit dan menjaga kualitas hidup. 
    Dengan menggunakan aplikasi ini, Anda dapat:
""")
st.markdown("""
    <ul style='font-size: 18px;'>
        <li>Memahami status kesehatan Anda melalui BMI dan kalori harian.</li>
        <li>Mendeteksi potensi masalah kesehatan lebih awal dengan prediksi penyakit kulit.</li>
        <li>Mengambil langkah-langkah yang diperlukan untuk menjaga kesehatan Anda.</li>
    </ul>
""", unsafe_allow_html=True)

# Penutup
st.write("<h3>Mari kita jaga kesehatan bersama!</h3>", unsafe_allow_html=True)

# Footer

# HTML untuk footer yang lebih menarik
footer_html = """
<div style="text-align: center; padding: 20px; background-color: #f8f9fa; color: black; border-top: 2px solid #000000;">
    <h4 style="margin-bottom: 10px;">Follow Us on Instagram</h4>
    <a href="https://www.instagram.com/faishalah97?igsh=azA0dGFjM3lkd2Jm" target="_blank" style="color: blue; text-decoration: none; margin: 0 15px; font-size: 18px; transition: color 0.3s;">
        <svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width="24" height="24" viewBox="0 0 50 50" style="vertical-align: middle; margin-right: 5px;">
            <path d="M 16 3 C 8.8324839 3 3 8.8324839 3 16 L 3 34 C 3 41.167516 8.8324839 47 16 47 L 34 47 C 41.167516 47 47 41.167516 47 34 L 47 16 C 47 8.8324839 41.167516 3 34 3 L 16 3 z M 16 5 L 34 5 C 40.086484 5 45 9.9135161 45 16 L 45 34 C 45 40.086484 40.086484 45 34 45 L 16 45 C 9.9135161 45 5 40.086484 5 34 L 5 16 C 5 9.9135161 9.9135161 5 16 5 z M 37 11 A 2 2 0 0 0 35 13 A 2 2 0 0 0 37 15 A 2 2 0 0 0 39 13 A 2 2 0 0 0 37 11 z M 25 14 C 18.936712 14 14 18.936712 14 25 C 14 31.063288 18.936712 36 25 36 C 31.063288 36 36 31.063288 36 25 C 36 18.936712 31.063288 14 25 14 z M 25 16 C 29.982407 16 34 20.017593 34 25 C 34 29.982407 29.982407 34 25 34 C 20.017593 34 16 29.982407 16 25 C 16 20.017593 20.017593 16 25 16 z"></path>
        </svg>
        faishalah97
    </a>
    <a href="https://www.instagram.com/haydarfahri" target="_blank" style="color: blue; text-decoration: none; margin: 0 15px; font-size: 18px; transition: color 0.3s;">
        <svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width="24" height="24" viewBox="0 0 50 50" style="vertical-align: middle; margin-right: 5px;">
            <path d="M 16 3 C 8.8324839 3 3 8.8324839 3 16 L 3 34 C 3 41.167516 8.8324839 47 16 47 L 34 47 C 41.167516 47 47 41.167516 47 34 L 47 16 C 47 8.8324839 41.167516 3 34 3 L 16 3 z M 16 5 L 34 5 C 40.086484 5 45 9.9135161 45 16 L 45 34 C 45 40.086484 40.086484 45 34 45 L 16 45 C 9.9135161 45 5 40.086484 5 34 L 5 16 C 5 9.9135161 9.9135161 5 16 5 z M 37 11 A 2 2 0 0 0 35 13 A 2 2 0 0 0 37 15 A 2 2 0 0 0 39 13 A 2 2 0 0 0 37 11 z M 25 14 C 18.936712 14 14 18.936712 14 25 C 14 31.063288 18.936712 36 25 36 C 31.063288 36 36 31.063288 36 25 C 36 18.936712 31.063288 14 25 14 z M 25 16 C 29.982407 16 34 20.017593 34 25 C 34 29.982407 29.982407 34 25 34 C 20.017593 34 16 29.982407 16 25 C 16 20.017593 20.017593 16 25 16 z"></path>
        </svg>
        haydarfahri
    </a>
    <a href="https://www.instagram.com/mumtazfn" target="_blank" style="color: blue; text-decoration: none; margin: 0 15px; font-size: 18px; transition: color 0.3s;">
        <svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width="24" height="24" viewBox="0 0 50 50" style="vertical-align: middle; margin-right: 5px;">
            <path d="M 16 3 C 8.8324839 3 3 8.8324839 3 16 L 3 34 C 3 41.167516 8.8324839 47 16 47 L 34 47 C 41.167516 47 47 41.167516 47 34 L 47 16 C 47 8.8324839 41.167516 3 34 3 L 16 3 z M 16 5 L 34 5 C 40.086484 5 45 9.9135161 45 16 L 45 34 C 45 40.086484 40.086484 45 34 45 L 16 45 C 9.9135161 45 5 40.086484 5 34 L 5 16 C 5 9.9135161 9.9135161 5 16 5 z M 37 11 A 2 2 0 0 0 35 13 A 2 2 0 0 0 37 15 A 2 2 0 0 0 39 13 A 2 2 0 0 0 37 11 z M 25 14 C 18.936712 14 14 18.936712 14 25 C 14 31.063288 18.936712 36 25 36 C 31.063288 36 36 31.063288 36 25 C 36 18.936712 31.063288 14 25 14 z M 25 16 C 29.982407 16 34 20.017593 34 25 C 34 29.982407 29.982407 34 25 34 C 20.017593 34 16 29.982407 16 25 C 16 20.017593 20.017593 16 25 16 z"></path>
        </svg>
        mumtazfn
    </a>
    <p style="margin-top: 10px; font-size: 14px;">&copy; 2023 Aplikasi Kesehatan. All rights reserved.</p>
</div>
"""

# Menampilkan footer
st.markdown(footer_html, unsafe_allow_html=True)
