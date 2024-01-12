from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Keep Chrome browser open after program finished
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

# Create and configure the Chrome Webdriver
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

# Navigate to where you want
driver.get("https://orteil.dashnet.org/experiments/cookie/")

count = 0
sleep(3)
while True:
    # Find the cookie and click
    cookie = driver.find_element(By.ID, value="cookie")
    for x in range(100):
        cookie.click()

    # Find how much money/cookies I have
    money = int(driver.find_element(By.ID, value="money").text.replace(",", ""))

    # find the upgrades
    buy_cursor = driver.find_element(By.ID, value="buyCursor")
    buy_grandma = driver.find_element(By.ID, value="buyGrandma")
    buy_factory = driver.find_element(By.ID, value="buyFactory")
    buy_mine = driver.find_element(By.ID, value="buyMine")
    buy_shipment = driver.find_element(By.ID, value="buyShipment")
    buy_alchemy = driver.find_element(By.ID, value="buyAlchemy lab")
    buy_portal = driver.find_element(By.ID, value="buyPortal")
    buy_timemachine = driver.find_element(By.ID, value="buyTime machine")
    # buy_elderpledge = driver.find_element(By.ID, value="buyElder Pledge")

    # variables receiving int numbers to compare
    value_cursor = int(buy_cursor.text.split()[2].replace(",", ""))
    value_grandma = int(buy_grandma.text.split()[2].replace(",", ""))
    value_factory = int(buy_factory.text.split()[2].replace(",", ""))
    value_mine = int(buy_mine.text.split()[2].replace(",", ""))
    value_shipment = int(buy_shipment.text.split()[2].replace(",", ""))
    value_alchemy = int(buy_alchemy.text.split()[3].replace(",", ""))
    value_portal = int(buy_portal.text.split()[2].replace(",", ""))
    value_timemachine = int(buy_timemachine.text.split()[3].replace(",", ""))
    # value_elderpledge = buy_elderpledge.text

    # Find cps (cookie per second)
    cps = driver.find_element(By.ID, value="cps").text
    count += 1
    print(f"I have {cps} now. It's the run number {count}")

    # Try to buy the most expensive things first
    if money > value_timemachine:
        buy_timemachine.click()
    elif money > value_portal:
        buy_portal.click()
    elif money > value_alchemy:
        buy_alchemy.click()
    elif money > value_shipment:
        buy_shipment.click()
    elif money > value_mine:
        buy_mine.click()
    elif money > value_factory:
        buy_factory.click()
    elif money > value_grandma:
        buy_grandma.click()
    elif money > value_cursor:
        buy_cursor.click()

# driver.quit()
