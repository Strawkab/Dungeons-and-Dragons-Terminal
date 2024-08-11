from monster import Monster

def diceRoller(rolls, faces):
	
	#roll a x sided die y number of times
	total = 0
	for i in range(rolls):
		total += randint(1, faces)

	return total

def PlayerCharacter(Monster):
	#PC additional info
	age = 0
	def __init__(self, name, player_race, player_class):
		self.name = name

		#racial modifier table
		match self.player_race:
			case "Dwarf":
				self.dexterity += 2
				self.size = "Medium"
				self.speed = 25
				self.traits.extend(["Darkvision", "Dwarven Resilience", "Stonecunning"])
				self.combat_proficencies.extend(["battleaxe", "handaxe", "light hammer", "warhammer"]) #dwarven combat training
				self.proficiencies.append("artisan tools")
				self.languages.extend(["Common", "Dwarvish"])

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
