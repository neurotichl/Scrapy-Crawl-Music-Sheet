from PyPDF2 import PdfFileReader
from config import *
import sqlite3
import os

conn = sqlite3.connect('musicsheets.db')
c = conn.cursor()

def create_table():
	'''
	Create the table if not exist
	'''
	c.execute('CREATE TABLE IF NOT EXISTS sheets(title TEXT, link TEXT, converted TEXT, pages REAL)')

def check_link(link):
	'''
	Check whether the link/title exist in the database
	'''
	c.execute("SELECT title, link FROM sheets WHERE link = '{}'".format(link))
	title_link = c.fetchall()
	return title_link

def title_entry(title,link,status = 'No',pages=0):
	'''
	Insert data into the database
	'''
	c.execute("INSERT INTO sheets(title, link, converted, pages) VALUES ('{}','{}','{}',{})".format(title,link,status,pages))

def unconverted_songlist():
	'''
	Read title of songs that is not converted to pdf yet
	'''
	c.execute("SELECT title from sheets WHERE converted = 'No'")
	songs = [i[0] for i in c.fetchall()]
	return songs

def update_db(title, pages):
	'''
	Change converted-status of the song to Yes
	'''
	c.execute("UPDATE sheets SET converted = 'Yes', pages = {} WHERE title = '{}'".format(pages,title))
	
def commit_and_close():
	conn.commit()
	conn.close()

def invalidate_metadata():
	'''
	Check the database if it's up-to-date
	'''
	def check_status_pages(title, pages=0):
		c.execute("UPDATE sheets SET converted = CASE WHEN converted = 'No' THEN 'Yes' ELSE converted END, pages = {} WHERE title = '{}'".format(pages, title))

	def get_pdf_pages(title):
		return PdfFileReader(open('{}/{}.pdf'.format(pdf_folder,title),'rb')).getNumPages()

	def check_db(title, case):
		print(title,case)
		if case in [3,7]:
			check_status_pages(title,get_pdf_pages(title))
		elif case == 5:
			check_status_pages(title)
		elif case == 6:
			title_entry(title, 'Unknown','Yes',len(os.listdir(os.path.join(img_folder,title))))
		elif case == 4:
			title_entry(title, 'Unknown','No')
		elif case == 2:
			title_entry(title, 'Unknown','Yes',get_pdf_pages(title))
		elif case == 1:
			c.execute("DELETE FROM sheets WHERE title = '{}'".format(title))

	c.execute("SELECT title FROM sheets")
	db_songlist = [s[0] for s in c.fetchall()]
	img_songlist = os.listdir(img_folder)
	pdf_songlist = [i.replace('.pdf','') for i in os.listdir(pdf_folder)]
	
	for i in set(db_songlist).union(set(img_songlist), set(pdf_songlist)):
		check_db(i,(i in img_songlist)*4+(i in pdf_songlist)*2+(i in db_songlist))

	conn.commit()


if __name__=='__main__':
	invalidate_metadata()