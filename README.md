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
### Menu
<br>
<img width="377" height="104" alt="image" src="https://github.com/user-attachments/assets/73976ebf-7429-4020-a771-760c80488f48" />
<br>
On program run, the screen above displays and we are given 3 options. Create User, Login, and Exit.
<br>
<br>

### Create User
<br>
<img width="274" height="154" alt="image" src="https://github.com/user-attachments/assets/248ee195-56d2-4cea-9ef1-8bb5e6e7af21" />
<br>
Upon selecting "1", Create user we are prompted to enter account details for account creation. 
<br>
<br>

### Logging In
<br>
<img width="174" height="144" alt="image" src="https://github.com/user-attachments/assets/7e7f99f0-8cdf-4771-9b1a-ebe250cbdbfe" />
<br>
When choosing to log in, the system will prompt you to enter your username and password. If successful, it will verify and display your username and role. 
<br>
<br>

### Buyer, Seller and Admin Menu
<br>
<img width="206" height="209" alt="image" src="https://github.com/user-attachments/assets/501d3a81-ff80-4011-babe-9ffbfb521283" />
<br>
Once you log in you are face a new menu, specific to your role. The image above shows the Buyer menu.
<br>
<br>

### View Profile
<br>
<img width="197" height="288" alt="image" src="https://github.com/user-attachments/assets/7ea62a54-498c-4965-86c7-f4c852dd6af4" />
<br>
Allows you to view account details. This is available to all roles
<br>
<br>

### Update Profile
<br>
<img width="241" height="263" alt="image" src="https://github.com/user-attachments/assets/c145dc8b-402e-495d-8b74-2903787c10e2" />
<br>
Allows you to change your account details, except for your role and password.
<br>
<br>



## Performance Testing
