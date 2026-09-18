# 1) Instance Method:

class students:

    def introduction(self):
        print("I am a student")

# Wont work without an object. it need one to call or even the work the function out.



# 2) Class Method:


class Student:

    School = "ABC"

    @classmethod
    def show_school(cls):
        print(cls.School)
# It needs the class itself




# 3) STATIC METHOD:  (it need neither object nor class)

# Suppose we want to check whether a name is valid:

class Student:

    @staticmethod
    def is_valid_name(name):
        return name.isalpha()

# it only needs name.





