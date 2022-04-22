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
            score = self._score_if_player_advantage()

        else:
            score = (_points_to_point_names(self.player1_points)
            + "-"
            + _points_to_point_names(self.player2_points))

        return score

    def _score_if_even(self):
        if self.player1_points < 4:
            return _points_to_point_names(self.player1_points) + "-All"
        elif self.player1_points == 4:
            return "Deuce"
        else:
            return "Invalid"

    def _score_if_player_advantage(self):
        point_difference = self.player1_points - self.player2_points

        if point_difference == 1:
            return "Advantage player1"
        elif point_difference == -1:
            return "Advantage player2"
        elif point_difference >= 2:
            return "Win for player1"
        elif point_difference <= -2:
            return "Win for player2"
        else:
            return "Invalid"


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
