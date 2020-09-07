import utils

path = r'/Users/caosheng/Documents/tranSub/temp/Sahsiyet S01E06 ZH_CN&EN.ass'
output_file_name = utils.get_filename(path)


def ass2srt(path):
    setimes = utils.get_setimes(path)
    plaintext = utils.get_plaintext(path)
    format_sub = []
    for i in range(len(setimes)):
        format_sub.append('%s\n' % (i+1))
        format_sub.append(setimes[i]+'\n')
        format_sub.append(plaintext[i]+'\n')
    utils.write_txt('%s.srt' % (output_file_name), format_sub)


ass2srt(path)
