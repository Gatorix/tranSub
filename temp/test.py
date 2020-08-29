import re

str = 'a22sdf111今JJJ11天?'

s = re.sub(
    # u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", str)
    u"([^\u4e00-\u9fa5\u0030-\u0039\?])", "", str)
print(s)