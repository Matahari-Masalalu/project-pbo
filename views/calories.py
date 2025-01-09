import streamlit as st

class User:
    def __init__(self, age, height, weight, gender, activity_level):
        self.age = age
        self.height = height
        self.weight = weight
        self.gender = gender
        self.activity_level = activity_level

class CalorieCalculator:
    def __init__(self, user):
        self.user = user

    def calculate_bmr(self):
        if self.user.gender == "Laki-laki":
            return 10 * self.user.weight + 6.25 * self.user.height - 5 * self.user.age + 5
        else:
            return 10 * self.user.weight + 6.25 * self.user.height - 5 * self.user.age - 161

    def calculate_daily_calories(self):
        bmr = self.calculate_bmr()
        activity_multiplier = {
            "Sedentari (tidak aktif)": 1.2,
            "Ringan (olahraga ringan 1-3 hari/minggu)": 1.375,
            "Sedang (olahraga sedang 3-5 hari/minggu)": 1.55,
            "Tinggi (olahraga berat 6-7 hari/minggu)": 1.725,
        }
        return bmr * activity_multiplier[self.user.activity_level]

# Set the title of the app
st.title("Kalkulator Kebutuhan Kalori Harian dan Informasi Kesehatan")

# Default state if first time running
if 'page' not in st.session_state:
    st.session_state.page = 'info'  # Default to information page

# Create layout for buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("Informasi tentang Kebutuhan Kalori", key="info_button"):
        st.session_state.page = "info"  # Change state to information page

with col2:
    if st.button("Hitung Kebutuhan Kalori", key="calorie_button"):
        st.session_state.page = "calorie"  # Change state to calorie calculator page

# Render the corresponding content based on the state
if st.session_state.page == "calorie":
    st.header("Hitung Kebutuhan Kalori Harian")

    # Input data pengguna
    st.header("Masukkan Data Anda")

    # Input fields using columns for better layout
    age = st.number_input("Umur (tahun)", min_value=0, format="%d")
    height = st.number_input("Tinggi Badan (cm)", min_value=0.0, format="%.2f")
    weight = st.number_input("Berat Badan (kg)", min_value=0.0, format="%.2f")
    gender = st.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])
    activity_level = st.selectbox("Tingkat Aktivitas", ["Sedentari (tidak aktif)", 
                                                          "Ringan (olahraga ringan 1-3 hari/minggu)", 
                                                          "Sedang (olahraga sedang 3-5 hari/minggu)", 
                                                          "Tinggi (olahraga berat 6-7 hari/minggu)"])

    # Button to calculate daily calories
    if st.button("Hitung Kebutuhan Kalori Harian", key="calculate_calories"):
        if weight > 0 and height > 0 and age > 0:
            user = User(age, height, weight, gender, activity_level)
            calculator = CalorieCalculator(user)
            daily_calories = calculator.calculate_daily_calories()

            # Display results
            st.subheader("Hasil")
            st.write(f"Kebutuhan kalori harian Anda adalah: **{daily_calories:.2f} kalori**")
        else:
            st.warning("Silakan masukkan data yang valid.")

elif st.session_state.page == "info":
    st.header("Informasi tentang Kebutuhan Kalori Harian")
    st.write("""
        Kebutuhan kalori harian bervariasi tergantung pada beberapa faktor termasuk umur, jenis kelamin, 
        tinggi badan, berat badan, dan tingkat aktivitas. 
        Penting untuk mengetahui kebutuhan kalori agar Anda dapat menjaga berat badan yang sehat dan 
        menghindari masalah kesehatan yang terkait dengan asupan kalori yang tidak seimbang.
        
        Berikut adalah rumus untuk menghitung BMR (Basal Metabolic Rate):
        
        $$
        BMR = 10 \times berat \, (kg) + 6.25 \times tinggi \, (cm) - 5 \times umur \, (tahun) + 5 \, (Laki-laki) \, atau \, -161 \, (Perempuan)
        $$
        
        Setelah BMR dihitung, kali dengan faktor aktivitas untuk mendapatkan kebutuhan kalori harian:
        - Sedentari (tidak aktif): BMR × 1.2
        - Ringan (olahraga ringan/satu kali seminggu): BMR × 1.375
        - Sedang (olahraga sedang/3-5 kali seminggu): BMR × 1.55
        - Aktif (olahraga berat/6-7 kali seminggu): BMR × 1.725
    """)

    st.subheader("Mengapa Penting untuk Menghitung Kebutuhan Kalori?")
    st.write("""
        Menghitung kebutuhan kalori dapat membantu Anda menentukan asupan kalori yang tepat untuk mencapai tujuan 
        kesehatan Anda, baik itu untuk menurunkan berat badan, mempertahankan berat badan, atau menambah berat badan. 
        Dengan pemahaman yang baik tentang kebutuhan kalori Anda, Anda dapat membuat pilihan makanan yang lebih sehat 
        dan mengikuti pola hidup yang lebih aktif.
    """)
