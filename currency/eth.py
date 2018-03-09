import urllib.request as req
import json


# class Spectrocoin():

def __init__():
    pass

def getBnk():
    # spectrocoinから相場価格を取得(From:BNK To:BTC)
    url = 'https://spectrocoin.com/scapi/ticker/BNK/ETH'
    res = req.urlopen(url)

    # 取得した価格をjsonに変換
    price_ticker = json.loads(res.read().decode('utf8'))

    # 価格のメッセージを設定
    msg = "1ETHで約" + str("{:,.3f}".format(round(price_ticker['last'], 3))) + "BNK購入できます。"

    return msg
