'''
Created on 16 Jan 2019

@author: Zsolt
'''
import unittest
import requests
from smart import SmartContract


class ContractTest(unittest.TestCase):

    def test_load_contract(self):
        contract = SmartContract()
        
    def test_add_item(self):
        contract = SmartContract()
        contract.add_item("myitem2", "http://groupbuying.rocks2", "Im a dog", 1111)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()