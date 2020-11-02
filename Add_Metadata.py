
dir_path = "D:\\Jen\\Documents\\Dissertation\\"
csv_path = dir_path + "Bee_Data_Test.csv"
new_csv_path = dir_path + "Bee_Data_with_metadata.csv"

with webdriver.Firefox() as driver:
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.brc.ac.uk/irecord")
    driver.find_element(By.ID, "edit-name").send_keys("jmollett1@sheffield.ac.uk" + Keys.TAB)
    driver.find_element(By.ID, "edit-pass").send_keys(password + Keys.ENTER)
    time.sleep(15)
    with open(csv_path, 'r', newline='') as f:
        with open(new_csv_path, 'w', newline='') as f_new:
            beereader = csv.reader(f)
            beewriter = csv.writer(f_new)
            for row in beereader:
                driver.get("https://www.brc.ac.uk/irecord/record-details?occurrence_id=" + row[0])
                time.sleep(5)
                #print(driver.find_element_by_xpath("//*[@id='detail-panel-recorddetails']/div[1]/dd[8]").text)
                labels = ["EUNIS Habitat", "Stage", "Sex", "Quantity", "Certainty", "Record status"]
                details = {"Record status": "", "EUNIS Habitat": "", "Stage": "", "Certainty": "", "Sex": "", "Quantity": ""}
                found = False
                categories = driver.find_elements(By.CLASS_NAME, "record-details-fields")
                elements = categories[0].find_elements_by_xpath(".//*") + categories[1].find_elements_by_xpath(".//*")
                for element in elements:
                    if found:
                        details[found] = element.text
                        found = False
                    if element.text in labels:
                        found = element.text
                for label in labels:
                    row.append(details[label])
                beewriter.writerow(row)