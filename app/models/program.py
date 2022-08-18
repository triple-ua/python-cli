from database.database import Database
from models.user import User
from models.command import Command


class Program:
    
    def __init__(self):
        self.database = Database()

        while True:
            login, password = self.invitation()

            response = self.database.get_user(login, password)

            if(len(response) != 0):
                break

            print("\nError: no user with such credentials\n")

        user_id = response[0][0]
        status = response[0][3]

        self.user = User(user_id, login, password, status)

        print(f"\nSuccessfully logged with {self.user.status} permissions\n")
        print("Type 'h' to see help list")
            
    def invitation(self):
        login = input("Enter your login (or 'die' to terminate): ")

        if(login.lower().strip() == "die"):
            self.die()
            
        password = input("Enter your password: ")

        return login, password

    def run(self):
        while True:
            request = input(f"\n{self.user.login}>> ")

            if(request.strip() == ""):
                continue

            if(request.lower().strip() == "die"):
                self.die()

            command = Command(request, self)
            command.execute()

    def die(self):
        del self.database
        print("\nProgram successfully terminated")
        exit()