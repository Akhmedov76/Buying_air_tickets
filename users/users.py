from month_4.lesson_4.file_manager import flight_manager, user_datas


def search_flights():
    try:
        departure_airport = input("Enter the name of the departure airport: ").capitalize().strip()
        destination_airport = input("Enter the name of the landing airport: ").capitalize().strip()
        flights = flight_manager.read()
        for flight in flights:
            print(flight)
            if (flight["from_airport"]['country'] == departure_airport and flight["to_airport"]['country']
                    == destination_airport):
                return True
            else:
                print("No flights found.")
                return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def check_email(email):
    if '@' in email:
        return True
    return False


def my_booked_flights():
    try:
        passport_number = input("Enter your passport number: ").lower().strip()
        email = input("Enter your email address: ").lower().strip()
        if not check_email(email):
            print("Invalid email address!")
            return my_booked_flights()
        departure_air = input("Enter the name of the departure country: ").capitalize().strip()
        destination_air = input("Enter the name of the landing country: ").capitalize().strip()
        ticket = int(input("Enter the number of tickets: "))
        data = user_datas.read()
        for user in data:
            if user['passport_number'] == passport_number and user['email'] == email:
                print("This flight is already booked!")
                return False
            else:
                return True
        flights = flight_manager.read()
        for plane in flights:
            print(plane)
            if plane['from_airport']['name'] == departure_air and plane['to_airport']['name'] == destination_air:
                print("his flight is already booked!")
                return False
            else:
                if plane['tickets'] >= ticket:
                    plane['tickets'] -= ticket
                    flight_manager.write(flights)
                    datas = {
                        'passport_number': passport_number,
                        'email': email,
                        'departure_airport': departure_air,
                        'destination_airport': destination_air,
                        'booked_flight_id': plane['plane']['id'],
                        'ticket': ticket,
                        'total_price': plane['price'] * ticket
                    }
                    user_datas.add_data(datas)
                    print("Your flight is booked!")
                    return True
                else:
                    print("Not enough tickets for the selected plane.")
                    return False

    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def show_my_booked_flight():
    try:
        passport_number = input("Enter your passport number: ").lower().strip()
        email = input("Enter your email address: ")
        if not check_email(email):
            print("Invalid email address!")
            return False
        data = user_datas.read()
        for user in data:
            if user['passport_number'] == passport_number and user['email'] == email:
                print(
                    f"Booked flight ID: {user['booked_flight_id']},\nDeparture airport: {user['departure_airport']},\n"
                    f"Destination airport: {user['destination_airport']},\nTicket:{user['ticket']},\n"
                    f"Total price: {user['total_price']}\n")
                return True
        print("No booked flight found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
