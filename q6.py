# ### Problem 6
# Create a class called ClubMember 
# Each club member has a name and a role  
# Create ClubMember instances for the following people:
# ```
# Alfred - Club President
# Troy - Club Vice President
# Albert - Club Secretary
# Bob - Club Treasurer
# ```
# Add each member instance to a new club_members list that you create.
# Write the code needed to loop through the club member list and print the
# current number of members in the list, then the member’s name and club role, one per line using f strings.

# Example Output:
# ```
# There are currently 4 club members in the list!

# Club President: Alfred
# Club Vice President: Troy
# Club Secretary: Albert
# Club Treasurer: Bob
# ```

class ClubMember:
    #initialization of properties in class
    def __init__(self, name, role):
        self.name = name
        self.role = role


club_member1 = ClubMember("Alfred","Club President")#instance of club member created
club_member2 = ClubMember("Troy","Club Vice President")#instance of club member created
club_member3 = ClubMember("Albert","Club Secretary")#instance of club member created
club_member4 = ClubMember("Bob","Club Treasurer")#instance of club member created

club_members =[club_member1,club_member2,club_member3,club_member4] #each member instance added to a new club_members
count = 0 #initialization of count
for eachMember in club_members:
    #print the current number of members in the list, then the member’s name and club role, one per line using f strings.
    count = count+1
    print(f"{str(count)} {eachMember.name} {eachMember.role}\n")#current number of members in the list, the member’s name and club role, one per line using f strings.