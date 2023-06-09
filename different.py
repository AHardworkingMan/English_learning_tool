# @author:顾志豪
# @time:2023/6/8 11:25
# @describe:直接运行，单词去重

from read import read_file


def different(word_list):
    list2 = []
    for l1 in word_list:
        if l1 not in list2:
            list2.append(l1)
    return list2


def write_to_file(fpath, ls):
    fw = open(fpath, "w", encoding="utf-8")
    for l in ls:
        word = l[0]
        explain = l[1]
        fw.write(word + " " + explain + "\n")
    fw.close()


if __name__ == "__main__":
    path = 'english.txt'
    wd_ls = read_file(path)
    ls2 = different(wd_ls)
    write_to_file(path, ls2)

