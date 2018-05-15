import csv, re
import numpy as np
from sklearn.naive_bayes import GaussianNB

samples = []
labels = []
# sample_fields = ["ChampionID1","ChampionID2","ChampionID3","ChampionID4","ChampionID5"]
sample_fields = ["class1","class2","class3","class4","class5"]
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
					sample.append(player[0])
			labels.append(row[not_include])
			samples.append(sample)

print(len(samples))
print(len(labels))

i = 0
while (i < 10):
	print(samples[i])
	print(labels[i])
	i += 1

# training_samples = samples[:40000]
# training_labels  = labels[:40000]
# model=GaussianNB()
# model.fit(training_samples,training_labels)

# test_samples = samples[40000:]
# test_labels  = labels[40000:]
# print(model.score(test_samples, test_labels))
