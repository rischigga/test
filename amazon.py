from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

url = "https://www.amazon.com/"
driver.get(url)

time.sleep(2)
driver.find_element("id", "twotabsearchtextbox").send_keys("computer")
driver.find_element("id", "nav-search-submit-button").click()

time.sleep(2)
driver.find_element("id", "twotabsearchtextbox").send_keys("HP Elite Desktop PC Computer Intel Core i5 3.1-GHz, 8 gb Ram, 1 TB Hard Drive, DVDRW, 19 Inch LCD Monitor, Keyboard, Mouse, Wireless WiFi, Windows 10 (Renewed)")
driver.find_element("id", "nav-search-submit-button").click()

image = driver.find_element(By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div[1]/div/div[2]/div/span/a/div/img')
image.click()
time.sleep(2)

time.sleep(2)
combobox = driver.find_element(By.XPATH, '//*[@id="a-autoid-0-announce"]')
combobox.click()

time.sleep(2)
qty = driver.find_element(By.XPATH, '//*[@id="quantity_9"]')
qty.click()

time.sleep(2)
add = driver.find_element(By.XPATH, '//*[@id="add-to-cart-button"]')
add.click()

time.sleep(2)
cart = driver.find_element(By.XPATH, '//*[@id="sw-gtc"]/span/a')
cart.click()

time.sleep(2)
delete = driver.find_element(By.XPATH, '//*[@id="sc-active-Cc30d3cc3-c386-4e76-9f87-dd7516828084"]/div[4]/div/div[2]/div[1]/span[2]/span/input')
delete.click()

time.sleep(2)
deleted = driver.find_element(By.XPATH, '//*[@id="sc-active-cart"]/div/div/div/h1')