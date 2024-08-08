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
	level = 0
	experience = 0

	#inventory
	wielded_weapon = None
	equiped_armor = None
	magic = []

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
		#armor class equipment and class feature AC table
		match self.equiped_armor:
			#naked
			case None:
				self.armor_class = 10 + self.con_mod
			#light armor
			case "Padded":
				self.armor_class = 11 + self.dex_mod
			case "Leather":
				self.armor_class = 11 + self.dex_mod
			case "Studded Leather":
				self.armor_class = 12 + self.dex_mod

		self.hit_points = self.hit_die * self.level + self.con_mod
		
		
		
		#senses
		self.passive_perception = 10 + self.wis_mod
		
#Monsters TODO: move to separate file
class Rat(Monster):
	alignment = "Unaligned"
	monster_type = "Beast"
	size = "Tiny"
	combat_proficiencies = []
	speed = 20
	languages = []
	challenge_rating = 0
	exp_dropped = 10
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
			print(str(d20_result) + ": " + self.name + " bites " + target.name + "for 1 dmg")

		else:
			print(str(d20_result) + ": " + self.name + " missed")

class Bandit(Monster):
	#monster info
	alignment = "Chaotic Neutral" #any non lawful alignment
	monster_type = "Humanoid"
	size = "Medium"
	combat_proficiencies = []
	speed = 30
	languages = ["Common"]
	challenge_rating = 1/8
	exp_dropped = 25
	hit_die = 8

	#inventory
	wielded_weapon = ["Scimitar", "Light Crossbow"]
	equiped_armor = "Leather"
	magic = []

	#ability scores
	strength = 11
	dexterity = 12
	constitution = 12
	intelligence = 10
	wisdom = 10
	charisma = 10
	level = 2
	experience = 0

	#actions
	def scimitar(self, target):
		d20_result = diceRoller(1, 20) + 3
		if d20_result >= target.armor_class:
			damage_roll = diceRoller(1, 6) + 1
			target.hit_points -= damage_roll

			#successful roll flavor table
			table_die = diceRoller(1, 4)
			match table_die:
				case 1:
					print(self.name + " parried " + target.name + "\'s attack and thrusted them  with a scimitar for " + str(damage_roll) + " damage")
				case 2:
					print(self.name + " ducked under " + target.name + "\'zs attack and slashed them with a scimitar for " + str(damage_roll) + " damage")
				case 3:
					print(target.name + " was attacked by " + self.name + " with a scimitar and took " + str(damage_roll) + " damage")
				case 4:
					print(target.name + " was slashed with a scimitar by " + self.name + " and took " + str(damage_roll) + " damage")
		else:
			#failed roll flavor table
			table_die = diceRoller(1, 4)
			match table_die:
				case 1:
					print(self.name + " swung their scimitar at " + target.name + " but they stepped out of the way")
				case 2:
					print(self.name + " swung their scimitar at " + target.name + " but missed")
				case 3:
					print(target.name + " grabbed " + self.name + "\'s arm before they could do anything")
				case 4:
					print(target.name + " parried " + self.name + "\'s attack")

	def lightCrossbow(self, target):
		d20_result = diceRoller(1, 20) + 3
		if d20_result >= target.armor_class:
			damage_roll = diceRoller(1, 8) + 1
			target.hit_points -= damage_roll

			#successful roll flavor table
			table_die = diceRoller(1, 4)
			match table_die:
				case 1:
					print(self.name + " shoots " + target.name + " with a crossbow for " + str(damage_roll) + " damage")
				case 2:
					print(self.name + " runs away and shoots " + target.name + " with a crossbow for " + str(damage_roll) + " damage")
				case 3:
					print(target.name + " was shot by a crowwbow by " + self.name + " took " + str(damage_roll) + " damage")
				case 4:
					print(target.name + " was slashed with a scimitar by " + self.name + " and took " + str(damage_roll) + " damage")
		else:
			#failed roll flavor table
			table_die = diceRoller(1, 4)
			match table_die:
				case 1:
					print(self.name + " wasn't able to pull back the string on their crossbow")
				case 2:
					print(self.name + " shot their crossbow at " + target.name + " but missed")
				case 3:
					print(target.name + " jumped away from " + self.name + "\'s crossbow bolt")
				case 4:
					print(target.name + " ducked under " + self.name + "\'s crossbow bolt")


			
			
			
			


#make 2 bandits fight eachother	
def fight(creature1, creature2):
	while creature1.hit_points > 0 and creature2.hit_points > 0:
		print(creature1.name + ": " + str(creature1.hit_points) + " " + creature2.name + ": " + str(creature2.hit_points))
		
		if diceRoller(1, 2) == 1:
			creature1.scimitar(creature2)
		else:
			creature1.lightCrossbow(creature2)

		if diceRoller(1, 2) == 1:
			creature2.scimitar(creature1)
		else:
			creature2.lightCrossbow(creature1)

	if creature1.hit_points <= 0:
		print(creature1.name + " has died")

	if creature2.hit_points <= 0:
		print(creature2.name + " has died")




bandit1 = Bandit("bandit1")
bandit2 = Bandit("bandit2")
rat1 = Rat("rat1")
rat2 = Rat("rat2")

fight(bandit1, bandit2)

def initiative(creatures_rolling):
	print("!ROLLING FOR INITIATIVE!")
	initiative_rolls = {}

	for creature in creatures_rolling:
		roll = diceRoller(1, 20)
		modified_roll = roll + creature.dex_mod #d20 plus dex mod
		initiative_rolls.update({creature: modified_roll}) #add a key:pass of creature instance and their roll
		print(creature.name + " rolled a " + str(roll) + " + " + str(creature.dex_mod) + " : (" + str(modified_roll) + ")")

	sorted_lowest_to_highest = dict(sorted(initiative_rolls.items(), key=lambda item: item[1])) #sorts dictionary lowest to highest by initiative roll
	initiative_list = list(sorted_lowest_to_highest.keys()) #convert keys to list
	initiative_list.reverse() #reverse order
	
	turn_counter = 0
	for creature in initiative_list:
		turn_counter += 1
		print(str(turn_counter) + ". " + creature.name)

	return initiative_list

def encounter(creatures):
	print(creatures)
	for creature in creatures:
		print(creature.name)



encounter(initiative([bandit1, bandit2, rat1, rat2]))	

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






