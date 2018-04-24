# -*- coding: utf-8 -*-
import csv, os

def main():

	#get the players info
	currentDirectory = os.path.dirname(os.path.abspath(__file__))
	partiFile = open(currentDirectory + '/participantSample.csv')
	partiRead = csv.reader(partiFile, delimiter=',')
	players = []
	for row in partiRead:
		app = []
		app.append(row[0])
		app.append(row[1])
		app.append(row[2])
		app.append(row[3])
		app.append(row[6])
		players.append(app)
	del players[0]
	playersDict = {}
	for app in players:
		playersDict[app[0]] = app
	#print(players)

	#add result to player info
	statsFile = open(currentDirectory + '/statsSample.csv')
	statsRead = csv.reader(statsFile, delimiter=',')
	resultsAndID = []
	for row in statsRead:
		app = []
		app.append(row[0])
		app.append(row[1])
		resultsAndID.append(app)
	del resultsAndID[0]
	for i in resultsAndID:
		try:
			playersDict[i[0]].append(i[1])
		except:
			pass

	#sort players into their team
	result = {}
	#print(playersDict)
	for i in playersDict.items():
		if (i[1][1], i[1][5]) in result.keys():
			result[(i[1][1], i[1][5])].append((i[1][3], str(i[1][4])))
		else:
			result[(i[1][1], i[1][5])] = [(i[1][3], str(i[1][4]))]

	#delete the match result dont have full five players
	delList = []
	for i in result.items():
		if len(i[1]) != 5:
			delList.append(i[0])
	for i in delList:
		del result[i]

	#get chamClasses
	classesFile = open(currentDirectory + '/champclasses.csv')
	classesRead = csv.reader(classesFile, delimiter=',')
	classesAndID = {}
	for row in classesRead:
		classesAndID[row[1]] = (row[0], row[2], row[3])
	for i in result.items():
		for index in range(len(i[1])):
			result[i[0]][index] += classesAndID[result[i[0]][index][0]]
	
	#write result into csv
	writeFile = open(currentDirectory + '/playersResults.csv', 'w')
	fieldnames = ['match ID', 'result', 'player 1', 'player 2', 'player 3', 'player 4', 'player 5']
	writer = csv.DictWriter(writeFile, fieldnames=fieldnames)
	writer.writeheader()
	for i in result.items():
		writer.writerow({'match ID': i[0][0], 'result': i[0][1], 'player 1': i[1][0], 'player 2':i[1][1], 'player 3':i[1][2], 'player 4': i[1][3], 'player 5':i[1][4]})
	

if __name__=="__main__":
		main()
