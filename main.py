# MAIN FILE
# This is what we are going to interact with! You can think of this file as the conductor in an orchestra
# It imports all the other files and plays them only when needed

import setup, encryption, scraper
from os import path # This is important to read the config.ini
import json 

def main():
        #Check if config.ini exist
    if not path.exists("config.ini"):
        setup.initialize()
    else:
        #Decrypt password
        masterpw = input("Enter master password: ")
        file = open("config.ini", "r")
        username = file.readline()
        enc_dict = file.readline()
        decrypted = encryption.decrypt(json.loads(enc_dict), masterpw)

        #Run scraper
        scraper.run_Scraper(username, decrypted)
        scraper.get_announcements()
        scraper.enter_courses()
if __name__ == "__main__":
    main()
