import random

words = ("skillfactory", "testing", "blackbox", "pytest", "unittest", "coverage")

secret_word = random.choice(words)

first_word = ['_ '] * len(secret_word)
print(''.join(first_word))

error_count = 0 
def rungame():
	error_count = 0 
	while True:
	    letter = input('\nвведите одну английскую букву: ')	#ввод буквы
	    if letter in secret_word:#если буква есть в рандомном слове
	    	for index, simbol in enumerate(secret_word): # разбиение букв в слове на индексы
	    		if simbol == letter: # если символ слова совпал с введенной буквой
	    			first_word[index] = simbol # тогда индекс элемента в слове будет равняться этой букве
	    	if '_ ' not in first_word:
	    		print("Победа: " + secret_word.upper())
	    		break
	    else:
	    	error_count += 1
	    	print('ошибок допущенно: ' + str(error_count) )
	    	if error_count == 4:
	    		print("Поражение")
	    		break
	
	    print(''.join(first_word))
#rungame()	 
