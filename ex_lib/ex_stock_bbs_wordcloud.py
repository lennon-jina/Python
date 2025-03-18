import pandas as pd
from PIL.ImageOps import scale

from week2.ex_db.DBManager import DBManager
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
from konlpy.tag import Okt
from PIL import Image

from week2.ex_lib.ex_wordcloud02 import stop_words

sql = """
    SELECT *
    FROM stock_bbs
"""
db = DBManager()
okt = Okt()
nouns = []
conn = db.get_connection()
df = pd.read_sql(con=conn, sql=sql)
for i, v in df.iterrows():
    print(v['BBS_CONTENTS'])

    stop_words = {"주식", "회사", "주주", "주가"}  # 제외 단어 목록
    for i, v in df.iterrows():
    # 1. 명사 추출
        word_list = okt.nouns(v['BBS_CONTENTS'])  # 명사만 추출
        filter_list = [x for x in word_list if len(x) > 1 and x not in stop_words]
        nouns += filter_list
    # 2. 단어 카운트 생성
    count = Counter(nouns)

    wc = WordCloud(background_color='white', width=800, height=400
                   , scale=2.0, max_font_size=250
                   , min_font_size=15
                   , font_path="../../datatset/NanumGothicBold.ttf")
    gen = wc.generate_from_frequencies(count)
    # 3. 워드 클라우드 생성
    plt.figure(figsize=(10, 5))
    plt.imshow(gen)
    plt.axis("off")
    plt.show()
