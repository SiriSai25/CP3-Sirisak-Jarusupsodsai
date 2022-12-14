u = input("Username :")
p = input("Password :")
if u == "boat" and p == "boat1234":
    print("Welcome to WhatTheShop")
    print("--------------WhatTheShop-------------")
    print("---------This is our products---------")
    print("1. LPhone       :  20,000THB per price")
    print("2. LPad         :  10,000THB per price")
    print("What do you want")
    uc = int(input("Please enter number : "))
    if uc == 1:
        Nm1 = int(input("Enter the amount you want to buy : "))
        totalsc = Nm1*20000
        ac1 = input("Are you sure : Enter Yes or No? : ")
        if ac1 == "Yes":
            print("--------------------------------------")
            print("total :", totalsc, "THB")
            print("--------------------------------------")
        if ac1 == "No":
            print("--------------------------------------")
            print("Canceled")
            print("--------------------------------------")
    elif uc == 2:
        Nm2 = int(input("Enter the amount you want to buy : "))
        totalsc2 = Nm2*10000
        ac2 = input("Are you sure : Enter Yes or No? : ")
        if ac2 == "Yes":
            print("--------------------------------------")
            print("total :", totalsc2, "THB")
            print("--------------------------------------")
        if ac2 == "No":
            print("--------------------------------------")
            print("Canceled")
            print("--------------------------------------")
    else:
        print("--------------------------------------")
        print("Not found, Please try again!")
        print("--------------------------------------")