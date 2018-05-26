import csv, re, operator
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier

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
#                  "Losesubclass4", "Winsubclass4", "Losesubclass5", "Winsubclass5"]
sample_fields = ["LoseChampionID1", "WinChampionID1", "LoseChampionID2", "WinChampionID2", "LoseChampionID3", "WinChampionID3",
                 "LoseChampionID4", "WinChampionID4", "LoseChampionID5", "WinChampionID5"]

with open("allTeamClassSubclass.csv", newline='') as csvfile:
	reader = csv.DictReader(csvfile)
	print(reader.fieldnames)
	samples = []
	labels  = []
	for row in reader:
		pos_sample = []
		neg_sample = []
		for name in sample_fields:
			if name[0] == "L":
				# neg_sample.append(int(classes_and_subclasses[row[name]]))
				neg_sample.append(int(row[name]))
			else:
				# pos_sample.append(int(classes_and_subclasses[row[name]]))
				pos_sample.append(int(row[name]))
		samples.append(pos_sample)
		samples.append(neg_sample)
		labels.append(int(1))
		labels.append(int(0))

print(len(samples))
print(len(labels))

# i = 0
# while (i < 10):
# 	print(samples[i])
# 	print(labels[i])
# 	i += 1

training_samples = samples[:330000]
training_labels = labels[:330000]
# model=GaussianNB()
model = MLPClassifier(solver='lbfgs', alpha=1e-5,
	                  hidden_layer_sizes=(5, 2), random_state=1)
model.fit(training_samples,training_labels)

test_samples = samples[330000:]
test_labels = labels[330000:]
print(model.score(test_samples, test_labels))