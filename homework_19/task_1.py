import json
import os

def calculate_average_salaries(input_file, output_file):
    try:
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"This file '{input_file}' does not exist")
        
        with open(input_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        avg_salaries = {}   #თითოეული დეპარტამენტის საშუალო ხელფასი
        for department, details in data.items():
            try:
                employees = details.get("employees", [])
                if not isinstance(employees, list):
                    raise ValueError(f"This department's '{department}' employees are in a wrong format")
                
                #ხელფასების რიცხვებში კონვერტირება და არარიცხვითი მნიშვნელობების გამოტოვება
                salaries = []
                for emp in employees:
                    salary = emp.get("salary")
                    try:
                        salaries.append(float(salary))
                    except (ValueError, TypeError):
                        print(f"ATTANTION: '{salary}' there's no salary in this department '{department}'")

                if not salaries and employees:
                    raise ValueError(f"For departments '{department}' salaries are in a wrong format")
                
                #საშუალო ხელფასის გამოთვლა ან ცარიელი დეპარტამენტი
                avg_salaries[department] = sum(salaries) / len(salaries) if salaries else 0
            except ZeroDivisionError:
                avg_salaries[department] = 0  #ცარიელი თანამშრომლების სია
            except ValueError as ve:
                print(f"FAIL: {ve}")
        
        print("Avarage salaries in each department: ")
        for department, avg_salary in avg_salaries.items():
            print(f"{department}: {avg_salary:.2f}")
        
        with open(output_file, 'w', encoding='utf-8') as file:
            json.dump(avg_salaries, file, ensure_ascii=False, indent=4)
        print(f"\nResults are in '{output_file}' files")
    
    except FileNotFoundError as e:
        print(f"FAIL: {e}")
    except json.JSONDecodeError:
        print("FAIL: File is not in a correct JSON format")
    except Exception as e:
        print(f"უცნობი შეცდომა: {e}")


if __name__ == "__main__":
    input_file = "salaries.json"  
    output_file = "avg_salary.json"  

    calculate_average_salaries(input_file, output_file)        

