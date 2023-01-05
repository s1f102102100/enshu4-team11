Emp = list(map(str, input('従業員を入力(半角空白区切り)').split()))

#従業員希望休
H_hope_before = list(map(int, input('従1 業員の希望休を入力(半角空白区切り)').split()))
H_hope=list(zip( Emp,H_hope_before ))
print(H_hope)