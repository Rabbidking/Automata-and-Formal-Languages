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
	
for j in range(0, 7):
	for i in phrase:
	
		if i[0] == 1:
				#no ASCII character in binary starts with a 1
				print("Not a valid ASCII character!")
				
		if i[0] == 0:	#0
			if i[1] == 0:
				if i[2] == 1:
					if i[3] == 0:
						if i[4] == 0:
							if i[5] == 0:
								if i[6] == 0:
									if i[7] == 0:
										print(letters[26]) #space
			if i[1] == 1:	#01
				if i[2] == 1:	#011
					if i[3] == 0:	#0110
						if i[4] == 0:	#01100
							if i[5] == 0:	#011000
								if i[6] == 0:	#0110000
									if i[7] == 1:
										print(letters[0]) #A -> 01100001
								if i[6] == 1:
									if i[7] == 0:
										print(letters[1]) #B -> 01100010
									if i[7] == 1:
										print(letters[2]) #C
							if i[5] == 1:
								if i[6] == 0:
									if i[7] == 0:
										print(letters[3]) #D
									if i[7] == 1:
										print(letters[4]) #E	
								if i[6] == 1:
									if i[7] == 0:
										print(letters[5]) #F
									if i[7] == 1:
										print(letters[6]) #G
										
						if i[4] == 1:
							if i[5] == 0:
								if i[6] == 0:
									if i[7] == 0:
										print(letters[7]) #H
									if i[7] == 1:
										print(letters[8]) #I
								if i[6] == 1:
									if i[7] == 0:
										print(letters[9]) #J
									if i[7] == 1:
										print(letters[10]) #K
							if i[5] == 1:
								if i[6] == 0:
									if i[7] == 0:
										print(letters[11]) #L
									if i[7] == 1:
										print(letters[12]) #M
								if i[6] == 1:
									if i[7] == 0:
										print(letters[13]) #N
									if i[7] == 1:
										print(letters[14]) #O
							
					if i[3] == 1:
						if i[4] == 0:
							if i[5] == 0:
								if i[6] == 0:
									if i[7] == 0:
										print(letters[15])	#P
									if i[7] == 1:
										print(letters[16])	#Q
										
								if i[6] == 1:
									if i[7] == 0:
										print(letters[17]) 	#R
									if i[7] == 1:
										print(letters[18])	#S
										
							if i[5] == 1:
								if i[6] == 0:
									if i[7] == 0:
										print(letters[19])	#T
									if i[7] == 1:
										print(letters[20])	#U
								if i[6] == 1:
									if i[7] == 0:
										print(letters[21]) #V
									if i[7] == 1:
										print(letters[22]) #W
								
						if i[4] == 1:
							if i[5] == 0:
								if i[6] == 0:
									if i[7] == 0:
										print(letters[23])	#X
									if i[7] == 1:
										print(letters[24])	#Y
								if i[6] == 1:
									if i[7] == 0:
										print(letters[25])	#Z