from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random
import time
from string import ascii_letters

ym = time.strftime("%Y-%m-%H-%M-%S")
steps = []
f = open(ym + '.txt', 'w')


def click_link():
    script = "let el = document.createElement('div'); el.innerHTML='"+ (" → ").join(steps)+"'; el.style.position = 'fixed';el.style.zIndex = '999999';el.style.left = '0';el.style.top = '0';el.style.width = 'calc(20% - 5rem)';el.style.height='calc(100vh - 5rem)';el.style.padding='2.5rem';el.style.background = '#fff';el.style.lineHeight = '2';el.style.fontWeight='bold';el.style.color='black';el.style.textShadow='2px 2px 10px yellow';el.style.fontSize='12px';document.body.prepend(el);"
    time.sleep(3)
    driver.execute_script(script)
    print(steps)
    els = driver.find_elements(By.CSS_SELECTOR, "#mw-content-text .mw-content-ltr > p > a")
    if len(els) > 0:
        integer = random.randint(0, len(els)-1)
        driver.execute_script("document.querySelectorAll('#mw-content-text p > a')[" + str(integer) + "].style.background='yellow';")
        driver.execute_script("document.querySelectorAll('#mw-content-text p > a')[" + str(integer) + "].style.fontSize='24px';")
        driver.execute_script("document.querySelectorAll('#mw-content-text p > a')[" + str(integer) + "].style.scrollMargin='300px';")
        driver.execute_script("document.querySelectorAll('#mw-content-text p > a')[" + str(integer) + "].scrollIntoView({ behavior: 'smooth', block: 'end', inline: 'nearest' });")
        steps.append(els[integer].get_attribute('innerHTML'))
        f.write(('->').join(steps))
        url = els[integer].get_attribute('href')
        time.sleep(2)
        driver.get(url)
        click_link()
    else:
        del steps[-1]
        driver.execute_script("window.history.go(-1)")
        click_link()

driver = webdriver.Firefox()
driver.get("https://en.wikipedia.org/wiki/Main_Page")
start = driver.find_element(By.CSS_SELECTOR, "#mp-tfa > p > b > a")
steps.append(start.get_attribute('innerHTML'))
url = start.get_attribute('href')
driver.get(url)
click_link()

driver.close()