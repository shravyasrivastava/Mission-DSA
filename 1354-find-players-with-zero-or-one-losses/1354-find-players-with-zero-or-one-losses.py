from collections import defaultdict
class Solution:
    def findWinners(self,matches):
        losses=defaultdict(int)
        players=set()
        for winner,loser in matches:
            players.add(winner)
            players.add(loser)
            losses[loser]+=1
        zero_loss=[]
        one_loss=[]
        for player in players:
            if losses[player]==0:
                zero_loss.append(player)
            elif losses[player]==1:
                one_loss.append(player)
        return [sorted(zero_loss),sorted(one_loss)]
        