import requests
import time
while True:
	url = "https://icanhazdadjoke.com/"
	response = requests.get(url, headers={"Accept":"application/json"})
	data = response.json()
	print(data["joke"])
	time.sleep(1)
	val = input ('\n q to quit or enter for more jokes! \n')
	if(val == 'q'):
		break
	for i in range(5):
		time.sleep(1)
		print(f"New joke in {5 - i}")
 