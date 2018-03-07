import csv
#from collections import OrderedDict
import operator 
#file_numbers=['1','2']
#for filenum in file_numbers:
#    pybankcsv=os.path.join( 'budget_data_' + filenum + '.csv')
file_to_load = "raw_data/election_data_2.csv"

votes = 0
winner_votes = 0
total_candidates = 0
greatest_votes = ["", 0]
candidate_options = []
candidate_votes = {}


with open(file_to_load) as election_data:
    reader = csv.DictReader(election_data)

    for row in reader:
        votes = votes + 1
        total_candidates = row["Candidate"]        

        if row["Candidate"] not in candidate_options:
            
            candidate_options.append(row["Candidate"])

            candidate_votes[row["Candidate"]] = 1
            
        else:
#            candidate_votes[row["Candidate"]] = candidate_votes[row["Candidate"]] + 1
            candidate_votes[row["Candidate"]] += 1            
#----------------------------------------------------------------------------------------
    # Determine the Winner:
    #if (votes > winner_votes[2]):
     #   greatest_increase[1] = revenue_change
      #  greatest_increase[0] = row["Candidate"]
#----------------------------------------------------------------------------------------
    
    print()
    print()
    print()
    print("Election Results")
    print("-------------------------")
    print("Total Votes " + str(votes))
    print("-------------------------")
#results
    for candidate in candidate_votes:
        print(candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 
        candidate_results = (candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 
    
candidate_votes

winner = sorted(candidate_votes.items(), key=itemgetter(1), reverse=True)

#print("WINNERTEST: " + str(winner_name[0]))


#print ("WINNER: " + str(winner_name.split(","))


#results
print("-------------------------")
print("Winner: " + str(winner[0][0]))
print("-------------------------")

