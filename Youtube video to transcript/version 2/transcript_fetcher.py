from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

def fetch_transcripts(links):
    transcripts = []
    for link in links:
        video_id = link.split("v=")[-1]
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        formatter = TextFormatter()
        transcripts.append(formatter.format_transcript(transcript))
    return transcripts
