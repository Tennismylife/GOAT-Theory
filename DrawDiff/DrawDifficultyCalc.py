import pandas as pd
import numpy as np

df = pd.read_csv('1983.csv')

g =  df.groupby('tourney_id')

df2 = pd.read_csv('tournament.csv')

for index, row in df2.iterrows():
    tournament = g.get_group(row['Tournament'])

    winner_ranking = tournament[['winner_age']]
    loser_ranking = tournament[['loser_age']] 

    #collect all rankings
    allranking = np.concatenate((winner_ranking, loser_ranking))
    allranking = np.unique(allranking)

    #sum first 20 ranked players of the draw
    drawdiff = [sum(allranking[0:20])]
    print(drawdiff)