# -*- coding: utf-8 -*-

class TennisGame1:
    POINTS_TO_TEXT_DICTIONARY = {
        0: "Love",
        1: "Fifteen",
        2: "Thirty",
        3: "Forty",
    }

    EQUALITY_SCORING_TEXT = {
        0: "Love-All",
        1: "Fifteen-All",
        2: "Thirty-All",
        3: "Deuce",
        4: "Deuce",
    }

    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.p1points += 1
        else:
            self.p2points += 1

    def score(self):
        if self.p1points == self.p2points:
            return TennisGame1.EQUALITY_SCORING_TEXT[self.p1points]
        if self.p1points >= 4 or self.p2points >= 4:
            return self.tiebreak_scoring()

        return self.general_case_scoring()

    def general_case_scoring(self):
        player1_text = TennisGame1.POINTS_TO_TEXT_DICTIONARY[self.p1points]
        player2_text = TennisGame1.POINTS_TO_TEXT_DICTIONARY[self.p2points]
        return f"{player1_text}-{player2_text}"

    def tiebreak_scoring(self):
        points_difference = self.p1points - self.p2points
        if points_difference == 1:
            score = "Advantage player1"
        elif points_difference == -1:
            score = "Advantage player2"
        elif points_difference >= 2:
            score = "Win for player1"
        else:
            score = "Win for player2"
        return score
