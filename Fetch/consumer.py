import sys


import sys
import json
import logging
import os
sys.path.append(os.path.realpath(os.path.dirname(__file__)))

import time
from wsgiref import headers
import requests

import fetch_util


LOGFIL = "fetcher.log"
LOGFIL = "{}/{}".format(os.path.dirname(__file__),LOGFIL)
fetch_util.refresh_logger(LOGFIL)

logging.basicConfig(filename=LOGFIL, level=logging.DEBUG)
logging.getLogger('urllib3').setLevel(logging.WARNING)


class Consumer(object):
    def __init__(
        self,
        start=True,
        APIkey='c6246e3831ab49fdb3217fe0f2623268',
        host="https://mainnet.infura.io/v3/",
        delay=0.0001) -> None:
        
        #initialize the consumer to get block
        self.url = "{}:{}".format(host, APIkey)
        self.headers = {"content-type": "application/json"}
        #relational database
        self.pgsql = None
        self.delay = delay
        #

        self.max_block_postgres = None   
        self.max_block_geth = None

        if start:
            self.max_block_geth = self.highestBlockEth()
            self.run()


    def _rpcRequest(self, method, params, key):
        #make an RPC request.
        payload = {
            "method": method,
            "params": params,
            "jsonrpc": "2.0",
            "id": 1
        }
        time.sleep(self.delay)
        res = requests.post(
            self.url,
            data=json.dumps(payload),
            headers=self.headers).json()

        return res[key]

    def highestBlockPostgres(self):

        return None

    def highestBlockEth(self):
        """Find the highest numbered block in geth"""
        num_hex = self._rpcRequest("eth_blockNumber", [], "result")
        return int(num_hex, 16)

    def getHead():
        return data[key]

    def getTransactions():
        return data[txs]

    def getLogs():
        return data[logs]

    def run(self):
        """
        Run the process.
        Iterate through the blockchain on geth anf fill up postgreSql with data

        """

        logging.debug("Processing geth node to fetch block")
        logging.info("start and end the span of parsed blocks: {}".format(5))
        logging.info("highest block number of get is: {}".format(self.max_block_geth))

        #Get new blocks
        print("Processing selected blocks")


        print("Done!\n")