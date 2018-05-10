# -*- coding: utf-8 -*-
import csv, os

def main():

	#get the players info
	currentDirectory = os.path.dirname(os.path.abspath(__file__))
	partiFile = open(currentDirectory + '/participants.csv')
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
	statsFile1 = open(currentDirectory + '/stats1.csv')
	statsRead1 = csv.reader(statsFile1, delimiter=',')
	resultsAndID1 = []
	for row in statsRead1:
		app = []
		app.append(row[0])
		app.append(row[1])
		resultsAndID1.append(app)
	del resultsAndID1[0]
	for i in resultsAndID1:
		try:
			playersDict[i[0]].append(i[1])
		except:
			pass
	#add result to player info
	statsFile2 = open(currentDirectory + '/stats2.csv')
	statsRead2 = csv.reader(statsFile2, delimiter=',')
	resultsAndID2 = []
	for row in statsRead2:
		app = []
		app.append(row[0])
		app.append(row[1])
		resultsAndID2.append(app)
	del resultsAndID2[0]
	for i in resultsAndID2:
		try:
			playersDict[i[0]].append(i[1])
		except:
			pass
	#sort players into their team
	result = {}
	#print(playersDict)
	for i in playersDict.items():
		try:
			if (i[1][1], i[1][5]) in result.keys():
				result[(i[1][1], i[1][5])].append((i[1][3], str(i[1][4])))
			else:
				result[(i[1][1], i[1][5])] = [(i[1][3], str(i[1][4]))]
		except:
			pass

	#delete the match result dont have full five players
	delList = []
	for i in result.items():
		if len(i[1]) != 5:
			delList.append(i[0])
	for i in delList:
		del result[i]

	#delete the losing team
	lostTeam = []
	for i in result.items():
		if i[0][1] == '0':
			lostTeam.append(i[0])
	for i in lostTeam:
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
	fieldnames = ['ChampionID1', 'class1', 'subclass1', 'ChampionID2', 'class2', 'subclass2','ChampionID3', 'class3', 'subclass3','ChampionID4', 'class4', 'subclass4','ChampionID5', 'class5', 'subclass5']
	writer = csv.DictWriter(writeFile, fieldnames=fieldnames)
	writer.writeheader()
	for i in result.items():
		writer.writerow({'ChampionID1': i[1][0][0], 'class1': i[1][0][3], 'subclass1': i[1][0][4], 'ChampionID2': i[1][1][0], 'class2': i[1][1][3], 'subclass2': i[1][1][4],'ChampionID3': i[1][2][0], 'class3': i[1][2][3], 'subclass3': i[1][2][4],'ChampionID4': i[1][3][0], 'class4': i[1][3][3], 'subclass4': i[1][3][4],'ChampionID5': i[1][4][0], 'class5': i[1][4][3], 'subclass5': i[1][4][4]})
	

if __name__=="__main__":
		main()
