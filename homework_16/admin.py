import random
from homework_16.common import process_user_input
from homework_16.db import sessions


def list_admin_menu_items():
    print("1. list all sessions ")
    print("2. remove session")
    print("3. add session")
    print("4. edit session")
    return process_user_input()


def greetings():
    print("Welcome to the admin panel")
    print("Please sign in to continue")


def add_session():
    print("Adding session")
    print("Enter the session details")
    film_name = input("Film name: ")
    start_time = input("Start time (e.g., 18:00): ")
    room_number = input("Room number: ")
    room_length = int(input("Room length: "))
    room_width = int(input("Room width: "))
    capacity = room_length * room_width
    session_id = random.randint(1, 1000)

    
    while any(session["session_id"] == session_id for session in sessions):
        session_id = random.randint(1, 1000)

    session = {
        "session_id": session_id,
        "film_name": film_name,
        "start_time": start_time,
        "room_number": room_number,
        "room_length": room_length,
        "room_width": room_width,
        "capacity": capacity,
        "booked_seats": []
    }
    sessions.append(session)
    print(f"Session added successfully with ID: {session_id}")


def list_sessions():
    print("Listing sessions")
    if not sessions:
        print("No sessions found")
        return
    for session in sessions:
        print(f"\tSession ID: {session['session_id']}")
        print(f"\tFilm name: {session['film_name']}")
        print(f"\tStart time: {session['start_time']}")
        print(f"\tRoom number: {session['room_number']}")
        print(f"\tCapacity: {session['capacity']}")
        print(f"\tBooked seats: {len(session['booked_seats'])}")
        print("\n")


def remove_session():
    list_sessions()
    session_id = int(input("Enter the Session ID to remove: "))
    global sessions
    sessions = [s for s in sessions if s["session_id"] != session_id]
    print(f"Session {session_id} removed successfully.")


def admin_loop():
    greetings()
    while True:
        user_input = list_admin_menu_items()
        match user_input:
            case "1":
                list_sessions()
            case "2":
                remove_session()
            case "3":
                add_session()
            case "4":
                print("Editing session functionality coming soon.")
            case _:
                print("Invalid input")