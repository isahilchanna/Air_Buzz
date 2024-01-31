import sys
import re
import time
class Flight_1:

    def __init__(self):
        name1 =  "Welcome to Air_buzz"
        print(name1)

    def booking(self):
        global fr , to, date
        fr = input("From:- ")
        to = input("To:- ")
        date = input("Date:- ")
        return fr,to

    def available_flight(self):
        print(" ")
        print("Two Flights are available.")
        print("From- " + fr + ", To:- " + to +", Date:- " + date +", Time:- 07:00 am - 09:30 am, Flight_code:- F00123, First_class:- INR.5000/-, Second_class:- INR 2500/-" )
        print("From- " + fr + ", To:- " + to +", Date:- " + date + ", Time:- 12:30 pm - 02:30 pm, Flight_code:- F00567, First_class:- INR.5000/-, Second_class:- INR 2500/-")
        print("From- " + fr + ", To:- " + to +", Date:- " + date + ", Time:- 1:30 pm - 03:30 pm, Flight_code:- F00789, First_class:- INR.5000/-, Second_class:- INR 2500/-")

    def Mandatory_Details(self):
        print(" ")
        f1 = True
        f2 = True

        def isValid(mob):
            '''  1) Begins with 0 or 91
                 2) Then contains 7 or 8 or 9.
                 3) Then contains 9 digits  '''
            Pattern = re.compile("91[7-9][0-9]{9}")
            return Pattern.match(mob)

        while (f1):
            print("Note* ")
            print("1) Begins with 91\n2) Then contains 7 or 8 or 9. \n3) Then contains 9 digits")
            mob = input("mobile:-  ")
            if (isValid(mob)):
                print("Valid Number")
                print(" ")
                f1 = False
            else:
                print("Invalid Number")
                f1 = True

        while (f2):
            print("Note* \nOnly gmail id will be accepted")
            email = input("Please provide Email id:- ")
            if "@gmail.com" in email:
                print("valid info")

                f2 = False

            else:
                print("please enter valid gmail address")
                f2 = True

    def Passenger_form(self):
        print(" ")
        print("Submit Passengers Information")
        global no_seats
        no_seats = int(input("Number of seats:- "))
        i = 0
        while (no_seats != i):

            name_1 = input("Passenger Name:- ")
            address = input("Address:- ")
            try:
                mob = int(input("Mobile Number:- "))
                adhar = int(input("Adhar Number:- "))

            except ValueError:
                print("Do not type alphabets")
                time.sleep(2)
                adhar = int(input("Adhar Number:- "))

            print(" --------------------------------")
            print(" Passenger_name   :- ", name_1)
            print(" Passenger_Mobile :- ", mob)
            print(" Passenger_Address:- ", address)
            print("  Passenger_Adhar  :- ", adhar)
            print(" --------------------------------")
            i = i + 1

    def Payment(self):
        print(" ")
        print("* Armed_Force (AF) ")
        print("* Senior Citizen (SC)")
        print("* Family & Friends (FF)")
        print("* Students (S)")

        type = input("\nPlease select your convenient type:- ")

        if type == "AF":
            print("Welcome to armed force section.")
            print(" ")
            print("Press 1 for Credit/Debit Card ")

            cd = int(input("Your Choice:- "))
            if cd == int(1):
                print("Thank You for choosing Credit/Debit card.")
                c_no = int(input("Enter card number:- "))
                cvv = int(input("Enter cvv number:- "))

                print("(Press = 1) First_Class = 5000/- \n(Press = 2) Second_Class = 2500/- ")
                press = int(input("Which Class? "))

                if press == int(1):
                    print(" ")
                    global price, sum_1
                    price = 5000
                    sum_1 = price * no_seats
                    print("Basic Price * Number Of Seats:- ", sum_1)
                    total = (int(sum_1) * 2) / 100
                    print("2% Charges on total amount:- ", total)
                    base = int(sum_1) + total
                    print("Final Amount:- ", base)
                    t1 = (int(sum_1) + total)
                    p1 = (t1 * 10) / 100
                    d1 = t1 - p1
                    print("You got 10% Discount on Final Price :-", d1)
                if press == int(2):
                    print(" ")
                    global price_1, sum_2
                    price_1 = 2500
                    sum_2 = price_1 * no_seats
                    print("Basic Price * Number Of Seats:- ", sum_2)
                    total_1 = int(sum_2) * 2 / 100
                    print("2% Charges on total amount:-  ", total_1)
                    base_1 = int(sum_2) + total_1
                    print("Final Amount:- ", base_1)
                    t2 = int(sum_2) + total_1
                    p2 = (t2 * 10) / 100
                    d2 = t2 - p2
                    print("You got 10% Discount on Final Price:- ", d2)

        if type == "SC":
            print("Welcome senior citizen section.")

            print(" ")
            print("Press 1 for Credit/Debit Card ")

            cd = int(input("Your Choice:- "))
            if cd == int(1):
                print("Thank You for choosing Credit/Debit card.")
                c_no = int(input("Enter card number:- "))
                cvv = int(input("Enter cvv number:- "))

                print("(Press = 1) First_Class = 5000/- \n(Press = 2) Second_Class = 2500/- ")
                press = int(input("Which Class? "))

                if press == int(1):
                    print(" ")
                    global price_S_1, sum_S_1
                    price_S_1 = 5000
                    sum_S_1 = price_S_1 * no_seats
                    print("Basic Price * Number Of Seats:- ", sum_S_1)
                    total = (int(sum_S_1) * 2) / 100
                    print("2% Charges on total amount:- ", total)
                    base = int(sum_S_1) + total
                    print("Final Amount:- ", base)
                    t1 = (int(sum_S_1) + total)
                    p1 = (t1 * 10) / 100
                    d1 = t1 - p1
                    print("You got 10% Discount on Final Price :-", d1)
                if press == int(2):
                    print(" ")
                    global price_S_2, sum_S_2
                    price_S_2 = 2500
                    sum_S_2 = price_S_2 * no_seats
                    print("Basic Price * Number Of Seats:- ", sum_S_2)
                    total_1 = int(sum_S_2) * 2 / 100
                    print("2% Charges on total amount:-  ", total_1)
                    base_1 = int(sum_S_2) + total_1
                    print("Final Amount:- ", base_1)
                    t2 = int(sum_S_2) + total_1
                    p2 = (t2 * 6) / 100
                    d2 = t2 - p2
                    print("You got 6% Discount on Final Price:- ", d2)

        if type == "FF":
            print("Welcome to family and friends section. ")

            print(" ")
            print("Press 1 for Credit/Debit Card ")

            cd = int(input("Your Choice:- "))
            if cd == int(1):
                print("Thank You for choosing Credit/Debit card.")
                c_no = int(input("Enter card number:- "))
                cvv = int(input("Enter cvv number:- "))

                print("(Press = 1) First_Class = 5000/- \n(Press = 2) Second_Class = 2500/- ")
                press = int(input("Which Class? "))

                if press == int(1):
                    print(" ")
                    global price_F_1, sum_F_1
                    price_F_1 = 5000
                    sum_F_1 = price_F_1 * no_seats
                    print("Basic Price * Number Of Seats:- ", sum_F_1)
                    total = (int(sum_F_1) * 2) / 100
                    print("2% Charges on total amount:- ", total)
                    base = int(sum_F_1) + total
                    print("Final Amount:- ", base)
                    t1 = (int(sum_F_1) + total)
                    p1 = (t1 * 5) / 100
                    d1 = t1 - p1
                    print("You got 5% Discount on Final Price :-", d1)
                if press == int(2):
                    print(" ")
                    global price_F_2, sum_F_2
                    price_F_2 = 2500
                    sum_F_2 = price_F_2 * no_seats
                    print("Basic Price * Number Of Seats:- ", sum_F_2)
                    total_1 = int(sum_F_2) * 2 / 100
                    print("2% Charges on total amount:-  ", total_1)
                    base_1 = int(sum_F_2) + total_1
                    print("Final Amount:- ", base_1)
                    t2 = int(sum_F_2) + total_1
                    p2 = (t2 * 5) / 100
                    d2 = t2 - p2
                    print("You got 5% Discount on Final Price:- ", d2)

        if type == "S":
            print("Welcome to students section. ")

            print(" ")
            print("Press 1 for Credit/Debit Card ")

            cd = int(input("Your Choice:- "))
            if cd == int(1):
                print("Thank You for choosing Credit/Debit card.")
                c_no = int(input("Enter card number:- "))
                cvv = int(input("Enter cvv number:- "))

                print("(Press = 1) First_Class = 5000/- \n(Press = 2) Second_Class = 2500/- ")
                press = int(input("Which Class? "))

                if press == int(1):
                    print(" ")
                    global price_SS_1, sum_SS_1
                    price_SS_1 = 5000
                    sum_SS_1 = price_SS_1 * no_seats
                    print("Basic Price * Number Of Seats:- ", sum_SS_1)
                    total = (int(sum_SS_1) * 2) / 100
                    print("2% Charges on total amount:- ", total)
                    base = int(sum_SS_1) + total
                    print("Final Amount:- ", base)
                    t1 = (int(sum_SS_1) + total)
                    p1 = (t1 * 6) / 100
                    d1 = t1 - p1
                    print("You got 6% Discount on Final Price :-", d1)
                if press == int(2):
                    print(" ")
                    global price_SS_2, sum_SS_2
                    price_SS_2 = 2500
                    sum_SS_2 = price_SS_2 * no_seats
                    print("Basic Price * Number Of Seats:- ", sum_SS_2)
                    total_1 = int(sum_SS_2) * 2 / 100
                    print("2% Charges on total amount:-  ", total_1)
                    base_1 = int(sum_SS_2) + total_1
                    print("Final Amount:- ", base_1)
                    t2 = int(sum_SS_2) + total_1
                    p2 = (t2 * 6) / 100
                    d2 = t2 - p2
                    print("You got 6% Discount on Final Price:- ", d2)
                    print("thankyou for using Air_Buzz")


h =Flight_1()

h.booking()


h.available_flight()
h.Mandatory_Details()
h.Passenger_form()
h.Payment()
