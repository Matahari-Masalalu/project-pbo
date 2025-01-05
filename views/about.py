import streamlit as st

st.title("Tentang Aplikasi")
st.write("""
    Aplikasi ini dibuat untuk membantu Anda menghitung Indeks Massa Tubuh (BMI) dan kebutuhan kalori harian Anda.
    BMI adalah ukuran yang digunakan untuk menilai berat badan seseorang berdasarkan tinggi badan.
    
    **Catatan:** Hasil ini hanya untuk informasi dan tidak menggantikan saran medis profesional.
""")

st.header("Tentang Penulis")

# Informasi Penulis
penulis = [
    {
        "nama": "Fasihal Anwar Hasyim",
        "nim": "32602300021",
        "gambar": "obesitas.png"  # Ganti dengan URL gambar profil yang sesuai
    },
    {
        "nama": "Haydar Fahri Alaudin",
        "nim": "32602300010",
        "gambar": "obesitas.png"  # Ganti dengan URL gambar profil yang sesuai
    },
    {
        "nama": "Mumtaz Fikri Nasrullan",
        "nim": "32602300002",
        "gambar": "obesitas.png"  # Ganti dengan URL gambar profil yang sesuai
    }
]

for penulis_info in penulis:
    st.subheader(penulis_info["nama"])
    st.write(f"NIM: {penulis_info['nim']}")
    st.image(penulis_info["gambar"], width=150)  # Menampilkan gambar profil
