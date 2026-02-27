from googletrans import Translator
from gtts import gTTS
from io import BytesIO

def translate_and_speak(text, language):
    """
    Translates text to the target language and generates audio using gTTS.
    Returns translated text and audio bytes for Streamlit playback.
    """
    lang_codes = {
        "English": "en",
        "Telugu": "te",
        "Hindi": "hi",
        "Tamil": "ta",
        "Malayalam": "ml",
        "Odia": "or",
        "Marathi": "mr",
        "Kannada": "kn",
        "Punjabi": "pa"
    }
    if language not in lang_codes:
        raise ValueError("Unsupported language")
    
    code = lang_codes[language]
    
    # Translate text
    translator = Translator()
    translated = translator.translate(text, dest=code).text
    
    # Generate TTS audio
    tts = gTTS(translated, lang=code, slow=False)
    audio_bytes = BytesIO()
    tts.write_to_fp(audio_bytes)
    audio_bytes.seek(0)
    
    return translated, audio_bytes