class MyPerson:
    value = 50

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.value = 30

    def say_hello(self):
        return f'Hello {self.first_name} {self.last_name}'


obj = MyPerson(last_name='Ivan', first_name='Ivanov')
print(obj.first_name)
