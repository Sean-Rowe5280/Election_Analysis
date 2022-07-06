#Retrieve Data from CSV
    # Add our dependencies.
import csv
import os
    # Assign a variable to load a file from a path.
file_to_load=os.path.join("Resources","election_results.csv")
    #write data to the file(file to save)
        # Assign a variable to save the file to a path.
file_to_save=os.path.join("analysis","election_analysis.txt")
    #initialize variable total votes start at 0(ACCUMULATOR initializer)
total_votes=0
    #declare an empty canidate list, add canidate_name to the list in for loop using append() method.
candidate_options=[]
    #Create an empty canidate votes dictionary(keys are canidates, values are votes)
candidate_votes={}
 #Winning Candidate and Winning Count Tracker
winning_candidate=""
winning_count= 0
winning_percentage= 0

      # Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do: read and analyze the data here. 
           # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
     # Read the header row
    headers=next(file_reader)
     # Print each row in the file_reader
    for row in file_reader:
        #Add to the total vote count
        total_votes+=1
        #print the canidate name from each row
        candidate_name=row[2]
        # If the candidate does not match any existing candidate...
              #add the canidate name to the canidate list.
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            #begin tracking the canidates vote count always start at zero. Add second statment to begin incrementing the votes for each canidate.
            candidate_votes[candidate_name]=0
            #increment the votes by 1 evey time a canidats name appears in a row.
        candidate_votes[candidate_name]+=1    #same as =canidate_vote[canidate_name] + 1
# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    for candidate_name in candidate_votes:
            #Retrieve vote count of a candidate.
        votes=candidate_votes[candidate_name]
            #Calculate the percentage of votes
        percentage_votes=float(votes)/float(total_votes)*100
            # Print the candidate name and percentage of votes.
        #print(f"{canidate_name}: Recieved {total_votes} Total Votes;{percentage_votes:.2f}%")
        candidate_results=(f'{candidate_name}:{percentage_votes:.1f}% ({votes:,})\n')
        print(candidate_results)        #(commented out print function per module instruction)
        txt_file.write(candidate_results)
    #Determine the winning vote count and the canidate
        #determine if the votes is greater than the winning count.
        if (votes > winning_count) and (percentage_votes > winning_percentage):
            #if TRUE then set the winning count = vote and winning % = percenatage of voters
            winning_count=votes
            winning_percentage=percentage_votes
            #set the winning canidate= canidates name
            winning_candidate=candidate_name
    winning_candidate_summary=(
                f"--------------------------\n"
                f'Winner:{winning_candidate}\n'
                f'Winner Vote Count:{winning_count:,}\n'
                f'Winning Percentage:{winning_percentage:1f}%\n'
                f'---------------------------')
    print(winning_candidate_summary)        #(commented out print function per module instruction)
    txt_file.write(winning_candidate_summary)
    


            

       
  


    

        

    
    #Determine the canidates(complete list of canidates who recieved votes)
    #the total number of votes cast
    #the total number of votes cast per canidate
    #the % of votes each canidate recieved
    #the winner of the election based on popular vote