import streamlit as st
import os
from ocr_module import extract_text_from_image
from nlp_module import parse_prescription
from translation_module import translate_and_speak

st.title("Vernacular Medical Prescription Parser")

# Sidebar for API key
api_key = st.sidebar.text_input("OpenAI API Key", type="password")
if not api_key:
    st.warning("Please enter your OpenAI API Key to proceed.")
    st.stop()

# Language selection
languages = ["English", "Telugu", "Hindi", "Tamil", "Malayalam", "Odia", "Marathi", "Kannada", "Punjabi"]
language = st.selectbox("Select Output Language", languages)

# Input method selection
input_method = st.radio("Choose Input Method", ("Take Photo with Camera", "Upload Image"))

image = None
if input_method == "Take Photo with Camera":
    image = st.camera_input("Capture Prescription Photo")
else:
    image = st.file_uploader("Upload Prescription Image", type=["png", "jpg", "jpeg"])

if image:
    # Create uploads directory if it doesn't exist
    uploads_dir = "uploads"
    os.makedirs(uploads_dir, exist_ok=True)
    
    # Save the image temporarily
    image_path = os.path.join(uploads_dir, "prescription.jpg")
    with open(image_path, "wb") as f:
        f.write(image.getvalue())
    
    # Display the captured/uploaded image
    st.image(image_path, caption="Prescription Image", use_column_width=True)
    
    # Step 1: OCR Extraction
    with st.spinner("Extracting text from image..."):
        raw_text = extract_text_from_image(image_path)
    st.text_area("Extracted Raw Text", raw_text, height=150)
    
    # Step 2: NLP Parsing (simplify and explain in English)
    with st.spinner("Parsing and simplifying medical terms..."):
        parsed_text = parse_prescription(raw_text, api_key)
    st.text_area("Simplified Explanation (English)", parsed_text, height=200)
    
    # Step 3: Translation and Voice Output
    with st.spinner("Translating and generating voice output..."):
        translated_text, audio_bytes = translate_and_speak(parsed_text, language)
    st.text_area(f"Explanation in {language}", translated_text, height=200)
    st.audio(audio_bytes, format="audio/mp3")