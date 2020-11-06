from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

<<<<<<< HEAD

i = 0
while True:
    for i in range(50):
        driver = webdriver.Firefox()
        driver.get("https://afazenda.r7.com/a-fazenda-12/votacao")
        # assert "Python" in driver.title
        time.sleep(3)
        elem = driver.find_element_by_class_name("voting-button--hidden").click()
        time.sleep(2)
        try:
            elem = driver.find_element_by_xpath('//*[@id="593"]').click()
            time.sleep(1)
        except:
            continue
        try:
            elem = driver.find_element_by_xpath("//button[@class='voting-button voting-button--medium disabled']").click()
            time.sleep(1)
        except:
            continue
        i = i+1
        print(i)
        driver.close()

=======
driver = webdriver.Firefox()
driver.get("https://afazenda.r7.com/a-fazenda-12/votacao")
#assert "Python" in driver.title
time.sleep(3)
elem = driver.find_element_by_class_name("voting-button--hidden").click()
time.sleep(1)
i= 0

while True:
    elem = driver.find_element_by_xpath('//*[@id="463"]').click()
    time.sleep(0.5)
    elem = driver.find_element_by_xpath("//button[@class='voting-button voting-button--medium disabled']").click()
    time.sleep(0.5)
    elem = driver.find_element_by_xpath("//button[@data-element='button-vote-again']").click()
    time.sleep(1)
    i += 1 
    print(i)
>>>>>>> ad4105ea8502ed28262db3d6bd244c22a082362d
# elem = driver.find_element_by_class_name("voting-button voting-button--medium disabled").click()


elem.clear()

elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()