#!/usr/bin/env python3

def main():

    char_name = input("What character do you want to know about? (Starlord, Mystique, Hulk) \n>")

    char_stat = input("What statistic do you want to know about? (real name, powers, archenemy) \n>")

    marvelchars= {
            "Starlord":
            {"real name": "peter quill",
                "powers": "dance moves",
                "archenemy": "Thanos"},

            "Mystique":
            {"real name": "raven darkholme",
                "powers": "shape shifter",
                "archenemy": "Professor X"},


            "Hulk":
            {"real name": "bruce banner",
                "powers": "super strength",
                "archenemy": "adrenaline"}
            }



    unique_char_stat = marvelchars.get(char_name).get(char_stat) 

    print(char_name + "'s " + char_stat + " is:" ,  unique_char_stat.title())

if __name__ == "__main__":
    main()

