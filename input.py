# @author:顾志豪
# @time:2023/6/8 10:15
# @describe:写入单词与释义，单词输入exit结束，释义输入re重新输入单词

def input_word(fpath):
    fw = open(fpath, 'a', encoding='utf-8')
    while 1:
        word = input("word:")
        explain = input("explain:")
        if word == "exit":
            break
        if explain == "re":
            continue
        fw.write(word + ' ' + explain + '\n')
    fw.close()


if __name__ == "__main__":
    path = 'english.txt'
    input_word(path)