class Person:
    def __init__(self, first_name, last_name, age, email, day, month, year):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.birth_day = (day, month, year)

    def get_info(self):
        return(f"Ismi - {self.first_name}\nFamiliyasi - {self.last_name}\nYoshi - {self.age}\nTug\'ilgan sanasi - {self.birth_day[0]}, {self.birth_day[1]}, {self.birth_day[2]}\nPochta manzili - {self.email}")
    
    def get_life_path_number(self):
        
        def digit_sum(n):
            while n > 9:
                n = sum(int(d) for d in str(n))
            return n
        day_sum = digit_sum(self.birth_day[0])
        month_sum = digit_sum(self.birth_day[1])
        year_sum = digit_sum(self.birth_day[2])

        total = day_sum + month_sum + year_sum
        return(digit_sum(total))
    
    def get_info_by_number(self, number):
        with open("HayotYuli.txt", "r") as f:
            text = f.read().replace('\n', '').split("#")

        return(text[number])


name = input("Iltimos ismingizni kiritng: ")
surname = input("Iltimos familiyangizni kiritng: ")
age =  int(input("Iltimos yoshingizni kiriting: "))
email = input("Iltimos elektron pochatngizni kiriting: ")
day = int(input("Iltimos tug'ilgan kunizni sanasini kiritng: "))
month = int(input("Iltimos tug'ilgan kunizni oyini kiriting: "))
year = int(input("Iltimos tug'ilgan yilizni kiritng: "))

Odam = Person(name, surname, age, email, day, month, year)

print(Odam.get_info())

raqam = Odam.get_life_path_number()

print(Odam.get_info_by_number(raqam))

    

    


        


    

        



        