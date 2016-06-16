#!/usr/bin/env python
from selenium import webdriver
from StringIO import StringIO
import gzip, os, sys, time, urllib

def main():
    num = int(sys.argv[1])

    path = sys.argv[2]
    if not path.endswith("/"):
        path += "/"
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except Exception, e:
        print str(e)

    dl_doc(num, path)

def log(msg):
    print "[ScribDL]", msg

def dl_doc(num, path):
    log("Fetching doc #%d" % num)

    driver = webdriver.Firefox()
    driver.get("https://www.scribd.com/doc/%d/" % num)
    time.sleep(2) # make sure page loads

    title = driver.current_url.split("/")[5]
    title_path = path + title + "_%d/" % num
    images_path = title_path + "images/"
    log("Found doc title: " + title)
    try:
        if not os.path.exists(images_path):
            os.makedirs(images_path)
    except Exception, e:
        print str(e)
    page_num = 0
    data = driver.page_source.split("\n")
    for line in data:
        if "pageParams.contentUrl = " in line:
            page_url = line.split("pageParams.contentUrl = ")[1].replace("\"", "").replace(";", "") # regex is hard
            image_url = gzip_decompress(urllib.urlopen(page_url).read()).split("orig=\\\"")[1].split("\\")[0] # server returns gzipped data, decompress (regex is still hard)
            urllib.urlretrieve(image_url, images_path + "%d.jpg" % (page_num))
            page_num += 1
    log("%d images retrieved" % (page_num - 1))
    log("Compiling images to PDF...")
    # compile saved images to pdf
    os.system("convert '%s%s.jpg[0-%d]' %s.pdf" % (images_path, "%d", page_num - 1, title_path + title))
    log("Done!")

def gzip_decompress(raw):
    return gzip.GzipFile(fileobj=StringIO(raw)).read()

if __name__ == "__main__":
    main()
