# -*- coding: utf-8 -*-
from pyCapture import config
from pyCapture.main import check_env, single_team_check, all_check
import argparse
import loadconfig


if __name__ == '__main__':
    # 创建解析器对象
    parser = argparse.ArgumentParser(description='pyCapture')

    # 添加选项
    parser.add_argument('-t', '--test', action='store_true', help='测试环境或资源是否合法')
    parser.add_argument('-s', '--single', action='store_true', help='对比两个队伍代码的相似度')
    parser.add_argument('-a', '--ateam', help='ateam filename')
    parser.add_argument('-b', '--bteam', help='bteam filename')
    parser.add_argument('-A', '--All', help='对比所有队伍代码相似度', action='store_true')

    # 解析命令行参数
    args = parser.parse_args()
    config.problems = loadconfig.problems
    config.writeup_zipfile_path = loadconfig.writeup_zipfile_path
    config.similarity_max = loadconfig.similarity_max
    config.img_md5_csv = loadconfig.img_md5_csv
    config.similarity_result_excel = loadconfig.similarity_result_excel

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

