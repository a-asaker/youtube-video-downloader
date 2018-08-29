# Youtube Video Downloader 
  Youtube Video Downloader Is A Python Project That Downloads Youtube Videos From Video URL On Youtube .
  
  Coded By : a-asaker
  
# Requirements : 

    - python 2 Or 3 installed .
    - selenium Module Installed With WebDriever For your Web Browser.
    - xvfbwrapper Module Installed (For Linux Users).

# Notes :
  * If you Use Google Chrome Or Another Web Browser Unless FireFox , Then You Should Change Line 19 In The Code :`browser = webdriver.Firefox()` To Your Browser Selenium WebDriver .
  * If You Use Windows, You'll need To Comment Lines With Numbers [ 6 , 17 , 18 , 23 ] : 
            
            6  =>	# from xvfbwrapper import Xvfb
            17 =>	# vdisplay = Xvfb(width=1280, height=720)
            18 =>	# vdisplay.start()
            23 =>	# vdisplay.stop()
