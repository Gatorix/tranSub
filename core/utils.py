import sys
import re
import pysubs2


def load_sub_file(path):
    return pysubs2.load(path)


def write_txt(file_name, lines):
    with open(file_name, mode='w') as f:
        f.writelines(lines)
        f.close()


def chinese_only(str):
    s = re.sub(
        u"([^\u4e00-\u9fa5\u0030-\u0039\，\。\？\！])", "", str)
    return s


def english_only(str):
    s = re.sub(
        u"([^\u0030-\u0039\u0041-\u005a\u0061-\u007a\' '\,\.\?\!])", "", str)
    return s


def remove_brackets(li):
    nli = []
    for i in range(len(li)):
        nli.append(re.sub(u"\\(.*?\\)|\\{.*?}|\\[.*?]", "", li[i]))
    return nli
