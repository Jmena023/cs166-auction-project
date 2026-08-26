import psycopg2

from users import create_user, login_user, view_profile, update_profile
from item import create_item, update_item, view_item, browse_items, admin_remove_item
from auction import create_auction, browse_auctions, search_auctions, end_auction
from bid import place_bid, view_auction_bids, view_user_bids
from payment import make_payment, view_payment, view_user_payments, update_payment_status
from shipment import create_shipment, view_shipment, update_shipment_status


def main():
    connection = psycopg2.connect(
        database="cpham133_DB",
        user="cpham133",
        host="localhost",
        port="40493"
    )

    while True:
        print()
        print("1. Create User")
        print("2. Login User")
        print("3. View Profile")
        print("4. Update Profile")
        print("5. Create Item")
        print("6. Update Item")
        print("7. View Item")
        print("8. Browse Items")
        print("9. Admin Remove Item")
        print("10. Create Auction")
        print("11. Browse Auctions")
        print("12. Search Auctions")
        print("13. End Auction")
        print("14. Place Bid")
        print("15. View Auction Bids")
        print("16. View User Bids")
        print("17. Make Payment")
        print("18. View Payment")
        print("19. View User Payments")
        print("20. Update Payment Status")
        print("21. Create Shipment")
        print("22. View Shipment")
        print("23. Update Shipment Status")
        print("24. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            create_user(connection)

        elif choice == "2":
            login_user(connection)

        elif choice == "3":
            view_profile(connection)

        elif choice == "4":
            update_profile(connection)

        elif choice == "5":
            create_item(connection)

        elif choice == "6":
            update_item(connection)

        elif choice == "7":
            view_item(connection)

        elif choice == "8":
            browse_items(connection)

        elif choice == "9":
            admin_remove_item(connection)

        elif choice == "10":
            create_auction(connection)

        elif choice == "11":
            browse_auctions(connection)

        elif choice == "12":
            search_auctions(connection)

        elif choice == "13":
            end_auction(connection)

        elif choice == "14":
            place_bid(connection)

        elif choice == "15":
            view_auction_bids(connection)

        elif choice == "16":
            view_user_bids(connection)

        elif choice == "17":
            make_payment(connection)

        elif choice == "18":
            view_payment(connection)

        elif choice == "19":
            view_user_payments(connection)

        elif choice == "20":
            update_payment_status(connection)

        elif choice == "21":
            create_shipment(connection)

        elif choice == "22":
            view_shipment(connection)

        elif choice == "23":
            update_shipment_status(connection)

        elif choice == "24":
            break

        else:
            print("Invalid choice")

    connection.close()


main()