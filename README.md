# CS 166 Auction Database Project
Joshua Mena and Colin Pham

## Introduction
We are building an online bidding marketplace. The platform supports real-time auction and bid updates for buyers, sellers, and administrators, with a PostgreSQL backend for  data management. Sellers can list items, buyers can place bids and monitor auctions, and administrators can manage users, items, payments, and shipments. 
+ We are basing our project off of this ER Diagram:
<img width="629" height="342" alt="image" src="https://github.com/user-attachments/assets/aeb8547b-9a5d-408c-94fd-3a74e4f47a03" />


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

## Performance Testing
