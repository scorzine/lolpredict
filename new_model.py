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

# sample_fields = ["Losesubclass1", "Winsubclass1", "Losesubclass2", "Winsubclass2", "Losesubclass3", "Winsubclass3",
#                  "Losesubclass4", "Winsubclass4", "Losesubclass5"]
# label_field   = "Winsubclass5"
sample_fields = ["LoseChampionID1", "WinChampionID1", "LoseChampionID2", "WinChampionID2", "LoseChampionID3", "WinChampionID3",
                 "LoseChampionID4", "WinChampionID4", "LoseChampionID5"]
label_field   = "WinChampionID5"

with open("allTeamClassSubclass.csv", newline='') as csvfile:
	reader = csv.DictReader(csvfile)
	print(reader.fieldnames)
	samples = []
	labels  = []
	for row in reader:
		sample = []
		for name in sample_fields:
			if name[0] == "L":
				# number = 0 - classes_and_subclasses[row[name]]
				number = 0 - int(row[name])
			else:
				# number = classes_and_subclasses[row[name]]
				number = int(row[name])
			sample.append(number)
		samples.append(sample)
		# labels.append(classes_and_subclasses[row[label_field]])
		labels.append(int(row[label_field]))

print(len(samples))
print(len(labels))

# i = 0
# while (i < 10):
# 	print(samples[i])
# 	print(labels[i])
# 	i += 1

training_samples = samples[:120000]
training_labels = labels[:120000]
model=GaussianNB()
model.fit(training_samples,training_labels)

test_samples = samples[120000:]
test_labels = labels[120000:]
print(model.score(test_samples, test_labels))
