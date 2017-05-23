class Parent():
    def __init__(self,last_name,eye_color):
        print("Parent constuctor called")
        self.last_name = last_name
        self.eye_color = eye_color

billy_cyrus = Parent("Cyrus", "Blue")
print(billy_cyrus.last_name)
