class Person:
    def __init__(self, name, sex, heigh, age, eyes, hair):
        self.name = name
        self.sex = sex
        self.heigh = heigh
        self.age = age
        self.eyes = eyes
        self.hair = hair

    def describe_yourself(self):
        return f'Hello my name is {self.name} \nI am {self.sex}, {self.heigh} heigh, {self.age} years old, \nMy eyes are {self.eyes}, and my hair is {self.hair}.'


    def change_name(self, new_name):
        if new_name.isnumeric() == False:
            self.name = new_name
            return True
        else:
            return False

    def change_sex(self, new_sex):
        if new_sex.isnumeric() == False:
            self.sex = new_sex
            return True
        else:
            return False

    def change_heigh(self, new_heigh):
        if new_heigh.isnumeric() == True:
            self.heigh = new_heigh
            return True
        else:
            return False

    def change_eyes(self, new_eyes):
        if new_eyes.isnumeric() == False:
            self.eyes = new_eyes
            return True
        else:
            return False


    def change_hair(self, new_hair):
        if new_hair.isnumeric() == False:
            self.hair = new_hair
            return True
        else:
            return False


Marek = Person('Marek','Male','190cm','20','Blue','Orange')
print(Marek.describe_yourself())
try:
    Marek.change_name('Olek')
    print(Marek.describe_yourself())
except:
    print('erorr')
