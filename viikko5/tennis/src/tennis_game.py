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
            score = _score_if_even_in_earlygame(self.player1_points)

        elif self.player1_points >= 4 or self.player2_points >= 4:
            score = _score_if_endgame(self.player1_points - self.player2_points)

        else:
            score = _score_if_earlygame(self.player1_points, self.player2_points)

        return score

def _score_if_earlygame(player1_points, player2_points):
    return (_points_to_point_names(player1_points)
            + "-"
            + _points_to_point_names(player2_points))

def _score_if_even_in_earlygame(points):
    if points < 4:
        return _points_to_point_names(points) + "-All"
    elif points == 4:
        return "Deuce"
    else:
        return "Invalid"

def _score_if_endgame(player_point_difference):
    if player_point_difference == 1:
        return "Advantage player1"
    elif player_point_difference == -1:
        return "Advantage player2"
    elif player_point_difference >= 2:
        return "Win for player1"
    elif player_point_difference <= -2:
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
