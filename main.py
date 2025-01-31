import speech_recognition as sr
import spacy
import re

# Load the NLP model (specialized in scientific/medical text)
nlp = spacy.load("en_core_sci_sm")

def audio_to_text(audio_file):
    """Convert an audio file to text using speech recognition."""
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
    """Extract and categorize keywords from text using NLP and regex."""
    doc = nlp(text)
    keywords = {
        "Drugs": set(),
        "Age": set(),
        "Name": set()
    }

    # Extract chemical entities for Drugs
    for ent in doc.ents:
        if ent.label_ == "CHEMICAL":
            keywords["Drugs"].add(ent.text)

    # Extract proper nouns for Name
    for token in doc:
        if token.pos_ == "PROPN":
            keywords["Name"].add(token.text)

    # Extract age using regex pattern
    age_pattern = re.compile(r'(\d+)\s+years?\s+old', re.IGNORECASE)
    age_matches = age_pattern.findall(text)
    keywords["Age"].update(age_matches)

    # Convert sets to sorted lists
    for category in keywords:
        keywords[category] = sorted(keywords[category])
    
    return keywords

def save_to_file(filename, transcript, keywords):
    """Save transcript and keywords to a text file."""
    with open(filename, "w") as f:
        f.write("Transcript:\n")
        f.write(f'"{transcript}"\n\n')
        f.write("Keywords:\n")
        
        # Write non-empty categories
        for category, items in keywords.items():
            if items:
                f.write(f"{category}: {', '.join(items)}\n")

# Example Usage
if __name__ == "__main__":
    audio_file = "sample_audio.wav"  # Replace with your audio file
    output_file = "transcript_keywords.txt"
    
    text = audio_to_text(audio_file)
    if text:
        keywords = extract_keywords(text)
        save_to_file(output_file, text, keywords)
        print(f"\nTranscript and keywords saved to '{output_file}'")