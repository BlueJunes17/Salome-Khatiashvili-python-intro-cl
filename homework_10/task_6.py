from datetime import datetime

def car(producer, year = datetime.now().year, **kwargs):
    print("The car was produced by: ", producer)
    print("The car was produced in: ", year)

    if kwargs:
        print("Additional_information :")
        for additional_information in kwargs:
            print(f'\t{additional_information}')


car("Ferrari", Model = "SF23")
car("Ferrari", 2023, Engine = "Ferrari", Driver = "Charles Leclerc" )

