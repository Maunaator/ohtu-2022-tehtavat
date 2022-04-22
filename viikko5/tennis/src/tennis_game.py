class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_points += 1
        elif player_name == self.player2_name:
            self.player2_points += 1

    def get_score(self):
        score = ""

        if self.player1_points == self.player2_points:
            score = self._score_if_even()
            
        elif self.player1_points >= 4 or self.player2_points >= 4:
            minus_result = self.player1_points - self.player2_points

            if minus_result == 1:
                score = "Advantage player1"
            elif minus_result == -1:
                score = "Advantage player2"
            elif minus_result >= 2:
                score = "Win for player1"
            else:
                score = "Win for player2"

        else:
            score = (_points_to_point_names(self.player1_points)
            + "-"
            + _points_to_point_names(self.player2_points))

        return score

    def _score_if_even(self):
        if self.player1_points == 4:
            return "Deuce"
        else:
            return _points_to_point_names(self.player1_points) + "-All"


def _points_to_point_names(points):
        if points == 0:
            return "Love"
        elif points == 1:
            return "Fifteen"
        elif points == 2:
            return "Thirty"
        elif points == 3:
            return "Forty"
        else:
            return "Invalid"
