class Car:

	ability: str
	number_of_wheels = 4

	def __init__(self, name):
		self.ability = name

	def present(self):
                print(self.ability)

	def change_car(self):
		self.ability = "ride has been changed"
		self.number_of_wheels = 3


class Porsche(Car):

	cool_cabin = str

	def __init__(self):
		super().__init__("ride in cool way")		#super means that this class is a superclass
		self.cool_cabin = "really cool cabin"

	def present(self):
		print(self.cool_cabin)
