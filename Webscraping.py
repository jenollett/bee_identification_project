import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import os
import urllib.request
from urllib.error import HTTPError

dir_path = "D:\\Jen\\Documents\\Dissertation\\Bee_Data_2\\"
file_name = "bee"
image_num = 1

def download_image(url, num):
    print("[INFO] downloading {}".format(url))
    name = str(url.split('/')[-1])
    no_image = False
    try:
        urllib.request.urlretrieve(url, dir_path + file_name + str(num) + ".jpg")
    except HTTPError as err:
        if err.code == 404:
            no_image = True
        else:
            raise
    return no_image

def get_bee_data(num):
        no_image = False
        table = driver.find_element(By.ID, "explore-records-grid")
        csv_path = dir_path + "Bee_Data.csv"
        with open(csv_path, 'a', newline='') as f:
            beewriter = csv.writer(f)
            for row in driver.find_elements(By.CLASS_NAME, "data-row"):
                row_list = []
                if ("empty-row" != row.get_attribute("class")) and ("row18084047" != row.get_attribute("class")):
                    for cell in row.find_elements(By.TAG_NAME, "td"):
                        if "col-12" in cell.get_attribute("class"):
                            image = cell.find_element(By.CLASS_NAME, "fancybox")
                            if row_list[0] not in ["18084047", "12597517", "12504393", "12501491"]:
                                no_image = download_image(image.get_attribute("href"), num)
                            else:
                                no_image = True
                            image_name = "bee" + str(num)
                            row_list.append(image_name)
                            if not no_image:
                                num += 1
                        elif not(any(i in cell.get_attribute("class") for i in ["col-2", "col-5", "col-11", "col-actions"])) and ("footable-visible" != cell.get_attribute("class")):
                            row_list.append(cell.text)
                if (not no_image) and (row_list):
                    try:
                        beewriter.writerow(row_list[2:])
                    except:
                        num -=1
        return num

with webdriver.Firefox() as driver:
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.brc.ac.uk/irecord")
    driver.find_element(By.ID, "edit-name").send_keys("jmollett1@sheffield.ac.uk" + Keys.TAB)
    driver.find_element(By.ID, "edit-pass").send_keys(password + Keys.ENTER)
    time.sleep(5)
    driver.get("https://www.brc.ac.uk/irecord/all-records")
    time.sleep(5)
    driver.find_element(By.ID, "filter-build").click()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "fb-filter-link").click()
    time.sleep(1)
    driver.find_element(By.ID, "ui-id-2").click()
    time.sleep(1)
    driver.find_element(By.ID, "taxa_taxon_list_list:search:searchterm").send_keys("Bombus")
    time.sleep(3)
    driver.find_element(By.ID, "taxa_taxon_list_list:search:searchterm").send_keys(Keys.ENTER)
    time.sleep(1)
    driver.find_element(By.ID, "taxa_taxon_list_list:add").click()
    time.sleep(1)
    #driver.find_element_by_xpath("//div[@id='what-tabs']/button[@class='fb-apply']").click()
    driver.find_element_by_xpath("//div[@id='controls-filter_what']/form[@class='filter-controls']/fieldset/button[@class='fb-apply']").click()
    #driver.find_element(By.ID,"controls-filter_what").find_element(By.CLASS_NAME, "fb-apply").click()
    time.sleep(1)
    driver.find_element_by_xpath('//a[contains(@href,"#controls-filter_quality")]').click()
    time.sleep(1)
    Select(driver.find_element(By.NAME, "has_photos")).select_by_visible_text('Only include records which have photos')
    time.sleep(1)
    driver.find_element_by_xpath("//div[@id='controls-filter_quality']/form[@class='filter-controls']/fieldset/button[@class='fb-apply']").click()
    time.sleep(1)

    input("Press Enter to continue...")
    image_num = get_bee_data(image_num)
    while driver.find_element(By.CLASS_NAME, "next").is_enabled(): #checks if there are any pages left
        driver.find_element(By.CLASS_NAME, "next").click()
        time.sleep(30)
        image_num = get_bee_data(image_num)