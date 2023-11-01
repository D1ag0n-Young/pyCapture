# -*- coding: utf-8 -*-
import markdown
import markdown_it
from bs4 import BeautifulSoup


def parse_writeup(markdown_text):
    # 将 Markdown 转换为 HTML
    html = markdown.markdown(markdown_text)
    # 创建 markdown-it 解析器
    md_parser = markdown_it.MarkdownIt()
    # 将 Markdown 转换为 HTML
    html = md_parser.render(markdown_text)
    # 使用 Beautiful Soup 解析 HTML
    soup = BeautifulSoup(html, 'html.parser')
    # soup = BeautifulSoup(html, 'lxml')
    # 创建字典存储题目和代码内容
    code_dict = {}
    # 查找所有题目和代码块的父级标签
    parents_list = soup.find_all(['h1', 'code'])
    # 循环遍历父级标签
    for parent in parents_list:
        # code = ''
        if parent.name == 'h1':
            # 提取题目名称
            title = parent.text.strip().lower()
            code = ''
        elif parent.name == 'code':
            # 提取代码内容
            code += parent.text.strip()
            # 去除代码块中的换行符和空格
            # code = re.sub(r'\n\s*', '', code)
            # 将题目名称和代码内容添加到字典中
            code_dict[title] = code

    return code_dict


# 比较队伍之间图片MD5值是否重复
def compare_md5(all_team):
    md5_dict = {}
    # md5_dict_result = {}
    for team in all_team:
        for img_file, img_md5 in team.img.items():
            if img_md5 in md5_dict:
                md5_dict[img_md5].append((team.team_name, img_file))
            else:
                md5_dict[img_md5] = [(team.team_name, img_file)]

    # results = {}
    # for md5, teams in md5_dict.items():
    #     if len(teams) > 1:
    #         print(teams)
    #         result[md5].append(teams)
    #         for i in range(len(teams)):
    #             for j in range(i + 1, len(teams)):
    #                 results.append((teams[i][0], teams[j][0], teams[j][1], md5))
    # print(results)
    return md5_dict