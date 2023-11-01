# -*- coding: utf-8 -*-
import pandas as pd
from pyCapture import config
import csv


# 输出相似度结果到excel表格中
def output_similarity_results_to_execl(similarity_result):
    if not similarity_result:
        return
    # 将数据转换为 pandas DataFrame
    df = pd.DataFrame(similarity_result, columns=['teams\problems', 'column_label', 'value'])

    # 使用 pivot 函数将列标志作为列，并将行标志作为行
    df_pivot = df.pivot(index='teams\problems', columns='column_label', values='value')

    # 样式函数，根据条件设置单元格背景颜色
    def set_cell_background_color(value):
        if value > config.similarity_max:
            return 'background-color: yellow'
        return ''

    # 应用样式函数和表格样式到 DataFrame
    styled_df = df_pivot.style.applymap(set_cell_background_color).set_properties(**{'text-align': 'center'})

    # 保存为 Excel 文件
    writer = pd.ExcelWriter(config.similarity_result_excel, engine='xlsxwriter')
    styled_df.to_excel(writer, index=True)

    # 获取每一列中列标签的最大长度
    max_label_lengths = [len(df_pivot.index.values[0])]
    for column in df_pivot.columns:
        max_label_lengths.append(len(column))

    # 调整列宽度
    worksheet = writer.sheets["Sheet1"]  # 假设只有一个工作表且名称为 "Sheet1"
    for i, width in enumerate(max_label_lengths):
        worksheet.set_column(i , i, width * 1.2)  # 设置列宽度为最大长度的 1.2 倍

    # 保存修改后的 Excel 文件
    writer.close()


def output_img_md5_to_csv(data):
    if not data:
        return

    # data = {
    #     '5aba70705d905a53f6dff243e78b36ec': [('team1-writeup.zip', 'img/20231010141004.png')],
    #     'f59d1165757a9347d394e4be6807c388': [('team1-writeup.zip', 'img/20231010141040-1.png'),
    #                                          ('team1-writeup.zip', 'img/20231010141040.png'),
    #                                          ('team2-writeup.zip', 'img/20231010141040-1.png'),
    #                                          ('team3-writeup.zip', 'img/20231010141040-1.png'),
    #                                          ('签个到-writeup.zip', 'img/20231010141040-1.png')],
    #     '209a3163888d720115f070049d3c3b32': [('team2-writeup.zip', 'img/20231010142202.png'),
    #                                          ('team3-writeup.zip', 'img/20231010142202.png'),
    #                                          ('签个到-writeup.zip', 'img/20231010142202.png')],
    #     '856f25a7cdd920feccf51f5056c5d903': [('team2-writeup.zip', 'img/20231010142220.png'),
    #                                          ('team3-writeup.zip', 'img/20231010142220.png'),
    #                                          ('签个到-writeup.zip', 'img/20231010142220.png')]
    # }

    # 设置 CSV 文件路径
    csv_file = config.img_md5_csv

    # 将字典数据写入 CSV 文件
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)

        # 写入表头
        writer.writerow(['Key', 'Value'])
        # 逐行写入数据
        for key, values in data.items():
            value = [str(value) for value in values]
            value = [''.join(value)]
            writer.writerow([key] + value)

