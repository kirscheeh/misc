#!/usr/bin/env python

import sys, pyttsx3, PyPDF2

# reading a pdf and transforming it into mp3 file, reading the content of the pdf
# limitations: pdf length

pdf = PyPDF2.PdfReader(open(sys.argv[1], "rb"))
speaker = pyttsx3.init()

clean_text=""
for page_num in range(len(pdf.pages)):
    text = pdf.pages[page_num].extract_text()
    clean_text += text.strip().replace("\n", " ")

speaker.save_to_file(clean_text, sys.argv[3])
speaker.runAndWait()
speaker.stop()
