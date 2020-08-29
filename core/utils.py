import pysubs2


def load_sub_file(path):
    return pysubs2.load(path)


def write_txt(file_name, lines):
    with open(file_name,mode='w') as f:
        f.writelines(lines)
        f.close()
