import random

with open('Noun.txt', 'r') as f:
	nouns = [word for line in f for word in line.split()]
	
with open('Adjective.txt', 'r') as f:
	adjective = [word for line in f for word in line.split()]
	
with open('Adverb.txt', 'r') as f:
	adverb = [word for line in f for word in line.split()]
	
with open('Verb.txt', 'r') as f:
	verb = [word for line in f for word in line.split()]
	
with open('Determiner.txt', 'r') as f:
	determiner = [word for line in f for word in line.split()]
	
with open('Pronoun.txt', 'r') as f:
	pronoun = [word for line in f for word in line.split()]
	
conjunction = ("and", "but", "either", "or")

adjNum = random.randrange(0, len(adjective))
detNum = random.randrange(0, len(determiner))
nounNum = random.randrange(0, len(nouns))
advNum = random.randrange(0, len(adverb))
verbNum = random.randrange(0, len(verb))
proNum = random.randrange(0, len(pronoun))
conjunctNum = random.randrange(0, len(conjunction))

i = 0
while i < 5:
	if i == 0:
		if advNum == 3 or advNum == 5:
			print(adverb[advNum].capitalize() + ' ' + adjective[adjNum].lower() + ' ' + conjunction[conjunctNum].lower() + ' ' + determiner[detNum].lower() + ' ' + nouns[nounNum].lower() + "?")
		else:
			print(adverb[advNum].capitalize() + ' ' + adjective[adjNum].lower() + ' ' + conjunction[conjunctNum].lower() + ' ' + determiner[detNum].lower() + ' ' + nouns[nounNum].lower())
			
	if i == 1:
		print(pronoun[proNum].capitalize() + ' ' + verb[verbNum].lower() + ' ' + nouns[nounNum].lower())
			
	if i == 2:
		print(verb[verbNum].capitalize() + ' ' + verb[random.randrange(0, len(verb))].lower() + ' ' + adjective[adjNum] + ' ' + nouns[nounNum].lower())
			
	if i == 3:
		print(nouns[nounNum].capitalize() + ' ' + verb[verbNum].lower() + ' ' + conjunction[conjunctNum] + ' ' + determiner[detNum] + ' ' + nouns[random.randrange(0, len(nouns))].lower())
			
	if i == 4:
		if advNum == 3 or advNum == 5:
			print(adverb[advNum].capitalize() + ' ' + adjective[adjNum].lower() + ' ' + conjunction[conjunctNum].lower() + ' ' + determiner[detNum].lower() + ' ' + nouns[nounNum].lower() + "?")
		else:
			print(adverb[advNum].capitalize() + ' ' + adjective[adjNum].lower() + ' ' + conjunction[conjunctNum].lower() + ' ' + determiner[detNum].lower() + ' ' + nouns[nounNum].lower())
			
	advNum = random.randrange(0, len(adverb))
	adjNum = random.randrange(0, len(adjective))
	detNum = random.randrange(0, len(determiner))
	nounNum = random.randrange(0, len(nouns))
	verbNum = random.randrange(0, len(verb))
	proNum = random.randrange(0, len(pronoun))
	conjunctNum = random.randrange(0, len(conjunction))
	
	i += 1
	
print('\n')

i = 0
while i < 5:
	if i == 0:
		if advNum == 3 or advNum == 5:
			print(adverb[advNum].capitalize() + ' ' + adjective[adjNum].lower() + ' ' + conjunction[conjunctNum].lower() + ' ' + determiner[detNum].lower() + ' ' + nouns[nounNum].lower() + "?")
		else:
			print(adverb[advNum].capitalize() + ' ' + adjective[adjNum].lower() + ' ' + conjunction[conjunctNum].lower() + ' ' + determiner[detNum].lower() + ' ' + nouns[nounNum].lower())
			
	if i == 1:
		print(pronoun[proNum].capitalize() + ' ' + verb[verbNum].lower() + ' ' + nouns[nounNum].lower())
			
	if i == 2:
		print(verb[verbNum].capitalize() + ' ' + verb[random.randrange(0, len(verb))].lower() + ' ' + adjective[adjNum] + ' ' + nouns[nounNum].lower())
			
	if i == 3:
		print(nouns[nounNum].capitalize() + ' ' + verb[verbNum].lower() + ' ' + conjunction[conjunctNum] + ' ' + determiner[detNum] + ' ' + nouns[random.randrange(0, len(nouns))].lower())
			
	if i == 4:
		if advNum == 3 or advNum == 5:
			print(adverb[advNum].capitalize() + ' ' + adjective[adjNum].lower() + ' ' + conjunction[conjunctNum].lower() + ' ' + determiner[detNum].lower() + ' ' + nouns[nounNum].lower() + "?")
		else:
			print(adverb[advNum].capitalize() + ' ' + adjective[adjNum].lower() + ' ' + conjunction[conjunctNum].lower() + ' ' + determiner[detNum].lower() + ' ' + nouns[nounNum].lower())
			
	advNum = random.randrange(0, len(adverb))
	adjNum = random.randrange(0, len(adjective))
	detNum = random.randrange(0, len(determiner))
	nounNum = random.randrange(0, len(nouns))
	verbNum = random.randrange(0, len(verb))
	proNum = random.randrange(0, len(pronoun))
	conjunctNum = random.randrange(0, len(conjunction))
	
	i += 1
