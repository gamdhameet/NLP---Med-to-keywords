import speech_recognition as sr
import spacy

# Load the NLP model (specialized in scientific/medical text)
nlp = spacy.load("en_core_sci_sm")

def audio_to_text(audio_file):
    """
    Convert an audio file to text using speech recognition.
    """
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        print("Processing audio...")
        audio = recognizer.record(source)
    
    try:
        text = recognizer.recognize_google(audio)
        print("\nConverted Text:\n", text)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError:
        print("Speech Recognition service is unavailable")
        return None

def extract_keywords(text):
    """
    Extract important words and phrases from the text using NLP.
    """
    doc = nlp(text)
    keywords = set()

    for token in doc:
        # Extract nouns, proper nouns, and adjectives (important keywords)
        if token.pos_ in ["NOUN", "PROPN", "ADJ"]:
            keywords.add(token.text)

    # Extract named entities (could be medications, diseases, medical terms, etc.)
    for ent in doc.ents:
        keywords.add(ent.text)

    print("\nExtracted Keywords:")
    for keyword in keywords:
        print(f"- {keyword}")

    return keywords

# Example Usage
if __name__ == "__main__":
    audio_file = "sample_audio.wav"  # Replace with your audio file
    text = audio_to_text(audio_file)
    if text:
        extract_keywords(text)
