from alt import *

with open("./words.csv", "a+") as file:
	start = True
	print("режим(1_ - із фото. 2_ - без фото), Слово, Значення, Приклад, мітка(verb, noun...), href-google, href-name, href-alt\n")

	while start:
		blank_text = input()
		blank_words = blank_text.split(', ')

		if blank_text == 'q':
			break

		elif blank_words[0] == "1_" and len(blank_words) == 8:
			file.write(f"{blank_words[1]}|{blank_words[2]}|{blank_words[3]}|{blank_words[4]}|{blank_words[5]}|{blank_words[6]}|{blank_words[7]}\n")
			
		elif blank_words[0] == "2_" and len(blank_words) == 5:
			file.write(f"{blank_words[1]}|{blank_words[2]}|{blank_words[3]}|{blank_words[4]}|{href_google}|{href_name}|{href_alt}\n")
			
		else:
			print("Рядок має бути коректним, маючи роздільник: ', ' або 'q' для виходу")