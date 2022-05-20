def translate(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    l = len(text)
    output = ''

    for i in range(0, l):
        if text[i] in vowels:
            if i > 0 and (text[i-1] in vowels):
                output += text[i]
            else: 
                output += 'av' + text[i]
        else:
            output += text[i]

    return output


#this is the same algorithm, but realizing the previously if/else statements could be shortened
#into this combined statement below. It does make the code slightly less readable in my opinion
def translate_shorter(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    l = len(text)
    output = ''

    for i in range(0, l):
        if text[i] in vowels and not(i > 0 and (text[i-1] in vowels)):
            output += 'av' + text[i]
        else:
            output += text[i]

    return output


print(translate('hello'))
print(translate('feu'))
print(translate('langue de feu'))