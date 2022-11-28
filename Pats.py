class Cat:
    def __init__(self,name,gender, age):
        self.name = name
        self.gender = gender
        self.age = age
    def info_Cat (self):
        print(f'Имя животного: {self.name}, \n Пол животного: {self.gender},  \n Возраст животного: {self.age}')