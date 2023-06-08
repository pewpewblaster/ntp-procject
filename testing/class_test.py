class MyClass:
    class_attribute = "I am a class attribute"

    def __init__(self):
        self.instance_attribute = "I am an instance attribute"

# my_instance = MyClass()
# print(my_instance.class_attribute)          # Output: I am a class attribute
# print(my_instance.instance_attribute)       # Output: I am an instance attribute

MyClass.class_attribute = "Updated value"   # Modifying the class attribute
print(MyClass.class_attribute)       