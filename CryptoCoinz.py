#!/usr/bin/env python2.7
# _*_ coding: utf-8 _*_

import requests
from bs4 import BeautifulSoup

formData = {
    'nvidia_hidden': 0,
    'amd_hidden': 0,
    'GTX_1080Ti': 0,
    'GTX_1080': 0,
    'GTX_1070Ti': 0,
    'GTX_1070': 3,
    'GTX_1060_6GB': 0,
    'GTX_1060_3GB': 0,
    'GTX_1050Ti': 0,
    'GTX_1050': 0,
    'GTX_980Ti': 0,
    'GTX_980': 0,
    'GTX_970': 0,
    'GTX_960': 0,
    'GTX_780': 0,
    'GTX_750Ti': 0,
    'cryptopia_hidden': 1,
    'bittrex_hidden': 1,
    'yobit_hidden': 1,
    'cryptobroker_hidden': 1,
    'tradesatoshi_hidden': 1,
    'coinmarketcap_hidden': 1,
    'c_cex_hidden': 1,
    'hitBTC_hidden': 1,
    'coinexchangeIo_hidden': 1,
    'coinsmarkets_hidden': 1,
    'cex_io_hidden': 1,
    'bitz_hidden': 1,
    'bitfinex_hidden': 1,
    'stockExchange_hidden': 1,
    'what_to_calculate': 1290,
    'what_to_calculate7': 3300,
    'what_to_calculate6': 0,
    'what_to_calculate5': 10.23,
    'what_to_calculate3': 5.4,
    'what_to_calculate2': 79.5,
    'what_to_calculate4': 132,
    'power1': 0,
    'power7': 0,
    'power6': 0,
    'power5': 0,
    'power3': 0,
    'power2': 0,
    'power4': 0,
    'what_to_calculate8': 45,
    'what_to_calculate9': 123,
    'what_to_calculate10': 102,
    'power8': 0,
    'power9': 0,
    'power10': 0,
    'order': 'profit1',
    'cost': 0,
    'submit_data': 'Calculate'
}


class CoinData:
    def __init__(self, coinname, coinsymbol, coincurrentprofit, coindailyprofit):
        self.coinname = coinname
        self.coinsymbol = coinsymbol
        self.coincurrentprofit = coincurrentprofit
        self.coindailyprofit = coindailyprofit


postRequest = requests.post("https://www.crypto-coinz.net/crypto-calculator/", data=formData)

soup = BeautifulSoup(postRequest.text, "html.parser")

content = soup.find('tr', {'id': 'row'})

log_coins = open("CryptoCoinz_Coins", "w")
log_currentproffits = open("CryptoCoinz_CurrentProfits", "w")
log_dailyprofits = open("CryptoCoinz_DailyProfits", "w")
log_coinsymbol = open("CryptoCoinz_CoinSymbol", "w")
# log_coinsnomine = open("CryptoCoinz_CoinsNoMine", "r")

coin_object = []
Coin = 'First'

while Coin != 'None':
    if content.text != '':
        contentText = content.text
        findCoin = contentText.find('Block Explorer')
        Coin = contentText[0:findCoin]
        CoinSymbol = Coin[Coin.find('(')+1:len(Coin)-1]
        with open("CryptoCoinz_CoinsNoMine") as f:
            for line in f:
                if line != CoinSymbol:
                    findFirstDollar = contentText.find('$')
                    findSecondDollar = contentText.find('$', findFirstDollar + 1)
                    findThirdDollar = contentText.find('$', findSecondDollar + 1)
                    CurrentProfit = contentText[findFirstDollar + 2:findSecondDollar - 1]
                    DailyProfit = contentText[findSecondDollar + 2:findThirdDollar - 1]
                    coin_object.append(CoinData(Coin, CoinSymbol, float(CurrentProfit), float(DailyProfit)))
        content = content.nextSibling
    else:
        Coin = 'None'

coin_object.sort(key=lambda coindata: coindata.coincurrentprofit, reverse=True)
for val in coin_object:
    log_coins.write(val.coinname + '\n')
    log_coinsymbol.write(val.coinsymbol + '\n')
    log_currentproffits.write(str(val.coincurrentprofit) + '\n')
    log_dailyprofits.write(str(val.coindailyprofit) +'\n')

log_coins.close()
log_currentproffits.close()
log_dailyprofits.close()