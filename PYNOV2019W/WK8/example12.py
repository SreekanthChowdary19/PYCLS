# Abstraction, Encapsualtion



# Hiding


class Application:


    def get_input_details(self, user, password):
        print("Got  user input details")

    def validate_user_input(self):
        print("Successfully validated user input")

    def login(self):
        print("Successfully login to the Application")

if __name__ == "__main__":
    
    app = Application()
    app.get_input_details('root', 'root@123')
    app.validate_user_input()
    app.login()
