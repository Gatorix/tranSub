import utils

path = r'/Users/caosheng/Documents/tranSub/temp/Sahsiyet S01E08 ZH_CN&EN.ssa'
output_file_name = utils.get_filename(path)


def ss2srt(path):

    timer = utils.Timer()
    timer.start()

    subs = utils.load_sub_file(path)

    start_time = utils.get_start_time(subs)
    end_time = utils.get_end_time(subs)
    plaintext = utils.get_plaintext(subs)

    format_sub = []

    for i in range(len(plaintext)):
        format_sub.append('%s\n' % (i+1))
        format_sub.append('%s --> %s\n' % (start_time[i], end_time[i]))
        format_sub.append('%s\n' % (plaintext[i]))

    utils.write_txt('%s.srt' % (output_file_name), format_sub)

    timer.stop()

    print('转换完成，用时%.2f秒' % (timer.elapsed))


ss2srt(path)
