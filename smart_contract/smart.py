'''
Created on 16 Jan 2019

@author: Zsolt
'''
from web3.main import Web3
import logging
from os.path import dirname, join

class SmartContract:
    
    PROVIDER = "https://ropsten.infura.io/v3/4efe6c8407424bfebbc531fdb8fb8540"
    
    CONTRACT_FILE = join(dirname(__file__),"item.sol")
    CONTRACT_ADDR = "0xe5f38f5bb4f02066f07be61603953d49de42ce2f"
    CONTRACT_ABI_FILE = join(dirname(__file__), "item_abi.json")
    
    ACCOUNT_KEY = join(dirname(__file__), "account.key")

    def __init__(self):
        testnet_provider = Web3.HTTPProvider(self.PROVIDER)
        self.w3 = Web3(testnet_provider)
        self.load_contract()
        
    def load_contract(self):
        logging.info("Loading contract at address: {}>".format(self.CONTRACT_ADDR))
        with open(self.CONTRACT_ABI_FILE) as f:
            abi = f.read()
        self.listings = self.w3.eth.contract(address=Web3.toChecksumAddress(self.CONTRACT_ADDR), abi=abi)

        with open(self.ACCOUNT_KEY) as f:
            self.account = self.w3.eth.account.privateKeyToAccount(f.read())

    def _send(self, function):
        txn = function.buildTransaction({
            'from': self.account.address,
            'nonce': self.w3.eth.getTransactionCount(self.account.address),
            'gas': 1728712,
            'gasPrice': self.w3.toWei('21', 'gwei')})
        signed = self.account.signTransaction(txn)
        tx_hash = self.w3.eth.sendRawTransaction(signed.rawTransaction) 
        self.w3.eth.waitForTransactionReceipt(tx_hash)
        
    def add_item(self, itemId:str, link:str, description:str, price:int):
        logging.info("Adding item to smart contract: <itemId {} link {} description {} price {}>".format(itemId, link, description, price))
        self._send(self.listings.functions.addItem(itemId, link, description, price))
        
    def add_bidder(self, itemId: str, user: str, postal: str, quantity: int):
        logging.info("Adding bidder to smart contract: <itemId {} user {} postal {} quantity {}>".format(itemId, user, postal, quantity))
        self._send(self.listings.functions.addBidder(itemId, user, postal, quantity))
    
    def get_item(self, itemId: str):
        logging.info("Getting item from smart contract: <itemId {}>".format(itemId))
        link, description, price = self.listings.functions.getItem(itemId).call()
        return {"itemId": itemId, "link":link, "description":description, "price":price}

    def get_bidder(self, itemId: str, user : str):
        logging.info("Getting bidder from smart contract: <itemId {} user {}>".format(itemId, user))
        postal, quantity = self.listings.functions.getBidder(itemId, user).call()
        return {"itemId":itemId, "user":user, "postal":postal, "quantity":quantity}
        

    