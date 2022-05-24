def solution(words):

    words_sorted = sorted(words)

    output = []

    current_word = words_sorted[0]
    current_word_count = 0

    for w in words_sorted:
        if(current_word == w): #if it's the current word, then we count+1
            current_word_count += 1
        else: #else, reset word count to 1, change curremt word and flush to output
            output.append(current_word_count)
            current_word_count = 1
            current_word = w

    output.append(current_word_count)


    return output


example = ['the', 'dog', 'got', 'the', 'bone']
print(solution(example))
