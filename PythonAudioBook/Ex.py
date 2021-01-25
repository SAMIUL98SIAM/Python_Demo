import pyttsx3
import PyPDF2
'''pdf = open('PDF.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdf)
pages = pdfReader.numPages
print(pages)'''
frind = pyttsx3.init()
'''page = pdfReader.getPage(0)
mssge = page.extractText()'''
frind.say("pdfReader")
frind.runAndWait()