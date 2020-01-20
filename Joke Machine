from random import randint
figlettext = figlet_format("Dad Jokinator 1.1","slant")
color_figlettext = colored(figlettext,"cyan")
print(color_figlettext)
k = 0
while k == 0:
	user_input = input("Take your daily dad joke dose. Give me a topic: ")
	url= "https://icanhazdadjoke.com/search"
	response=requests.get(
		url,
		headers = {"Accept":"Application/json"},
		params = {"term" : user_input}
	).json()
	num_jokes = response["total_jokes"]
	if num_jokes > 1:
		print(f"There are {num_jokes} {user_input} jokes. Here's a one!")
		print(response["results"][randint(0,num_jokes)]["joke"])
		k = 1
	elif num_jokes == 1:
		print(f"We have only a single {user_input} joke.")
		print(response["results"][0]["joke"])
		k = 1
	else:
		print(f"Sorry, we don't have any {user_input} jokes.")
