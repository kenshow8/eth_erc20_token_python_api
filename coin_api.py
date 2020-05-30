# coding:utf-8

from flask import Flask, render_template, request, jsonify, make_response, abort
import json
from pathlib import Path
import configparser

import util.coin_util as coin_util

app = Flask(__name__)

# API EndPointの定義
COIN_BALANCE = '/balance'
COIN_SEND = '/send'

# web3 tokenの取得
WEB3_TOKEN = coin_util.web3_token_get()

############  エラー処理を作る。 存在しないwallet_addressとか
@app.route(COIN_BALANCE, methods=['POST'])
def api_coin_balance():

    # ボディ(application/json)パラメータ
    params = request.json

    # postされた値を取得
    targetWalletAdress = params.get('wallet_address')

    balance, name, symbol, decimals = coin_util.get_coin_balance(targetWalletAdress, WEB3_TOKEN)
 
    response_dict = {
        'name' : name,
        'balance' : balance,
        'symbol' : symbol,
        'decimals' : decimals 
        }

    return make_response(json.dumps(response_dict),200)

@app.route(COIN_SEND, methods=['POST'])
def api_coin_send():

    # ボディ(application/json)パラメータ
    params = request.json

    # postされた値を取得
    fromWalletAdress = params.get('from_wallet_address')
    toWalletAdress = params.get('to_wallet_address')
    sendNumber = params.get('send_number')

    # 送金 sendFlg:1 => 成功、sendFlg:0 => 残高不足または何かしらのエラー
    sendFlg = coin_util.send_coin(fromWalletAdress, toWalletAdress, sendNumber, WEB3_TOKEN)

    # APIレスポンス result_code:0 => 成功、 result_code:1 => エラー
    if sendFlg == 1:
            result_code = 0
            result_message = 'success.'
    else :
            result_code = 1
            result_message = 'failed. need to check balance of send from.'

    response_dict = {
        'response_code' : 200,
        'result_code' : result_code,
        'result_message' : result_message
        }

    return make_response(json.dumps(response_dict),200)

@app.errorhandler(400)
@app.errorhandler(404)
@app.errorhandler(500)
def error_handler(error):
    response = jsonify({'message': error.name, 'result': error.code })
    return response, error.code
 
app.run(host="0.0.0.0", port=8080, debug=False)
