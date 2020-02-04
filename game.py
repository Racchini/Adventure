import random 

class User:
	def __init__(self, coins, health):
		self.coins = coins
		self.health = health

class Weapon:
	def __init__(self, name, damage, weight):
		self.name = name		
		self.weight = weight
		self.damage = damage
		self.skill = 1 
		
class Armor:
	def __init__(self, name, protection, weight):
		self.name = name
		self.protection = protection
		self.weight = weight
		
def userFightStats(user, weapon, armor):
	user.speed = 10 - (weapon.weight+armor.weight)
	user.damage = (weapon.damage * weapon.skill)

#visiting the blacksmith
def upgradeWeapons(user, weapon):
	print ("You have %d coins. One upgrade point costs ten coins." %user.coins)
	upgrade = str(input("Which would you like to upgrade: Damage or Weight? "))
	if upgrade.lower() == "damage":
		amnt = int(input("How many points would you like to upgrade " + upgrade + "? "))
		if (amnt*10) <= user.coins:
			for x in range(0, amnt): 			
				weapon.damage += 1
				user.coins -= 10
			print(weapon.name + "\'s damage is now %d" %weapon.damage)
			print("You have %d coins remaining." %user1.coins)
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
			print("You have %d coins remaining." %user1.coins)
		elif (amnt*10) > user.coins:
			print("Sorry, insufficient funds")
	elif choice.lower() == "stats":
		print("Health: %d\nMoney: %d coins" %(user.health, user.coins))
	
	moreSmithing = str(input("Anything else before you go? "))
	if moreSmithing == 'yes':
		upgradeWeapons(user1,sword)
	else:
		print("Fare thee well, traveler.")
		return
		
def inn(user):
	innOptions = ["rent room (10 coins)", "buy meal (5 coins)", "chat with patrons"]			
	innChoose = str(input("\nWhat would you like to do? \n>"))
	if innChoose.lower() == "help":
		for i in range(0,len(innOptions)):
			print(innOptions[i])
		inn(user)
	elif innChoose.lower() == "rent room":
		roomCost = 10
		if user.coins < roomCost:
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
		elif user.coins < mealCost:
			print("A little light in the wallet, eh? Looks like you'll be skipping a meal today.")
			inn(user)		
	elif innChoose.lower() == "chat" or innChoose.lower() == "chat with patrons":
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

def fightSimulator(user, weapon):
	enemyHealth = 25
	totalDealt=0
	totalReceived=0
	while enemyHealth > 0:
		ladyLuck = random.uniform(0.0, 1.0)
		blowDealt = (weapon.skill*weapon.damage-weapon.weight)*ladyLuck
		blowReceived = 5*random.uniform(0.0,1.0)*weapon.skill
		enemyHealth -= blowDealt
		if enemyHealth > 0:
			user.health -= blowReceived
			totalReceived+=blowReceived
		if user.health < 1:
			print("You fainted!")
			return
		totalDealt+=blowDealt
	print("You are victorious! You clutch the purse with your winnings, exhausted.")
	print("You dealt: %d damage \nYou received: %d damage" %(totalDealt,totalReceived))
	weapon.skill += 0.2
	user.coins += 25*int(weapon.skill)
	return

def training(user, weapon):
	trainOptions = ["fight in the arena", "train (5 gold)", "leave"]
	choice = str(input("\nWhat would you like to do? \n>"))
	if choice.lower() == "fight":
		fightSimulator(user, weapon)
		if user.health < 1:
			return
		else:
			training(user, weapon)
	elif choice.lower() == "train":
		if user.coins>4:
			weapon.skill += 0.1
			user.coins -= 5
			training(user,weapon)
		else:
			print("Trainers don't work for free, kid.")
			training(user,weapon)
	elif choice.lower()	== "leave":
		print("As you exit, the roar of the statium fades.")
		return
	elif choice.lower() == "stats":
		print("Health: %d\nMoney: %d coins" %(user.health, user.coins))
		training(user,weapon)
	elif choice.lower() == "help":
		for i in range(0,len(trainOptions)):
			print(trainOptions[i])
		training(user, weapon)
	else:
		training(user, weapon)
	
		
sword = Weapon("sword", 5, 4)
user1 = User(30, 100)				
whatdo = " "
print("Hello. 'Help' will show you your options. 'Stats' will show you your charater information. 'Leave' will leave your current location.")

while whatdo != "quit":	
	print("\nWhat would you like to do?")
	places = ["smithy", "inn", "training grounds", "leave"]				
	whatdo = str(input(">"))
	if whatdo.lower() == 'help':
		print("Your options are:")
		for i in range(0,len(places)):
			print (places[i])
	elif whatdo.lower() == "smithy":
		upgradeWeapons(user1, sword)
	elif whatdo.lower() == "inn":
		print("You walk into the inn. A fire crackles in the corner and you can smell the mutton they're serving today.")
		inn(user1)
	elif whatdo.lower() == "training grounds":
		print("Best of luck! \n \nYou walk into the training grounds. The smells of blood and beer hang in the air.")
		training(user1, sword)
		if user1.health <= 1:
			user1.coins -= 10
			if user1.coins>0:
				print("You wake up in a bed at the in. You're bruised, but alive. Perhaps some training would be in order.")
				user1.health = 15
				inn(user1)
			else:
				print("You wake up in a cell, your pockets empty. It's debtor's prison for you. Maybe in your next life you'll be more lucky...")
				whatdo="quit"
	elif whatdo.lower() == "money":
		user1.coins += 10
		print(user1.coins)
	elif whatdo.lower() == "stats":
		print("Health: %d \nMoney: %d coins" %(user1.health,user1.coins))
	elif whatdo.lower() == "leave":
		print("You venture forth from the small town...")
		whatdo="quit"
	else:
		print("I'm sorry, I don't understand.")
		
