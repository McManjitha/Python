class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return f'User(username = {self.name}, email = {self.email}.)'

    def __str__(self):
        return self.__repr__()

    def introduce_yourself(self, guest_name):
        print(f"Hi {guest_name}, I'm {self.name}! Contact me at {self.email} .")


class UserDatabase:
    def __init__(self):
        self.users = []
    
    def insert(self, user):
        i = 0
        while i < len(self.users):
            # Find the first username greater than the new user's username
            if self.users[i].name > user.name:
                break
            i += 1
        self.users.insert(i, user)
    
    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user
    
    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email
        
    def list_all(self):
        return self.users



aakash = User('aakash', 'aakash@example.com')
biraj = User('biraj', 'biraj@example.com')
hemanth = User('hemanth', 'hemanth@example.com')
jadhesh = User('jadhesh', 'jadhesh@example.com')
siddhant = User('siddhant', 'siddhant@example.com')
sonaksh = User('sonaksh', 'sonaksh@example.com')
vishal = User('vishal', 'vishal@example.com')
mm = User('mm', 'mm@example.com')


users = [aakash, biraj, hemanth, jadhesh, siddhant, sonaksh, vishal]

ob1 = UserDatabase()
ob1.insert(users)
print(ob1.list_all())
print("\n")
ob1.insert(mm)
print(ob1.list_all())
