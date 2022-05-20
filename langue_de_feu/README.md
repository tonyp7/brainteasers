# langue_de_feu

"Langue de feu" is a French slang where the extra syllable "av" is infixed inside a word before every vowel, but only if that vowel is itself not preceded by a vowel.

Write a function translate(text) that translates a text into its langue de feu version.

In this exercise we consider the text will always be all in lower cases.

Examples:

```
translate('hello') => 'havellavo'
A simple example

translate('feu') => 'faveu'
Here the first vowel 'e' get an 'av' prefix, but not 'u' since it's a double vowel

translate('langue de feu') => 'lavangavue dave faveu'
```