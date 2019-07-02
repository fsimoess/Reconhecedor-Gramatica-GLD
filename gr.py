#!/usr/bin/env python3

def openGrammar():
	file = open('./gr.txt', 'r')
	text = file.read()
	file.close()
	return text

def validateGrammar(grammar):
	#print(grammar[5]) # é o {
	phase = 1
	openBracket = False
	states = []
	characters = []
	initial = ""
	aux = ""
	transitions = []
	checkState = 0
	checkChar = 0

	for x in grammar:
		if x == '{' and openBracket == False:
			openBracket = True
		if openBracket == True:
			if phase == 1 and x.isupper():
				states.append(x)
			if phase == 2 and x.islower():
				characters.append(x)
			if phase == 4:
				if x == ',' or x == " " or x == "" or x == '{' or x == '}':
					if aux != "":
						transitions.append(aux)
					aux = ""
				else:
					aux+=x
		if x == '}' and openBracket == True:
			openBracket = False
			phase+=1		

		if phase==3 and openBracket == False:
			if x.isupper():
				initial = x
				phase+=1

	#Realizar verificação se states e characters estão em transitions - ARRUMAR
	for item in transitions:
		for s1 in states:
			if s1 in item:
				checkState+=1
				break
		for c1 in characters:
			if c1 in item:
				checkChar+=1
				break

	print (checkChar, checkState)
	return [states, characters, initial, transitions]

def recognizeGLD(transitions):
	for item in transitions:
		print(item)

text = openGrammar()
file = open('GLD.g4', 'w+')
file.write("grammar GLD;\n")
file.close()

states, characters, initial, transitions = validateGrammar(text)
print (states)
print (characters)
print (initial)
print (transitions)

recognizeGLD(transitions)

