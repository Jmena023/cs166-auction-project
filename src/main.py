import psycopg2

from users import create_user, login_user, view_profile, update_profile
from bid import place_bid, view_auction_bids, view_user_bids
from payment import make_payment, view_payment, view_user_payments, update_payment_status


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
        print("5. Place Bid")
        print("6. View Auction Bids")
        print("7. View User Bids")
        print("8. Make Payment")
        print("9. View Payment")
        print("10. View User Payments")
        print("11. Update Payment Status")
        print("12. Exit")

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
            place_bid(connection)

        elif choice == "6":
            view_auction_bids(connection)

        elif choice == "7":
            view_user_bids(connection)

        elif choice == "8":
            make_payment(connection)

        elif choice == "9":
            view_payment(connection)

        elif choice == "10":
            view_user_payments(connection)

        elif choice == "11":
            update_payment_status(connection)

        elif choice == "12":
            break

        else:
            print("Invalid choice")

    connection.close()


main()