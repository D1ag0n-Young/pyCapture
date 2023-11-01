import configparser

config_path = 'config.ini'
# 读取配置文件
config = configparser.ConfigParser()
try:
    config.read(config_path, encoding='utf-8')
except Exception as e:
    print(str(e))
    exit(1)

# 获取配置项的值
try:
    writeup_zipfile_path = config.get('DEFAULT', 'writeup_zipfile_path')
    problems = config.get('DEFAULT', 'problems').strip('()').split(',')
    problem_number = int(config.get('DEFAULT', 'problem_number'))
    similarity_result_excel = config.get('DEFAULT', 'similarity_result_excel')
    img_md5_csv = config.get('DEFAULT', 'img_md5_csv')
    similarity_max = int(config.get('DEFAULT', 'similarity_max'))
except Exception as e:
    print(str(e))
    exit(1)

