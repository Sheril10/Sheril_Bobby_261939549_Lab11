print("---------Task-1---------")

from math import pi
class Shape:
    def __init__(self,name):
        self.name = name
    
    def comparea(self):
        pass

    def display(self):
        print(self.name)


class Triangle(Shape):
    def __init__(self, name, hieght, base):
        super().__init__(name)
        self.hieght = hieght
        self.base = base
        self.area = 0.0
        
    def comparea(self):
        self.area = 0.5 * (self.base * self.hieght)
        return self.area

    def display(self):
        super().display()
        print(f"Area of the Triangle : {self.area}")

        
class Circle(Shape):
    def __init__(self,name,radius):
        super().__init__(name)
        self.radius = radius
        self.area = 0.0

    def comparea(self):
        self.area = pi*(self.radius*self.radius)
        return self.area

    def display(self):
        super().display()
        print(f"Area of the Circle : {self.area}")
        

def main():
    lst=[]
    triangle = Triangle('Triangle', 4, 6)
    circle = Circle('Circle',3)
    lst.append(triangle)
    lst.append(circle)
    for i in lst:
        i.comparea()
        i.display()
         


main()

print()
print()
print("---------Task-2---------")
print()
print()

class Employee:
    def __init__(self,name,id,salary):
        self.name = name 
        self.id = id
        self.salary = salary
    
    def SalaryStatus(self):
        print("Salary Status:", self.salary,"of",self.name,"with id :", self.id)

class BuildingManager(Employee):

    def __init__(self,name,id,salary =10000):
        super().__init__(name,id,salary)
        
    def SalaryStatus(self):
        super().SalaryStatus()

class ProcurementManager(Employee):
    def __init__(self,name,id,salary = 12000):
        super().__init__(name,id,salary)
        
    def SalaryStatus(self):
        super().SalaryStatus()

class LogisticsManager(Employee):
    def __init__(self,name,id,salary= 15000):
        super().__init__(name,id,salary)
    def SalaryStatus(self):
        super().SalaryStatus()

def main():
    lst =[]
    b1 = BuildingManager('Ali', 136586)
    p1 = ProcurementManager('Alina', 131223)
    l1 = LogisticsManager('Alexa', 123897)
    lst.append(b1)
    lst.append(p1)
    lst.append(l1)
    for i in lst:
        i.SalaryStatus()

main()   




 
