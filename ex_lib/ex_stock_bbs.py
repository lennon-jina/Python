import requests
import json

# db 에서 krx_yn 이 Y인 종목만 요청
def get_btn(code):
    code = "005930"
    url = f"https://m.stock.naver.com/front-api/discuss?discussionType=localStock&itemCode={code}&size=100"
    res = requests.get(url)
    json_data = json.loads(res.text)
    for v in json_data['result']:
        print(v)
if __name__ == '__main__':
    get_btn('069080')
