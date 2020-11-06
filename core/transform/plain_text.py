import utils
import sys

path = r'/Users/caosheng/Downloads/Kota Factory (webm)/(English)(499) Kota Factory - EP 01 - Inventory - YouTube.srt'

output_file_name = utils.get_filename(path)


def extract_plain_text(path, english_only=False, chinese_only=False):

    timer = utils.Timer()
    timer.start()

    subs = utils.load_sub_file(path)
    plaintext = utils.get_plaintext(subs)

    if english_only and chinese_only == True:
        print('仅保留中文和仅保留英文不能同时勾选\nChinese only and English only cannot be checked at the same time')
        sys.exit(0)

 
    elif chinese_only:
        chinese_lines=[]
        for i in range(len(plaintext)):
            chinese_lines.append(utils.chinese_only(plaintext[i])+'\n')
        utils.write_lines('%s.txt' % (output_file_name), chinese_lines)

    elif english_only:
        english_lines=[]
        for i in range(len(plaintext)):
            english_lines.append(utils.english_only(plaintext[i])+'\n')
        utils.write_lines('%s.txt' % (output_file_name), english_lines)

    else:
        utils.write_lines('%s.txt' % (output_file_name), plaintext)

    timer.stop()

    print('提取完成，用时%.2f秒' % (timer.elapsed))


extract_plain_text(path)
