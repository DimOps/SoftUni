class SteamUser:

    def __init__(self, username: str, games: list, played_hours=0):
        self.played_hours = played_hours
        self.games = games
        self.username = username

    def play(self, game, hours):

        if game in self.games:
            self.played_hours += hours
            return f"{self.username} is playing {game}"
        else:
            return f"{game} is not in library"

    def buy_game(self, game):
	
        if game not in self.games:
            self.games.append(game)
            return f"{self.username} bought {game}"
        else:
            return f"{game} is already in your library"

    def status(self):
        return f"{self.username} has {len(self.games)} games. Total play time: {self.played_hours}"

    def test_add_game_unsuccessful(self):
        user = SteamUser("Me", ["CSGO", "Like A Dragon"])
        res = user.buy_game("CSGO")
        self.assertEqual(res, "CSGO is already in your library")
        self.assertEqual(user.games, ["CSGO", "Like A Dragon"])
