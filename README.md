![Cookie Image](Cookie_Clicker_cover.jpg)

# Cookie Clicker Automation! 🍪

## Overview

This Python script utilizes the Selenium WebDriver to automate interactions with the "Cookie Clicker" web-based game. The script continuously clicks on the cookie, accumulates in-game currency (cookies), and purchases upgrades to increase the overall cookie production rate.

## Requirements

- Python 3.x
- Selenium library (`pip install selenium`)
- Chrome WebDriver (Make sure it matches your Chrome browser version)

## Usage

1. Clone or download the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Ensure that the Chrome WebDriver executable is in your system's PATH or provide the correct path in the script.
4. Run the script using `python cookie_clicker_automation.py`.

## Script Details

### WebDriver Configuration

The script uses the Selenium WebDriver with Chrome to interact with the web page. The `chrome_options` are configured to keep the Chrome browser open after the program finishes execution.

```python
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)
```

## Main Automation Loop
The script enters a continuous loop, clicking the cookie and purchasing upgrades based on the available in-game currency (money). The loop will run indefinitely until manually terminated.

## Upgrade Variables
Variables are used to store the cost of different upgrades for comparison and purchase decisions.

## Upgrade Purchase Logic
The script attempts to buy the most expensive upgrades first, based on the available in-game currency.

# Important Note
Ensure that you comply with the game's terms of service and the website. Automated interactions may violate terms of service, and usage of this script is at your own risk.

### My record
I have cookies/second : 2,931.6 cookies/second now. It's run number 3600
