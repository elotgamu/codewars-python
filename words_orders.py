def order(sentence):
    sentence_arr = sentence.split()
    ordered_sentence = []
    # print(sentence_arr)

    seq_arr = dict()
    for index, word in enumerate(sentence_arr):
        position = [int(l) for l in word if l.isdigit()]
        seq_arr[position[0]] = word

    # print(seq_arr)
    for item in sorted(seq_arr.keys()):
        if item in seq_arr:
            # word = replace_number(seq_arr[item])
            word = seq_arr[item]
            ordered_sentence.append(word)

    ordered = ' '.join([word for word in ordered_sentence])
    # print(ordered)
    return ordered


def replace_number(arg):
    arr = list(arg)
    index_number = [index for index, l in enumerate(arg) if l.isdigit()]
    arr[index_number[0]] = ''
    return ''.join(arr)


order('is2 Thi1s T4est 3a')
