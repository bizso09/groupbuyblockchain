pragma solidity ^0.4.25;

contract Listings {
    
    
    struct Bidder {
        string user;
        string postal;
        uint quantity;
    }
    
    struct Item {
	    string itemId;
	    string link;
	    string description;
	    uint price;
	    mapping(string => Bidder) bidders;
    }
    
    mapping(string => Item) items;
    address private _owner;
    
    
    modifier isOwner {
        require(_owner == msg.sender);
        _;
    }
    
    constructor() public {
        _owner = msg.sender;
    }

	function addItem(string itemId, string link, string description, uint price) isOwner public {
	    items[itemId] = Item(itemId, link, description, price);
	}
	function addBidder(string itemId, string user, string postal, uint quantity) isOwner public {
	    items[itemId].bidders[user] = Bidder(user, postal, quantity);
	}
	
	function getItem(string itemId) public view returns (string, string, uint) {
	    Item storage item = items[itemId];
	    return (item.link, item.description, item.price);
	}
	function getBidder(string itemId, string user) public view returns (string, uint) {
	    Bidder storage bidder = items[itemId].bidders[user];
	    return (bidder.postal, bidder.quantity);
	}
}
    

