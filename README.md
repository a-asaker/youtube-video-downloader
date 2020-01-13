# Youtube Video Downloader 
  Youtube Video Downloader Is A Python Project That Downloads Youtube Videos From Video URL On Youtube .
  
  Coded By : a-asaker
  
# Requirements : 

    - python 2 Or 3 installed .
    - selenium Module Installed With WebDriever For your Web Browser.
    - xvfbwrapper Module Installed (For Linux Users).

# For The `driver` ISSUE :
* Note : If The Project Works Fine, Don't Waste Your Time Reading This!
       
        - Download The `driver` Of The Browser Which You Will Use : 
             - FireFox : https://github.com/mozilla/geckodriver/releases .
             - Chrome  : https://sites.google.com/a/chromium.org/chromedriver/downloads .
             - Opera   : https://github.com/operasoftware/operachromiumdriver/releases .
        - Add The `driver` Executable To Your PATH .
             - Firefox `geckodriver` For Linux Users : 
                                                        -sudo cp {path-to-geckdriver} /usr/bin/geckodriver
                                                        -sudo cp {path-to-geckodriver} /usr/local/bin/geckodriver
                                                        * Note : Change {path-to-geckodriver} In The 2 lines Above
                                                          To The Path Of Your `geckodriver` Executable File .
             - Windows Users And Other Browsers Users : "Google It" !
     
                                                
# Notes :
  * If You Use Google Chrome Or Any Other Web Browser Unless FireFox , Then You Should Change Line 25 In The Code `browser = webdriver.Firefox()` To Your Browser WebDriver :
            
       * Chrome    : `browser = webdriver.Chrome()`
       * IE        : `browser = webdriver.Ie()`
       * PhantomJS : `browser = webdriver.PhantomJS()`
       * Edge      : `browser = webdriver.Edge()`
       * Safari    : `browser = webdriver.Safari()`
       * Opera     :
       
        options = webdriver.ChromeOptions()
        options.binary_location = "Path-To-Opera-Browser" #An Example, For Windows: "C:\\Program Files\\Opera\\launcher.exe"
        browser = webdriver.Opera(executable_path='Path-To-Opera-Driver', opera_options=options)
