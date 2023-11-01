# -*- coding: utf-8 -*-
import zipfile
import hashlib
from pyCapture import config
from pyCapture.checker import Checker
from pyCapture.writeup import parse_writeup


# 初始化队伍信息，包括zip文件名、图片名称和对应的md5值、writeup内容
class Team:
    def __init__(self, zip_file_path,team_name,team_writeup_content):
        self.zip_file_path = zip_file_path + team_name
        self.team_name = team_name
        self.img = {}
        self.writeup_content = team_writeup_content
        self.fmt_writeup = {}
        self.set_writeup_content_and_img()
        self.set_fmt_writeup()

    def set_writeup_content_and_img(self):
        with zipfile.ZipFile(self.zip_file_path) as zf:
            namelist = zf.namelist()
            if 'img/' in namelist:
                for img_file in zf.namelist():
                    if img_file.startswith('img/') and not zf.getinfo(img_file).is_dir():
                        img_bytes = zf.read(img_file)
                        self.img[img_file] = hashlib.md5(img_bytes).hexdigest()

    def set_fmt_writeup(self):
        self.fmt_writeup = parse_writeup(self.writeup_content)


# 获取所有队伍信息
def get_all_teams(ch:Checker):
    teams = []
    for team_name, writeup_content in ch.team_writeup_content.items():
        teams.append(Team(config.writeup_zipfile_path,team_name,writeup_content))
    # for file_name in os.listdir(writeup_zipfile_path):
    #     file_path = writeup_zipfile_path + file_name
    #     if not zipfile.is_zipfile(file_path):
    #         continue
    #     with zipfile.ZipFile(file_path) as zf:
    #         namelist = zf.namelist()
    #         if 'img/' not in namelist or 'writeup.md' not in namelist:
    #             continue
    return teams


def get_single_teams(zip_file_path, team_name):
    try:
        with zipfile.ZipFile(zip_file_path+team_name) as zf:
            namelist = zf.namelist()
            if 'img/' not in namelist or 'writeup.md' not in namelist:
                print(team_name, '缺少img文件夹或writeup.md文件')
            team_writeup_content = zf.read('writeup.md').decode(errors='ignore')
            return Team(zip_file_path, team_name, team_writeup_content)
    except Exception as e:
        print(str(e))
