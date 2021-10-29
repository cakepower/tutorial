#!/usr/bin/python
# -*- coding: utf-8 -*-

from konlpy.tag import Okt, Kkma
from collections import Counter

okt = Okt() 
kkma = Kkma()
#m = Mecab()

tweet_message = '[속보] 정은경 코로나 전담병원 의료진부터 2월 중 접종 시작 https://twitter.com/JTBC_news/status/1354659426787987463/photo/1'

tweet_okt = okt.nouns(tweet_message)
tweet_kkma = kkma.pos(tweet_message)
#print(m.pos(tweet_message))

print(tweet_okt)
print(tweet_kkma)
