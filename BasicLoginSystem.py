class LoginSystem:

    def __init__(self):
        self.users = {}
        self.logged_users = set()
        self.mapping = {
                "a" : "i", "b" : "l", "c" : "q", "d" : "f", "e" : "z", "f" : "s",
                "g" : "a", "h" : "g", "i" : "e", "j" : "p", "k" : "w", "l" : "o",
                "m" : "v", "n" : "u", "o" : "b", "p" : "j", "q" : "k", "r" : "n",
                "s" : "x", "t" : "d", "u" : "h", "v" : "y", "w" : "t", "x" : "m",
                "y" : "r", "z" : "c"
                }
    
    def register(self, username, password):
        if username in self.users: print("user already exists")
        else: 
            self.users[username] = self.encrypt(password)
            print('user registered successfully')

    def login(self, username, password):

        if username in self.users:
            if self.encrypt(password) == self.users[username]:
                self.logged_users.add(username)
                print("user logged in successfully")
            else: print("password doesn't match")
            
        elif username not in self.users:
            print("user isn't in the system")

    def sign_out(self, username):

        if username in self.users:
            if username in self.logged_users:
                self.logged_users.remove(username)
                print("user signed out successfully")
            elif username not in self.logged_users: print("user is not logged in")

        elif username not in self.users: print("user is not in the system")

    def encrypt(self, password):
        encrypted_password = ''
        for char in password:
            if char in self.mapping:
                encrypted_password += self.mapping[char]
            else: encrypted_password += char

        return encrypted_password
        
login_system = LoginSystem()

def run_login_system():
    command = str(input("enter command..... "))

    command_list = [("/register", "/reg"), ("/login", "/log"), ("/signOut", "/out")]

    
    if command in command_list[0]:
        user = input("Username: ")
        passw = input("Password: ")
        login_system.register(user, passw)

    elif command in command_list[1]:
        user = input("Username: ")
        passw = input("Password: ")
        login_system.login(user, passw)

    elif command in command_list[2]:
        user = input("Username: ")
        login_system.sign_out(user)


    next_command = input("Continue? (Y/N): ")

    if next_command.upper() == "Y":
        run_login_system()
    elif next_command.upper() == "N":
        return ("Goodbye! See you next time!")

run_login_system()
    