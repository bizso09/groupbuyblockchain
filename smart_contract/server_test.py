'''
Created on 16 Jan 2019

@author: Zsolt
'''
import unittest
import requests


class ServerTest(unittest.TestCase):

    HOST = "http://127.0.0.1:5000/"

    ITEM = "item2"
    USER = "meow"
    
    def test_add_item(self):
        resp = requests.post(self.HOST+"item", data={"itemId":self.ITEM, "link":"http://groupbuying.rocks", "description":"Im a cat", "price":"1234"}).text
        self.assertEqual(resp, "success")

    def test_add_bidder(self):
        resp = requests.post(self.HOST+"item/bidder", data={"itemId":self.ITEM, "user":self.USER, "postal":"Tree street 2", "quantity":"54"}).text
        self.assertEqual(resp, "success")
        
    def test_get_item(self):
        resp = requests.get(self.HOST+"item/{}".format(self.ITEM)).text
        self.assertTrue("1234" in resp)

    def test_get_bidder(self):
        resp = requests.get(self.HOST+"item/{}/bidder/{}".format(self.ITEM, self.USER)).text
        self.assertTrue("Tree street" in resp)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()