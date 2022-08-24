import pyttsx3
import PyPDF2

pdfreader = PyPDF2.PdfFileReader(open('story.pdf', 'rb'))
speaker = pyttsx3.init()
for page_num in range(pdfreader.numPages):
    # extracting text from the PDF
    text = pdfreader.getPage(page_num).extractText()
    # Removes unnecessary spaces and break lines
    cleaned_text = text.strip().replace('\n', ' ')
    print(cleaned_text)  # Print the text from PDF
    # speaker.say(cleaned_text)        ## Let The Speaker Speak The Text
    # Saving Text In a audio file 'story.mp3'
    speaker.save_to_file(cleaned_text, 'story.mp3')
    speaker.runAndWait()
speaker.stop()
