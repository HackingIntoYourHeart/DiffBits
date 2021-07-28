from colorama import Fore, Back, Style, init
init()

def divide(string):
	return [char for char in string]

string1 = input("String 1: ")
string2 = input("String 2: ")

print("")

if len(string1) > len(string2):
	length = len(string1)
else:
	length = len(string2)

diff_array = []
for i in range(0,length):
	try:
		if string1[i] != string2[i]:
			diff_array.append("d")
		else:
			diff_array.append("s")
	except IndexError:
		diff_array.append("l")

def output(string):
	try:
		for i in range(0,length):
			if diff_array[i] == "d":
				print(Fore.RED + string[i], end="")
			if diff_array[i] == "s":
				print(Fore.WHITE + string[i], end="")
			if diff_array[i] == "l":
				print(Fore.YELLOW + string[i], end="")
	except IndexError:
		pass

output(string1)
print("")
output(string2)
print("")

print(Style.RESET_ALL)
