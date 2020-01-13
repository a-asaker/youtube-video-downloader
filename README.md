# Youtube Video Downloader 
  Youtube Video Downloader Is A Python Project That Downloads Youtube Videos From Video URL On Youtube .
  
  Coded By : a-asaker
  
# Requirements : 

    - python 2 Or 3 installed .
    - selenium Module Installed With WebDriever For your Web Browser.
    - xvfbwrapper Module Installed (For Linux Users).
# For `geckodriver` ISSUE :

    - Download `geckodriver` From : https://github.com/mozilla/geckodriver/releases .
    - Add `geckodriver` Executable To Your PATH : -For Linux Users : 
                                                        -sudo cp {path-to-geckodriver} /usr/bin/geckodriver
                                                        -sudo cp {path-to-geckodriver} /usr/local/bin/geckodriver
                                                        * Note : Change {path-to-geckodriver} In The 2 lines Above
                                                          To The Path Of Your `geckodriver` Executable File .
                                                  -Windows Users : "Google It" !
     
                                                
# Notes :
  * If You Use Google Chrome Or Any Other Web Browser Unless FireFox , Then You Should Change Line 25 In The Code :`browser = webdriver.Firefox()` To Your Browser Selenium WebDriver .
