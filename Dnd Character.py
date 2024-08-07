import random

def diceRoller(rolls, faces):
	#roll a x sided die y number of times
	total = 0
	for i in range(rolls):
		total += random.randint(1, faces)

	return total

class Monster:
	alignment = None
	monster_type = None
	size = None

	#ability scores
	strength = 0
	dexterity = 0
	constitution = 0
	intelligence = 0
	wisdom = 0
	charisma = 0

	#ability modifiers
	str_mod = (strength - 10) // 2
	dex_mod = (dexterity - 10) // 2
	con_mod = (constitution - 10) // 2
	int_mod = (intelligence - 10) // 2
	wis_mod = (wisdom - 10) // 2
	cha_mod = (charisma - 10) // 2
	   
	#stats
	armor_class = 10 + dex_mod
	hit_die = 0
	hit_points = hit_die + con_mod
	speed = 0
	languages = []
	challenge_rating = 0
	exp_dropped = 0
	proficiency_bonus = 0
	combat_proficiencies = []
		
	#senses
	passive_perception = 10 + wis_mod

	def __init__(self, name):
		#monster info
		self.name = name
		

class Rat(Monsternster):
	#ability scores
	strength = 0
	dexterity = 0
	constitution = 0
	intelligence = 0
	wisdom = 0
	charisma = 0
	

rat = Rat("rat")
print(rat.str_mod)

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






