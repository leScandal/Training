            driver.find_element_by_link_text(StringName[j]).click() #выбор откgытки
            driver.implicitly_wait(max_wait_sec)
            try:
              WebDriverWait(driver, max_wait_sec).until(EC.presence_of_element_located((By.XPATH, "//input[@name='contacts-from-list']")))
            except:
              print('exception')
              driver.find_element_by_xpath("//input[@id='group-checkbox-"+ contactId + "']").click()
              driver.find_element_by_xpath("//input[@id='group-checkbox-" + contactId + "']").click()
#              clickIfSelected(driver.find_element_by_id("group-checkbox-" + contactId))
                #driver.find_element_by_id("group-checkbox-" + contactId).click()
              driver.find_element_by_xpath("//button[text()='Send']").click()
              #driver.find_element_by_scc_selector("//a[@href='javascript:doSend(true);']").click()
              WebDriverWait(driver, max_wait_sec).until(EC.alert_is_present())
              driver.switch_to_alert().accept()
              driver.implicitly_wait(max_wait_sec)
              driver.find_element_by_xpath("//a[@href='javascript:back()']").click()
              j=j+1
            driver.find_element_by_xpath("//a[@href='javascript:doSend(true);']").click()
            WebDriverWait(driver, max_wait_sec).until(EC.alert_is_present())
            driver.switch_to_alert().accept()
            # alert.accept()
            # WebDriverWait(driver, max_wait_sec).until(EC.visibility_of_element_located((By.XPATH, "//a[@href='javascript:back();']")))
            driver.implicitly_wait(max_wait_sec)
            driver.find_element_by_xpath("//a[@href='javascript:back()']").click()