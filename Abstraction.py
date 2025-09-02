from abc import ABC, abstractmethod
class Absclass(ABC):
    def display(self,x):
        print("The value of x is:",x)
    def task(self):
        print("We are in abstract class")
class test_class(Absclass):
    def task(self):
        print("We are inside the test_class task")
obj = test_class()
obj.display(10)
obj.task()