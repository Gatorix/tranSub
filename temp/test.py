# import re

# str = 'a22sdf111今JJJ11天?'

# s = re.sub(
#     # u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", str)
#     u"([^\u4e00-\u9fa5\u0030-\u0039\?])", "", str)
# print(s)
import os
import pysubs2
import time
path = r'/Users/caosheng/Documents/tranSub/temp/Sahsiyet S01E01 ZH_CN&EN.srt'
(filepath, tempfilename) = os.path.split(path)
(filename, extension) = os.path.splitext(tempfilename)

print(filename)
time1 = pysubs2.time.ms_to_times(2280)
# print(time.strftime("%H:%M:%S",time1))

# ms = "2280r"
# s, ms = divmod(ms, 1000)
# m, s = divmod(s, 60)
# h, m = divmod(m, 60)

# print("%d:%02d:%02d.%03d" % (h, m, s, ms))
# print(utils.format_ms(5000))