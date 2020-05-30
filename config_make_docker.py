# coding:utf-8

import os
import configparser
from pathlib import Path

file_dir = Path(__file__).parent
file_name = 'config/setting.ini'
file_path = file_dir.joinpath(file_name)

config = configparser.ConfigParser()

# コントラクト設定
config_web3 = 'web3_config'
config.add_section(config_web3)

## web3 設定 ##
## 環境変数用
config.set(config_web3, 'web3_url', os.environ['WEB3_URL'])
config.set(config_web3, 'contract_address', os.environ['CONTRACT_ADDRESS'])
config.set(config_web3, 'owner_address', os.environ['OWNER_ADDRESS'])

with open(file_path, 'w') as file:
    config.write(file)
