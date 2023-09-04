# Simulate a sports tournament

import csv
import sys
import random

# Number of simulations to run
N = 1000000


def main():

    # Ensure correct usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")

    teams = []
    filename = sys.argv[1]
    # Read teams into memory from file
    # (https://courses.cs.washington.edu/courses/cse140/13wi/csv-parsing.html)
    with open(filename, 'r') as file:
        csvreader = csv.DictReader(file)
        # note: DictReader uses header info to assign keys
        for team in csvreader:
            team['rating'] = int(team['rating'])
            teams.append(team)
    # print(f"{teams}") ## print for debugging

    counts = {}
    # Simulate N tournaments and keep track of tournament win counts
    simulations = N
    while simulations > 0:
        # run tournament
        winner = simulate_tournament(teams)
        # add winning team name if not already present
        if not winner in counts:
            counts[winner] = 0
        # Increment wins for winner
        counts[winner] += 1
        simulations -= 1
    

    # Print each team's chances of winning, according to simulation
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")


def simulate_game(team1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    return random.random() < probability


def simulate_round(teams):
    """Simulate a round. Return a list of winning teams."""
    winners = []

    # Simulate games for all pairs of teams
    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]):
            winners.append(teams[i])
            # print(f"{teams[i]}")
        else:
            winners.append(teams[i + 1])
            # print(f"{teams[i + 1]}")
    return winners


def simulate_tournament(teams):
    """Simulate a tournament. Return name of winning team."""
    # Note: simulate_rounds returns a list of winners, needs to run until len = 1
    # teams is a list of dictionaries. dicts are keyed with 'team' and 'rating'
    while len(teams) > 1:
        teams = simulate_round(teams)
    winner = teams[0]['team']
    # print(f"winner = {winner}")
    return winner

     
if __name__ == "__main__":
    main()
