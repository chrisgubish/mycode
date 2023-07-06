#!/usr/bin/env python3

"""Understanding dictionaries
    {key: value, key:value, ...}
    using the dict.get() method"""

def main():
    """runtime function"""

    ## create a dictionary with 4 key:value pairs
    switch = {"hostname": "sw1", "ip": "10.0.1.1", "version": "1.2", "vendor": "cisco"}

    ## display the entire dictionary
    print(switch)

    ## prove that switch is indeed a dictionary
    print(type(switch))

    ## display parts of the dictionary
    print( switch["hostname"] )        ##displays "sw1"
    print( switch["ip"] )       ##displays "10.0.1.1"


    ##request a "fake" key
    #print ( swithc["lynx"] )



    ##request a "fake" key with .get() method
    print ( "First test - .get()" )
    print( switch.get("lynx") )


    # if you want to customize what is returned when the key is not found
    print ( "Second test - .get()" )
    print( switch.get("lynx", "THE KEY IS IN ANOTHER CASTLE!") )

    print( "Third test - .get()")
    print( switch.get("version") )


##call our main function
if __name__ == "__main__":
    main()
