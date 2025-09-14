class Restaraunt:

    def __init__(self,  restaraunt_name, cuisine_type):
        self.restaraunt_name = restaraunt_name
        self.cuisine_type = cuisine_type

    def describe_restaraunt(self):
        print(self.restaraunt_name)
        print(self.cuisine_type)

    def open_restaraunt(self):
        print("Restaraunt opened")

kfc = Restaraunt("KFC", "Fastfood")
kfc.describe_restaraunt()
foodband = Restaraunt("Foodband", "Pizzaria")
foodband.describe_restaraunt()