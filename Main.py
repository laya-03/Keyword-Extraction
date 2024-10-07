import tkinter as tk
from tkinter import ttk
from rake_nltk import Rake
import numpy as np
import webbrowser
from googlesearch import search
import nltk
nltk.download('stopwords')
nltk.download('punkt_tab')

# Initialize Rake
r = Rake()

# Create the main application window
window = tk.Tk()
window.title("Keyword Extractor and Google Search")
window.geometry("700x600")
window.config(bg="#f0f0f0")

# Function to extract keywords from text
def key_word():
    txt = entry.get()  # Get user input from the text entry
    r.extract_keywords_from_text(txt)
    keywords = r.get_ranked_phrases()
    unique_keywords = np.unique(keywords)
    label_keywords.configure(text="Keywords: " + ", ".join(unique_keywords))

# Function to open a URL in a web browser
def callback(url):
    webbrowser.open_new_tab(url)

# Function to perform a Google search
def google_search():
    search_text = entry_search.get()
    for j in search(search_text, tld="co.in", num=5, stop=5, pause=2):
        # Create a clickable link for each search result
        link = tk.Label(window, text=j, font=('Helvetica', 15), fg="blue", cursor="hand2", bg="#f0f0f0")
        link.bind("<Button-1>", lambda e, url=j: callback(url)) 
        link.pack()

# Adding UI elements with modern styling
# Input Label for keyword extraction
label_entry = tk.Label(window, text="Enter Text for Keyword Extraction:", font=('Helvetica', 14), bg="#f0f0f0")
label_entry.pack(pady=10)

# Entry widget for user input text
entry = tk.Entry(window, width=60, font=('Helvetica', 12))
entry.pack(pady=5)

# Button to trigger keyword extraction
extract_button = ttk.Button(window, text="Get Keywords", width=20, command=key_word)
extract_button.pack(pady=20)

# Label to display extracted keywords
label_keywords = tk.Label(window, text="Keywords/Phrases are:", font=('Helvetica', 12), bg="#f0f0f0", wraplength=600)
label_keywords.pack(pady=10)

# Separator for better layout
ttk.Separator(window, orient='horizontal').pack(fill='x', pady=20)

# Input Label for Google search
label_search = tk.Label(window, text="Enter Keyword for Google Search:", font=('Helvetica', 14), bg="#f0f0f0")
label_search.pack(pady=10)

# Entry widget for Google search text
entry_search = tk.Entry(window, width=60, font=('Helvetica', 12))
entry_search.pack(pady=5)

# Button to trigger Google search
search_button = ttk.Button(window, text="Search", width=20, command=google_search)
search_button.pack(pady=20)

# Label to display Google search links
label_links = tk.Label(window, text="Google Search Links:", font=('Helvetica', 12), bg="#f0f0f0")
label_links.pack(pady=10)

# Run the application
window.mainloop()
