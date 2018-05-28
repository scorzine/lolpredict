import csv, re, operator
import numpy as np
from sklearn.naive_bayes import GaussianNB

classes_and_subclasses = {
    "Controller":   1,           # CLASSES (values 1-7)
    "Fighter":      2,
    "Mage":         3,
    "Marksman":     4,
    "Slayer":       5,
    "Specialist":   6,           # Note: "Specialist" is also a subclass
    "Tank":         7,
    "Artillery":    8,           # SUBCLASSES (values 8-18)
    "Assassin":     9,
    "Battlemage":  10,
    "Burst":       11,
	"BurstMage":   11,			# *** was not in original dictionary ***
    "Catcher":     12,
    "Diver":       13,
    "Enchanter":   14,
    "Juggernaut":  15,
    "Skirmisher":  16,
    "Vanguard":    17,
    "Warden":      18,
}

#preprocessing to find best winrate

sample_fields = ["Loseclass1", "Winclass1", "Loseclass2", "Winclass2", "Loseclass3", "Winclass3",
                 "Loseclass4", "Winclass4"]

set_dict = {}

with open("allTeamClassSubclass.csv", newline='') as csvfile:
	reader = csv.DictReader(csvfile)
	first_line = True
	for row in reader:
		if first_line:
			first_line = False
			continue

		win_set = [classes_and_subclasses[row["Winclass1"]], classes_and_subclasses[row["Winclass2"]], classes_and_subclasses[row["Winclass3"]], classes_and_subclasses[row["Winclass4"]]]
		lose_set = [classes_and_subclasses[row["Loseclass1"]], classes_and_subclasses[row["Loseclass2"]], classes_and_subclasses[row["Loseclass3"]], classes_and_subclasses[row["Loseclass4"]]]

		win_set.sort()
		win_string = " ".join(str(x) for x in win_set)
		lose_set.sort()
		lose_string = " ".join(str(x) for x in lose_set)

		if win_string not in set_dict:
			set_dict[win_string] = [[row["Winclass5"], 1, 0]]
		else:
			exists = False
			for label in set_dict[win_string]:
				if label[0] == row["Winclass5"]:
					label[1] += 1
					exists = True
					break
			if not exists:
				set_dict[win_string].append([row["Winclass5"], 1, 0])


		if lose_string not in set_dict:
			set_dict[lose_string] = [[row["Loseclass5"], 0, 1]]
		else:
			exists = False
			for label in set_dict[lose_string]:
				if label[0] == row["Loseclass5"]:
					label[2] += 1
					exists = True
					break
			if not exists:
				set_dict[win_string].append([row["Loseclass5"], 0, 1])

samples = []
labels = []

sample_fields = ["Loseclass1", "Winclass1", "Loseclass2", "Winclass2", "Loseclass3", "Winclass3",
                 "Loseclass4", "Winclass4", "Loseclass5"]

with open("playersResults.csv", "r") as csvfile:
	fieldnames = ["WinChampionID1","Winclass1","Winsubclass1","WinChampionID2","Winclass2","Winsubclass2","WinChampionID3","Winclass3","Winsubclass3","WinChampionID4","Winclass4","Winsubclass4","WinChampionID5","Winclass5","Winsubclass5","LoseChampionID1","Loseclass1","Losesubclass1","LoseChampionID2","Loseclass2","Losesubclass2","LoseChampionID3","Loseclass3","Losesubclass3","LoseChampionID4","Loseclass4","Losesubclass4","LoseChampionID5","Loseclass5","Losesubclass5"]
	reader = csv.DictReader(csvfile, fieldnames=fieldnames)
	first_line = True
	for row in reader:
		if first_line:
			first_line = False
			continue

		sample = [classes_and_subclasses[row["Winclass1"]], classes_and_subclasses[row["Winclass2"]], classes_and_subclasses[row["Winclass3"]], classes_and_subclasses[row["Winclass4"]]]
		samples.append(sample)

		sample.sort()
		sample_string = " ".join(str(x) for x in sample)

		best_label = set_dict[sample_string][0]
		best_wr = 0
		for label in set_dict[sample_string]:
				if label[1]/(label[1]+label[2]) > best_wr:
					best_label = label[0]
					best_wr = label[1]/(label[1]+label[2])
		labels.append(best_label)

# print(len(samples))
# print(len(labels))

training_samples = samples[:136896]
training_labels = labels[:136896]
model=GaussianNB()
model.fit(training_samples,training_labels)

test_samples = samples[136896:]
test_labels = labels[136896:]
print(model.score(test_samples, test_labels))
