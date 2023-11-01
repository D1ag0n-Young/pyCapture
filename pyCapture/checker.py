# -*- coding: utf-8 -*-
import importlib
import os
import zipfile
from pyCapture import config
from pyCapture.writeup import parse_writeup


# 检查zip包是否符合要求，返回不符合标准的zip包名称和原因
class Checker:
    def __init__(self):
        self.problem_flag = {}
        self.team_writeup_content = {}
        self.single_fmt_writeup = {}
        self.error_zip = []
        try:
            for pb_name in config.problems:
                self.problem_flag[pb_name.lower()] = False
            for file_name in os.listdir(config.writeup_zipfile_path):
                file_patch = config.writeup_zipfile_path + file_name
                if not zipfile.is_zipfile(file_patch):
                    continue
                with zipfile.ZipFile(file_patch) as zf:
                    namelist = zf.namelist()
                    if 'img/' not in namelist or 'writeup.md' not in namelist:
                        self.error_zip.append((file_name, '缺少img文件夹或writeup.md文件'))
                        continue
                    self.team_writeup_content[file_name] = zf.read('writeup.md').decode(errors='ignore')
        except Exception as e:
            self.error_zip.append(("Checker init", str(e)))

    def check_writeup_problems(self):
        try:
            for team_name, writeup_content in self.team_writeup_content.items():
                self.single_fmt_writeup = parse_writeup(writeup_content)
                for prob, _ in self.single_fmt_writeup.items():
                    if prob in [pr_name for pr_name, _ in self.problem_flag.items()]:
                        self.problem_flag[prob] = True
                    else:
                        self.error_zip.append((team_name, 'writeup.md中{}题目名称不符合要求'.format(prob)))
        except Exception as e:
            self.error_zip.append(("check_writeup_problems", str(e)))
        # if len(problems) > problem_number:
        #     self.error_zip.append((file_name, 'writeup.md中问题数目大于{}个'.format(problem_number)))

    def check_resources(self):
        self.check_writeup_problems()
        if self.error_zip:
            print('环境或资源存在以下错误:')
            for file, reason in self.error_zip:
                print(f'{file}: {reason}')
            exit(1)

    def check_env(self):
        package = ['pandas',
                   'zipfile',
                   'Levenshtein',
                   'sklearn',
                   'csv',
                   'markdown',
                   'bs4',
                   'configparser',
                   'argparse']
        for pk in package:
            try:
                importlib.import_module(pk)
            except ImportError:
                self.error_zip.append(("check_env_error", "package {} not install".format(str(pk))))
        self.check_resources()
