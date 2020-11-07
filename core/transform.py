import utils

path = r'/Users/caosheng/Documents/tranSub/temp/Sahsiyet S01E08 ZH_CN&EN.ssa'
output_filename = utils.get_filename(path)


def script_info(title=output_filename, warp_style=2):

    return '''
[Script Info]
; Converted by tranSub
Title: %s
; Original Script: 
; Original Translation:  
; Original Editing: 
; Original Timing: 
; Synch Point: 
; Script Updated By: 
; Update Details: 
ScriptType: 'v4.00+'
Collisions: Normal
; PlayResY: 
; PlayResX: 
; PlayDepth: 
Timer: 100.0000
WrapStyle: %s
ScaledBorderAndShadow: no

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,微软雅黑,40,&H00FFFFFF,&H00FFFFFF,&H19533B3B,&H910E0807,0,0,0,0,100.0,100.0,0.0,0.0,1,0.0,1.8292682,2,135,135,72,1
Style: Default-L2,微软雅黑,32,&H00FFFFFF,&H00FFFFFF,&H19533B3B,&H910E0807,0,-1,0,0,100.0,100.0,0.0,0.0,1,0.0,0.0,2,135,135,35,1
[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
    ''' % (title, warp_style)

# import numpy
# print(type(script_info()))
# Dialogue: 2, 1: 01: 57.52, 1: 02: 01.12, Default, , 0, 0, 0, , {\fad(200, 200)}救救我  内芙拉


def srt2ss(path, is_ass=True):

    timer = utils.Timer()
    timer.start()

    subs = utils.load_sub_file(path)

    start_time = utils.get_start_time(subs, 'ass')
    end_time = utils.get_end_time(subs, 'ass')
    plaintext = utils.get_plaintext(subs)

    sub_block = []
    LAYER = 0
    STYLE = 'Default'
    NAME = ''
    MARGINL = 0
    MARGINV = 0
    EFFECT = ''
    for i in range(len(subs)):
        sub_block.append('Dialogue: %d, %s, %s, %s, %s, %d, %d, %s, %s' % (
            LAYER, start_time[i], end_time[i], STYLE, NAME, MARGINL, MARGINV, EFFECT, plaintext[i]))
    utils.write_txt('%s.ass' % (output_filename), script_info())
    utils.write_lines('%s.ass' % (output_filename), sub_block, mode='a')

    timer.stop()

    print('转换完成，用时%.2f秒' % (timer.elapsed))


def ss2srt(path, chinese_only=False, english_only=False, Tchinese_only=False):

    timer = utils.Timer()
    timer.start()

    subs = utils.load_sub_file(path)

    start_time = utils.get_start_time(subs, 'srt')
    end_time = utils.get_end_time(subs, 'srt')
    plaintext = utils.get_plaintext(subs)
    format_sub = []

    if chinese_only == True:
        pass
    elif english_only == True:
        pass
    elif Tchinese_only == True:
        pass
    else:
        # 简体&英文双语
        for i in range(len(subs)):
            format_sub.append('%s\n' % (i+1))
            if start_time[i] == start_time[i-1] and end_time[i] == end_time[i-1]:
                format_sub.append('%s --> %s\n' % (start_time[i], end_time[i]))
                format_sub.append('%s' % (plaintext[i-1]))
                format_sub.append('%s\n' % (plaintext[i]))
            elif start_time[i] == start_time[i+1] and end_time[i] == end_time[i+1]:
                format_sub.remove(format_sub[-1])
                pass
            else:
                format_sub.append('%s --> %s\n' % (start_time[i], end_time[i]))
                format_sub.append('%s\n' % (plaintext[i]))

    utils.write_lines('%s.srt' % ("test"), format_sub)

    timer.stop()

    print('转换完成，用时%.2f秒' % (timer.elapsed))
