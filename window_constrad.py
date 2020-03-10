# -*- Coding:Utf-8 -*-

import os

from tkinter import *

from constrad import translate

scriptDir = os.path.dirname(os.path.abspath(__file__))

class Interface(Frame):
	""" Classe permettant la création d'une interface graphique

	"display_translation" récupère la saisie et l'affiche après l'avoir traduit
	"reverse_translation_way" inverse le sens de traduction

	"""
	def __init__(self, window, **kwargs):
		""" Constructeur de la classe Inferface

		Le sens de traduction est déterminé par l'attribut "language"

		"""
		# Titre et frames
		Frame.__init__(self, window, **kwargs)
		background_color = "#a92d2d"
		self["bg"] = background_color
		self.pack()
		self.language = "en-fr"

		# Polices
		font_label = "-family arial -size 20 -weight bold -underline 1"
		font_language = "-family arial -size 18 -slant italic"

		self.label = Label(self, text="Constrad - Mode interface graphique", \
bg=background_color, fg="#281d1d", font=font_label)
		self.label.pack(pady=15)

		self.frame_entries = Frame(self, bg=background_color)
		self.frame_entries.pack()

		self.frame_submit = Frame(self, bg=background_color)
		self.frame_submit.pack()

		# Contenu du frame_entries
		# Input
		self.frame_input = Frame(self.frame_entries, bg=background_color)
		self.frame_input.pack(side=LEFT, padx=20)

		# Language
		self.language_input = Label(self.frame_input, text="Anglais", \
bg=background_color, fg="#430808", font=font_language)
		self.language_input.pack(side=TOP, pady=10)
		# Field input
		self.field_input = Frame(self.frame_input)
		self.field_input.pack(side=TOP)
		self.input_scrollbar = Scrollbar(self.field_input)
		self.input_scrollbar.pack(side=RIGHT, fill=Y)
		self.values_input = Text(self.field_input, height=4, width=30, \
relief=RIDGE)
		self.values_input.pack()
		self.values_input.config(yscrollcommand=self.input_scrollbar.set)
		self.input_scrollbar.config(command=self.values_input.yview)
		# Label
		self.label_input = Label(self.frame_input, text="Texte à traduire", \
bg=background_color, fg="#281d1d", font="arial 16")
		self.label_input.pack(side=BOTTOM, pady=6)

		# Reverse button
		self.frame_button_reverse = Frame(self.frame_entries, bg=background_color)
		self.frame_button_reverse.pack(side=LEFT, fill=BOTH)
		self.photo = PhotoImage(file=scriptDir + "/images_constrad/reverse.png")
		self.reverse_button = Button(self.frame_button_reverse, image=self.photo, \
command=self.reverse_translation_way)
		self.reverse_button.pack(side=BOTTOM, padx=25, pady=50)

		# Output
		self.frame_output = Frame(self.frame_entries, bg=background_color)
		self.frame_output.pack(side=RIGHT, padx=20)

		# Language
		self.language_output = Label(self.frame_output, text="Français", \
bg=background_color, fg="#430808", font=font_language)
		self.language_output.pack(side=TOP, pady=10)
		# Field output
		self.field_output = Frame(self.frame_output)
		self.field_output.pack(side=TOP)
		self.output_scrollbar = Scrollbar(self.field_output)
		self.output_scrollbar.pack(side=RIGHT, fill=Y)
		self.values_output = Text(self.field_output, height=4, width=30, \
state=DISABLED, relief=RIDGE)
		self.values_output.pack()
		self.values_output.config(yscrollcommand=self.output_scrollbar.set)
		self.output_scrollbar.config(command=self.values_output.yview)
		# Label
		self.label_output = Label(self.frame_output, text="Texte traduit", \
bg=background_color, fg="#281d1d", font="arial 16")
		self.label_output.pack(side=BOTTOM, pady=6)

		#Contenu du frame_submit
		self.translate = Button(self.frame_submit, text="Traduction", font="arial 18", \
command=self.display_translation)
		self.translate.pack(pady=15)

	def display_translation(self):
		""" Récupère la saisie, la traduit et l'affiche """
		input_text = self.values_input.get(1.0, CURRENT)
		if input_text == "":
			input_text = " "
		output_text = translate(input_text, self.language).replace("\\n", "\n")
		self.values_output.config(state=NORMAL)
		self.values_output.delete(1.0, END)
		self.values_output.insert(END, output_text)
		self.values_output.config(state=DISABLED)

	def reverse_translation_way(self):
		""" Inverse le sens de traduction """
		if self.language == "en-fr":
			self.language = "fr-en"
			self.language_input["text"] = "Français"
			self.language_output["text"] = "Anglais"
		else:
			self.language = "en-fr"
			self.language_input["text"] = "Anglais"
			self.language_output["text"] = "Français"
