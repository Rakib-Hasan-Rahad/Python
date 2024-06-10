import spacy

# Load SpaCy model
nlp = spacy.load("en_core_web_sm")

def process_transcripts(cleaned_transcripts):
    processed_transcripts = []
    for transcript in cleaned_transcripts:
        doc = nlp(transcript)
        processed_transcripts.append(" ".join([sent.text for sent in doc.sents]))
    return processed_transcripts
