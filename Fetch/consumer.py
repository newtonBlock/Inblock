import json
import logging
import time
from wsgiref import headers
import requests


class Consumer(object):
    def __init__(
        self,
        start=True,
        rpc_port=8545,
        host="http://localhost",
        delay=0.0001) -> None:
        
        #initialize the consumer to get block
        self.url = "{}:{}".format(host, rpc_port)
        self.headers = {"content-type": "application/json"}
        #relational database
        self.pgsql = None
        self.delay = delay
        #

        self.max_block_postgres = None   
        self.max_block_geth = None

        if start:
            pass

    def _rpcRequest(self, method, params, key):
        #make an RPC request to geth on port 8545.
        payload = {
            "method": method,
            "params": params,
            "jsonrpc": "2.0",
            "id": 0
        }
        time.sleep(self.delay)
        block = requests.post(
            self.url,
            data=json.dumps(payload),
            headers=self.headers).json()

        return block[key]

    def highestBlockPostgres(self):

        return None

    def highestBlockEth(self):
        """Find the highest numbered block in geth"""
        num_hex = self._rpcRequest("eth_blockNumber", [], "")
        return 

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
        logging.info("start and end the span of parsed blocks: {}".format(len()))


        #Get new blocks
        print("Processing selected blocks")


        print("Done!\n")