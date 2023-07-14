#!/usr/bin/env python3

def main():

    county_dict = {"East":
   {"Adams": "00", "Asotin": "01"},
   "Benton": "02", "Chelan": "03", "Clallam": "04", "Clark": "05", "Columbia": "07", "Cowlitz": "08", "Douglas": "09", "Ferry": "10", "Franklin": "11", "Garfield": "12", "Grant": "13", "Grays Harbor" :"14", "Island":"15", "Jefferson": "16", "King": "17", "Kitsap":"18", "Kittitas": "19", "Klickitat": "20", "Lewis": "21", "Lincoln": "22", "Mason": "23", "Okanogan": "24", "Pacific": "25", "Pend Oreille": "26", "Pierce": "27", "San Juan": "28", "Skagit" : "29", "Skamania": "30", "Snohomish": "31", "Spokane": "32", "Stevens": "33", "Thurston": "34", "Wahkiakum": "35", "Walla Walla": "36", "Whatcom": "37", "Whitman": "38", "Yakima": "39"}

    county_input = (input("What county do you live in?\n>"))

    unique_county = county_dict.get(county_input)

    print(f"You're located in {unique_county}, correct?")
    
if __name__ == "__main__":
    main()
