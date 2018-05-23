import csv, re, operator
import numpy as np
from sklearn.naive_bayes import GaussianNB

samples = []
labels = []

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

# sample_fields = ["ChampionID1","ChampionID2","ChampionID3","ChampionID4","ChampionID5"]
# sample_fields = ["class1","class2","class3","class4","class5"]
sample_fields = ["subclass1", "subclass2", "subclass3", "subclass4", "subclass5"]

with open("playersResults.csv", "r") as csvfile:
	fieldnames = ["ChampionID1", "class1", "subclass1", "ChampionID2", "class2", "subclass2", "ChampionID3", "class3", "subclass3", "ChampionID4", "class4", "subclass4", "ChampionID5", "class5", "subclass5"]
	reader = csv.DictReader(csvfile, fieldnames=fieldnames)
	first_line = True
	for row in reader:
		if first_line:
			first_line = False
			continue
		sample = []
		duo_value = False 
		for not_include in sample_fields:
			sample = []
			for field in sample_fields:
				if (field != not_include):
					player = row[field]
					player = re.sub("[()',]", "", player)
					player = player.split(" ")
					number = classes_and_subclasses.get(player[0])
					# sample.append(int(player[0]))		# for champions
					sample.append(number)				# for classes and subclasses
			labels.append(row[not_include])
			samples.append(sample)

# print(len(samples))
# print(len(labels))

# i = 0
# while (i < 10):
# 	print(samples[i])
# 	print(labels[i])
# 	i += 1

training_samples = samples[:730112]
training_labels = labels[:730112]
model=GaussianNB()
model.fit(training_samples,training_labels)

test_samples = samples[182528:]
test_labels = labels[182528:]
print(model.score(test_samples, test_labels))
