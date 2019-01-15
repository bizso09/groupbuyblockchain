pragma solidity ^0.4.25;

contract AssetTracker {
    address creator;
    string id;
    
    mapping(string => Asset) private assetStore;
    mapping(address => mapping(string => bool)) private walletStore;
    

    constructor() public{
        creator = msg.sender;
    }

    // TODO Add functions

    function kill() public {
        if (msg.sender == creator) {
            selfdestruct(creator);
        }
    }

    function setId(string serial) public {
          id = serial;
    }
 
    function getId() public constant returns (string) {
          return id;
    }
    
    function createAsset(string name, string description, string uuid, string manufacturer) public {
 
        if(assetStore[uuid].initialized) {
            emit RejectCreate(msg.sender, uuid, "Asset with this UUID already exists.");
            return;
        }
 
        assetStore[uuid] = Asset(name, description, manufacturer, true);
        walletStore[msg.sender][uuid] = true;
        emit AssetCreate(msg.sender, uuid, manufacturer);
    }
    
    function transferAsset(address to, string uuid) public {
 
        if(!assetStore[uuid].initialized) {
            emit RejectTransfer(msg.sender, to, uuid, "No asset with this UUID exists");
            return;
        }
 
        if(!walletStore[msg.sender][uuid]) {
            emit RejectTransfer(msg.sender, to, uuid, "Sender does not own this asset.");
            return;
        }
 
        walletStore[msg.sender][uuid] = false;
        walletStore[to][uuid] = true;
        emit AssetTransfer(msg.sender, to, uuid);
    }
    
    function getAssetByUUID(string uuid) public constant returns (string, string, string) {
 
        return (assetStore[uuid].name, assetStore[uuid].description, assetStore[uuid].manufacturer);
 
    }

    function isOwnerOf(address owner, string uuid) public constant returns (bool) {
 
        if(walletStore[owner][uuid]) {
            return true;
        }
 
        return false;
    }
    
    struct Asset {
        string name;
        string description;
        string manufacturer;
        bool initialized;    
    }
    
    event AssetCreate(address account, string uuid, string manufacturer);
    event RejectCreate(address account, string uuid, string message);
    event AssetTransfer(address from, address to, string uuid);
    event RejectTransfer(address from, address to, string uuid, string message);
}
    

