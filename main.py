from selenium import webdriver

from Nasdaq import Nasdaq


def get_ticker():
    ticker_input = input("Please enter a ticker symbol: ")
    return ticker_input


# this prevents chrome from auto closing
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
nasdaqObject = Nasdaq()
ticker = get_ticker()

# The ChromeDriver is in my x86 folder. Either place yours there as well
# or change the path variable so that it works for you.
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH, options=options)

driver.maximize_window()

# nasdaq stock financials
target_site = nasdaqObject.financials(ticker)
driver.get(target_site)

target_site2 = nasdaqObject.earnings(ticker)
driver.get(target_site2)


# to-do:
# 1. error handling if incorrect ticker is put into the program.
# 2. hard coded file path may be a problem, think of a fix maybe
# 3. valid user input


