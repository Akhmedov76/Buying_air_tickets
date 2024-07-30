from month_4.lesson_4.users.common import register, login, logout, UserTypes
from month_4.lesson_4.users.users import search_flights, my_booked_flights, show_my_booked_flight
from users.logs import log_settings
from month_4.lesson_4.users.admin import (create_plane, show_all_planes, edit_plane, delete_plane,
                                          create_airport, show_all_airports, edit_airport, delete_airport,
                                          create_flight, show_all_flights)


def show_admin_menu():
    text = """
1. Add plane
2. Add airport
3. Add flight
4. Show all flights
5. Exit
    """
    print(text)

    user_input = input("Enter your choice: ")
    if user_input == "1":
        add_plane()
    elif user_input == "2":
        add_airport()
    elif user_input == "3":
        if create_flight():
            show_admin_menu()
        else:
            print("Error creating flight. Try again.")
            show_admin_menu()
    elif user_input == "4":
        if show_all_flights():
            show_admin_menu()
        else:
            print("Error showing flights. Try again.")
            show_admin_menu()
    elif user_input == "5":
        print("Exit successfully!")
        show_auth_menu()
    else:
        print("Invalid input. Please try again.")
        show_admin_menu()


def add_plane():
    txt_plane = """
Welcome to the plane service🛫:
1. Create a new plane
2. Show all planes
3. Edit the plane
4. Delete the plane
5. Exit
    """
    print(txt_plane)
    user_input = input("Enter your choice: ")
    if user_input == "1":
        if create_plane():
            add_plane()
        else:
            print("Error creating plane. Try again.")
            add_plane()
    elif user_input == "2":
        if show_all_planes():
            add_plane()
        else:
            print("Error showing planes. Try again.")
            add_plane()
    elif user_input == "3":
        if edit_plane():
            add_plane()
        else:
            print("Error editing plane. Try again.")
            add_plane()
    elif user_input == "4":
        if delete_plane():
            add_plane()
        else:
            print("Error deleting plane. Try again.")
            add_plane()
    elif user_input == "5":
        print("Exit successfully!")
        show_admin_menu()
    else:
        print("Invalid input. Please try again.")
        add_plane()


def add_airport():
    txt_airport = """
Welcome to the Airport Center✈️:
1. Create a new Airport
2. Show all Airports
3. Edit the Airport
4. Delete the Airport
5. Exit
"""
    print(txt_airport)
    user_input = input("Enter your choice: ")
    if user_input == "1":
        if create_airport():
            add_airport()
        else:
            print("Error creating airport. Try again.")
            add_airport()
    elif user_input == "2":
        if show_all_airports():
            add_airport()
        else:
            print("Error showing airports. Try again.")
            add_airport()
    elif user_input == "3":
        if edit_airport():
            add_airport()
        else:
            print("Error editing airport. Try again.")
            add_airport()
    elif user_input == "4":
        if delete_airport():
            add_airport()
        else:
            print("Error deleting airport. Try again.")
            add_airport()
    elif user_input == "5":
        print("Exit successfully!")
        show_admin_menu()
    else:
        print("Invalid input. Please try again.")
        add_airport()


def show_user_menu():
    text = """
1. Search flights
2. My booked flights
3. Exit    
"""
    print(text)

    user_input = input("Enter your choice: ")
    if user_input == "1":
        if search_flights():
            show_user_menu()
        else:
            show_user_menu()
    elif user_input == "2":
        user_menu()
    elif user_input == "3":
        print("Exit successfully!")
        show_auth_menu()
    else:
        print("Invalid input. Please try again.")
        show_auth_menu()


def user_menu():
    text = """
1. Buy tickets
2. Show my booked flights
3. Exit
    """
    print(text)

    user_input = input("Enter your choice: ")
    if user_input == "1":
        if my_booked_flights():
            user_menu()
        else:
            user_menu()
    elif user_input == "2":
        if show_my_booked_flight():
            user_menu()
        else:
            user_menu()
    elif user_input == "3":
        print("Exit successfully!")
        show_auth_menu()
    else:
        print("Invalid input. Please try again.")
        user_menu()


def show_auth_menu():
    text = """
1. Register
2. Login
3. Exit"""
    print(text)

    user_input = input("Enter your choice: ")
    if user_input == "1":
        if register():
            show_auth_menu()
    elif user_input == "2":
        user = login()
        if not user:
            print("Invalid username and password. Please try again.")
            show_auth_menu()
        elif user['user_type'] == UserTypes.ADMIN.value:
            show_admin_menu()
        elif user['user_type'] == UserTypes.USER.value:
            show_user_menu()
        else:
            print("Invalid credentials!")
            show_auth_menu()
    elif user_input == "3":
        if logout():
            print("Goodbye!🥹")
        else:
            print("Logout canceled!😊")
            show_auth_menu()

    else:
        print("Invalid input. Please try again.")
        show_auth_menu()


if __name__ == "__main__":
    log_settings()  # Enable logging for all functions in this module.
    show_auth_menu()
