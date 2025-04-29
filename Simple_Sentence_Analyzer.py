def text_analyzer(sentence):
    count = 0
    for char in sentence:
        if char in 'aA':
            count += 1
    words = sentence.split()
    longest = sorted(words, key=len, reverse=True)
    total_words = len(words)
    return (
        f'The sentence has {total_words} words',
        f'The letter a/A appears {count} times',
        f'The 5 longest words are {longest[0:5]}'
    )


result = text_analyzer('The wind whispers secrets among the leaves of the blooming mango tree.')
print(result)