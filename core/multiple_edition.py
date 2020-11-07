import os
import utils
import transform
folder = '/Users/caosheng/Documents/tranSub/core/subtitles'
ass_filepath = utils.get_all_filepath(folder)

# part1 输出双语srt：

transform.ss2srt(ass_filepath[1])

