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
config.set(config_web3, 'web3_url', 'http://127.0.0.1:7545') # contractのデプロイ先に応じて変更してください。
config.set(config_web3, 'contract_address', '0x238f011262D73a07c0bfACdf5f851CE467bc94ee') # contract addressを入力してください。
config.set(config_web3, 'owner_address', '0xB66d64EF0fACCebFd6F5E10Ece3dcBd3a65B82F1') # contractのowner addressを入力してください。


with open(file_path, 'w') as file:
    config.write(file)
