# Election_Analysis
## Project Overview
The purpose of this project was to retrieve the election data for colorado from a .csv file, analyze the data using Python 3.7.6 code to determine the winner, and produce a summary of the results in a .txt file. To complete this task we we're given an excel.csv file provided by the Colorado Board of Elections which contained Ballot ID, County, and Candidate voted for(name) with nearly 370k rows of data.  Utylizing python we opened this .csv file and totaled number of ballots(votes) cast in the election, determined the candidates, and the number of votes and percentage of the total votes each candidate recieved and ultimately who the winner was. We achieved this by using logical operators, creating lists,dictionarys and variables, and then writing repetition and conditional statements printing/writing those results to an output file(.txt file). This text output file summarized the results for the Board of Elections.

### Election-Audit Results
The analysis of the election data shows that:
- Total Votes: 369,711
- County Results:
  - Jefferson:10.5% (38,855  
  - Denver:82.8% (306,055))  
  - Arapahoe:6.7% (24,801)
- Largest Turnout County: Denver
- Candidate Results:
  - Charles Casper Stockham: 23.0% (85,213)
  - Diana DeGette: 73.8% (272,892)
  - Raymon Anthony Doane: 3.1% (11,606)
 - Election __Winner__:
   - Diana DeGette: 73.8% (272,892)
   
Utilizing Python to perform the analysis and summarize the results we can create an output file autmatically. We can see what that would look like below:

![image](https://user-images.githubusercontent.com/107006216/177647674-21e37e5f-59ce-46e7-b052-663776ec19e3.png)

### Breakdown of Key Compnents of the Code:
### 1. Calculate the total number of votes cast.
For this task we had to initialize a total votes variable and set it equal to 0 as our starting value(intitialzer variable, then create a for loop to iterate over the rows in the election data .csv file. Within the for loop we add the total votes variable but set it equal to itself plus 1(accumulator variable). Everytime the for loop function iterates over each row it adds to the vote count. Once the for loop completes we get a total votes count.

![image](https://user-images.githubusercontent.com/107006216/177879507-bef41c0e-dd83-48a9-a91a-2979bb4e0526.png)
![image](https://user-images.githubusercontent.com/107006216/177879592-151e03cf-a77c-421f-b6d7-595ec1e067ff.png)

### 2. Get a complete list of candidates who recieved the votes.
The first step to complete this task was to initialze a candidate empty list that would eventually house the 3 candidate options. After establishing this empty list we utilized the for loop we previously set up which iterates over the rows in the .csv file. Adding the variable candidate name within the for loop and using the indexing function set it equal to the data in column 3(index 2) gave us a list of every time that canidates name appeared in column 3 on the .csv file. To retrieve just the unique candidates names and not every occurence we needed to add an if statement along with the membership operator *not in*. Using the if statement __If candiate_name *not in* candidate_option:__ we then added the candidates name to the candidates options list using the append function when its not already in the list.  The syntax is as follows:

![image](https://user-images.githubusercontent.com/107006216/177884171-9d01601c-614f-48a5-a994-7f74158cb7e1.png)
![image](https://user-images.githubusercontent.com/107006216/177883476-50a881fa-abc8-43fe-b55a-783f6d2a833d.png)
![image](https://user-images.githubusercontent.com/107006216/177885016-3106157b-5044-40ec-895b-c036aa4ce852.png)

### 3. Calculate the total number of votes each candidate recieved.
Similiar to above where we created an empty list to calculate the total number of votes, here we created an empty candidate votes dictionary to contain the candidates name(key) and the number of votes(value). Within the prior if statement we again useed the index funtion and said that the candidate votes variable for the index candidate name is equal to 0. This initialzed the vote to start at 0, to then increment the votes by 1 everytime the candidates name appeared in the row[2] outside of the if statement but within the for loop we said that canidate votes for the canidate name index is equal to itself plus 1. This counts the votes for each candidate.

![image](https://user-images.githubusercontent.com/107006216/177887099-4a6a8bcd-f042-4c8b-ac6b-faafc83a945a.png)

### 4. Calculate the percentage of votes each candidate won.
We calculated the percentage by creating another for loop to iterate throught the candidate votes dictionary for candidate name. We created a new votes variable within the for loop to retrieve just the votes(value, not the key) for each candidate from the candidates votes dictionary. Since we had already calculated the total votes all we needed to do to determin the percentage of votes for each candidate was to take divided the votes by the total vote and multiple by 100. In order to perform this operation we had to convert those variables into floating values first. SYntax is as follows:

![image](https://user-images.githubusercontent.com/107006216/177889389-2274943d-b6af-4b03-8b76-de93e854b4f0.png)

### 5. Determine the winner of the election based on popular vote.
We had previously calculated votes whcih was just the list of the number of votes each candidate recieved. We had also already calculated  the percentage of the vote so now all we had to do was create an additional if statement within our for candidate name in candidate votes loop. We created 3 additional variables; winning candidate, winner vote count and winning percentage. With our if statement we set up 2 conditions to be true. Votes had to be greater than winning count and percentage of the votes had to be greater than winning  percentage. If true the winning count would be equal to votes, winning percentage would be equal to percentage votes and winning candidate would equal candidate name. When the for loop performs its iterations it replaces the winning variables(count, percentage, candidate) with the highest canidates values and determines the winner.

![image](https://user-images.githubusercontent.com/107006216/177889953-05a86ccd-0053-4319-9b47-36c97df532d0.png)
![image](https://user-images.githubusercontent.com/107006216/177890910-7f6de964-f636-4f46-b0de-0ad06c51fde8.png)
![image](https://user-images.githubusercontent.com/107006216/177890880-af1525ac-74ba-4b06-9ec5-a2c7396eb798.png)

## Resources:
### Data:  
election_results.csv-This was our Data set which we pulled from and performed our analysis on.
### Software: 
Visual Studio Code-Used to edit our Python code, analyze the data, and commit and push updates to Git Hub.
Python 3.7.6
Git Bash

##Election -Audit Summary
The Python code we wrote to retrieve the .csv data, perform the analysis, summarize the findings and write to a text file could be used in future elections assuming we recieved a similiar formatted .csv file.  It would be able to analyze data with additional counties and additional candidates.  Even it we recieved a .csv file with a different layout(columns, rows, additional data)we could even tweak our code fairly easily to perform the same kind of analysis as above. Additionally we could add more funtionality to our code and rank the canidates by the number of votes they recieved or the counties.  There is a lot of functinoality we could add into our code depending on what the board of elections wanted to observe.





