from admin import admin_loop
from homework_16.common import process_user_input
from homework_16.db import sessions

users = {"admin": "admin123", "user1": "password1"}  # იუზერების სახელების სიმულაცია გავაკეთო


def list_menu_items():
    print("\n1. List sessions")
    print("2. Search movie")
    print("3. Book ticket")
    print("4. Cancel ticket")
    print("5. View my tickets")
    print("6. Admin panel")
    print("7. Exit")
    return process_user_input()


def list_sessions():
    if not sessions:
        print("No sessions available.")
        return
    for session in sessions:
        print(f"Session ID: {session['session_id']}")
        print(f"Film Name: {session['film_name']}")
        print(f"Start Time: {session['start_time']}")
        print(f"Room Number: {session['room_number']}")
        print(f"Available Seats: {session['capacity'] - len(session['booked_seats'])}")
        print("\n")


def search_movie():
    search_term = input("Enter the movie name or part of it: ").lower()
    found_movies = [
        session for session in sessions if search_term in session["film_name"].lower()
    ]
    if not found_movies:
        print("No movies found.")
        return
    print("Movies found:")
    for session in found_movies:
        print(f"Session ID: {session['session_id']}")
        print(f"Film Name: {session['film_name']}")
        print(f"Start Time: {session['start_time']}")
        print("\n")


def book_ticket():
    list_sessions()
    session_id = int(input("Enter the Session ID to book a ticket for: "))
    selected_session = next((s for s in sessions if s["session_id"] == session_id), None)

    if not selected_session:
        print("Invalid Session ID.")
        return

    if len(selected_session["booked_seats"]) >= selected_session["capacity"]:
        print("Sorry, this session is fully booked.")
        return

    display_seat_map(selected_session)
    seat_number = len(selected_session["booked_seats"]) + 1
    selected_session["booked_seats"].append(seat_number)
    print(f"Ticket booked successfully! Your seat number is {seat_number}")


def cancel_ticket():
    session_id = int(input("Enter the Session ID: "))
    selected_session = next((s for s in sessions if s["session_id"] == session_id), None)

    if not selected_session:
        print("Invalid Session ID.")
        return

    if not selected_session["booked_seats"]:
        print("No tickets booked for this session.")
        return

    seat_number = int(input("Enter your seat number: "))
    if seat_number in selected_session["booked_seats"]:
        selected_session["booked_seats"].remove(seat_number)
        print(f"Seat {seat_number} canceled successfully.")
    else:
        print("Invalid seat number.")


def view_my_tickets():
    print("Listing all your booked tickets:")
    for session in sessions:
        if session["booked_seats"]:
            print(f"Film Name: {session['film_name']}")
            print(f"Session ID: {session['session_id']}")
            print(f"Start Time: {session['start_time']}")
            print(f"Booked Seats: {session['booked_seats']}")
            print("\n")


def display_seat_map(session):
    print(f"Seat Map for {session['film_name']} (Session ID: {session['session_id']}):")
    rows, cols = session["room_length"], session["room_width"]
    for row in range(1, rows + 1):
        row_display = ""
        for col in range(1, cols + 1):
            seat_number = (row - 1) * cols + col
            if seat_number in session["booked_seats"]:
                row_display += "[X] "  # დაკავებული ადგილებისთვის
            else:
                row_display += "[ ] "  # თავისუფალი ადგილებისთვის
        print(row_display)
    print("\n")


def authenticate_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if users.get(username) == password:
        print("Login successful!")
        return username
    print("Invalid credentials.")
    return None


def exit_program():
    confirm = input("Are you sure you want to exit? (yes/no): ").lower()
    if confirm == "yes":
        print("Goodbye!")
        exit()


def greetings():
    print("Welcome to the movie ticket booking system!")
    print("Please enter EXIT to exit.")


def program_loop():
    while True:
        user_input = list_menu_items()
        match user_input:
            case "1":
                list_sessions()
            case "2":
                search_movie()
            case "3":
                book_ticket()
            case "4":
                cancel_ticket()
            case "5":
                view_my_tickets()
            case "6":
                admin_loop()
            case "7":
                exit_program()
            case _:
                print("Invalid input.")


def main():
    greetings()
    authenticated_user = authenticate_user()
    if authenticated_user:
        program_loop()


if __name__ == "__main__":
    main()

