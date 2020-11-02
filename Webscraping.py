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

dir_path = "D:\\Jen\\Documents\\Dissertation\\Bee_Data\\"
file_name = "bee"
image_num = 8588

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
        #for image in driver.find_elements(By.CLASS_NAME, "fancybox"):
            #download_image(image.get_attribute("href"), num)
            #num += 1
        no_image = False
        table = driver.find_element(By.ID, "report-grid-0")
        csv_path = dir_path + "Bee_Data.csv"
        with open(csv_path, 'a', newline='') as f:
            beewriter = csv.writer(f)
            for row in table.find_elements(By.TAG_NAME, "tr"):
                row_list = []
                if ("empty-row" != row.get_attribute("class")) and ("row18084047" != row.get_attribute("class")):
                    for cell in row.find_elements(By.TAG_NAME, "td"):
                        if "col-images" in cell.get_attribute("class"):
                            image = cell.find_element(By.CLASS_NAME, "fancybox")
                            if row_list[0] not in ["14537123", "14537122", "14537121", "14537119"]:
                                no_image = download_image(image.get_attribute("href"), num)
                            else:
                                no_image = True
                            image_name = "bee" + str(num)
                            row_list.append(image_name)
                            if not no_image:
                                num += 1
                        elif ("col-actions" not in cell.get_attribute("class")) and ("footable-visible" != cell.get_attribute("class")):
                            row_list.append(cell.text)
                if not no_image:
                    beewriter.writerow(row_list)
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
    driver.find_element_by_xpath('//a[contains(@href,"#controls-filter_quality")]').click()
    time.sleep(1)
    Select(driver.find_element(By.NAME, "has_photos")).select_by_visible_text('Only include records which have photos')
    time.sleep(1)
    driver.find_element_by_xpath("//div[@id='controls-filter_quality']/form[@class='filter-controls']/fieldset/button[@class='fb-apply']").click()
    time.sleep(1)

    driver.find_element_by_xpath('//a[contains(@href,"#controls-filter_when")]').click()
    time.sleep(1)
    driver.find_element(By.ID, "date_from").send_keys("1/12/2019" + Keys.ENTER)
    time.sleep(1)
    driver.find_element(By.ID, "date_to").send_keys("31/12/2019" + Keys.ENTER)
    time.sleep(1)
    driver.find_element_by_xpath("//div[@id='controls-filter_when']/form[@class='filter-controls']/fieldset/button[@class='fb-apply']").click()

    input("Press Enter to continue...")
    image_num = get_bee_data(image_num)
    page_num = 2
    while driver.find_elements(By.ID, "page-report-grid-0-" + str(page_num)): #checks if there are any pages left
        driver.find_element(By.ID, "page-report-grid-0-" + str(page_num)).click()
        time.sleep(15)
        image_num = get_bee_data(image_num)
        page_num += 1