import time
import os
import webbrowser

today = time.ctime()
print(today)
name = input("Hello My Name is Ammi what's your name : ")
print(f"Hello {name}\n")

services = "\nOpen Whatsapp\nOpen Facebook\nSearch\nMake me Laugh\nSearch Image\n"
serv = {"open whatsapp": "https://web.whatsapp.com/", "open facebook": "https://www.facebook.com/",
        "search": "google search", "make me laugh": "https://www.google.co.in/search?q=jokes&hl=en&tbm=isch",
        "search image": "Which Image", }

bot = {
    "who are you?": "My name is Ammi! I am your personal ChatBot",
    "how are you?": "absolutely fine! What about you?",
    "services": "I provide theses services :\n" + services,
    "father of python": "Guido van Rossum is known as Father of Python Programming language",
    "what kind of music do you like?": "i love rock music",
    "today's date and time": today,
    "what type of language you use?": "English! and I was written in Python Programming language.",
}

while True:

    ques = input("How can I help you " + name + " : ")
    ques = ques.lower()
    if (ques == "quit"):
        print("See you soon, Bye")
        break

    elif ques in bot.keys():
        print(bot[ques])

    elif ques in serv.keys():
        if ques == "search":
            webbrowser.open("https://www.google.com/search?q=" + input('what to search : '))
        elif (ques == "open whatsapp"):
            con = input("Do you want to send message to someone\nPress 1 for yes or Press 2 for no : ")
            if con == "1":
                from selenium import webdriver
                from selenium.webdriver.common.keys import Keys
                from selenium.webdriver.chrome.options import Options

                options = webdriver.ChromeOptions()
                options.add_experimental_option("excludeSwitches", ["enable-automation"])
                options.add_experimental_option('useAutomationExtension', False)
                options.add_argument("--log-level=3")
                options.add_argument("--disable-blink-features=AutomationControlled")
                driver = webdriver.Chrome(options=options)
                driver.get("https://web.whatsapp.com/")
                quitt = "0"
                while (quitt == "0"):
                    try:
                        chat = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
                        chat.click()
                        driver.minimize_window()
                        receiver = input("Enter Name or Number of Saved Contact")
                        chat.send_keys(receiver)
                        chat.send_keys(Keys.ENTER)
                        mssg = driver.find_element_by_xpath(
                            '//*[@id="main"]/footer/div[1]/div[2]/div/div[1]/div/div[2]')
                        message = input("Message You want to send")
                        mssg.send_keys(message)
                        mssg.send_keys(Keys.ENTER)
                        quitt = input("Exit WhatsApp bot?\nPress 1 to exit 0 to continue\n")
                    except:
                        time.sleep(3)
                else:
                    webbrowser.open(serv[ques])
        elif (ques == "search image"):
            webbrowser.open(
                "https://www.google.co.in/search?q=" + input("Which Image to search : ") + "&hl=en&tbm=isch")
        else:
            webbrowser.open(serv[ques])

    else:
        print(
            "Sorry I can't help you with this\nI am new to this world and learning new things\nHere is a list of things I know\n")
        for ik in bot.keys():
            print(ik + "\n")