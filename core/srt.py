import utils

path = r'/Users/caosheng/Downloads/kota factory/Kota Factory - EP 01 - Inventory.ass'
output_path
output_filename = utils.get_filename(path)


def ss2srt(path):

    timer = utils.Timer()
    timer.start()

    subs = utils.load_sub_file(path)

    start_time = utils.get_start_time(subs,'srt')
    end_time = utils.get_end_time(subs,'srt')
    plaintext = utils.get_plaintext(subs)
    format_sub = []

    for i in range(len(subs)):
        format_sub.append('%s\n' % (i+1))
        format_sub.append('%s --> %s\n' % (start_time[i], end_time[i]))
        format_sub.append('%s\n' % (plaintext[i]))

    utils.write_lines('%s.srt' % (output_filename), format_sub)

    timer.stop()

    print('转换完成，用时%.2f秒' % (timer.elapsed))


ss2srt(path)
