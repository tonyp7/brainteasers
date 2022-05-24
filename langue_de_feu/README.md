# langue_de_feu

"Langue de feu" is a French slang where the extra syllable "av" is infixed inside a word before every vowel, but only if that vowel is itself not preceded by a vowel.

Write a function translate(text) that translates a text into its langue de feu version.

In this exercise we consider the text will always be all in lower cases.

Examples:

```python
# simple example
translate('hello') #'havellavo'

# double voyel
# Here the first vowel 'e' get an 'av' prefix, but not 'u' since it's a double vowel
translate('feu') => 'faveu'

# a more complex example
translate('langue de feu') => 'lavangavue dave faveu'
```

Note that the real langue de feu slang is a bit more complicated than that, but in this coding exercise the rules have been extremely simplified.

# solution

<details>
    <summary markdown="span">click to reveal</summary>
    
This would be extremely simple if the rule for the double vowel did not exist. However this does not make it a lot more difficult.

In this algorithm, we simply iterate character per character over the original text, and build an output with the following rule:
 - if the character is a vowel
   - if the preceding character is a vowel, do not add 'av', else add 'av'
 - else add the character straight to the output

This is as straightforward as it gets.

</details>