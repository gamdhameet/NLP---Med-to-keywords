# Medical Audio to Text Processing

This project converts medical audio recordings to text and extracts important keywords using Natural Language Processing (NLP). The current implementation uses **speech recognition** to transcribe audio and **spaCy with SciSpaCy** to analyze the text.

## Features
- Converts speech to text from an audio file
- Extracts important keywords dynamically using NLP
- Uses **SciSpaCy's** medical NLP model (`en_core_sci_sm`) for better accuracy

## Installation
Ensure you have Python installed, then run:
```sh
pip install -r requirements.txt
```
Additionally, download the necessary NLP model:
```sh
python -m spacy download en_core_sci_sm
```

## Usage
Run the script and provide an audio file:
```sh
python main.py
```
Replace `sample_audio.wav` with your actual audio file.

## Future Improvements
This is a basic implementation. NLP can be improved by:
- **Using more advanced medical NLP models** (e.g., `en_core_sci_md` or `en_core_sci_lg`)
- **Customizing entity recognition** to focus on specific medical terms
- **Integrating machine learning models** for better keyword extraction
- **Improving speech recognition** with domain-specific language models


