from random import randint
import monster

def diceRoller(rolls, faces):
	#roll a x sided die y number of times
	total = 0
	for i in range(rolls):
		total += randint(1, faces)

	return total


		
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




bandit1 = monster.Bandit("bandit1")
bandit2 = monster.Bandit("bandit2")
rat1 = monster.Rat("rat1")
rat2 = monster.Rat("rat2")

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