#https://www.rithmschool.com/blog
import requests
from bs4 import BeautifulSoup
import csv
url = "https://www.rithmschool.com/blog"
# gen strings for crawler
responses = []
payload = [f'page={x}' for x in range(12)]

response =requests.get(url)
responses.append(response)
	
for package in payload:
	try:
		new_response=requests.get(url,params=package)
		responses.append(new_response)
	
	except e:
		print('fail')
		break
	

print(responses)

whole_data= []
for response in responses:
	#parsing page one repsonse
	soup = BeautifulSoup(response.text,'html.parser')
	articals = soup.find_all('article')
		#parsing data from blog with BS
		#csv_writer.writerow(['Title','Date', 'Link'])
	for artical in articals:
		anchor = artical.find('a')
		title = anchor.get_text()
		link = anchor['href']
		time = artical.find('time')['datetime']
		whole_data.append([title,time,link])
		

whole_data = tuple(whole_data)
with open("blog_data_tuple.csv",'w') as f:
	csv_writer = csv.writer(f)
	for blog_post in whole_data:
		csv_writer.writerow(blog_post)
#titles = [artical.find('a').get_text() for artical in articals]
#print(articals)
#print(titles)