#!/bin/bash
# usage: ./run.sh LotteryBankAddress ServerSecret

ADDR=$1
SECRET=$2

rm TXS
cd crawler/
scrapy crawl collect_tx -a address=$ADDR -o ../TXS -t json

cd ../
./lottery.py $SECRET

