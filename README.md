# Crawl-Music-Sheet
Crawl music sheet images from http://m.hqgq.com, download the music sheet and convert them to pdf

1. [Scrapy crawl script](https://github.com/neurotichl/Crawl-Music-Sheet/blob/master/src/crawlsheet.py)

2. [Convert to PDF script](https://github.com/neurotichl/Crawl-Music-Sheet/blob/master/src/convert_to_pdf.py)

3. [Crawled Sheet Images](https://github.com/neurotichl/Crawl-Music-Sheet/tree/master/musicsheet/sheet_img)

4. [Converted Sheet PDF](https://github.com/neurotichl/Crawl-Music-Sheet/tree/master/musicsheet/sheet_pdf)


### Step 1:
```
scrapy runspider src/crawlsheet.py
```

### Step 2:
```
python src/convert_to_pdf.py
```

