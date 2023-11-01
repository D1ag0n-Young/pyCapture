# -*- coding: utf-8 -*-
from pyCapture import config
from pyCapture.checker import Checker
from pyCapture.similarity import compare_teams
from pyCapture.team import get_all_teams, get_single_teams
from pyCapture.tools import output_similarity_results_to_execl, output_img_md5_to_csv
from pyCapture.writeup import compare_md5
import argparse


def check_env():
    checker = Checker()
    checker.check_env()
    print('env check success!')
    exit(0)


def single_team_check(team1_name,team2_name):
    # 在这里处理 -s 选项生效的逻辑
    if team1_name and team2_name:
        result_similarity = compare_teams(get_single_teams(config.writeup_zipfile_path, team1_name),
                                          get_single_teams(config.writeup_zipfile_path, team2_name))
        for pb in result_similarity:
            print(pb)
    else:
        print('-a or -b not provided!')


def all_check():
    checker = Checker()
    checker.check_env()

    similarity_results = []
    all_teams = get_all_teams(checker)
    for i in range(len(all_teams)):
        for j in range(i + 1, len(all_teams)):
            if all_teams[i] != all_teams[j]:
                result = compare_teams(all_teams[i], all_teams[j])
                similarity_results.extend([sim for sim in result])
                # similarity_results.extend([(team1, team2, sim) for sim in result])
    print("Code Compare Result:")
    # 输出相似度高于85%的数据
    for team_two, problem, similarity in similarity_results:
        if similarity > config.similarity_max:
            print(f'{team_two}: {problem}, {similarity :.2f}%')
    print("IMG Compare Result:")
    # 输出图片MD5值相同的数据
    md5_results = compare_md5(all_teams)
    output_img_md5_to_csv(md5_results)
    for md5 in md5_results:
        if len(md5_results[md5]) > 1:
            print("%s:%s" % (md5, md5_results[md5]))

    # 输出结果到excel表格中
    output_similarity_results_to_execl(similarity_results)


if __name__ == '__main__':
    # 创建解析器对象
    parser = argparse.ArgumentParser(description='pyCapture')

    # 添加选项
    # parser.add_argument('-c', '--config', required=True, help='项目配置文件')
    parser.add_argument('-t', '--test', action='store_true', help='测试环境或资源是否合法')
    parser.add_argument('-s', '--single', action='store_true', help='对比两个队伍代码的相似度')
    parser.add_argument('-a', '--ateam', help='ateam filename')
    parser.add_argument('-b', '--bteam', help='bteam filename')
    parser.add_argument('-A', '--All', help='对比所有队伍代码相似度', action='store_true')

    # 解析命令行参数
    args = parser.parse_args()
    config.problems=['little_game-web', 'babynote-web', 'ezJava-web', 'Browser_OS-web', '可疑数据-reverse', '小偷在哪里-reverse',
                     'authpack-pwn','strangeheap-pwn','easykvm-pwn','GetYourKey-mobile','EzQ-virtual','easy_cgi-iot',
                     'escape-cloud','extremefake-ai','easy_ecu-car','ez_reg','ez_pcap','ezcrypto','mpc_in_three']
    config.writeup_zipfile_path = "F:\\2023华为内部赛\\writeup提交模板\\"
    config.similarity_max = 80
    config.img_md5_csv = "img_md5_csv.csv"
    config.similarity_result_excel = "similarity_result_excel.xlsx"
    # 使用选项
    if args.test:
        check_env()
    elif args.single:
        single_team_check(args.ateam, args.bteam)
    elif args.All:
        all_check()

    '''
    
    1. 环境检测：资源包检测独立成选项、环境依赖检测
    2. 单例检测：两队单独检测选项，输出控制台
    3. 全部检测：统一检测相似度，结果输出excel
    '''

