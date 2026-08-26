import os
import getpass
import psycopg2

from users import create_user, login_user, view_profile, update_profile, update_user_role
from item import create_item, update_item, view_item, browse_items, admin_remove_item
from auction import create_auction, browse_auctions, search_auctions, end_auction
from bid import place_bid, view_auction_bids, view_user_bids
from payment import make_payment, view_payment, view_user_payments, update_payment_status
from shipment import create_shipment, view_shipment, update_shipment_status

def buyer_menu(connection, login):
    while True:
        print()
        print("Buyer Menu")
        print("1. View Profile")
        print("2. Update Profile")
        print("3. Browse Items")
        print("4. Browse Auctions")
        print("5. Search Auctions")
        print("6. Place Bid")
        print("7. View Auction Bids")
        print("8. View User Bids")
        print("9. Make Payment")
        print("10. View Payment")
        print("11. View User Payments")
        print("12. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            view_profile(connection)

        elif choice == "2":
            update_profile(connection)

        elif choice == "3":
            browse_items(connection)

        elif choice == "4":
            browse_auctions(connection)

        elif choice == "5":
            search_auctions(connection)

        elif choice == "6":
            place_bid(connection)

        elif choice == "7":
            view_auction_bids(connection)

        elif choice == "8":
            view_user_bids(connection)

        elif choice == "9":
            make_payment(connection)

        elif choice == "10":
            view_payment(connection)

        elif choice == "11":
            view_user_payments(connection)

        elif choice == "12":
            print("Logged out")
            break

        else:
            print("Invalid choice")


def seller_menu(connection, login):
    while True:
        print()
        print("Seller Menu")
        print("1. View Profile")
        print("2. Update Profile")
        print("3. Create Item")
        print("4. Update Item")
        print("5. View Item")
        print("6. Browse Items")
        print("7. Create Auction")
        print("8. Browse Auctions")
        print("9. Search Auctions")
        print("10. End Auction")
        print("11. View Auction Bids")
        print("12. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            view_profile(connection)

        elif choice == "2":
            update_profile(connection)

        elif choice == "3":
            create_item(connection)

        elif choice == "4":
            update_item(connection)

        elif choice == "5":
            view_item(connection)

        elif choice == "6":
            browse_items(connection)

        elif choice == "7":
            create_auction(connection)

        elif choice == "8":
            browse_auctions(connection)

        elif choice == "9":
            search_auctions(connection)

        elif choice == "10":
            end_auction(connection)

        elif choice == "11":
            view_auction_bids(connection)

        elif choice == "12":
            print("Logged out")
            break

        else:
            print("Invalid choice")


def admin_menu(connection, login):
    while True:
        print()
        print("Admin Menu")
        print("1. View Profile")
        print("2. Update Profile")
        print("3. Update User Role")
        print("4. Admin Remove Item")
        print("5. Browse Items")
        print("6. Browse Auctions")
        print("7. View Payment")
        print("8. Update Payment Status")
        print("9. Create Shipment")
        print("10. View Shipment")
        print("11. Update Shipment Status")
        print("12. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            view_profile(connection)

        elif choice == "2":
            update_profile(connection)

        elif choice == "3":
            update_user_role(connection)

        elif choice == "4":
            admin_remove_item(connection)

        elif choice == "5":
            browse_items(connection)

        elif choice == "6":
            browse_auctions(connection)

        elif choice == "7":
            view_payment(connection)

        elif choice == "8":
            update_payment_status(connection)

        elif choice == "9":
            create_shipment(connection)

        elif choice == "10":
            view_shipment(connection)

        elif choice == "11":
            update_shipment_status(connection)

        elif choice == "12":
            print("Logged out")
            break

        else:
            print("Invalid choice")


def main():
    user = getpass.getuser()

    connection = psycopg2.connect(
        database=user + "_DB",
        user=user,
        host="localhost",
        port=os.environ["PGPORT"]
    )

    while True:
        print()
        print("Online Auction System")
        print("1. Create User")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            create_user(connection)

        elif choice == "2":
            login, role = login_user(connection)

            if role == "Buyer":
                buyer_menu(connection, login)

            elif role == "Seller":
                seller_menu(connection, login)

            elif role == "Admin":
                admin_menu(connection, login)

            elif role is not None:
                print("Invalid user role")

        elif choice == "3":
            break

        else:
            print("Invalid choice")

    connection.close()


if __name__ == "__main__":
    main()