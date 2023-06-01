from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

import os
import time
import wget

options  = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome('/home/dell/Work/instagram-scrapper/instagram_scrapper/chromedriver_linux64', options = options)
driver.get('https://www.instagram.com/')

time.sleep(1)


username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

username.clear()
password.clear()

time.sleep(1)


username.send_keys('test.omer100')
password.send_keys('Spider12')

time.sleep(1)

log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
time.sleep(5)
# try:
# not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Not Now')]"))).click()
# //button[contains(text(),'Not Now')]
# except:
    # print('some error')

# while True:
#     pass
users = ['cristiano','jlo','rubab.khan32']
for user in users:
    driver.get('https://www.instagram.com/' + user)
    # desc = driver.find_element(By.XPATH, '//*[@id="mount_0_0_YO"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/div[1]/h1')
    # desc = driver.find_element(By.XPATH, '//*[@id="mount_0_0_GO"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[3]/a[1]/div')
    time.sleep(5)
    try:
        desc = driver.find_element(By.XPATH, '//h1[@class="_aacl _aaco _aacu _aacx _aad6 _aade"]').text
    except:
        print('no desc')
        desc = ''
    try:
        website = driver.find_element(By.XPATH, '//div[@class="_aacl _aaco _aacw _aacz _aada _aade"]').text
    except:
        print('no website')
        website = ''
    # print(desc.text)
    try:
        posts = driver.find_elements(By.XPATH, '//div[@class="_ac7v  _al3n"]//a')
    except:
        posts = None

    # driver.execute_script("window.scrollTo(0,100)")


    ul = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.TAG_NAME, "ul"))).text
    print(user)
    print(desc)
    print(website)
    print(ul)
    # driver.get('https://www.instagram.com/' + 'cristiano')
    time.sleep(5)
    # images = driver.find_elements(By.XPATH, "//img[@class='x5yr21d xu96u03 x10l6tqk x13vifvy x87ps6o xh8yej3']")
    # my_images = set()
    # for image in images:
    #     source = image.get_attribute('src')
    #     my_images.add(source)

    # for image in my_images:
    #     wget.download(image,"/home/dell/Downloads")

    links = []
    for i in range(len(posts)):
        links.append(posts[i].get_attribute('href'))


    if links:
        for ele in links:
            # post_link = ele.get_attribute('href')
            driver.get(ele)
            try:
                post_desc = WebDriverWait(driver, timeout=3).until(lambda d: d.find_element(By.XPATH, '//h1[@class="_aacl _aaco _aacu _aacx _aad7 _aade"]')).text
                print(post_desc)
            except:
                post_desc = ''
            image = WebDriverWait(driver, timeout=3).until(lambda d: d.find_element(By.XPATH, "//img[@class='x5yr21d xu96u03 x10l6tqk x13vifvy x87ps6o xh8yej3']"))
            source = image.get_attribute('src') 
            wget.download(source,"/home/dell/Downloads")
            driver.get('https://www.instagram.com/' + user)
            # my_images = set()
            # for image in images:
            #     source = image.get_attribute('src')
            #     my_images.add(source)

# items = driver.find_element(By.TAG_NAME, 'li')
# items = [items.get_attribute('li')]
# print(items)
# items = 
# for li in items:
#     print(li.text)