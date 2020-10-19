import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

import urllib.request
import os

dir_path = "D:\\Jen\\Documents\\Dissertation\\when\\"
file_name = "bee"

def download_image(url, num):
    print("[INFO] downloading {}".format(url))
    name = str(url.split('/')[-1])
    urllib.request.urlretrieve(url, dir_path + file_name + str(num) + ".jpg")

def get_bee_data(num):
        for image in driver.find_elements(By.CLASS_NAME, "fancybox"):
            download_image(image.get_attribute("href"), num)
            num += 1
        return num

with webdriver.Firefox() as driver:
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.brc.ac.uk/irecord")
    driver.find_element(By.ID, "edit-name").send_keys("jmollett1@sheffield.ac.uk" + Keys.TAB)
    driver.find_element(By.ID, "edit-pass").send_keys(password + Keys.ENTER)
    time.sleep(15)
    driver.find_element(By.ID, "menu-3718-1").click()#send_keys("m.t.smith@sheffield.ac.uk" + Keys.TAB)    
    time.sleep(1)
    #first_result = wait.until(presence_of_element_located((By.ID, "menu-3718-1")))
    driver.find_element(By.ID, "menu-1112-1").click()
    time.sleep(1)
    driver.find_element(By.ID, "filter-build").click()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "fb-filter-link").click()
    time.sleep(1)
    driver.find_element(By.ID, "ui-id-2").click()
    time.sleep(1)
    driver.find_element(By.ID, "taxa_taxon_list_list:search:searchterm").send_keys("Bombus")
    time.sleep(1)
    driver.find_element(By.ID, "taxa_taxon_list_list:search:searchterm").send_keys(Keys.ENTER)
    time.sleep(1)
    driver.find_element(By.ID, "taxa_taxon_list_list:add").click()
    time.sleep(1)
    #driver.find_element_by_xpath("//div[@id='what-tabs']/button[@class='fb-apply']").click()
    driver.find_element_by_xpath("//div[@id='controls-filter_what']/form[@class='filter-controls']/fieldset/button[@class='fb-apply']").click()
    #driver.find_element(By.ID,"controls-filter_what").find_element(By.CLASS_NAME, "fb-apply").click()
    time.sleep(1)
    driver.find_element_by_xpath('//a[contains(@href,"#controls-filter_when")]').click()
    time.sleep(1)
    driver.find_element(By.ID, "date_from").send_keys("15/10/2020" + Keys.ENTER)
    time.sleep(1)
    driver.find_element(By.ID, "date_to").send_keys("16/10/2020" + Keys.ENTER)
    time.sleep(1)
    driver.find_element_by_xpath("//div[@id='controls-filter_when']/form[@class='filter-controls']/fieldset/button[@class='fb-apply']").click()
    time.sleep(15)
    image_num = 1
    image_num = get_bee_data(image_num)
    page_num = 2
    while driver.find_elements(By.ID, "page-report-grid-0-" + str(page_num)): #checks if there are any pages left
        driver.find_element(By.ID, "page-report-grid-0-" + str(page_num)).click()
        time.sleep(15)
        image_num = get_bee_data(image_num)
        page_num += 1