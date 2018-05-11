from selenium import webdriver

chromedriver = 'D:\Python\Django\chromedriver.exe'
browser  = webdriver.Chrome(chromedriver)
browser.get('http://localhost:8000')

assert 'Django' in browser.title
