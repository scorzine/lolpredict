Run the wonTeamClassSubclass.py script in the same folder as the Kaggle 
data set to produce the necessary csv file, allTeamClassSubclass.csv.
The data set can be found at:
https://www.kaggle.com/paololol/league-of-legends-ranked-matches

To test the accuracy of the basic input models, run nb_set_model.py 
in the same folder as the csv file.

Alternately, to test the accuracy of the winrate implementations of 
the models, run nb_winrate_model.py.

It is recommended that you comment out the last four lines of both the
set and winrate files if you do not have graphviz set up and added to your
path. The only reliable way I found to use graphviz is to first use
"pip install graphviz" then "sudo apt-get install graphviz". The first 
installs the actual python package, while the second adds the necessary
command lines access (needed even if rendering through python).
