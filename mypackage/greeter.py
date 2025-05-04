class Greeter:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        self.name = name

    def say_hello(self):
        return f"Hello, {self.name}!"