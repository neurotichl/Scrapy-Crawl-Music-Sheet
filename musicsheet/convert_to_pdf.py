# -*- coding: utf-8 -*-
from fpdf import FPDF
import os

def convert_to_pdf():
	pdf = FPDF()

	folder_name = os.listdir('musicsheet/sheet_img')[0]####REPLACE WITH DATABASE CALL

	img_folder = os.path.join('musicsheet','sheet_img',folder_name)

	for image in os.listdir(img_folder):
	    pdf.add_page()
	    pdf.image(os.path.join(img_folder,image),0,0,210,297) #A4 is 210mm x 297mm

	pdf.output(os.path.join('musicsheet','sheet_pdf',folder_name+".pdf"), "F")

convert_to_pdf()