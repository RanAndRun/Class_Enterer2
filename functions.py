def Literature_Class():
    from selenium import webdriver
    from pynput.mouse import Controller, Button
    from time import sleep
    import pynput.keyboard
    chromedriver = "D:/Ran/Programing/Whatsapp/chromedriver_win32/chromedriver"
    driver = webdriver.Chrome(chromedriver)

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

def Hebrew_Class():
    from selenium import webdriver
    import pynput.keyboard
    from pynput.mouse import Controller, Button
    from time import sleep
    chromedriver = "D:/Ran/Programing/Whatsapp/chromedriver_win32/chromedriver"
    driver = webdriver.Chrome(chromedriver)

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


def Arabic_Class():
    from selenium import webdriver
    from pynput.mouse import Controller, Button
    from time import sleep
    import pynput.keyboard
    chromedriver = "D:/Ran/Programing/Whatsapp/chromedriver_win32/chromedriver"
    driver = webdriver.Chrome(chromedriver)
    user = driver.find_element_by_xpath("//profile-picture[@class='profile-picture-style' and @title='כיתה ט2 ערבית']")
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


def Time_Left_For_Sleep(wake_up_hour, wake_up_min, wake_up_sec):
    from time import sleep
    from datetime import datetime
    now = datetime.now()
    hour = now.strftime("%H")
    min = now.strftime("%M")
    sec = now.strftime("%S")
    hour = int(hour)
    min = int(min)
    sec = int(sec)
    til_sec = 60 - sec + wake_up_sec
    til_min = (60 - min + wake_up_min) * 60
    til_hour = (24 - hour + wake_up_hour)
    til_hour = til_hour * 3600
    time_left = til_sec + til_min + til_hour
    sleep(time_left)

# def Art_Class():
#     from selenium import webdriver
#     from pynput.mouse import Controller, Button
#     from time import sleep
#     chromedriver = "D:/Ran/Programing/Whatsapp/chromedriver_win32/chromedriver"
#     driver = webdriver.Chrome(chromedriver)
#     user = driver.find_element_by_xpath("//img[@src='https://teams.microsoft.com/api/mt/part/emea-02/beta/teams/d02d4667-20b6-4920-98b0-bb491f93397f/profilepicturev2?etag=\"61CA4ACC\"&displayName=ט2&size=HR96x96&highResolution=true&voidCache=true']")
#
#     user.click()
#     user = driver.find_elements_by_xpath("//div[@class='title' and @title='Join our Cloud HD Video Meeting' and "
#                                   "@ng-if='upc.urlPreview.title' and @data-tid='urlPreviewTitle']")[-1]
#     user.click()
#
#     sleep(4)
#     driver.maximize_window()
#
#     mouse = Controller()
#     loc_open = (849, 225)
#     mouse.position = loc_open
#     mouse.click(Button.left, 1)

