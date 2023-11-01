# pyCapture

This is a writeup audit tool with two functions:

1. Audit the code similarity between the codes involved in each topic in a fixed format of the writeup

2. udit whether images under IMG have the same hash value

## Install

Installation related dependencies:
```
pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```
Clone this project and configure the `config.ini` related items to use it

```bash 
git clone https://github.com/D1ag0n-Young/pyCapture.git
cd pyCapture
```

## Usage

```conf
[DEFAULT]
writeup_zipfile_path=F:\2023ctf\writeups\  
problems=Little_game-web,babynote-web,ezJava-web,browser_OS-web,可疑数据-reverse,小偷在哪里-reverse,authpack-pwn,strangeheap-pwn,easykvm-pwn,GetYourKey-mobile,EzQ-virtual,easy_cgi-iot,escape-cloud,extremefake-ai,easy_ecu-car,ez_reg,ez_pcap,ezcrypto,mpc_in_three
problem_number=6
similarity_result_excel=./out/similarity_output.xlsx
img_md5_csv=./out/img_md5.csv
similarity_max=80 # Code similarity, two teams exceeding this similarity will be recorded as similarity_ Result_ In an Excel table

```
The question name in the problem option should match the question name in the writeup. 

Writeup is a zip package, and the specific format can be found in the zip file under writeupdemo

```python
# 添加选项
parser.add_argument('-t', '--test', action='store_true', help='测试环境或资源是否合法')
parser.add_argument('-s', '--single', action='store_true', help='对比两个队伍代码的相似度')
parser.add_argument('-a', '--ateam', help='ateam filename')
parser.add_argument('-b', '--bteam', help='bteam filename')
parser.add_argument('-A', '--All', help='对比所有队伍代码相似度', action='store_true')

```

`-A` is for comparing all teams, `-s` is for comparing two teams

```bash
python3 -t # Whether there are dependencies related to testing tools in the running environment
python3 -A # Compare all teams
python3 -s -a team1writeup_zip_file_patch -b team1writeup_zip_file_patch # Compare two teams
```

## writeup demo

Please refer to the readme file under writeupdemo for the specific format.










