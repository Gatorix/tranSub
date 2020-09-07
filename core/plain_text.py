import utils

path = r'/Users/caosheng/Documents/tranSub/temp/Sahsiyet S01E01 ZH_CN&EN.srt'


def extract_plain_text(path, english_only=False, chinese_only=False):
    
    output_file_name = utils.get_filename(path)

    plaintext = utils.get_plaintext(path)

    if english_only and chinese_only == True:
        print('仅保留中文和仅保留英文不能同时勾选\nChinese only and English only cannot be checked at the same time')

    elif chinese_only:
        chinese_lines = []
        for i in range(len(plaintext)):
            chinese_lines.append(utils.chinese_only(plaintext[i])+'\n')
        utils.write_txt('%s.txt' % (output_file_name), chinese_lines)

    elif english_only:
        english_lines = []
        for i in range(len(plaintext)):
            english_lines.append(utils.english_only(plaintext[i])+'\n')
        utils.write_txt('%s.txt' % (output_file_name), english_lines)

    else:
        utils.write_txt('%s.txt' % (output_file_name), plaintext)


extract_plain_text(path)
