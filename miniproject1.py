#!/usr/bin/env python3

"""Mini Project"""

def main():

    round = 0
    while True:  

        welcome_message = input("Welcome to the Emergency Heart Attack Hotline. Would you like assistance? \n>")

        if welcome_message.lower() == "yes":
            print("Please continue forward")
 

            user_input = input("Are you having chest pains? \n>")

            if user_input.lower() == "yes":
                print("Do you need us to contact emergency personnel for you?")
                
                user_input2 = input(">")
                   
                if user_input2.lower() == "yes":
                    print("Thank you, we are contacting emergency personnel right now")
                    break

                elif user_input2.lower() == "no":
                    print("Thank you, we will not contact emergency personnel at this time however we are here to help")
                    break


            elif user_input.lower() == "i don't know":
                print("Are you having difficulty breathing?")
                
                user_input3 = input(">")
               
                if user_input3.lower() == "yes":
                    print("We can contact emergency personnel")
                    break

                elif user_input3.lower() == "no":
                    print("Please seek medical help")
                    break


            elif user_input.lower() == "no":
                print("Thank you for your response.")
                break

            else:
                print("You did not provide input.")


        elif welcome_message.lower() =="no":
            print("Thank you have a nice day!")
            break
           
        else:
            print("You did not provide input")

if __name__ == "__main__":
    main()

