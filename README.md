# NSE Yahoo Finance - Financial Statements Scraper


[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)



# Introduction

This script scrapes Yahoo Finance & downloads income statement, balance sheet & cash flow statement in csv. Automatically creates directory with symbol name in your save-to-path folder to save all downloaded data.

I prefer running this script on [Google Colab](https://colab.research.google.com/), so I will further talk you through the steps to run this script on Colab Notebook.

It's a plug & play script and you just need to change **/path/to/save/folder/** with the path of where you want to download the information.

# Requirements
- `Python3`
- `os`
- `numpy`
- `pandas`
- `requests`
- `lxml`
- `fake-headers`

# Install
Run this on Google colab line by line
```bash
!pwd
```
Output should be **/content**
```bash
!git clone https://github.com/ohlc-ai/nse-yahoo-finance-scraper.git
```
```bash
%cd /content/nse-yahoo-finance-scraper
```
Voila! You are in repo's directory.

```bash
pip install -r requirements.txt
```
Now that all the required libraries are installed, it's time to change the download path and run the whole script finally! Expand the nse-yahoo-finance-scraper folder and:

1. If you wish to scrape data for only **one symbol**, double click on financial_st_scraper.py. A new tab will open the file. Search for /path/to/save/folder/ and replace it with /content/nse-yahoo-finance-scraper/. Change `symbol = 'RELIANCE'` with the symbol of your choice. Changes will be saved automatically.

Close the tab and run
```bash
!python financial_st_scraper.py
```
It will create a folder with the symbol name inside /content/nse-yahoo-finance-scraper. In the folder you will find all the scraped information in a clean csv format.

2. If you wish to scrape data for only **multiple symbols**, double click on financial_st_scraper_multiple.py. A new tab will open the file. Search for /path/to/save/folder/ and replace it with /content/nse-yahoo-finance-scraper/.
By default, the script has a list of symbols of NIFTY500 companies. You can add/remove symbols of your choice. Changes will be saved automatically.

Close the tab and run
```bash
!python financial_st_scraper_multiple.py
```
It will start creating folders dynamically inside /content/nse-yahoo-finance-scraper. Folder will be created with the symbols passed in`symbol = []` In each folder you will find all the scraped information in a clean csv format of the particular company.

Please don't use more than 30-40 symbols at a time. It is recommended lest you should get blocked by Yahoo. The script generates random proxies using fake-headers library, but don't misuse it for scraping unnecessary data.

### Downloading on Google Drive
If you are planning to utilise the data for future use, consider downloading it on Google Drive. We will mount our Google drive on this notebook so that data could be directly downloaded. To do that, click on the Google Drive icon. It will ask for permission to mount the drive. Click on **Connect to Google Drive** to grant access.

Once Google Drive is mounted, you will see another directory - **drive**. Expand drive folder and you will probably have **My Drive** folder in it. You can create a new directory inside. I'm creating a new directory named **Companies**

My Google Drive directory structure now looks like /content/drive/My Drive/Companies

From here, you just need to repeat Step 1 or 2 to replace /path/to/save/folder/ with /content/drive/My Drive/Companies/

After running the script, all the information would be downloaded directly to your Google Drive.



![Powered by Python](https://raw.githubusercontent.com/willtheorangeguy/Python-Logo-Widgets/master/pythonpoweredlengthgif.gif)

### Contact

**Issues should be raised directly in the repository.** For additional questions or comments please email me at mohit@ohlc.ai
