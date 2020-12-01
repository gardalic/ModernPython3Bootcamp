class User:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

    def likes(self, thing):
        return f"{self.first} likes {thing}"

    def is_senior(self):
        return self.age >= 65


user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 42)
print(user1.likes("Ice cream"))

print(user2.initials())

print(f"Is {user1.first} a senior? It is {user1.is_senior()}")