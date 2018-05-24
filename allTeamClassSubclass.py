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


	#get chamClasses
	classesFile = open(currentDirectory + '/champclasses.csv')
	classesRead = csv.reader(classesFile, delimiter=',')
	classesAndID = {}
	for row in classesRead:
		classesAndID[row[1]] = (row[0], row[2], row[3])
	for i in result.items():
		for index in range(len(i[1])):
			result[i[0]][index] += classesAndID[result[i[0]][index][0]]

	#delete the losing team
	lostTeam = []
	for i in result.items():
		if i[0][1] == '0':
			lostTeam.append(i[0])
	for i in result.keys():
		if i[1] == '1':
			try:
				result[i]+= result[(i[0], '0')]
			except: 
				pass
	for i in lostTeam:
		del result[i]
	delList2 = []
	for i in result.items():
		if len(i[1]) != 10:
			delList2.append(i[0])
	for i in delList2:
		del result[i]
	print(result)
	
	#write result into csv
	writeFile = open(currentDirectory + '/allTeamClassSubclass.csv', 'w')
	fieldnames = ['gameID','WinChampionID1', 'Winclass1', 'Winsubclass1', 'WinChampionID2', 'Winclass2', 'Winsubclass2','WinChampionID3', 'Winclass3', 'Winsubclass3','WinChampionID4', 'Winclass4', 'Winsubclass4','WinChampionID5', 'Winclass5', 'Winsubclass5','LoseChampionID1', 'Loseclass1', 'Losesubclass1', 'LoseChampionID2', 'Loseclass2', 'Losesubclass2','LoseChampionID3', 'Loseclass3', 'Losesubclass3','LoseChampionID4', 'Loseclass4', 'Losesubclass4','LoseChampionID5', 'Loseclass5', 'Losesubclass5']
	writer = csv.DictWriter(writeFile, fieldnames=fieldnames)
	writer.writeheader()
	for i in result.items():

		writer.writerow({'gameID': i[0][0], 'WinChampionID1': i[1][0][0], 'Winclass1': i[1][0][3], 'Winsubclass1': i[1][0][4], 'WinChampionID2': i[1][1][0], 'Winclass2': i[1][1][3], 'Winsubclass2': i[1][1][4],'WinChampionID3': i[1][2][0], 'Winclass3': i[1][2][3], 'Winsubclass3': i[1][2][4],'WinChampionID4': i[1][3][0], 'Winclass4': i[1][3][3], 'Winsubclass4': i[1][3][4],'WinChampionID5': i[1][4][0], 'Winclass5': i[1][4][3], 'Winsubclass5': i[1][4][4] , 'LoseChampionID1': i[1][5][0], 'Loseclass1': i[1][5][3], 'Losesubclass1': i[1][5][4], 'LoseChampionID2': i[1][6][0], 'Loseclass2': i[1][6][3], 'Losesubclass2': i[1][6][4],'LoseChampionID3': i[1][7][0], 'Loseclass3': i[1][7][3], 'Losesubclass3': i[1][7][4],'LoseChampionID4': i[1][8][0], 'Loseclass4': i[1][8][3], 'Losesubclass4': i[1][8][4],'LoseChampionID5': i[1][9][0], 'Loseclass5': i[1][9][3], 'Losesubclass5': i[1][9][4]})
	

if __name__=="__main__":
		main()
