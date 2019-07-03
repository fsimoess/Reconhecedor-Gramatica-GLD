#!/usr/bin/env python3

import os

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
	checkState = []
	checkChar = []
	last = False

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
	numChar = 0
	numState = 0

	for item in transitions:
		for x in item:
			if x == '>':
				last = True
			if x not in checkState:
				if last and x.isupper():
					if x in states:
						numState+=1
						checkState.append(x)
					else:
						print("A Gramatica não é válida")
						exit()
			if x not in checkChar:
				if last and x.islower():
					if x in characters:
						numChar+=1
						checkChar.append(x)
					else:
						print("A Gramatica não é válida")
						exit()
		last = False

	if numChar == len(characters) and numState == len(states):
		print("A Gramatica foi entrada corretamente")		

	return [states, characters, initial, transitions]

def recognizeGLD(transitions):
	att = False
	verif = False
	last = ""
	count = 0

	for item in transitions:
		for x in item:
			if last == "$":
				print("A Gramatica não é uma GLD")
				exit()
			if x == '>':
				att = True
			if att and x.islower():
				last = x
			if last.islower() and x.isupper():
				last = x
				verif = True
			if x == "$":
				last = x
				verif = True
			if verif and x.islower():
				verif = False
		
		if verif:
			count+=1
		att = False
		verif = False
		last = ""

	if count == len(transitions):
		print("A Gramatica é uma GLD")
		return True
	else:
		print("A Gramatica não é uma GLD")
		return False

def saveAntlr(transitions):
	listRead = []
	text = ""
	hasRead = ""
	att = False

	for item in transitions:
		if item[0] in listRead:
			text = text + ' ' + "\n"
		elif listRead != []:
			text = text + ' ' + ';' + "\n"

		for x in item:
			if x == '>':
				att = True
			if not att and x.isupper():
				if x not in listRead:
					text = text + x.lower() + ' ' + ':' + ' '
					listRead.append(x)
				else:
					text = text + '  ' + '|' + ' '
			if att and x.islower():
				text = text + '\'' + x + '\'' + ' '
			if att and x.isupper():
				text = text + x.lower()
			if x == "$":
				text = text + 'EOF'

		file.write("%s" % text)
		text = ""
		att = False
	file.write(" ; \n")

text = openGrammar()
file = open('GLD.g4', 'w+')
file.write("grammar GLD;\n\n")

states, characters, initial, transitions = validateGrammar(text)
print("-----------------------------------------")
print (states)
print (characters)
print (initial)
print (transitions)
print("-----------------------------------------")

gld = recognizeGLD(transitions)

if gld:
	saveAntlr(transitions)
else:
	exit()

file.close()

myCmd = 'antlr4 -Dlanguage=Python3 GLD.g4'
os.system(myCmd)

myCmd = 'python3 T.py palavra.txt'
os.system(myCmd)