from selenium import webdriver
import unittest
import time

tc = unittest.TestCase('__init__')

driver = webdriver.Chrome("D:\AutomationProjectsGit\PythonWebTest\AutomationPracticePageProject\Test\chromedriver.exe")

driver.get('http://www.automationpractice.com/index.php')

driver.find_element_by_id('search_query_top').send_keys('hola')
time.sleep(2)

driver.find_element_by_name('submit_search').click()
time.sleep(2)

tc.assertEqual('No results were found for your search "hola"',driver.find_element_by_xpath('//p[@class="alert alert-warning"]').text)

driver.close()#Cierra el browser
driver.quit()#Cierra el webdriver
