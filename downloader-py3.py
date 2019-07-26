#!/usr/bin/env python3
# Coded By : A_Asaker

#!/usr/bin/env python3
import urllib.request
from selenium import webdriver
from xvfbwrapper import Xvfb
from time import time
import os,sys

def process(n_blocks,block_size,file_size):
	print("\r\t -> [ {0:.2f} % ]".format(round(n_blocks*block_size/float(file_size)*100,2)),end = "")

def get_url(yt_url):
	savefromnet="https://en.savefrom.net/#url={}&utm_source=youtube.com&utm_medium=short_domains&utm_campaign=ssyoutube.com".format(yt_url)
	return savefromnet

def get_vid_lst(save_url):
	vdisplay = Xvfb(width=1280, height=720)
	vdisplay.start()
	browser = webdriver.Firefox()
	browser.get(save_url)
	iframe_source = browser.page_source
	browser.close()
	vdisplay.stop()
	page_html=iframe_source
	while (page_html.find("&amp;")!= -1):
		page_html=page_html.replace("&amp;","&")
	return page_html

def main():
	man=False
	if len(sys.argv)<3:
		man=True
		print(' [**] Usage :  Downloader-3 [Quality] [Video URL]')
		x=input(' [**] Continue Maniually ?(y/n) : ')
		if x.lower()=='y':
			pass
		elif x.lower()=='n':
			os._exit(0)
		else:
			print(' [xx] Unknown Answer !')
			os._exit(0)

	if man:
		yt_url=input("Enter Youtube URL : ")
	else :
		yt_url=sys.argv[2]

	save_url=get_url(yt_url)
	page_html=get_vid_lst(save_url)

	quality = []
	strt=0
	while 1:
		q_start = page_html.find('data-quality="',strt)
		if (q_start != -1):
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
		print(" [*] Avilable Qualities : " )
		for i in quality:
			print("\t -{}".format(i))
		chsn_qlty=input("Choose Quality : ")
	else:
		if sys.argv[1] in quality:
			chsn_qlty=sys.argv[1]
		else :
			print(" [*] Video Is Not Available In The Quality You've Choosen , Please Choose Another Quality ...")
			print(" [*] Avilable Qualities : " )
			for i in quality:
				print("\t -{}".format(i))
			chsn_qlty=input("Choose Quality : ")

	start_srch='data-quality="{}" data-type="'.format(chsn_qlty)
	start=page_html.find(start_srch)+len(start_srch)+11
	end=page_html.find('"',start)+1
	url=page_html[start:end]

	ext=str(page_html[start-11:start-8])

	name_start=page_html.rfind('download=',start)+10
	name_end=page_html.find('.',name_start)
	file_name=page_html[name_start:name_end]+"("+chsn_qlty+"p)."+ext
	file_name=file_name
	try:
		if quality != []:
			print(" [*] Video To Download : {} ".format(file_name))
			# file_name=input("Save With Name : ")
			print(" [*] Downloading Progress :  ")
			start_time=time()
			os.chdir("/home/user/Desktop")
			urllib.request.urlretrieve(url,file_name,process)
			end_time=time()
			downloading_time=round((end_time-start_time)/60,2)
			print("\n [*] Downloading Completed ! ")
			print(" [*] Time Taken For Downloading <| {} Minutes |>".format(downloading_time))
			return
	except:
		main()
if __name__ == '__main__':
	q=main()
	if q=="no":
		main()
