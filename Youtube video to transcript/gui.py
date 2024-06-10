import tkinter as tk
from tkinter import messagebox
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

# Function to fetch transcript and save to a text file
def fetch_transcript():
    links = text_input.get("1.0", "end-1c").strip().split('\n')
    transcript_texts = []

    for link in links:
        video_id = link.split("v=")[-1]
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            formatter = TextFormatter()
            transcript_text = formatter.format_transcript(transcript)
            transcript_texts.append(f"Transcript for {link}:\n\n{transcript_text}\n\n")
        except Exception as e:
            messagebox.showerror("Error", f"Could not fetch transcript for {link}: {e}")
            return

    # Save transcripts to a text file
    with open("transcripts.txt", "w", encoding="utf-8") as file:
        for transcript_text in transcript_texts:
            file.write(transcript_text)

    messagebox.showinfo("Success", "Transcripts saved to transcripts.txt")

# GUI setup
root = tk.Tk()
root.title("YouTube Transcript Downloader")

# Instructions
instructions = tk.Label(root, text="Enter YouTube video id (one per line):")
instructions.pack(pady=10)

# Text input for YouTube links
text_input = tk.Text(root, height=10, width=50)
text_input.pack(pady=10)

# Button to fetch transcript
fetch_button = tk.Button(root, text="Fetch Transcript", command=fetch_transcript)
fetch_button.pack(pady=10)

# Start the GUI loop
root.mainloop()
