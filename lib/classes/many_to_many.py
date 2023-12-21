class Game:
    def __init__(self, title):
        self.title = title
    @property
    def title(self):
        return self._title 
    @title.getter
    def title(self):
        return self._title
    @title.setter
    def title(self,val):
        if not hasattr(self,'title'):
            self._title = val
    def results(self):
        return list(set(result for result in Result.all if result.game == self))



    def players(self):
        return list(set(result.player for result in self.results() ))

    def average_score(self, player):
        total = self.results()
        total_score = sum(total.score for total in total)
        return total_score / len(total)


class Player:
    def __init__(self, username):
        self.username = username
    @property
    def username(self):
        return self._username 
    @username.getter
    def username(self):
        return self._username
    @username.setter
    def username(self,val):
        if isinstance(val,str) and 2<= len(val)<=16:
            self._username = val

   
    def results(self):
        return list(set(result for result in Result.all if result.player == self))

    def games_played(self):
        return list(set(result.game for result in self.results()))
        #  return list(set(result.game for result in self.results() if result == self))

    def played_game(self, game):
        return any(result.game == game for result in self.results())


    def num_times_played(self, game):
        gamess= 0
        for result in self.results():
            if result.game == game:
                gamess += 1
        return gamess

class Result:
    all = []
    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)
    @property
    def score(self):
        return self._score
    @score.getter
    def score(self):
        return self._score
    @score.setter 
    def score(self,val):
        if not hasattr(self,'score') and isinstance(val,int):
            self._score = val