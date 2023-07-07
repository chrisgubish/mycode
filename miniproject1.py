#!/usr/bin/env python3

"""Mini Project"""


user_input = input("Are you having chest pains? \n>")

if user_input == "Yes":
   user_input2 = print(input("Do you need us to contact emergency personnel for you? \n>"))

if user_input2 == "Yes":
        print("Thank you, we are contacting emergency personnel right now")

if user_input2 == "No":
        print("Thank you, we will not contact emergency personnel at this time however we are here to help")

if user_input2 == "I dont know":
        print("We are here to help. Please let us know if you need assistance")

else:
        print("You did not provide input")


if user_input == "I don't know":
    print("Are you having difficulty breathing?")

if user_input == "No":
    print("Thank you for your response.")

else: 
    print("You did not provide input.")
