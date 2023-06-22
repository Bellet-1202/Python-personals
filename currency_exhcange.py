def currency_converter ():
    import requests
    url = ""    #insert your API

    response = requests.get(url)

    if response.status_code == 200: #make the response readable and manageable
        data = response.json()  
        rates = data['conversion_rates']    

    print("insert currency to convert: ")   #setting up currency to convert
    inserted_currency = input()
    if not rates.__contains__(inserted_currency):
        return( "no such currency exists")
    print("insert how much ", inserted_currency," you want to convert: ")
    inserted_value = input()

    print("insert result currency: ")   #setting up resulting currency
    result_currency = input()
    if not rates.__contains__(inserted_currency):
        return( "no such currency exists")
    result_value = int(inserted_value) * (1/rates.get(inserted_currency)) * rates.get(result_currency)  #calculate the tax of convertion between every currency, by using USD standard (1)
    return( "convertion done: " + str(inserted_value) + " " + inserted_currency + " = " + str(result_value) + " " + result_currency)    #creating output


