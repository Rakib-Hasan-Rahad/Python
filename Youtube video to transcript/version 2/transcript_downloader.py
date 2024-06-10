import tkinter as tk
from tkinter import messagebox
from transcript_fetcher import fetch_transcripts
from transcript_cleaner import clean_transcripts
from nlp_processor import process_transcripts
from script_generator import generate_script

def fetch_and_process_transcripts():
    links = text_input.get("1.0", "end-1c").strip().split('\n')
    try:
        transcripts = fetch_transcripts(links)
        cleaned_transcripts = clean_transcripts(transcripts)
        processed_transcripts = process_transcripts(cleaned_transcripts)
        final_script = generate_script(processed_transcripts)
        
        with open("final_script.txt", "w", encoding="utf-8") as file:
            file.write(final_script)
        
        messagebox.showinfo("Success", "Final script saved to final_script.txt")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI setup
root = tk.Tk()
root.title("YouTube Transcript Downloader")

# Instructions
instructions = tk.Label(root, text="Enter YouTube links (one per line):")
instructions.pack(pady=10)

# Text input for YouTube links
text_input = tk.Text(root, height=10, width=50)
text_input.pack(pady=10)

# Button to fetch and process transcript
fetch_button = tk.Button(root, text="Fetch and Process Transcript", command=fetch_and_process_transcripts)
fetch_button.pack(pady=10)

# Start the GUI loop
root.mainloop()
