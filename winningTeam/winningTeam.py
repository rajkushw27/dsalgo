def tournamentWinner(competitions, results):

    currentBestTeam = ""
    scores = {currentBestTeam: 0}

    for idx, team in enumerate(competitions):
        result = results[idx]
        homeTeam, awayTeam = team

        winningTeam = homeTeam if result == 1 else awayTeam

        updateScore(winningTeam, 3, scores)

        if scores[winningTeam] > scores[currentBestTeam]:
            currentBestTeam = winningTeam

        return currentBestTeam


def updateScore(winningTeam, point, scores):
    scores[winningTeam] = scores.get(winningTeam, 0) + point
