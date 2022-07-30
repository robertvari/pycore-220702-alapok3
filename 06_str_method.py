class Person:
    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email

    def __str__(self):
        return f"Name: {self.name}\nAddress:{self.address}\nEmail:{self.email}"

tamas = Person("Kiss Tamás", "Budapes", "tamas@gmail.com")
kriszta = Person("Nagy Krisztina", "Pécs", "kriszta@gmail.com")


print(tamas)
print("*"*50)
print(kriszta)