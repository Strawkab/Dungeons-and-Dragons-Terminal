import random

def diceRoller(rolls, faces):
	#roll a x sided die y number of times
	total = 0
	for i in range(rolls):
		total += random.randint(1, faces)

	return total

class Monster:
	#monster info
	alignment = None
	monster_type = None
	size = None
	combat_proficiencies = []
	speed = 0
	languages = []
	challenge_rating = 0
	exp_dropped = 0
	hit_die = 0

	#ability scores
	strength = 0
	dexterity = 0
	constitution = 0
	intelligence = 0
	wisdom = 0
	charisma = 0

	

	def __init__(self, name):
		self.name = name

		#ability modifiers
		self.str_mod = (self.strength - 10) // 2
		self.dex_mod = (self.dexterity - 10) // 2
		self.con_mod = (self.constitution - 10) // 2
		self.int_mod = (self.intelligence - 10) // 2
		self.wis_mod = (self.wisdom - 10) // 2
		self.cha_mod = (self.charisma - 10) // 2
	   
		#stats
		self.armor_class = 10 + self.dex_mod
		self.hit_points = self.hit_die + self.con_mod
		
		
		
		#senses
		self.passive_perception = 10 + self.wis_mod
		

class Rat(Monster):
	alignment = None
	monster_type = None
	size = None
	combat_proficiencies = []
	speed = 0
	languages = []
	challenge_rating = 0
	exp_dropped = 0
	hit_die = 4

	#ability scores
	strength = 2
	dexterity = 11
	constitution = 9
	intelligence = 2
	wisdom = 10
	charisma = 4

	#actions
	def bite(self, target):
		d20_result = diceRoller(1, 20)
		if d20_result >= target.armor_class:
			target.hit_points -= 1
			print(str(d20_result) + ": " + self.name + " hit " + target.name + "for 1 dmg")

		else:
			print(str(d20_result) + ": " + self.name + " missed")


	
def fight(creature1, creature2):
	while creature1.hit_points > 0 and creature2.hit_points > 0:
		print(creature1.name + ": " + str(creature1.hit_points) + " " + creature2.name + ": " + str(creature2.hit_points))
		creature1.bite(creature2)
		creature2.bite(creature1)

	if creature1.hit_points <= 0:
		print(creature1.name + "has died")

	if creature2.hit_points <= 0:
		print(creature2.name + "has died")


rat1 = Rat("ratatoile")
rat2 = Rat("biggiecheese")

fight(rat1, rat2)


'''
def characterCreation(name, character_race, character_class, age, strength, dexterity, constitution, intelligence, wisdom, charisma):
	character = Creature(name, strength, dexterity, constitution, intelligence, wisdom, charisma, 0)
	match character_class:

	match character_race:
		case "dwarf":
			character.constitution += 2
			character.size = "medium"
			character.speed = 25
			character.combat_proficiencies.extend()
'''
	



#def levelUp(character)






