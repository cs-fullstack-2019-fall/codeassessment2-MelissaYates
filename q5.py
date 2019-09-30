# ### Problem 5
# Create a SportsTeam Class for tracking sports teams. The class should have the properties team_name_p, team_city, and team_ranking_p.
# The class should have a method to change a Team’s ranking. 
# The class should implement the ```__str__``` method so that when an instance of the SportsTeam is printed it will output a string
# containing the team name, team city, and team rank (use f strings to format the output).
# Your program should create a SportsTeam instance with an initial ranking of 2.
# Print out the class.
# Your program should change the ranking of the team to 8 using only the class method.
# Print out the class (should use your ```__str__``` method).


# Example Output:
# ```
# The Grizzlies are from Memphis and are 2 in the standings.
# # Update the rating from 2 to 8 from your code
# The Grizzlies are from Memphis and are 8 in the standings.
# ```
class SportsTeam:
    def __init__(self, team_name, team_city, team_ranking):
        self.team_name = team_name
        self.team_city = team_city
        self.team_ranking = team_ranking

    def changeRanking(self, sports_team):
        self.team_ranking = new_ranking
        return new_ranking

    def __str__(self):
        print(f"Team Name: {self.team_name}, City: {self.team_city}, and Rank: {self.team_rank}")

sportsTeam1 = SportsTeam("Chicago Bulls", "Chicago", 2)

changeRanking(8)