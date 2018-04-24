import csv, re
import numpy as np
from sklearn.naive_bayes import GaussianNB

positions = {'DUO': 0, 'SOLO': 1, 'NONE': 2, 'DUO_SUPPORT': 3, 'DUO_CARRY': 4}

samples = []
labels = []
sample_fields = ["player 1","player 2","player 3","player 4","player 5"]
with open("playersResults.csv", "r") as csvfile:
	fieldnames = ["match ID","result","player 1",
	"player 2","player 3","player 4","player 5"]
	reader = csv.DictReader(csvfile, fieldnames=fieldnames)
	first_line = True
	for row in reader:
		if first_line:
			first_line = False
			continue
		sample = []
		duo_value = False 
		for field in sample_fields:
			player = row[field]
			player = re.sub("[()',]", "", player)
			player = player.split(" ")
			sample.append(int(player[0]))
			sample.append(positions[player[1]])
			if positions[player[1]] == 0:
				duo_value = True
		if duo_value:
			continue
		else:
			labels.append(bool(row["result"]))
			samples.append(sample)
training_samples = samples[:40000]
training_labels  = labels[:40000]
model=GaussianNB()
model.fit(training_samples,training_labels)

test_samples = samples[40000:]
test_labels  = labels[40000:]
print(model.score(test_samples, test_labels))



