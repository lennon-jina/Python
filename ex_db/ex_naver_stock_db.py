import requests
import json
from DBManager import DBManager
myDb = DBManager()
conn = myDb.get_connection()
sql = """
    INSERT INTO tb_stocks(item_code, close_price)
    VALUES (:1, :2)
    """
for page in range(1, 25):
    url = f"https://m.stock.naver.com/api/stocks/marketValue/all?page={page}&pageSize=20"
    res = requests.get(url)
    if res.status_code == 200:
        stocks = json.loads(res.text)['stocks']
        for stock in stocks:
            code = stock['itemCode']
            price = stock['closePrice'].replace(',','')
            myDb.insert(sql, [code, price])

conn.commit()
conn.close()

# tb_stocks
# item_code, close_price, update_date(default sysdate)
# insert