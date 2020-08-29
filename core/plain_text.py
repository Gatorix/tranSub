import utils

path = r'/Users/caosheng/Documents/tranSub/temp/Sahsiyet S01E01 ZH_CN&EN.ass'


def extract_plain_text(path,output_file_name):
    subs = utils.load_sub_file(path)
    lines = []
    for i in range(len(subs)):
        lines.append(subs[i].text+'\n')
    utils.write_txt('%s.txt'%(output_file_name), lines)


# print(__name__)
extract_plain_text(path,'111')
