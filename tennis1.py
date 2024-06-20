# -*- coding: utf-8 -*-

class TennisGame1:

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
            return self.equality_scoring(self.p1points)
        if self.p1points >= 4 or self.p2points >= 4:
            return self.tiebreak_scoring()

        result = ""
        for i in range(1, 3):
            if i == 1:
                temporary_score = self.p1points
            else:
                result += "-"
                temporary_score = self.p2points
            result += {
                0: "Love",
                1: "Fifteen",
                2: "Thirty",
                3: "Forty",
            }[temporary_score]
        return result

    def tiebreak_scoring(self):
        minus_result = self.p1points - self.p2points
        if minus_result == 1:
            result = "Advantage player1"
        elif minus_result == -1:
            result = "Advantage player2"
        elif minus_result >= 2:
            result = "Win for player1"
        else:
            result = "Win for player2"
        return result

    @staticmethod
    def equality_scoring(points):
        return {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All",
        }.get(points, "Deuce")
