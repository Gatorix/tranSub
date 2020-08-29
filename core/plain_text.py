import utils

path = r'/Users/caosheng/Documents/tranSub/temp/Sahsiyet S01E06 ZH_CN&EN.srt'


def extract_plain_text(path, output_file_name, english_only=False, chinese_only=False):
    subs = utils.load_sub_file(path)
    lines = []
    for i in range(len(subs)):
        lines.append(subs[i].text.replace('\\N', ' ')+'\n')
    rblines = utils.remove_brackets(lines)

    if english_only and chinese_only == True:
        print('仅保留中文和仅保留英文不能同时勾选')

    elif chinese_only:
        chinese_lines = []
        for i in range(len(rblines)):
            chinese_lines.append(utils.chinese_only(rblines[i])+'\n')
        utils.write_txt('%s.txt' % (output_file_name), chinese_lines)

    elif english_only:
        english_lines = []
        for i in range(len(rblines)):
            english_lines.append(utils.english_only(rblines[i])+'\n')
        utils.write_txt('%s.txt' % (output_file_name), english_lines)

    else:
        utils.write_txt('%s.txt' % (output_file_name), rblines)


# print(__name__)
extract_plain_text(path, '111', chinese_only=True)
