import os
import random


def list_construct():

	list_one_size = random.randint(10,20)

	list_one = []

	x = range(1,list_one_size)

	for elem in x:
		
		num = random.randint(1,20)

		list_one.append(num)
	
	return list_one



def remove(list_c):


		clean_list = []
		for item in list_c:

			if item not in clean_list:
				clean_list.append(item)

		print(clean_list)


		











def main():
	play = True
	print("This will print a random list of numbers and will remove any duplicate numbers.")
	while play == True:

		list_c = list_construct()
		remove(list_c)



		play_again = input('Do you want to run it again? "Yes" or "No": ')

		if play_again == "yes":
			play = True
			os.system('clear')
		else:

			play = False



if __name__ == '__main__':
	main()