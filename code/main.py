import csv
import pyautogui
import time
import webbrowser as web
from urllib.parse import quote
from whatsapp_template import message
from utils import get_arguments


def send_message(phone, message):
    web_url = f"https://web.whatsapp.com/send?phone={phone}&text={quote(message)}"
    web.open(web_url)
    time.sleep(20)  #adjust duration if required

    # Paste the image after loading the web whatsapp
    pyautogui.hotkey("ctrl", "v")
    time.sleep(5)

    # Sends the message by pressing Enter
    pyautogui.press('enter')
    time.sleep(5)

    # Closes the browser window
    pyautogui.hotkey('ctrl', 'w')
    pyautogui.press('enter')


def send_whatsapp(data_file='contacts.csv', message=None, x_cord=761, y_cord=884):
    with open(data_file, 'r') as contacts:
        csvreader = csv.reader(contacts)
        for row in csvreader:
            name, phone = row[0], row[1]
            send_message(phone, message)
            print("Message sent to {} --> {}".format(name, phone))


if __name__ == '__main__':
    args = get_arguments()
    contacts_file = args.contacts
    path = "../contacts/{}".format(contacts_file)
    data_file = path
    message = message
    send_whatsapp(data_file, message)
