#!/usr/bin/env python
# Coded By : A_Asaker

import urllib
from selenium import webdriver
from xvfbwrapper import Xvfb

def process(n_blocks,block_size,file_size):
	print "\r\t -> [ %f %% ]" %(n_blocks*block_size/float(file_size)*100), 

def get_url(yt_url):
	savefromnet="https://en.savefrom.net/#url=%s&utm_source=youtube.com&utm_medium=short_domains&utm_campaign=ssyoutube.com"%yt_url
	return savefromnet

def get_vid_lst(save_url):
	vdisplay = Xvfb(width=1280, height=720)
	vdisplay.start()
	browser = webdriver.Firefox()
	browser.get(save_url)
	iframe_source = browser.page_source
	browser.close()
	vdisplay.stop()
	page_html=str(iframe_source.encode('UTF-8'))
	while page_html.find("&amp;")!= -1:
		page_html=page_html.replace("&amp;","&")
	return page_html

yt_url=raw_input("Enter Youtube URL : ")
save_url=get_url(yt_url)
page_html=get_vid_lst(save_url)

quality = []
strt=0
while 1:
	q_start = page_html.find('data-quality="',strt)
	if q_start != -1:
		q_end=page_html.find('"',q_start+14)
		new_quality=str(page_html[q_start+14:q_end])
		strt=q_end
		if new_quality not in quality:
			quality.append(new_quality)
		else: pass
	else: break

print " [*] Avilable Qualities : " 
for i in quality:
	print "\t -%s" %i

chsn_qlty=raw_input("Choose Quality : ")

start_srch='data-quality="%s" data-type="'%chsn_qlty
start=page_html.find(start_srch)+len(start_srch)+11
end=page_html.find('"',start)+1
url=page_html[start:end]

ext=str(page_html[start-11:start-8])

name_start=page_html.rfind('download=',start)+10
name_end=page_html.find('.',name_start)
file_name=page_html[name_start:name_end]+"("+chsn_qlty+"p)."+ext
print " [*] Video To Download : %s "%file_name

# file_name=raw_input("Save With Name : ")
print " [*] Downloading Progress :  "
urllib.urlretrieve(url,file_name,process)

print "\n [*] Download Completed !"

