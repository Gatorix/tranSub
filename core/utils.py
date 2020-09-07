import os
import sys
import re
import pysubs2


def load_sub_file(path):
    # 加载字幕文件
    return pysubs2.load(path)


def get_plaintext(path):
    # 提取字幕中的纯文本
    subs = load_sub_file(path)
    lines = []
    for i in range(len(subs)):
        lines.append(subs[i].plaintext+'\n')
    return lines


def get_setimes(path):
    # 获取每条字幕的起止时间
    subs = load_sub_file(path)
    se=[]
    for i in range(len(subs)):
        se.append('%s --> %s' %
              (format_ms(subs[i].start), format_ms(subs[i].end)))
    return se

def write_txt(file_name, lines):
    # 创建txt文件，并写入文本
    with open(file_name, mode='w') as f:
        f.writelines(lines)
        f.close()


def chinese_only(str):
    # 仅保留中文及中文标点
    s = re.sub(
        u"([^\u4e00-\u9fa5\u0030-\u0039\，\。\？\！])", "", str)
    return s


def english_only(str):
    # 仅保留英文和英文标点
    s = re.sub(
        u"([^\u0030-\u0039\u0041-\u005a\u0061-\u007a\' '\,\.\?\!])", "", str)
    return s


def get_filename(path):
    # 获取不带后缀的文件名
    (filepath, tempfilename) = os.path.split(path)
    (filename, extension) = os.path.splitext(tempfilename)
    return filename


def format_ms(ms):
    # 毫秒转换成h:m:s.ms
    if str(ms).isdigit():
        s, ms = divmod(ms, 1000)
        m, s = divmod(s, 60)
        h, m = divmod(m, 60)
        return "%02d:%02d:%02d,%03d" % (h, m, s, ms)
    else:
        print('字幕文件中存在时间格式错误\nThere is a time format error in the subtitle file')
