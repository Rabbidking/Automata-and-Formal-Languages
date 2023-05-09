curWord = []
sep = ''
phrase = "011101000110100101100101011100110010000001110011011101010110001101101011"
letters = {
	0:'a', 
	1:'b', 
	2:'c', 
	3:'d', 
	4:'e', 
	5:'f', 
	6:'g', 
	7:'h', 
	8:'i', 
	9:'j', 
	10:'k', 
	11:'l', 
	12:'m', 
	13:'n', 
	14:'o', 
	15:'p', 
	16:'q', 
	17:'r', 
	18:'s', 
	19:'t', 
	20:'u', 
	21:'v', 
	22:'w', 
	23:'x', 
	24:'y', 
	25:'z', 
	26:' '
	}

#This breaks up the phrase into individual 8-bit binary strings to determine individual characters
phrase_chars = [phrase[i:i+8] for i in range(0, len(phrase), 8)]

with open('words.txt') as f:
	for j in phrase_chars:
		for i in phrase_chars:
			if i[0] == 1:
				#no ASCII character in binary starts with a 1
				print("Not a valid ASCII character!")
		
			#check for character
			
			#a
			if j == '01100001':
				curWord += letters[0]
				
			#b
			elif j == '01100010':
				curWord += letters[1]
				
			#c
			elif j == '01100011':
				curWord += letters[2]
				
			#d
			elif j == '01100100':
				curWord += letters[3]
				
			#e
			elif j == '01100101':
				curWord += letters[4]
				
			#f
			elif j == '01100110':
				curWord += letters[5]
				
			#g
			elif j == '01100111':
				curWord += letters[6]
				
			#h
			elif j == '01101000':
				curWord += letters[7]
				
			#i
			elif j == '01101001':
				curWord += letters[8]
				
			#j
			elif j == '01101010':
				curWord += letters[9]
				
			#k
			elif j == '01101011':
				curWord += letters[10]
				
			#l
			elif j == '01101100':
				curWord += letters[11]
				
			#m
			elif j == '01101101':
				curWord += letters[12]
				
			#n
			elif j == '01101110':
				curWord += letters[13]
				
			#o
			elif j == '01101111':
				curWord += letters[14]
				
			#p
			elif j == '01110000':
				curWord += letters[15]
				
			#q
			elif j == '01110001':
				curWord += letters[16]
				
			#r
			elif j == '01110010':
				curWord += letters[17]
				
			#s
			elif j == '01110011':
				curWord += letters[18]
			
			#t
			elif j == '01110100':
				curWord += letters[19]
			
			#u
			elif j == '01110101':
				curWord += letters[20]
				
			#v
			elif j == '01110110':
				curWord += letters[21]
			
			#w
			elif j == '01110111':
				curWord += letters[22]
				
			#x
			elif j == '01111000':
				curWord += letters[23]
				
			#y
			elif j == '01111001':
				curWord += letters[24]
				
			#z
			elif j == '01111010':
				curWord += letters[25]
				
			#space character
			elif j == '00100000':
				curWord += letters[26]
				#if sep.join(curWord) in f.read():
					#print(sep.join(curWord), end = ' ')
				#curWord.clear()
				#continue
			
		else:
			print("Not valid!")
			break