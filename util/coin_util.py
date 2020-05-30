# coding:utf-8

from web3 import Web3, HTTPProvider
import json
from pathlib import Path
import configparser

# このファイルの親の親ディレクトリ(kenshow8_eth_api)の絶対パスを取得
FILE_DIR = Path(__file__).parent.parent

# 設定を取得
config = configparser.ConfigParser()
conf_filepath = FILE_DIR.joinpath('config/setting.ini')
config.read(conf_filepath, 'UTF-8')
config_web3 = config['web3_config']
WEB3_URL = config_web3['web3_url']
CONTRACT_ADDRESS = config_web3['contract_address']
OWNER_ADDRESS = config_web3['owner_address']

# abiをロード
def load_abi():
    # abiファイルのパスを取得
    file_path = FILE_DIR.joinpath('resource/abi.json')

    # abiファイルをdict型でロード
    artifact = open(file_path, 'r')
    json_dict = json.load(artifact)

    return json_dict

# web3 tokenを取得
def web3_token_get():
    #web3利用準備
    web3 = Web3(HTTPProvider(WEB3_URL))
    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    abi = load_abi()
    Token = web3.eth.contract(abi=abi, address=contract_address)

    return Token

# 残高を取得
def get_coin_balance(userWallet,token):
    balance = token.functions.balanceOf(userWallet).call()
    name, symbol, decimals = get_coin_info(token)
    balance = balance / (10 ** decimals)

    return balance, name, symbol, decimals

# 詳細情報を取得
def get_coin_info(token):
    name = token.functions.name().call()
    symbol = token.functions.symbol().call()
    decimals = token.functions.decimals().call()

    return name, symbol, decimals

# 送金
def send_coin(fromWallet, toWallet, sendNumber, token):
    # 送金者の残高を取得
    fromWalletBalance, name, symbol, decimals = get_coin_balance(fromWallet, token)

    # 送金額と送金者の残高を取得
    sendNumber = int(sendNumber * (10 ** decimals))
    fromWalletBalance = int(fromWalletBalance * (10 ** decimals))

    # 送金実行フラグ
    sendFlg = 0
    
    #残高が送金金額以上であれば送金処理を実行、残高不足であればsendFlgを変更せずにリターン
    if fromWalletBalance >= sendNumber:
        print('exe sendToken')
        tx_hash = token.functions.transferByOwner(fromWallet, toWallet, sendNumber).transact({'from': OWNER_ADDRESS})
        sendFlg = 1

    return sendFlg