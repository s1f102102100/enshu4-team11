#ライブラリの用意
import pulp

#リストの定義
#日付リスト
Day = list(range(1,32))

#従業員リスト
Emp = ['a','b','c','d','e','f','g','h','i','j']

#従業員希望休
H_hope = [
          ('a',1),('a',4),('b',12),('b',13),('c',26),('d',9),('d',27),
          ('e',21),('f',6),('h',15),('i',25),('j',27),('j',28)
          ]

#定数の定義
#最適休暇人数リスト
S_req = {d:3 for d in Day}

#必要休暇日数
H_req = {e:hr for e,hr in zip(Emp,[9,8,9,8,9,9,10,8,9,9])}

#最適化モデルの定義
prob = pulp.LpProblem('ShiftFittingProblem',pulp.LpMinimize)

#変数の定義
ED = [(e,d) for e in Emp for d in Day]
x = pulp.LpVariable.dicts('x',ED,cat='Binary')

#制約式の定義

#必要休暇日数を守る
for e in Emp:
  prob += pulp.lpSum([x[e,d] for d in Day]) == H_req[e]

#希望休を守る
for e,d in H_hope:
  prob += x[e,d] == 1

#1日当たりの休暇人数は２～３人
for d in Day:
  prob += pulp.lpSum([x[e,d] for e in Emp]) <= S_req[d]
  prob += pulp.lpSum([x[e,d] for e in Emp]) >= S_req[d]-1

#3連休以上を作らない
n1=int(input('n連休以上を作らない'))
q=0
for e in Emp:
  for d in Day[:-n1]:
    for f in range(n1):
        n = x[e,d+f]
    prob += n<=n1 

#5連勤以上を作らない
n2=input('n連勤以上を作らない')
for e in Emp:
  for d in Day[:-4]:
    prob += x[e,d] + x[e,d+1] + x[e,d+2] + x[e,d+3] + x[e,d+4] >= 1

#飛び石連休を作らない
for e in Emp:
  for d in Day[:-2]:
    prob += x[e,d] + x[e,d+2] <= 1

#目的関数の定義
'なし'

#求解
status = prob.solve()
print('Status:', pulp.LpStatus[status])

#計算結果の表示
import pandas as pd
print(pd.DataFrame([[x[e,d].value() for d in Day] for e in Emp]))