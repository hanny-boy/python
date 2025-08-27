class MyClass:
    def _privatemethod(self):
        print("This is a private method")
    _privatevar = 20
    def hello(self):
        print("Hello World")
obj = MyClass()
obj.hello()
print(obj._privatevar)