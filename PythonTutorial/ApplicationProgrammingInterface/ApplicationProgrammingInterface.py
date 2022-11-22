def hyn():
    print("------------")
# integration with the plataform 
# The platform controls what data is available in the API


# Request Public API 

# API quotes 
import requests 
import json 

quotes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
quotes = quotes.json()

quotesHigh_dolar = float(quotes['USDBRL']['high'])
quotesLow_dolar = float(quotes['USDBRL']['low'])
dolar_pctChange = float(quotes['USDBRL']['pctChange'])

quotesHigh_BTC = float(quotes['BTCBRL']['high'])
quotesLow_BTC = float(quotes['BTCBRL']['low'])
BTC_pctChange = float(quotes['BTCBRL']['pctChange'])

print("One dolar to Real")
print("Low quote:",quotesHigh_dolar )
print("High quote:",quotesLow_dolar )
print("Variation: ",dolar_pctChange,"%")

hyn()

print("One Bitcoin to Real")
print("Low quote:",quotesHigh_BTC)
print("High quote:",quotesLow_BTC)
print("Variation: ",BTC_pctChange,"%")
