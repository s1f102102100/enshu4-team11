#ライブラリの用意
import pulp

#リストの定義
#日付リスト
Day = list(range(1,32))

#従業員リスト
# -*- coding: utf-8 -*-
Emp = list(map(str, input('従業員を入力(半角空白区切り)').split()))

#従業員希望休
H_hope_before = list(map(int, input('従業員の希望休を入力(半角空白区切り)').split()))
H_hope=list(zip( Emp,H_hope_before ))
#定数の定義
#最適出勤人数リスト

S_req = {d:3 for d in Day}

#必要出勤日数
H_req = {e:hr for e,hr in zip(Emp,list(map(int, input('必要出勤日数(半角空白区切り)').split())))}

#最適化モデルの定義
prob = pulp.LpProblem('ShiftFittingProblem',pulp.LpMinimize)

#変数の定義
ED = [(e,d) for e in Emp for d in Day]
x = pulp.LpVariable.dicts('x',ED,lowBound=0,upBound=1,cat='Binary')

#制約式の定義


#希望休を守る
for e,d in H_hope:
  prob += x[e,d] == 1

#1日当たりの出勤人数
for d in Day:
  prob += pulp.lpSum([x[e,d] for e in Emp]) <= S_req[d]
  prob += pulp.lpSum([x[e,d] for e in Emp]) >= S_req[d]-1

#3連休以上を作らない
n1=int(input('n連勤以上を作らない'))
q=0
for e in Emp:
  for d in Day[:-n1-1]:
    for f in range(n1):
        n = x[e,d+f]
    prob += n<=n1



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