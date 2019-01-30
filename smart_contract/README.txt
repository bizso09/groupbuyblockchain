Install python 3.6 or greater

pip install Flask
pip install web3

export FLASK_APP=server.py ; flask run

http://127.0.0.1:5000/

This is Smart contract running at 0xe5f38f5bb4f02066f07be61603953d49de42ce2f

The following methods are supported:
GET /item/<itemId>
GET /item/<itemId>/bidder/<user>
POST /item 
params: itemId (str), link (str), description (str), price (int) 
POST /item/bidder
params: itemId (str), user (str), postal (str), quantity (int) 

To add a new item, call /item