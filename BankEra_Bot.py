from twitter import Twitter, OAuth
import discord
import urllib.request as req
import json

#from coinmarketcap import Market
#from bs4 import BeautifulSoup


# 本番token
token = "NDA1MzY1ODI0NDQyOTkwNTky.DUjV6A.kVeYsW0rldoLX4BtKczQCiXqI58"
# テストtoken
#token = "NDA0NjE4MDA4MjA0NTQxOTYy.DUoAtQ.DqDyvVDhSIQSMD-KNRtx86WKRgo"
# 1万円計算用
yukichi = 10000

#Twitter Auth
t = Twitter(auth=OAuth(
    '935058768563339265-7eIsN2892DRYL6tCrTjzPGnySQQUHfr',
    'G3xDy4lUsRBQbR3GQ1ZEF7ankZgNY64gBpf7x0edPwBxF',
    'xMzUeWmIimG83P9QMhFnENCG4',
    'REDBG6CH9LkiR5ACBgB5hNBEYnwP00Als7TLi39WZCSdS3qLcG'
))

client = discord.Client()
client.get_all_members()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    # 送り主がBotだった場合反応したくないので
    if client.user != message.author:
        if message.content.startswith("?エラリスト") | message.content.startswith("？エラリスト"):
            count = 0
            for member in client.get_all_members():
                count += 1
            m = "報告します！ 現在 " + str(count) + "人のエラリストが参加中です！"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await client.send_message(message.channel, m)
        elif message.content.startswith("?btc") | message.content.startswith("?BTC"):
            # spectrocoinから相場価格を取得(From:BNK To:BTC)
            url = 'https://spectrocoin.com/scapi/ticker/BNK/BTC'
            res = req.urlopen(url)

            # 取得した価格をjsonに変換
            price_ticker = json.loads(res.read().decode('utf8'))

            # 価格のメッセージを設定し、出力
            echo = "1BTCで約" + str(round(price_ticker['last'], 1)) + "BNK購入できます。"
            await client.send_message(message.channel, echo)

        elif message.content.startswith("?xem") | message.content.startswith("?XEM"):
            # spectrocoinから相場価格を取得(From:BNK To:XEM)
            url = 'https://spectrocoin.com/scapi/ticker/BNK/XEM'
            res = req.urlopen(url)

            # 取得した価格をjsonに変換
            price_ticker = json.loads(res.read().decode('utf8'))

            # 価格のメッセージを設定し、出力
            echo = "1XEMで約" + str(round(price_ticker['last'], 1)) + "BNK購入できます。"
            await client.send_message(message.channel, echo)

        elif message.content.startswith("?eth") | message.content.startswith("?ETH"):
            # spectrocoinから相場価格を取得(From:BNK To:XEM)
            url = 'https://spectrocoin.com/scapi/ticker/BNK/ETH'
            res = req.urlopen(url)

            # 取得した価格をjsonに変換
            price_ticker = json.loads(res.read().decode('utf8'))

            # 価格のメッセージを設定し、出力
            echo = "1ETHで約" + str(round(price_ticker['last'], 1)) + "BNK購入できます。"
            await client.send_message(message.channel, echo)

        elif message.content.startswith("?諭吉") | message.content.startswith("？諭吉"):
            # spectrocoinから相場価格を取得(From:BNK To:JPY)
            url = 'https://spectrocoin.com/scapi/ticker/BNK/JPY'
            res = req.urlopen(url)
            # 取得した価格をjsonに変換
            price_ticker = json.loads(res.read().decode('utf8'))

            # １万円あたりの購入数を算出
            bankera = price_ticker['last'] * yukichi

            # 価格のメッセージを設定し、出力
            echo = "1万円で約" + str(round(bankera, 1)) + "BNK購入できます。"
            await client.send_message(message.channel, echo)

        elif message.content.startswith("?最新情報") | message.content.startswith("？最新情報"):
            #Get list from Twitter
            remain          = True
            while remain:
                userTweets      = []
                #Last Tweet
                max_id          = '976364667172982784'
                #BankeraJP ID
                user_id         = '908504581797113856'
                remainNum       = 0
                #Get Tweet
                numberOfTweets  = 1
                count           = 1
                #Get TimeLine
                aTimeLine = t.statuses.user_timeline(user_id=user_id, count=count, max_id=max_id)
                for tweet in aTimeLine:
                    userTweets.append(tweet['text'])
                    max_id = aTimeLine[-1]['id']-1
                    remainNum = numberOfTweets - len(userTweets)
                    count = remainNum
                    if len(userTweets)+1 > numberOfTweets:
                        m = userTweets
                        remain = False
                        await client.send_message(message.channel, m)

client.run(token)
