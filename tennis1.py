# -*- coding: utf-8 -*-

class TennisGame1:
    """
    A class used to represent a Tennis Game.

    Attributes
    ----------
    POINTS_TO_TEXT_DICTIONARY : dict
        A dictionary to map points to their textual representation.
    EQUALITY_SCORING_TEXT : dict
        A dictionary to map points to their textual representation when scores are equal.
    player1Name : str
        The name of the first player.
    player2Name : str
        The name of the second player.
    p1points : int
        The points of the first player.
    p2points : int
        The points of the second player.

    Methods
    -------
    won_point(playerName)
        Increases the points of the specified player.
    score()
        Returns the current score as a string.
    general_case_scoring()
        Returns the score for the general case (when no player has reached 4 points and scores are not equal).
    tiebreak_scoring()
        Returns the score for the tiebreak case (when at least one player has reached 4 points).
    """
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
        """
        Increases the points of the specified player.

        Parameters
        ----------
        playerName : str
            The name of the player who won the point.
        """
        if playerName == self.player1Name:
            self.p1points += 1
        else:
            self.p2points += 1

    def score(self):
        """
        Returns the current score as a string.

        Returns
        -------
        str
            The current score.
        """
        if self.p1points == self.p2points:
            return TennisGame1.EQUALITY_SCORING_TEXT[self.p1points]
        if self.p1points >= 4 or self.p2points >= 4:
            return self.tiebreak_scoring()

        return self.general_case_scoring()

    def general_case_scoring(self):
        """
        Returns the score for the general case (when no player has reached 4 points and scores are not equal).

        Returns
        -------
        str
            The score for the general case.
        """
        player1_text = TennisGame1.POINTS_TO_TEXT_DICTIONARY[self.p1points]
        player2_text = TennisGame1.POINTS_TO_TEXT_DICTIONARY[self.p2points]
        return f"{player1_text}-{player2_text}"

    def tiebreak_scoring(self):
        """
        Returns the score for the tiebreak case (when at least one player has reached 4 points).

        Returns
        -------
        str
            The score for the tiebreak case.
        """
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
