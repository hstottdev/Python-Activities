#RATES
USD_TO_GBP = 0.78
USD_TO_AUD  = 1.51
USD_TO_EUR = 0.91
USD_TO_TRY = 33.65
USD_TO_JPY = 147.22

rate = {"GBP" : USD_TO_GBP,"AUD" : USD_TO_AUD,"EUR" : USD_TO_EUR,"TRY" : USD_TO_TRY,"JPY" : USD_TO_JPY}

def indexToCurrency(index):
    count = 0
    for key in rate:
            if(count == index):
                return key
            count += 1
    return "USD"
    
