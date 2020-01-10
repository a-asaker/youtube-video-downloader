#!/usr/bin/env python
# Coded By : A_Asaker

import urllib
from selenium import webdriver
from time import time
import os,sys
pf='windows' if sys.platform.find('win')!=-1 and sys.platform != 'darwin' else 'unix'

if pf=='unix':
	from xvfbwrapper import Xvfb

def process(n_blocks,block_size,file_size):
	if n_blocks*block_size/float(file_size)*100<0:
		print "\r\t -> [Unknown File Size] - Downloading... " ,
	else: print "\r\t -> [ %.2f %% ]" %(n_blocks*block_size/float(file_size)*100),

def get_url(yt_url):
	savefromnet="https://en.savefrom.net/#url=%s&utm_source=youtube.com&utm_medium=short_domains&utm_campaign=ssyoutube.com"%yt_url
	return savefromnet

def get_vid_lst(save_url,yt_url):
	vdisplay = Xvfb(width=1280, height=720) if pf=='unix' else None
	vdisplay.start() if pf=='unix' else None
	browser = webdriver.Firefox()
	browser.get(save_url)
	browser.find_element_by_id("sf_url").send_keys(yt_url)
	iframe_source = browser.page_source
	browser.close()
	vdisplay.stop() if pf=='unix' else None
	page_html=str(iframe_source.encode('UTF-8'))
	while page_html.find("&amp;")!= -1:
		page_html=page_html.replace("&amp;","&")
	return page_html

def main():
	man=False
	if len(sys.argv)<3:
		man=True
		print ' [**] Usage :  Downloader-2 [Quality] [Video URL]'
		x=raw_input(' [**] Continue Maniually ?(y/n) : ')
		if x.lower()=='y':
			pass
		elif x.lower()=='n':
			os._exit(0)
		else:
			print ' [xx] Unknown Answer !'
			os._exit(0)


	if man:
		yt_url=raw_input("Enter Youtube URL : ")
	else :
		yt_url=sys.argv[2]

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
	if not quality:
		return "no"

	if man:
		print " [*] Avilable Qualities : " 
		for i in quality:
			print "\t -%s" %i
		chsn_qlty=raw_input("Choose Quality : ")
	else:
		if sys.argv[1] in quality:
			chsn_qlty=sys.argv[1]
		else :
			print " [*] Video Is Not Available In The Quality You've Choosen , Please Choose Another Quality ..."
			print " [*] Avilable Qualities : " 
			for i in quality:
				print "\t -%s" %i
			chsn_qlty=raw_input("Choose Quality : ")

	start_srch='data-quality="%s" data-type="'%chsn_qlty
	start=page_html.find(start_srch)+len(start_srch)+11
	start=page_html.find(start_srch)+len(start_srch)+12 if page_html[start]=="\"" else start
	end=page_html.find('"',start)+1
	url=page_html[start:end]

	ext=str(page_html[start-11:start-8]) if str(page_html[start-12])=="\"" else str(page_html[start-12:start-8])

	name_start=page_html.rfind('download=',start)+10
	name_end=page_html.find('.',name_start)
	file_name=page_html[name_start:name_end]+"("+chsn_qlty+"p)."+ext
	try:
		if quality:
			print " [*] Video To Download : %s "%file_name
			start_time=time()
			print " [*] Downloading Progress :  "
			os.chdir("/home/user/Desktop")
			urllib.urlretrieve(url,file_name,process)
			end_time=time()
			downloading_time=round((end_time-start_time)/60,2)
			print "\n [*] Download Completed !"
			print " [*] Time Taken For Downloading <| %f Minutes |>"%downloading_time
			return
	except:
		main()

if __name__ == '__main__':
	q=main()
	if q=="no":
		main()
