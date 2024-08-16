import exchange_rates

#We can do all conversions with these:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def toUSD(amount, currency):
    return amount / exchange_rates.rate[currency]

def fromUSD(usd, currency):
    return usd*exchange_rates.rate[currency]

#Don't really need these but they're there if you want them:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def GBP(usd):
    return usd*exchange_rates.rate["GBP"]

def AUD(usd):
    return usd*exchange_rates.rate["AUD"]

def EUR(usd):
    return usd*exchange_rates.rate["EUR"]

def TRY(usd):
    return usd*exchange_rates.rate["TRY"]

def JPY(usd):
    return usd*exchange_rates.rate["JPY"]
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def tryIntConvert(var):
        try:
            return int(var)            
        except:
            return var

def isChoiceInRange(choice,_min, _max):
    if(type(choice) is not int):
        print("not int")
        return False
    elif(choice > _max or choice < _min):
        print("outside range")
        return False
    else:
        print("In range")
        return True

def chooseCurrency(message):
    #let the user select a choice, ensuring its an int and in range
    choice = ""
    while(type(choice) is str):
        choice = input(message+
    """
    1. US Dollars
    2. Great British Pounds
    3. Australian Dollars
    4. Euros
    5. Turkish Lira
    6. Japanese Yen
    
    : """)
        #make sure it was a number
        choice = tryIntConvert(choice)

        #make sure it was in range of 1-6
        if(not isChoiceInRange(choice,1,6)):
            choice = ""

    #convert int into currency string       
    my_currency = ""    
    if(choice == 1):
        my_currency = "USD"
    else:
        my_currency = exchange_rates.indexToCurrency(choice-2)

    return my_currency
               
    
def main():
    currency1 = chooseCurrency("\nWhat currency do you want to convert FROM?") 
                 
    if(currency1 != ""):
        amount1 = ""
        while(type(amount1) is str):
            amount1 = input("How many {} do you have?: ".format(currency1))
            amount1 = tryIntConvert(amount1)
            

    currency2 = chooseCurrency("\nWhat currency do you want to convert TO?")

    #first, always convert to dollars
    if(currency1 != "USD"):
        dollars = toUSD(amount1,currency1)
    else:
        dollars = amount1

    #then use dollars to convert to final currency
    if(currency2 != "USD"):
              amount2 = fromUSD(dollars,currency2)
    else:
        amount2 = dollars
        
    print("You have {0} in {1}\n".format(amount1, currency1))
    print("Which is {0} in {1}\n".format(round(amount2,2), currency2))
    
main()
