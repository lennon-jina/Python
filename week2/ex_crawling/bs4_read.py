import csv
data_list = []
with open('paxnet.csv', mode='r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter='|')
    for row in reader:
        data_list.append(row)

for v in data_list:
    url = f"https://www.paxnet.co.kr/tbbs/list?tbbsType=L&id=N10841&page={v[0]}"
    print(v[1])
    print(url)

f