# oop_person.py

# Object-Oriented Programming
# examples: Python, Ruby, Java, C++, Objective-C
# vs imperative / procedural

# class - analogous to data type
# int a
# shape x, y, z (objects)
# class has both data and methods
# eg shape - data (point[x,y]), method (move[m,n])

# person
# data - name, weight, height
# methods
# - constructor: Person() - allocate memory and create object
# - accessor/getty: read data
# - modifier/mutator/setty: change data
# - helper / support: perform utility function
# - destructor: ~Person() - free memory and destroy object

# a class is a blueprint/template for objects
# object is an instance of a class
# class - Person
# objects - p1 (Mr Thng), p2 (Mr Leong), p3 (Mr Fan)

# encapsulation
# - class bundles data and methods
# - use public methods to access private data
# inheritance - code reuse
# - subclass will adopt superclass data and methods
# - subclass can create its own data and methods
# polymorphism
# - ability to invoke different class methods using same name
# - appropriate method will be bound dynamically at runtime

class Person(object):
    # constructor
    def __init__(self, nName, nWeight, nHeight):
        self.name = nName
        self.weight = nWeight
        self.height = nHeight

    # accessors
    def get_name(self):
        return self.name

    def get_weight(self):
        return self.weight

    def get_height(self):
        return self.height    

    # modifiers
    def set_weight(self, newWeight):
        self.weight = newWeight

    def eat(self, addWeight):
        #self.weight = self.weight + addWeight
        self.weight += addWeight

    def shit(self, remWeight):
        self.weight = self.weight - remWeight

    def set_height(self, newHeight):
        self.height = newHeight

    def sleep(self, addHeight):
        self.height = self.height + addHeight

    # helper/support
    def display(self):
        print(self.name)
        print(self.weight)
        print(self.height)

    def bmi(self):
        return self.weight / (self.height * self.height)


class Student(Person):

    # constructor
    def __init__(self, nName, nWeight, nHeight, nClassid):
        super().__init__(nName, nWeight, nHeight)
        self.classid = nClassid

    # accessor
    def get_classid(self):
        return self.classid

    # modifier
    def set_classid(self, newClassid):
        self.classid = newClassid

    # helper / support
    def display(self): # overriding
        super().display()
        print(self.classid)


class Staff(Person):

    # constructor
    def __init__(self, nName, nWeight, nHeight, nDepartment):
        super().__init__(nName, nWeight, nHeight)
        self.department = nDepartment

    # accessor
    def get_department(self):
        return self.department

    # modifier
    def set_department(self, newDepartment):
        self.department = newDepartment

    # helper/support
    def display(self):
        super().display()
        print(self.department)

# main
stud1 = Student("Mr Li", 60, 1.75, "5C23")
#stud1.display()

staff1 = Staff("Boss Pang", 57, 1.60, "Computing")
#staff1.display()

school = []
school.append(stud1)
school.append(staff1)

for user in school:
    user.display() # code generality
