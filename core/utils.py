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


def get_start_time(subs,fmt):
    # 获取每条字幕的开始时间
    st = []
    for i in range(len(subs)):
        st.append(format_ms(subs[i].start,fmt))
    return st


def get_end_time(subs,fmt):
    # 获取每条字幕的结束时间
    et = []
    for i in range(len(subs)):
        et.append(format_ms(subs[i].end,fmt))
    return et


def write_lines(file_name, lines, mode='w'):
    # 创建txt文件，并写入list
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
