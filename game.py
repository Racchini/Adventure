import random 

class User:
	def __init__(self, coins, health):
		self.coins = coins
		self.health = health

#placeholder for future functionality
class Weapon:
	def __init__(self, name, damage, weight):
		self.name = name		
		self.weight = weight
		self.damage = damage
		self.skill = 1 

#placeholder for future functionality
class Armor:
	def __init__(self, name, protection, weight):
		self.name = name
		self.protection = protection
		self.weight = weight

#placeholder for future functionality
def userFightStats(user, weapon, armor):
	user.speed = 10 - (weapon.weight+armor.weight)
	user.damage = (weapon.damage * weapon.skill)

'''Visiting the blacksmith. Decrease weapon weight or increase weapon damage, which will increase 
chances of success in battle. Checks to user.coins make sure the player can afford the upgrade. '''
def upgradeWeapons(user, weapon):
	print ("You have %d coins. One upgrade point costs ten coins." %user.coins)
	upgrade = str(input("Which would you like to upgrade: Damage or Weight? "))
	if upgrade.lower() == "damage":
		amnt = int(input("How many points would you like to upgrade " + upgrade + "? "))
		if (amnt*10) <= user.coins: 		#multiply upgrade points by cost
			for x in range(0, amnt): 			
				weapon.damage += 1
				user.coins -= 10
			print(weapon.name + "\'s damage is now %d" %weapon.damage)
			print("You have %d coins remaining." %user.coins)
		elif (amnt*10) > user.coins:
			print("Sorry, insufficient funds")
	elif upgrade.lower() == "weight":
		amnt = int(input("How many points would you like to upgrade " + upgrade + "? "))
		if (amnt*10) <= user.coins:			
			for x in range(0, amnt):					
				if weapon.weight == 1:
					print("Weapon is now at minimum weight")
					break
				else:	
					weapon.weight -= 1
					user.coins -= 10
			print(weapon.name + "\'s weight is now %d." %weapon.weight)
			print("You have %d coins remaining." %user.coins)
		elif (amnt*10) > user.coins:
			print("Sorry, insufficient funds")
	elif upgrade.lower() == "stats":
		print("Health: %d\nMoney: %d coins" %(user.health, user.coins))
	
	moreSmithing = str(input("Anything else before you go? "))
	if moreSmithing == 'yes':		#todo: handle input for weight, damage, any other future upgrades
		upgradeWeapons(user,sword)
	else:
		print("Fare thee well, traveler.")
		return

'''Inn. Allows the traveler to restore hit point in exchange for coin. Requires explicit 'leave' 
command to leave. This is in order to handle unrecognized input without breaking. Anything not listed 
will call back into the function, allowing the user to input viable options.'''
def inn(user):
	innOptions = ["rent room (10 coins)", "buy meal (5 coins)", "chat with patrons","leave"]			
	innChoose = str(input("\nWhat would you like to do? \n>"))
	if innChoose.lower() == "help":		#help function lists out options available to player. 
		for i in range(0,len(innOptions)):
			print(innOptions[i])
		inn(user)
	elif innChoose.lower() == "rent room":
		roomCost = 10
		if user.coins < roomCost:		#check to see if player has enough coin
			print("Insufficient coin")
			inn(user)
		elif user.coins >= roomCost:
			user.health += 15
			user.coins -= roomCost
			print("You rent a room and sleep for the evening, waking up feeling refreshed.")	
			inn(user)
	elif innChoose.lower() == "buy meal":
		mealCost = 5
		if user.coins >= mealCost:
			user.health += 5
			user.coins -= mealCost
			print("Ah, delicious! You can feel the meal warm your belly.")
			inn(user)
		elif user.coins < mealCost:		#same check for player coin here too
			print("A little light in the wallet, eh? Looks like you'll be skipping a meal today.")
			inn(user)		
	elif innChoose.lower() == "chat" or innChoose.lower() == "chat with patrons":
		#todo: useful information about fighting strategies, opponents, etc. 
		print("Politics, rumors, and gossip. Nothing useful right now.")
		inn(user)
	elif innChoose.lower() == "stats":
		print("Health: %d \nMoney: %d coins" %(user.health,user.coins))
		inn(user)
	elif innChoose.lower() == "leave":
		print("Come back again soon!")
		return	
	else:
		inn(user)

