import pandas as pd
data_xls = pd.read_excel('1988.xlsx', 'View', index_col=None)
data_xls.to_csv('csvfile.csv', encoding='utf-8')


df = pd.read_csv('csvfile.csv')

df.columns=['','Tournament','Draw' ,'Prize money','W Real Points','F','SF','QF','R16','R32','R64','R128','Rankings Opponents','W ATP Calc Points']

tournaments = df['Tournament']
atppoints = df['W ATP Calc Points']
rankingopponents = df['Rankings Opponents']
rankingarray = df['Rankings Opponents'].str.rsplit(',')


for i in range(len(rankingarray)):
    totalpointstograb = 0
    for val in rankingarray[i]:
     #print(val)
     val = int(val)
     if val >= 1 and val <= 5:
       bonuspoints = 30
     if val >= 6 and val <= 10:
       bonuspoints = 24
     if val >= 11 and val <= 15:
       bonuspoints = 20
     if val >= 15 and val <= 20:
       bonuspoints = 16     
     if val >= 21 and val <= 30:
       bonuspoints = 12 
     if val >= 31 and val <= 50:
       bonuspoints = 6
     if val >= 51 and val <= 75:
       bonuspoints = 3
     if val >= 76 and val <= 100:
       bonuspoints = 2
     if val >= 101 and val <= 150:
       bonuspoints = 1
     #print("Bonus points: ", bonuspoints)  
     totalpointstograb = totalpointstograb + bonuspoints
    
    print(totalpointstograb)

#realpoints = rankingopponents - totalpointstograb


    


