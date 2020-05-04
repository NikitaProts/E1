import random

words = ("skillfactory", "testing", "blackbox", "pytest", "unittest", "coverage")

secret_word = random.choice(words)

first_word = ['_ '] * len(secret_word)
print(''.join(first_word))

error_count = 0 
def rungame():
	error_count = 0
	while True:
	    letter = input('\nвведите одну английскую букву: ')	
	    if letter in secret_word:
	    	for index, simbol in enumerate(secret_word):
	    		if simbol == letter:
	    			first_word[index] = simbol
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
