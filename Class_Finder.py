
def class_enterer():
    from selenium import webdriver
    from time import sleep
    from datetime import datetime
    from pynput.mouse import Controller, Button
    import pynput.keyboard

    # Get into the website
    chromedriver = "D:/Ran/Programing/Whatsapp/chromedriver_win32/chromedriver"
    driver = webdriver.Chrome(chromedriver)
    driver.get('https://teams.microsoft.com/_#/school//?ctx=teamsGrid')
    # Wait until it's loaded
    sleep(3)
    driver.maximize_window()
    # Write email and get into the Eduil login site
    user = driver.find_element_by_xpath("//input[@type='email' and @id='i0116']")
    user.send_keys('ran.gideon.haber@kfaryarok.eduil.org')
    clicker = driver.find_element_by_xpath("//input[@type='submit' and @id='idSIButton9']")
    clicker.click()
    sleep(11)
    user = driver.find_element_by_xpath("//button[@class='btn btn-sso' and @type='button']")
    user.click()
    # Writing email and password
    user = driver.find_element_by_xpath("//input[@type='text' and @id='HIN_USERID']")
    user.send_keys('4006342')
    user = driver.find_element_by_xpath(
        "//input[@type='password' and @class='capslock-msg prevent-heb' and @placeholder='סיסמה']")
    user.send_keys('Ranoz2006')
    # Get into Teams
    user = driver.find_element_by_xpath("//button[@class='submit user-pass-submit' and @type='button']")
    user.click()
    user = driver.find_element_by_xpath("//input[@id='KmsiCheckboxField' and @type='checkbox']")
    user.click()
    user = driver.find_element_by_xpath("//input[@id='idBtn_Back' and @type='button' and @value='לא']")
    user.click()
    user = driver.find_element_by_xpath("//a[@class='use-app-lnk' and @data-tid='early-desktop-promo-use-web']")
    user.click()
    sleep(7)

    # Get into the right team by day
    today = datetime.now().weekday()
    print(today)
    if today == 6:
        # Class finder
        user = driver.find_element_by_xpath(
            "//profile-picture[@class='profile-picture-style' and @title='ט/2 - הבעה ולשון']")
        user.click()
        # Find the last post in team
        user = driver.find_elements_by_xpath("//div[@class='title' and @title='Join our Cloud HD Video Meeting' and "
                                             "@ng-if='upc.urlPreview.title' and @data-tid='urlPreviewTitle']")[-1]
        user.click()
        # Define things for pynput
        mouse = Controller()
        keyboard = pynput.keyboard.Controller()
        # Sleep and maximize chrome
        sleep(4)
        driver.maximize_window()
        # Open zoom class
        mouse.position = (849, 225)
        mouse.click(Button.left, 1)
        # Wait for entering class
        sleep(120)
        # Click on the screen
        mouse.position = (1148, 674)
        mouse.click(Button.left, 1)
        # Open Chat
        keyboard.press(pynput.keyboard.Key.alt)
        sleep(0.12)
        keyboard.press('h')
        sleep(1)
        keyboard.release(pynput.keyboard.Key.alt)
        keyboard.release('H')
        # Write a costume line
        sentence = "היי אביגיל, אני כאן פשוט המיקרופון שלי נהרס"
        for char in sentence:
            keyboard.press(char)
            keyboard.release(char)
            sleep(0.12)
        keyboard.press(pynput.keyboard.Key.enter)
    elif today == 0:
        pass
    elif today == 1:
        pass
    elif today == 2:
        user = driver.find_element_by_xpath(
            "//profile-picture[@class='profile-picture-style' and @title='ט2 ספרות']")
        user.click()
        user = driver.find_elements_by_xpath(
            "//div[@class='title' and @title='Join our Cloud HD Video Meeting' and @ng-if='upc.urlPreview.title' and @data-tid='urlPreviewTitle']")[
            -1]
        user.click()
        # Define things for pynput
        mouse = Controller()
        keyboard = pynput.keyboard.Controller()
        # Sleep and maximize chrome
        sleep(4)
        driver.maximize_window()
        # Open zoom class
        mouse.position = (849, 225)
        mouse.click(Button.left, 1)
        # Wait for entering class
        sleep(120)
        # Click on the screen
        mouse.position = (1148, 674)
        mouse.click(Button.left, 1)
        # Open Chat
        keyboard.press(pynput.keyboard.Key.alt)
        sleep(0.12)
        keyboard.press('h')
        sleep(1)
        keyboard.release(pynput.keyboard.Key.alt)
        keyboard.release('H')
        # Write a costume line
        sentence = "היי עודד, אני כאן פשוט המיקרופון שלי נהרס"
        for char in sentence:
            keyboard.press(char)
            keyboard.release(char)
            sleep(0.12)
        keyboard.press(pynput.keyboard.Key.enter)
    elif today == 3:
        user = driver.find_element_by_xpath(
            "//profile-picture[@class='profile-picture-style' and @title='כיתה ט2 ערבית']")
        user.click()
        user = driver.find_elements_by_xpath("//div[@class='title' and @title='Join our Cloud HD Video Meeting' and "
                                             "@ng-if='upc.urlPreview.title' and @data-tid='urlPreviewTitle']")[-1]
        user.click()
        # Define things for pynput
        mouse = Controller()
        keyboard = pynput.keyboard.Controller()
        # Sleep and maximize chrome
        sleep(4)
        driver.maximize_window()
        # Open zoom class
        mouse.position = (849, 225)
        mouse.click(Button.left, 1)
        # Wait for entering class
        sleep(120)
        # Click on the screen
        mouse.position = (1148, 674)
        mouse.click(Button.left, 1)
        # Open Chat
        keyboard.press(pynput.keyboard.Key.alt)
        sleep(0.12)
        keyboard.press('h')
        sleep(1)
        keyboard.release(pynput.keyboard.Key.alt)
        keyboard.release('H')
        # Write a costume line
        sentence = "היי לימור, אני כאן פשוט המיקרופון שלי נהרס"
        for char in sentence:
            keyboard.press(char)
            keyboard.release(char)
            sleep(0.12)
        keyboard.press(pynput.keyboard.Key.enter)
        pass
