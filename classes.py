class Student:
    def __init__(self, uid, name):
        self.uid = int(uid)
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Student(uid: {self.uid}, name: {self.name})"
