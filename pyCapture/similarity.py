# -*- coding: utf-8 -*-
"""
通过测试，现有的基于文本距离比对的方式较适合代码相似度比对
基于Levenshtein、jaccard、cosine文本相似度效果优于difflib库
"""
import Levenshtein
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from pyCapture import config
from pyCapture.team import Team


# 比较两个队伍的代码相似度
def compare_teams(team1:Team, team2:Team):
    similarity_result = []
    for problem_name in config.problems:
        code1 = team1.fmt_writeup.get(problem_name.lower())
        code2 = team2.fmt_writeup.get(problem_name.lower())
        similarity = text_similarity(code1, code2)
        similarity_result.append((f'{team1.team_name} <-> {team2.team_name}', problem_name, similarity))
    return similarity_result


def levenshtein_similarity(str1, str2):
    lev_dist = Levenshtein.distance(str1, str2)
    max_len = max(len(str1), len(str2))
    similarity = (max_len - lev_dist) / max_len
    return similarity


def jaccard_similarity(str1, str2):
    set1 = set(str1)
    set2 = set(str2)
    intersection = len(set1.intersection(set2))
    union = len(set1) + len(set2) - intersection
    return intersection / union


def calculate_cosine_similarity(str1, str2):
    vec = CountVectorizer(tokenizer=lambda x: x.split())
    X = vec.fit_transform([str1, str2])
    return cosine_similarity(X)[0][1]


def text_similarity(str1, str2):
    if not str1 or not str2:
        return 0
    lev_dist = levenshtein_similarity(str1, str2)
    jac_sim = jaccard_similarity(str1, str2)
    cos_sim = calculate_cosine_similarity(str1, str2)  # 更改为新名称的函数
    # print(lev_dist , jac_sim,cos_sim)
    avg_sim = (lev_dist + jac_sim + cos_sim) / 3.0
    similarity_percentage = avg_sim * 100.0
    return similarity_percentage

