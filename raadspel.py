#Raad het woord

import random
import time
import os

woordenlijst = 'woordenlijst.txt'
lijst_goede_letters = []
lengte = 1
os.system('clear')
count = int(0)
goed_geraden = int(1)

#Open woordenlijst. Dit .txt bestand kan worden aangevuld met nieuwe woorden
#Het .txt bestand wordt omgezet naar een [list], hieruit wordt een random woord gekozen
with open(woordenlijst) as woorden_lijst:
	alle_woorden = woorden_lijst.read()
	woord_in_list = list(map(str, alle_woorden.split()))
	random_woord = random.choice(woord_in_list)
	print(random_woord)
		
#bepaal de lengte van het random woord
woord_lengte = (len(random_woord))
print(woord_lengte)
#Zet het woord per letter in een [list]
losse_letters = list(random_woord)


def vul_puntjes_in():
	"""Print het juiste aantal puntjes en vul de reeds geraden letters op hun plek"""
	tel_woord = int(0)
	while tel_woord < woord_lengte:
		if losse_letters[tel_woord] in lijst_goede_letters:
			print(losse_letters[tel_woord], end = '  ')
			tel_woord = tel_woord + 1
		else:
			print(".  ", end = '')
			tel_woord = tel_woord + 1
	print("\n\n")
			

def check_gewonnen():
	"""Vergelijk de [list] met het random woord met de [list] van juist geraden letters,
	als beiden dezelfde letters bevatten, is het woord geraden en dus het spel gewonnen"""
	if all(item in lijst_goede_letters for item in losse_letters):
		os.system('clear')
		print("\n\n\nGefeliciteerd! Je hebt gewonnen...")
		time.sleep(2)
		exit()

def verloren():
	"""Print het eindscherm als de speler heeft verloren"""
	os.system('clear')
	print("\n\n\nHelaas, verloren :-(")
	time.sleep(2)
	exit()

#Onderstaande while loop checkt de speler input
while all(item in lijst_goede_letters for item in losse_letters) == False:
	#Print begin scherm
	os.system('clear')
	print(f"Welkom bij RAAD HET WOORD! \t\t\t\tPoging {count} van 10\n\n\n\n")
	vul_puntjes_in()
	kies_letter = input("\n\n\nKies een letter: ")	
	if kies_letter in losse_letters:
		#Check de status of de speler gewonnen heeft
		lijst_goede_letters.append(kies_letter)
		check_gewonnen()
	elif len(kies_letter) >= 2:
		#Geeft foutmelding als er meer dan 1 letter wordt ingevoerd
		print("\nJe mag 1 letter kiezen! \nProbeer het opnieuw... ")
		time.sleep(2)
		continue
	elif kies_letter == '':
		#Geeft foutmelding als er niets wordt ingevoerd
		print("\nWel iets intypen! \nProbeer het opnieuw... ")
		time.sleep(2)
		continue
	elif str.isdigit(kies_letter):
		#Geeft foutmelding als er een cijfer wordt ingevoerd
		print("\nGeen cijfers, alleen letters invoeren! \nProbeer het opnieuw... ")
		time.sleep(2)
		continue
	elif kies_letter in losse_letters:
		#Geeft melding bij een juiste letter
		goed_geraden = goed_geraden + 1
		print("Goed geraden! ")
		continue
	elif not kies_letter in losse_letters:
		#Geeft melding bij een onjuiste letter en telt de foutieve antwoorden
		os.system('clear')
		print(f"Welkom bij RAAD HET WOORD! \t\t\t\tPoging {count} van 10")
		print("\n\n\n\nHelaas, foute letter! ")
		count = count + 1
		print(f"\n\n\n\n\nProbeer het opnieuw...\n")
		time.sleep(2)
		if count == 10:
			verloren()
		else:
			continue
	

		
		




	


