class Player:
    def __init__(self, name, team, nationality, goals, assists):
        self.name = name
        self.team = team
        self.nationality = nationality
        self.goals = goals
        self.assists = assists

    def __str__(self):
        return (self.name + " " + 
        self.team + " " + 
        str(self.goals) + " + " + 
        str(self.assists) + " = " + 
        str(self.goals + self.assists)
        )
