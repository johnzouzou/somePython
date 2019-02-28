##returns the position of the International space station
import requests
from datetime import datetime

def locate_iss():
	 response = requests.get("http://api.open-notify.org/iss-now.json")
	 if response.status_code != 200:
	 	return print('Failed')
	 else:
	 	data = response.json()
	 	lat = data['iss_position']['latitude']
	 	log = data['iss_position']['longitude']
	 	print(f"{lat} is the latiude ")
	 	print(f"{log} is the longitude ")
	 	print(f"{lat}, {log}")
	 	print(f"{datetime.fromtimestamp(data['timestamp'])} is the date and Time")


locate_iss()

