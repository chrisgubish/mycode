#!/usr/bin/env python3

"""Mini Project"""


user_input = input("Are you having chest pains? \n>")

if user_input == "Yes":
   user_input2 = print(input("Do you need us to contact emergency personnel for you? \n>"))

   if user_input == "Yes" and "Yes":
        print("Thank you, we are contacting emergency personnel right now")

        if user_input == "Yes" and "No":
            print("Thank you, we will not contact emergency personnel at this time however we are here to help")

        else:
            print("We are here to help. Please let us know if you need assistance")

elif user_input == "I don't know":
    print(input("Are you having difficulty breathing? \n>"))
    
    if user_input == "I don't know" and "yes":
             print("We can contact emergency personnel")

    elif user_input == "I don't know" and "yes":
            print("Please seek medical help")

    

elif user_input == "No":
    print("Thank you for your response.")

else: 
    print("You did not provide input.")
