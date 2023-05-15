import sys
import itertools
import concurrent.futures

file = sys.argv[1]
with open(file) as f:
	files = [user.strip() for user in f]
	f.close()

def permutator(user):

	with open("u.txt",'a')as nu:
		#lowercase the first letter
		user = user.lower()
		nu.write(user+'\n')

    #change all letter i to 1
		change = user.replace('i','1')
		nu.write(change+'\n')
    #change all letter a to @
		change = user.replace('a','@')
		nu.write(change+'\n')
    #change all letter s to $
		change = user.replace('s','$')
		nu.write(change+'\n')
    #change all letter e to 3
		change = user.replace('e','3')
		nu.write(change+'\n')
	#change all letter o to 0
		change = user.replace('o','0')
		nu.write(change+'\n')


	#capitalize the first letter
		user = user.capitalize()
		nu.write(user+'\n')


	#capitalized change specific letters


	#change all letter i to 1
		change = user.replace('i','1')
		nu.write(change+'\n')
    #change all letter a to @
		change = user.replace('a','@')
		nu.write(change+'\n')
    #change all letter s to $
		change = user.replace('s','$')
		nu.write(change+'\n')
	#change all letter e to 3
		change = user.replace('e','3')
		nu.write(change+'\n')
	#change all letter o to 0
		change = user.replace('o','0')
		nu.write(change+'\n')

	#change all occurances of letters


	#change all letter i to 1
		change = user.casefold().replace('i','1')
		nu.write(change+'\n')
	#change all letter a to @
		change = user.casefold().replace('a','@')
		nu.write(change+'\n')
	#change all letter s to $
		change = user.casefold().replace('s','$')
		nu.write(change+'\n')
	#change all letter e to 3
		change = user.casefold().replace('e','3')
		nu.wirte(cahnge+'\n')
	 #change all letter o to 0
		change = user.casefold().replace('o','0')
		nu.write(change+'\n')

	nu.close()

with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
    executor.map(permutator, files)



with open('u.txt','r')as nu:
	lines = nu.readlines()
	lines = set(lines)
	with open("newusers.txt",'a')as users:
		users.writelines(lines)
	
