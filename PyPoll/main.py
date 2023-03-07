# import os module
import os
# import csv module
import csv

#read in csv
csvpath = os.path.join('Resources', 'election_data.csv')
print(csvpath)
#create variable for total votes cast in dataset
#create variable for total votes cast for each of the candidates
total_votes =[]
stockham_votes = 0
degette_votes = 0
doane_votes = 0
