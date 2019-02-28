#dad joke 3000
import pyfiglet
import requests
import random
title = "CHOAD Jokes 3000"
my_title = pyfiglet.figlet_format(title)
print(my_title)
url = 'https://icanhazdadjoke.com/search'
topic = input("Enter Joke Topic: ")
response = requests.get(url, headers={'Accept':'application/json'},params={'term': topic})
data = response.json()
if data.get('total_jokes') == 0:
	print(f"No jokes about {topic}, please try again.")
elif data.get('total_jokes') == 1:
	print(f"One joke found about {topic} ")
	#print(dict(joke))
	val = data['results']
	print(val[0].get('joke'))
	#fin = joke.get('joke')
	#print(fin)
else:
	jokes = [x['joke'] for x in data['results']]
	print(f"Total Jokes on {topic} are { data.get('total_jokes') }")
	print(f"One is: {pyfiglet.figlet_format(random.choice(jokes))}")
