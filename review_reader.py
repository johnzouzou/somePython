#file for reading wiki movie reviews into object 
import csv
import time

def line_to_dic(line):
	return dict(year=line[0],title=line[1],orgin=line[2],director=line[3],cast=line[4],gene=line[5], url=line[6],plot = line[7])
	
with open('wiki_movie_plots_deduped.csv','r', encoding='utf-8') as file:
	start = time.time()
	movieReader = csv.reader(file ,delimiter=",")
	movies = []
	n = 0
	for line in movieReader:
		n+=1
		try:
			movies.append(line_to_dic(line))
		except:
			print(f"Error with line {n}\n")
			
	end = time.time()
	print(f"total lines: {n} in {end - start} secs")
