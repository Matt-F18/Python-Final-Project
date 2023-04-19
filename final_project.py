#Name: Matthew Freed
#Date: 5/3/2022
#Class: SDE-195: Programming in Python
#Purpose: Taking a PDF and turning it into Text-To-Speech/ Final Project for Python.

#Importing necessities
import gtts
from playsound import playsound
from PyPDF2 import PdfFileReader
#******************************************************************************************
#Reading the file path
#You need to edit the code so it has the right path. All you need to do is to edit the /User/"Your user"/ and save it to the desktop
pdf_path = r"/Users/matthewfreed/Desktop/Lost_in_the_fog.pdf"

#Opening the PDF
pdfFileObject = open(pdf_path, 'rb')

#Reading the PDF
pdfReader = PdfFileReader(pdfFileObject, strict=False)

#Blank for text, so stuff can be added to it 
text = ' '

#This scrapes the PDF page by page and converts it to text/ strings
for i in range(0, pdfReader.numPages):

    # creating a page object
    pageObj = pdfReader.getPage(i)

    # extracting text from page
    text = text+pageObj.extractText()
    print(text)

    #converts text to string
    text = str(text)

    #This avoides repition
    if i == 5: 

        #This gets the strings and converts it to english. 
        tts = gtts.gTTS(text, lang="en")

        #This saves the audio to a mp3 file format
        tts.save("lostInTheFog.mp3")

        #Prints the PDF line by line
        print(text)
        
#Plays the finished audio in text-to-speech voice
playsound("lostInTheFog.mp3")   