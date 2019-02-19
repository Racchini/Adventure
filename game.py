#dank memes dank memes dank memes dank memes
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

def smithy(verify):
	if verify == "y":
		upgradeWeapons(user1, sword)
		
	elif verify == "n":
		print("Aww, ok.") 

	else:
		verify
#visiting the blacksmith
def upgradeWeapons(user, weapon):
	print ("You have %d coins. One upgrade point costs one coin." %user.coins)
	upgrade = str(input("Which would you like to upgrade: Damage or Weight? "))
	if upgrade.lower() == "damage":
		amnt = int(input("How many points would you like to upgrade " + upgrade + "? "))
		if amnt <= user.coins:
			for x in range(0, amnt): 			
				weapon.damage += 1
				user.coins -= 1
			print(weapon.name + "\'s damage is now %d" %weapon.damage)
			print("You have %d coins remaining." %user1.coins)
		elif amnt > user.coins:
			print("Sorry, insufficient funds")
			
	if upgrade.lower() == "weight":
		amnt = int(input("How many points would you like to upgrade " + upgrade + "? "))
		if amnt <= user.coins:			
			for x in range(0, amnt):					
				if weapon.weight == 1:
					print("Weapon is now at minimum weight")
					break
				else:	
					weapon.weight -= 1
					user.coins -= 1
			print(weapon.name + "\'s weight is now %d." %weapon.weight)
			print("You have %d coins remaining." %user1.coins)
		elif amnt > user.coins:
			print("Sorry, insufficient funds")
	moreSmithing = str(input("anything else before you go? "))
	if moreSmithing == 'yes':
		upgradeWeapons(user1,sword)
	else:
		return
		
def inn(user):
	innOptions = ["rent room", "buy meal", "chat with patrons"]			
	innChoose = str(input("What would you like to do? \n>"))
	if innChoose.lower() == "list":
		for i in range(0,len(innOptions)):
			print(innOptions[i])
		inn(user)
	elif innChoose.lower() == "rent room":
		roomCost = 10
		if user.coins < roomCost:
			print("Insufficient coins")
			inn(user)
		elif user.coins >= roomCost:
			user.health += 15
			user.coins -= 10
			print("You rent a room and sleep for the evening, waking up feeling refreshed.")	
			inn(user)
	elif innChoose.lower() == "buy meal":
		mealCost = 5
		if user.coins >= mealCost:
			user.health += 5
			user.coins -= 5
			print("Ah, delicious! You can feel the meal warm your belly.")
			inn(user)
		elif user.coins < mealCost:
			print("A little light in the wallet, eh? Looks like you'll be skipping a meal today.")
			inn(user)		
	elif innChoose.lower() == "chat with patrons":
		print("Politics, rumors, and gossip. Nothing useful right now.")
		inn(user)
	elif innChoose.lower() == "leave":
		return	
	elif innChoose.lower() == "wallet":
		print(user.coins)
		inn(user)
	else:
		inn(user)

def fightSimulator(user, weapon):
	enemyHealth = 25
	while enemyHealth > 0:
		ladyLuck = random.uniform(0.0, 1.0)
		blowDealt = weapon.skill*weapon.damage*ladyLuck
		blowReceived = 5*random.uniform(0.0,1.0)
		enemyHealth -= blowDealt
		if enemyHealth > 0:
			user.health -= blowReceived
		if user.health < 1:
			print("You fainted!")
			return
	print("You are victorious!")	
	user.coins += 5
	weapon.skill += 0.1
	return

def training(user, weapon):
	trainOptions = ["fight in the arena", "train", "leave"]
	choice = str(input("What would you like to do? \n>"))
	if choice.lower() == "fight":
		fightSimulator(user, weapon)
		if user.health < 1:
			return
		else:
			training(user, weapon)
	elif choice.lower() == "train":
		weapon.skill += 0.1
		user.coins -= 5
	elif choice.lower()	== "leave":
		return
	elif choice.lower() == "stats":
		print("Health: %d\nMoney: %d coins" %(user.health, user.coins))
		training(user,weapon)
	elif choice.lower() == "list":
		for i in range(0,len(trainOptions)):
			print(trainOptions[i])
		training(user, weapon)
	else:
		training(user, weapon)
	
		
sword = Weapon("sword", 5, 4)
user1 = User(50, 100)				
whatdo = " "
print("Hello")

while whatdo != "quit":	
	places = ["smithy", "town square", "inn", "training grounds", "leave"]				
	whatdo = str(input(">"))
	if whatdo.lower() == 'help':
		print("Your options are:")
		for i in range(0,len(places)):
			print (places[i])
	if whatdo.lower() == "smithy":
		upgradeWeapons(user1, sword)
	if whatdo.lower() == "inn":
		print("You walk into the inn. A fire crackles in the corner and you can smell the mutton they're serving today.")
		inn(user1)
	if whatdo.lower() == "training grounds":
		print("Best of luck! \n \nYou walk into the training grounds. The smell of blood and beer hangs in the air")
		training(user1, sword)
		if user1.health <= 1:
			print("You wake up in a bed at the in. You're bruised, but alive.")
			user1.health = 15
			user1.coins -= 20
			inn(user1)
	if whatdo.lower() == "money":
		user1.coins += 10
		print(user1.coins)
	if whatdo.lower() == "stats":
		print("Health: %d \nMoney: %d coins" %(user1.health,user1.coins))
	if whatdo.lower() == "leave":
		print("You venture forth from the small town.")
		