import urllib.request as res

# 이미지 다운로드
url = "https://img.cgv.co.kr/Movie/Thumbnail/Poster/000089/89058/89058_320.jpg"   
res.urlretrieve(url, 'test.png')