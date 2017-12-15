from musicsheetdb import *
from fpdf import FPDF
import os

def get_folder_name():
	songlist = read_from_db()
	return songlist

def convert_to_pdf(song):
	pdf = FPDF()

	img_folder = os.path.join('musicsheet','sheet_img',song)

	pg = 0
	for image in os.listdir(img_folder):
		pg += 1
		pdf.add_page()
		pdf.image(os.path.join(img_folder,image),0,0,210,297) #A4 is 210mm x 297mm

	pdf.output(os.path.join('musicsheet','sheet_pdf',song+".pdf"), "F")
	update_db(song, pg)

for song in get_folder_name():
	convert_to_pdf(song[0])