'''Runs the fights. Main action loop of the game. Takes user and weapon stats and uses them in encounter.'''
def fightSimulator(user, weapon):
	enemyHealth = 25
	totalDealt=0
	totalReceived=0
	while enemyHealth > 0:
		ladyLuck = random.uniform(0.0, 1.0)
		blowDealt = (weapon.skill*weapon.damage-weapon.weight)*ladyLuck 	#This is where upgrades come in. Right now, they're the most effective way to win. todo: balance upgrades
		blowReceived = 5*random.uniform(0.0,1.0)*weapon.skill 				#multiplying by weapon skill to help balance encounters. Leveling foes at similar pace to player.
		enemyHealth -= blowDealt				#enemy always takes damage before player
		if enemyHealth > 0:
			user.health -= blowReceived
			totalReceived+=blowReceived			#only add the current player damage *after* confirming that the enemy is still alive
		if user.health < 1:
			print("You fainted!")
			return
		totalDealt+=blowDealt					#only add damage to enemys *after* confirming that player is still conscious
	print("You are victorious! You clutch the purse with your winnings, exhausted.")
	print("You dealt: %d damage \nYou received: %d damage" %(totalDealt,totalReceived))		#print damage stats to give player an idea of how they're leveling up
	weapon.skill += 0.2
	'''increase the pot as the player starts increasing their skill, and thus having more difficult encounters. 
	Using int() keeps the numbers nice and round, and provides the illusion of combat levels.'''
	user.coins += 25*int(weapon.skill)		
	return

'''Houses the main loops of the game. Training is done here, and fighting is its own function.  '''
def stadium(user, weapon):
	trainOptions = ["fight in the arena", "train (5 gold)", "leave"]
	choice = str(input("\nWhat would you like to do? \n>"))
	if choice.lower() == "fight":
		fightSimulator(user, weapon)
		if user.health < 1:			#if the user has less than 1 HP, they've fainted. Quit out to waking up in the Inn.
			return
		else:
			stadium(user, weapon)
	elif choice.lower() == "train":
		if user.coins>4: 		#check to see if player has enough coin
			weapon.skill += 0.1
			user.coins -= 5
			stadium(user,weapon)
		else:
			print("Trainers don't work for free, kid.")		#If player doesn't have enough coin, don't let them train. 
			stadium(user,weapon)
	elif choice.lower()	== "leave":
		print("As you exit, the roar of the stadium fades.")
		return
	elif choice.lower() == "stats":
		print("Health: %d\nMoney: %d coins" %(user.health, user.coins))
		stadium(user,weapon)
	elif choice.lower() == "help":
		for i in range(0,len(trainOptions)):
			print(trainOptions[i])
		stadium(user, weapon)
	else:
		stadium(user, weapon)
	
		
sword = Weapon("Dull Sword", 5, 4)
user1 = User(30, 100)				
whatdo = ""
print("Hello. 'Help' will show you your options. 'Stats' will show you your character information. 'Leave' will leave your current location.")

while whatdo != "quit":	
	print("\nWhat would you like to do?")
	places = ["smithy", "inn", "stadium", "leave"]				
	whatdo = str(input(">"))
	if whatdo.lower() == 'help': #show player available options by iterating through list representing current functions
		print("Your options are:")
		for i in range(0,len(places)):
			print (places[i])
	elif whatdo.lower() == "smithy":
		upgradeWeapons(user1, sword)
	elif whatdo.lower() == "inn":
		print("You walk into the inn. A fire crackles in the corner and you can smell the mutton they're serving today.")
		inn(user1)
	elif whatdo.lower() == "stadium":
		print("Best of luck! \n \nYou walk into the stadium training grounds. The smells of blood and beer hang in the air.")
		stadium(user1, sword)
		if user1.health <= 1:
			user1.coins -= 10
			if user1.coins>0:
				print("You wake up in a bed at the inn. You're bruised, but still alive. Perhaps some training would be in order.") #Hey you, you're finally awake. You were trying to cross the border, right?
				user1.health = 15
				inn(user1)
			else:
				print("You wake up in a cell, your pockets empty. It's debtor's prison for you. Maybe in your next life you'll be more lucky...") #handle player going below zero coins by quitting.
				whatdo="quit"
	elif whatdo.lower() == "money":		#dev mode to get more coins if necessary. No cheating :)
		user1.coins += 10
		print(user1.coins)
	elif whatdo.lower() == "stats":
		print("Health: %d \nMoney: %d coins" %(user1.health,user1.coins))
	elif whatdo.lower() == "leave":
		print("You venture forth from the small town...") #todo: add an adventure!
		whatdo="quit"
	else:
		print("I'm sorry, I don't understand.")
		
