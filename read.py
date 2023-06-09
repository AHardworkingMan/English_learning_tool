# @author:顾志豪
# @time:2023/6/8 10:15
# @describe:单词测试 mode==‘explain'写中文，mode==’word‘写英文，最后输出正确率以及错误单词
import random


def read_file(fpath):
    fr = open(fpath, 'r', encoding="utf-8")
    word_list = []
    for line in fr:
        a = line.strip()
        word = a.split(' ')[0]
        explain = a.split(' ')[1]
        word_list.append([word, explain])
    fr.close()
    return word_list


def all_test(word_list, mode):
    right = 0
    wrong = 0
    length = len(word_list)
    word_ind = list(range(0, length))

    wrong_ls = []
    times = 0
    while times < length:
        len_ind = len(word_ind)
        ind = random.randint(0, len_ind - 1)
        ind = word_ind[ind]
        word_ind.remove(ind)
        if mode == 'explain':
            exp = input(word_list[ind][0] + ' 的解释：')
            if exp == 'exit':
                break
            if exp == word_list[ind][1]:
                right += 1
            else:
                wrong += 1
                wrong_ls.append(ind)
                print(word_list[ind][0] + ' 的正确释义：' + word_list[ind][1])
        elif mode == 'word':
            word = input(word_list[ind][1] + ' 的英文：')
            if word == 'exit':
                break
            if word == word_list[ind][0]:
                right += 1
            else:
                wrong += 1
                wrong_ls.append(ind)
                print(word_list[ind][1] + ' 的正确拼写：' + word_list[ind][0])
        times += 1
    return right, wrong, wrong_ls


if __name__ == "__main__":
    path = 'english.txt'
    wd_ls = read_file(path)
    ri, wr, wr_ls = all_test(wd_ls, 'word')
    print('正确率:', (ri / (ri + wr)) * 100, "%")
    print('错误单词：')
    for i in wr_ls:
        print(wd_ls[i][0] + "  " + wd_ls[i][1])
