    
 # Add our dependencies.
import csv

import os

# Retrieve Data from CSV
# Assign a variable to load a file from a path.
file_to_load=os.path.join("Resources","election_results.csv")
   
 # Write data to the file(file to save)
 # Assign a variable to save the file to a path.
file_to_save=os.path.join("analysis","election_analysis.txt")

# Initialize variable total votes start at 0(ACCUMULATOR initializer)
total_votes=0

# Declare an empty canidate list, add canidate_name to the list in for loop using append() method.
 # Declare an empty canidate votes dictionary(keys are canidates, values are votes)
candidate_options=[] 
candidate_votes={}

# CHALLENGE: DELCARE AN EMPTY COUNTY LIST, ADD county_name TO THE LIST IN FOR LOOP USING APPEND() METHOD.
     # CREATE AN EMPTY COUNTY VOTES DICTIONARY(KEYS ARE COUNTIES, VALUES ARE VOTES
county_options=[]
county_votes={}

# CHALLENGE: INITIALIZE TOTAL COUNTY VOTES START AT 0
total_county_votes=0

# Winning Candidate and Winning Count Tracker
winning_candidate=""
winning_count= 0
winning_percentage= 0

# CHALLENGE: HIGHEST COUNTY BY VOTES AND PERCENTAGE TRACKER
highest_county=""
highest_county_count=0
highest_percentage=0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: Read and analyze the data here. 
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row.EXCLUDE HEADER ROW IN ANALYSIS.
    headers=next(file_reader)

#CHALLENGE ADD
#1 VOTER TURNOUT FOR EACH COUNTY
#2 PERCENTAGE OF VOTES FROM EACH COUNTY OUT OF THE TOTAL COUNTY OUT OF THE TOTAL COUNT
#3 THE COUNTY WITH THE HIGHEST RESULTS

    for row in file_reader:
    ##1 VOTER TURNOUT FOR EACH COUNTY
        # 1.A) ADD TO THE TOTAL COUNTY VOTE COUNT(REMEMBER SET INITIALLY TO 0 ABOVE)
        total_county_votes+=1

        # Add to the total vote count
        total_votes+=1

        # Print the canidate name from each row
        candidate_name=row[2]

        #1.B) ADD A COUNTY NAME VARIABLE
        county_name=row[1]

        # 1.C) ADD IF STATEMENT TO FIND COUNTY NAMES
        if county_name not in county_options:
            county_options.append(county_name)

            # 1.D) BEGIN TRACKING COUNTY VOTES START SETTING TO 0
            county_votes[county_name]=0

        # 1.E) INCREMENT THE VOTES BY 1 EVERY TIME A COUNTYS NAME APPEARS IN A ROW. 
        county_votes[county_name]+=1

        # If the candidate does not match any existing candidate...
              #add the canidate name to the canidate list.
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            #begin tracking the canidates vote count always start at zero. Add second statment to begin incrementing the votes for each canidate.
            candidate_votes[candidate_name]=0

        #increment the votes by 1 evey time a canidats name appears in a row. Note::same as =canidate_vote[canidate_name] + 1
        candidate_votes[candidate_name]+=1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results)

    # Save the final vote count to the text file.
    txt_file.write(election_results)

    ## 2) PERCENTAGE OF VOTES FROM EACH COUNTY OUT OF THE TOTAL COUNT
    for county_name in county_votes:
        c_votes=county_votes[county_name]
        county_percentage=float(c_votes)/float(total_county_votes)*100
        county_results=(f'\n{county_name}:{county_percentage:.1f}% ({c_votes:,})')
        # 2.A) PRINT RESULTS
        print(county_results)
        # 2.B) WRITE  RESULTS TO TEXT FILE
        txt_file.write(county_results)
        ## 3) THE COUNTY WITH THE HIGHEST RESULTS
        if (c_votes > highest_county_count) and (county_percentage > highest_percentage):
            highest_county_count=c_votes
            highest_percentage=county_percentage
            highest_county=county_name
    highest_county_summary=(
        f'\n-------------------------\n'
        f'Highest County Turnout: {highest_county}\n'
        f'-------------------------\n'
        f'Candidate Results:\n\n')
    ## 3.A) PRINT THE COUNTY WITH THE HIGHEST RESULTS
    print(highest_county_summary)
    ## 3.B) WRITE RESULTS TO TEXT FILE
    txt_file.write(highest_county_summary)

    # For loop with Membership operator to iterate over candidates name in the candidate votes  dictionary
    for candidate_name in candidate_votes:

        # Retrieve vote count of a candidate.
        votes=candidate_votes[candidate_name]

        # Calculate the percentage of votes
        percentage_votes=float(votes)/float(total_votes)*100

        # Create candidate results( names, % of votes, votes per candidate),Print the candidate name and percentage of votes, then write to text file
        candidate_results=(
            f'{candidate_name}: {percentage_votes:.1f}% ({votes:,})\n\n')
        print(candidate_results)
        txt_file.write(candidate_results)

        # Determine the winning vote count and the canidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (percentage_votes > winning_percentage):

            # If TRUE then set the winning count = vote and winning % = percenatage of voters
            winning_count=votes
            winning_percentage=percentage_votes

            # Set the winning canidate= canidates name
            winning_candidate=candidate_name
    # Create winning cadidate summary, print, then write to text. **Keep out of if but within for.**
    winning_candidate_summary=(
                f"--------------------------\n"
                f'WINNER: {winning_candidate}\n'
                f'Winner Vote Count: {winning_count:,}\n'
                f'Winning Percentage: {winning_percentage:1f}%\n'
                f'---------------------------\n')
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
           

       
  


    

        

    
    #Determine the canidates(complete list of canidates who recieved votes)
    #the total number of votes cast
    #the total number of votes cast per canidate
    #the % of votes each canidate recieved
    #the winner of the election based on popular vote