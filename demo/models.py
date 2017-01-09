class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    def __str__(self):
        return "{class_} {name}, {age}. {job} paid {pay}".format(
            class_=self.__class__.__name__,
            name=self.name,
            age=self.age,
            job=self.job,
            pay=self.pay,
        )
