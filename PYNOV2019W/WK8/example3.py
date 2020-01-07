

class Application:

    def __init__(self, suer, password):
        self.user = user
        self.password = password
        
    def _get_input_details(self):
        print("Got  user input details")

    def _validate_user_input(self):
        print("Successfully validated user input")

    def login(self):
        self.get_input_details()
        self.validate_user_input()
        print("Successfully login to the Application")

if __name__ == "__main__":
    
    app = Application('root', 'root@123')
    #app.get_input_details('root', 'root@123')
    #app.validate_user_input()
    app.login()



# Access specifier

  
