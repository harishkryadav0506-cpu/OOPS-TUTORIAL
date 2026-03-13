class employee:
    def __init__(self):
        print("started executing")
        self.id=123
        self.salary=50000
        self.designation="sde"
        print("attributes initialized")


    def travel(self,destination):
        print("this travel method called manually")
        print("employee is now traveling to {destination}")


sam = employee()
sam.name = "harish kumar"
print(id(sam))
print(sam.name)


#print(sam.id)


# calling a method   
sam.travel("ranchi")
print(type(sam))