# File: Pypoll_Challenge.py
# Author: Priyanka Senapati
# Description: Module 3 Challenge
#

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# County options and county votes
county_options = []
# Declare an empty dict
county_votes = {}
# Largest county turnover and largest Count Tracker
largest_county_turnover = ""
largest_county_turnover_count = 0
# Winning County and Winning Count Tracker
winning_county = ""
c_winning_count = 0
c_winning_percentage = 0


# Candidate options and candidate votes
candidate_options = []
# Declare an empty dict
candidates_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row. 
    headers = next(file_reader)
    # 2. Begin tracking that candidate's vote count. 
    #candidates_votes[candidate_name] = 0
   
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1 

        #Print the county name for each row
        county_name = row[1]
        if county_name not in county_options:
             # Add the county name to the county list.
            county_options.append(county_name)
            # 2. Begin tracking that county's vote count. 
            county_votes[county_name] = 0
        # Add a vote to that county's count.
        county_votes[county_name] += 1

        # Print the candidate name from each row.
        candidate_name = row[2]
        if candidate_name not in candidate_options:
             # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # 2. Begin tracking that candidate's vote count. 
            candidates_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidates_votes[candidate_name] += 1
        # Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Determine the percentage of votes for each county by looping through the counts.
    # 1. Iterate through the county list.
    print(county_votes)
    county_results = (f"County Votes:\n")
    txt_file.write(county_results)
    for county in county_votes:
        # 2. Retrieve vote count of a county.
        c_votes = county_votes[county]
        # 3. Calculate the percentage of votes.
        c_vote_percentage = int(c_votes) / int(total_votes) * 100
        # 4. Print the county name and percentage of votes.
        county_results = (f"{county}: {c_vote_percentage:.1f}% ({c_votes})\n")
        # Print each county's voter count and percentage to the terminal.
        print(county_results)
        #  Save the county results to our text file.
        txt_file.write(county_results)
        # Determine winning vote count and county
        # Determine if the votes is greater than the winning count.
        if (c_votes > c_winning_count) and (c_vote_percentage > c_winning_percentage):  
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            c_winning_count = c_votes
            c_winning_percentage = c_vote_percentage
            # And, set the largest county turnover equal to the county's name.
            winning_county = county
        winning_county_summary = (
        f"\n-------------------------\n"
        f"Largest County Turnover: {winning_county}\n"
        f"-------------------------\n")
    print(winning_county_summary)
    # Save the winning county's results to the text file.
    txt_file.write(winning_county_summary)

    print(county_votes)

    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    print(candidates_votes)
    for candidate in candidates_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidates_votes[candidate]
        # 3. Calculate the percentage of votes.
        vote_percentage = int(votes) / int(total_votes) * 100
        # 4. Print the candidate name and percentage of votes.
        candidate_results = ( f"{candidate}: {vote_percentage:.1f}% ({votes})\n")
        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):  
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate
        winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)


