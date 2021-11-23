def reverse_the_inplace(string1):
    words = string1.split(' ')
    reverse_sentence = ' '.join(reversed(words))
    return reverse_sentence


print(reverse_the_inplace('welcome to gfg'))
