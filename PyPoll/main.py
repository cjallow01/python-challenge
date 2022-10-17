# The goal for is to create a Python script that analyzes the votes and calculates each of the following values:
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote
# 6. The final script should both print the analysis to the terminal and export a text file with the results.

# Import dependencies
import os
import csv
import collections
from collections import Counter

# Define PyPoll's variables
voters_candidates = []
votes_per_candidate = []