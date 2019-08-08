#!/usr/bin/python3.6
# -*- coding:Utf-8 -*-

import argparse
import json
from tkinter import *

from ibm_watson import LanguageTranslatorV3

from window_constrad import *

# Une apikey est nécéssaire ici pour utiliser l'API d'IBM. Remplacez {apikey} \
# par votre apikey https://www.ibm.com/watson/services/language-translator/
APIKEY = '{apikey}'

def translate(text, language):
	""" Reçoit un texte et un string décrivant le sens de traduction voulu
	Utilise l'API d'IBM Watson Language Translator et renvoie le texte traduit

	"""
	language_translator = LanguageTranslatorV3(
			version='2018-05-01',
			iam_apikey=APIKEY,
			url='https://gateway-lon.watsonplatform.net/language-translator/api')

	translation = language_translator.translate(
			text,
			language).get_result()
	return json.dumps(translation['translations'][0]['translation'], \
ensure_ascii=False).replace("\"", "")

def graphical_interface():
	""" Lance l'interface graphique """
	window = Tk()
	window.title("Constrad")
	window.resizable(height=False, width=False)
	interface = Interface(window)

	interface.mainloop()

def main():
	""" Fonction principale """
	parser = argparse.ArgumentParser(description="Script de traduction angl\
ais => français en ligne de commande")
	group = parser.add_mutually_exclusive_group()
	parser.add_argument("text", nargs="?", type=str, default="", help="texte à traduire")
	group.add_argument("-f", "--francais", action="store_true", \
help="traduit dans le sens anglais => français (par défaut)")
	group.add_argument("-e", "--english", action="store_true", \
help="traduit dans le sens français => anglais")
	group.add_argument("-g", "--graphik", action="store_true", \
help="lance l'interface graphique")
	args = parser.parse_args()

	if args.graphik:
		graphical_interface()

	elif args.text == "":
		print("Veuillez indiquer le texte à traduire en argument ou consulter \
l'aide avec l'option \"--help\"\n")

	else:
		if args.english:
			language = "fr-en"

		else:
			language = "en-fr"

		translation = translate(args.text, language)
		print(translation)

if __name__ == "__main__":
	main()
