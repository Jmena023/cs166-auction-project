# CS 166 Auction Database Project
Joshua Mena and Colin Pham

## Languages Used:
+ PostgreSQL 
+ Python

## Installation Guide:
### Clone the repo
git clone (link)

### Copy into server
scp -r "(file path)" <netid>@cs166.cs.ucr.edu:~/

### Connect to CS166 server
ssh (netid)@cs166.cs.ucr.edu

### Start Postgre Server
source startPostgreSQL.sh

### Create Database
source createPostgreDB.sh

### Run 
python3 main.py

### Close DB 
source stopPostgreDB.sh 

## Project Assumptions:
+ Only Admin users can change another user's role to "Buyer" or "Seller"
+ Admin Users can manage and remove items.
  
+ All users can update their profile after creation except for their login and role

+ Only "Sellers" can create and manage Auctions listings
+ Only "Sellers" can create and update their own items

+ Auctions start with status "Active"
+ Auctions can end at any time, controlled by the Seller who created the Auction
+ When the Auction ends, the highest bidder is the winner.
+ Completed Auctions are listed as "Closed"

+ When bidding on an item, it must be higher than the starting / highest bid.
+ Sellers cannot bid on their own Auction

+ Payments can be completed by the Buyer once the Auction is complete.
+ Shipments can be completed by the Seller once the Payment is complete.

## Usage + Example Output:
