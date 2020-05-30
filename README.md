# eth_erc20_token_python_api
python flaskを使ったerc20準拠トークンのAPIです。  

# 環境
macOS Catalina : 10.15.4  
python : Python 3.7.6(Anaconda)  

# 使い方 docker版
※macOS Catalinaの場合  
.zshrc にホストのIPアドレスを出力する環境変数を追加  
```
vi ~/.zshrc
export LOCAL_HOST_IP=`ifconfig en0 | grep inet | grep -v inet6 | sed -E "s/inet ([0-9]{1,3}.[0-9]{1,3}.[0-9].{1,3}.[0-9]{1,3}) .*$/\1/" | tr -d "\t"`
```

docker-composeファイルを起動  
```
cd docker
mv .env.sample .env
vi .env
docker-compose up -d
```

# 使い方 localhost版
pythonのweb3モジュールをインストール  
```
pip install web3
```

config_make.pyを編集  
```
vi config_make.py
```

設定ファイルを生成  
```
python config_make.py
```

apiを実行  
```
python coin_api.py
```

# api仕様
※docker版のAPIにリクエストを投げる場合はganacheのIPアドレスを127.0.0.1からプライベートIPアドレスへの変更が必要です。  

残高確認  
```
POST
/balance
Content-Type : application/json
Body:
{
	"wallet_address": "0xaE7A6b72C2Ac93D79a9F6D744366cd9d752ecB7A"
}
Response:
{   
    "name": "KenshowCoin", 
    "balance": 10.0, 
    "symbol": "KSC", 
    "decimals": 18
}
```

送金  
```
POST
/send
Content-Type : application/json
Body:
{
	"from_wallet_address": "0xaE7A6b72C2Ac93D79a9F6D744366cd9d752ecB7A",
	"to_wallet_address": "0xB66d64EF0fACCebFd6F5E10Ece3dcBd3a65B82F1",
	"send_number": 100.0
}
Response-0:
{
    "response_code": 200,
    "code": 0,
    "message": "success."
}
Response-1:
{
    "response_code": 200,
    "code": 1,
    "message": "failed. need to check balance of send from."
}
```
