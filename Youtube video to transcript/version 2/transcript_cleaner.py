import re

def clean_transcripts(transcripts):
    cleaned_transcripts = []
    for transcript in transcripts:
        # Remove timestamps and other non-verbal cues
        cleaned = re.sub(r'\[.*?\]', '', transcript)
        cleaned = re.sub(r'\(\d{1,2}:\d{2}\)', '', cleaned)
        cleaned_transcripts.append(cleaned)
    return cleaned_transcripts
