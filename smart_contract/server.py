'''
Created on 16 Jan 2019

@author: Zsolt
'''

import json

from flask import Flask
from flask.globals import request
from flask_cors import CORS

from smart import SmartContract

app = Flask(__name__)
CORS(app)


@app.route('/')
def main():
    return """
    This is Smart contract running at {address}<br/><br/>
    
    The following methods are supported:<br/>
    GET /item/&lt;itemId&gt;<br/>
    GET /item/&lt;itemId&gt;/bidder/&lt;user&gt;<br/>
    POST /item <br/>
      params: itemId (str), link (str), description (str), price (int) </br>
    POST /item/bidder<br/>
      params: itemId (str), user (str), postal (str), quantity (int) </br>
""".format(address=SmartContract.CONTRACT_ADDR)


@app.route('/item', methods=['POST'])
def add_item():
    itemId = request.form['itemId']
    link = request.form['link']
    description = request.form['description']
    price = int(request.form["price"])

    contract = SmartContract()
    contract.add_item(itemId, link, description, price)
    return "success"


@app.route('/item/bidder', methods=['POST'])
def add_bidder():
    itemId = request.form['itemId']
    user = request.form['user']
    postal = request.form['postal']
    quantity = int(request.form["quantity"])

    contract = SmartContract()
    contract.add_bidder(itemId, user, postal, quantity)
    return "success"


@app.route('/item/<itemId>')
def get_item(itemId):
    contract = SmartContract()
    return json.dumps(contract.get_item(itemId))


@app.route('/item/<itemId>/bidder/<user>')
def get_bidder(itemId, user):
    contract = SmartContract()
    return json.dumps(contract.get_bidder(itemId, user))
