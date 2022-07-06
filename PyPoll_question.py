
import csv
import os
  
file_to_load=os.path.join("Resources","election_results.csv")

file_to_save=os.path.join("analysis","election_analysis.txt")

total_votes=0 
canidate_options=[]  
canidate_votes={}

winning_canidate=""
winning_count= 0
winning_percentage= 0
  
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers=next(file_reader)

    for row in file_reader:
        total_votes+=1
        canidate_name=row[2]
        if canidate_name not in canidate_options:
            canidate_options.append(canidate_name)
            canidate_votes[canidate_name]=0
        canidate_votes[canidate_name]+=1

    for canidate_name in canidate_votes:
        votes=canidate_votes[canidate_name]
        percentage_votes=float(votes)/float(total_votes)*100
        canidate_results=(f'{canidate_name}:{percentage_votes:.1f}% ({votes:,})\n')
        print(canidate_results)
    #Dont understand how this code is determining the winner
        if (votes > winning_count) and (percentage_votes > winning_percentage):
            winning_count=votes
            winning_percentage=percentage_votes
            winning_canidate=canidate_name
    winning_canidate_summary=(
                f"--------------------------\n"
                f'Winner:{winning_canidate}\n'
                f'Winner Vote Count:{winning_count:,}\n'
                f'Winning Percentage:{winning_percentage:1f}%\n'
                f'---------------------------')
    print(winning_canidate_summary)

    


            

       
  


    

        

    
    #Determine the canidates(complete list of canidates who recieved votes)
    #the total number of votes cast
    #the total number of votes cast per canidate
    #the % of votes each canidate recieved
    #the winner of the election based on popular vote