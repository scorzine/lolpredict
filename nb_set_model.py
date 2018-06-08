import csv, re, operator, graphviz
import numpy as np
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
from sklearn.neural_network import MLPClassifier
from sklearn import tree

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
	"BurstMage":   11,			 # *** was not in original dictionary ***
	"Catcher":     12,
	"Diver":       13,
	"Enchanter":   14,
	"Juggernaut":  15,
	"Skirmisher":  16,
	"Vanguard":    17,
	"Warden":      18,
}

# sample_fields = ["ChampionID1","ChampionID2","ChampionID3","ChampionID4","ChampionID5"]
sample_fields = ["Winclass1","Winclass2","Winclass3","Winclass4","Winclass5"]
# sample_fields = ["subclass1", "subclass2", "subclass3", "subclass4", "subclass5"]

with open("allTeamClassSubclass.csv", newline='') as csvfile:
	# fieldnames = ["ChampionID1", "class1", "subclass1", "ChampionID2", "class2", "subclass2", "ChampionID3", "class3", "subclass3", "ChampionID4", "class4", "subclass4", "ChampionID5", "class5", "subclass5"]
	reader = csv.DictReader(csvfile)
	# first_line = True
	for row in reader:
		# if first_line:
		# 	first_line = False
		# 	continue
		sample = []
		duo_value = False 
		for not_include in sample_fields:
			sample = []
			for field in sample_fields:
				if (field != not_include):
					player = row[field]
					# print(player)
					# player = re.sub("[()',]", "", player)
					# player = player.split(" ")
					number = classes_and_subclasses[player]
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

training_samples = samples[:730000]
training_labels = labels[:730000]

test_samples = samples[730000:]
test_labels = labels[730000:]

# ---- Gaussian Naive Bayes ----
model=GaussianNB()
model.fit(training_samples,training_labels)
print("Gaussian Naive Bayes:")
print(model.score(test_samples, test_labels))

# ---- Multinomial Naive Bayes ----
model=MultinomialNB()
model.fit(training_samples,training_labels)
print("Multinomial Naive Bayes:")
print(model.score(test_samples, test_labels))

# ---- Bernoulli Naive Bayes ----
model=BernoulliNB()
model.fit(training_samples,training_labels)
print("Bernoulli Naive Bayes:")
print(model.score(test_samples, test_labels))

# ---- Decision Tree ----
model=tree.DecisionTreeClassifier()
model.fit(training_samples,training_labels)
print("Decision Tree:")
print(model.score(test_samples, test_labels))

# ---- Multi-layer Perceptron ----
clf = MLPClassifier(solver='lbfgs', alpha=1e-3, hidden_layer_sizes=(22, 18), random_state=1)
clf.fit(training_samples, training_labels)
print("Multi-layer Perceptron:")
print(clf.score(test_samples, test_labels))

# ---- Decision Tree Graph export ----
dot_data = tree.export_graphviz(model, out_file=None)
graph = graphviz.Source(dot_data)
graph.gormat = "pdf"
graph.render()