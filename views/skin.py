import streamlit as st
import numpy as np
from PIL import Image, ImageOps
import tensorflow as tf

# Load labels
def load_labels(label_path):
    with open(label_path, 'r') as file:
        labels = [line.strip().split(' ', 1)[1] for line in file.readlines()]
    return labels

# Load model
@st.cache_resource
def load_model(model_path):
    return tf.keras.models.load_model(model_path)

# Classify image
def classify_image(image, model, class_names, img_size=(450, 450)):
    image = ImageOps.fit(image, img_size, Image.Resampling.LANCZOS)  # Resize image
    image_array = np.asarray(image) / 255.0  # Normalize image
    data = np.expand_dims(image_array, axis=0)  # Expand dimensions for the model input

    prediction = model.predict(data)
    top_prob_index = np.argmax(prediction[0])
    confidence_score = float(prediction[0][top_prob_index])
    return class_names[top_prob_index], confidence_score

# Streamlit UI setup
st.title("Klasifikasi Penyakit Kulit dengan Machine Learning")

# Default state if this is the first time running
if 'page' not in st.session_state:
    st.session_state.page = 'info'  # Default to information page

# Create layout for buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("Informasi tentang Penyakit Kulit", key="info_button"):
        st.session_state.page = "info"

with col2:
    if st.button("Prediksi Gambar Penyakit Kulit", key="predict_button"):
        st.session_state.page = "predict"

# Render the corresponding content based on the state
if st.session_state.page == "info":
    st.header("Informasi tentang Penyakit Kulit 🩺")
    st.write("""
        Teknologi machine learning dapat digunakan untuk mendiagnosis dan memprediksi penyakit kulit berdasarkan 
        gambar dan data pasien. Beberapa penyakit kulit yang umum diprediksi meliputi:
        - **Actinic keratosis**
        - **Atopic Dermatitis**
        - **Benign keratosis**
        - **Dermatofibroma**
        - **Melanocytic nevus**
        - **Melanoma**
        - **Squamous cell carcinoma**
        - **Tinea Ringworm Candidiasis**
        - **Vascular lesion**
        
        Model machine learning dapat dilatih menggunakan dataset gambar kulit yang telah diberi label untuk 
        mengenali pola dan gejala yang terkait dengan penyakit tertentu. Dengan demikian, pasien dapat 
        mendapatkan diagnosis awal yang lebih cepat dan akurat.
        
        Penting untuk diingat bahwa meskipun teknologi ini menjanjikan, konsultasi dengan dokter kulit tetap 
        diperlukan untuk diagnosis dan perawatan yang tepat.
    """)

elif st.session_state.page == "predict":
    # Load model and labels
    model_path = 'model/model.h5'
    label_path = 'model/labels.txt'
    model = load_model(model_path)
    class_names = load_labels(label_path)

    # Upload image
    uploaded_file = st.file_uploader("Pilih gambar...", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        
        # Classify the image
        class_name, confidence_score = classify_image(image, model, class_names)

        # Display the classification result above the image
        st.write(f"Prediksi Kelas: **{class_name}**")
        st.write(f"Skor Kepercayaan: **{confidence_score:.2f}**")
        st.image(image, caption='Gambar yang Diupload', width=300)  # Set a maximum width for the image