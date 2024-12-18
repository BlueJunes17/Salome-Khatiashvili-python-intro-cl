class Student:
    #დაცული ველები
    def __init__(self, name):
        self._name = name          #სტუდენტის სახელი
        self._scores = []          #ქულების ცარიელი სია

    #ქულის დამატების მეთოდი
    def add_score(self, score):
        if 0 <= score <= 100:
            self._scores.append(score)
        else:
            print("არასწორი ქულა")

    #ქულების საშუალოს დასათვლელი მეთოდი
    def get_average(self):
        if len(self._scores) == 0:
            return 0  #თუ ქულები არ არის 0 დაბრუნდეს
        return sum(self._scores) / len(self._scores)

    #ქულების სიის დაბრუნების მეთოდი
    def get_scores(self):
        return self._scores

    #დაცულ ველის წვდომის მეთოდი (name)
    def get_name(self):
        return self._name


#სტუდენტების სიის შექმნა და ქულების დამატება
students = []

#სტუდენტების შექმნა
student1 = Student("ანა")
student2 = Student("ბექა")

#ქულების დამატება
student1.add_score(95)
student1.add_score(85)
student1.add_score(120)  # არასწორი ქულა

student2.add_score(70)
student2.add_score(80)
student2.add_score(90)

#სტუდენტების სიის დამატება
students.append(student1)
students.append(student2)

#თითოეული სტუდენტის ქულებისა და საშუალოს დაბეჭდვა
for student in students:
    print(f"სტუდენტი: {student.get_name()}")
    print(f"ქულები: {student.get_scores()}")
    print(f"საშუალო ქულა: {student.get_average():.2f}")
    print("-" * 20)

#ახალი სტუდენტის დამატება
student3 = Student("გიორგი")
student3.add_score(88)
student3.add_score(92)
students.append(student3)

#ახალი სტუდენტის ინფორმაციის ბეჭდვა
print("ახალი სტუდენტის ინფორმაცია:")
print(f"სტუდენტი: {student3.get_name()}")
print(f"ქულები: {student3.get_scores()}")
print(f"საშუალო ქულა: {student3.get_average():.2f}")
