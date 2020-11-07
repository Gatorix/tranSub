import time
import os
import sys
import re
import pysubs2


def load_sub_file(path):
    # 加载字幕文件
    return pysubs2.load(path)


def get_plaintext(subs):
    # 提取字幕中的纯文本
    lines = []
    for i in range(len(subs)):
        lines.append(subs[i].plaintext+'\n')
    return lines


def get_start_time(subs, fmt):
    # 获取每条字幕的开始时间
    st = []
    for i in range(len(subs)):
        st.append(format_ms(subs[i].start, fmt))
    return st


def get_end_time(subs, fmt):
    # 获取每条字幕的结束时间
    et = []
    for i in range(len(subs)):
        et.append(format_ms(subs[i].end, fmt))
    return et


def write_lines(file_name, lines, mode='w'):
    # 创建文件，并写入list
    with open(file_name, mode=mode) as f:
        f.writelines(lines)
        f.close()


def write_txt(file_name, txt, mode='w'):
    # 创建txt文件，并写入文本
    with open(file_name, mode=mode) as f:
        f.write(txt)
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


def format_ms(ms, fmt):
    # 毫秒转换成h:m:s.ms

    try:
        s, ms = divmod(ms, 1000)
        m, s = divmod(s, 60)
        h, m = divmod(m, 60)
        if fmt == 'srt':
            return "%02d:%02d:%02d,%03d" % (h, m, s, ms)
        elif fmt == 'ass':
            return "%d:%02d:%02d.%03d" % (h, m, s, ms)
    except Exception as e:
        print(e)


class Timer:
    # 计时器
    def __init__(self, func=time.perf_counter):
        self.elapsed = 0.0
        self._func = func
        self._start = None

    def start(self):
        if self._start is not None:
            raise RuntimeError('Already started')
        self._start = self._func()

    def stop(self):
        if self._start is None:
            raise RuntimeError('Not started')
        end = self._func()
        self.elapsed += end - self._start
        self._start = None

    def reset(self):
        self.elapsed = 0.0

    @property
    def running(self):
        return self._start is not None

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *args):
        self.stop()

# def get_all_filepath(filepath):
#     # 遍历filepath下所有文件，包括子目录
#     files = os.listdir(filepath)
#     for fi in files:
#         fi_d = os.path.join(filepath, fi)
#         # 判断是否子文件夹
#         # 如果是，重新运行此函数，直到最末级
#         if os.path.isdir(fi_d):
#             get_all_filepath(fi_d)
#         # 不是输出文件路径
#         else:
#             print(os.path.join(filepath, fi_d))

def get_all_filepath(folder):
    # 获取指定路径下的所有.ass文件
    file_path = []
    for fpathe, dirs, fs in os.walk(folder):
        for f in fs:
            if '.DS_Store' in os.path.join(fpathe, f):
                pass
            elif os.path.join(fpathe, f)[-4:] != '.ass':
                pass
            else:
                file_path.append(os.path.join(fpathe, f))
    return file_path
