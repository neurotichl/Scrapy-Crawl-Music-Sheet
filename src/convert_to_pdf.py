from musicsheetdb import *
from config import *
from fpdf import FPDF
import os

def convert_to_pdf(song):
	pdf = FPDF()

	song_folder = os.path.join(img_folder,song)
	pg = 0
	for image in os.listdir(song_folder):
		pg += 1
		pdf.add_page()
		pdf.image(os.path.join(song_folder,image),0,0,210,297) #A4 is 210mm x 297mm

	pdf.output(os.path.join(pdf_folder,song+".pdf"), "F")
	update_db(song, pg)

if __name__=='__main__':

	for title in unconverted_songlist():
		convert_to_pdf(title)

	commit_and_close()