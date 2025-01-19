# main

import kontrol_function
import begrussung_function

if __name__ == "__main__":
    begrussung_function.kunden_begrussung()
    choice = int(input("Ihre Wahl bitte: "))
    kontrol_function.eingabe_kontrolle(choice)
