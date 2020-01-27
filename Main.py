import requests
import time


starttime = time.time()
while True:
    r = requests.get(
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC&tsyms=USD&api_key={01b2bb65b77f9f0ec6addff9fd0ec69df69147a46016b559ad067a20e9a84c4d}")
    data = r.json()['DISPLAY']

    for d in data:
        coin = data[d]['USD']
        s = d + '_data.txt'
        addString = ""
        with open(s, "a") as f:
            for key in coin:
                if (key == 'PRICE' or key == 'VOLUMEDAYTO' or key == 'VOLUME24HOURTO' or key == 'MEDIAN' or key == 'CHANGEPCT24HOUR' or key == 'CHANGEPCTDAY' or key == 'CHANGEPCTHOUR'):
                    if (key == 'CHANGEPCT24HOUR' or key == 'CHANGEPCTDAY' or key == 'CHANGEPCTHOUR'):
                        addString = addString + "," + coin[key]
                    else:
                        newstr = coin[key][2:].replace(",", "")
                        addString = addString + "," + newstr

            f.write(str(int(time.time()))+","+addString[1:] + '\n')
    time.sleep(90.0 - ((time.time() - starttime) % 90.0))






