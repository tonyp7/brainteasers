# riddle

Given a string S of length N consisting of "?" and lowercase letters, the task is to replace "?" with lowercase letters such that no adjacent characters are the same. 
If more than one possible combination exists, print any one of them.

Examples

```python
# A simple solution that fits the task
solution('?a?a') #baba

# Anything is valid as long as no adjacent characters are the same
solution('gi?hub') #github

# Go nuts if you want!
solution('??????') #python
```

# solution

<details>
    <summary markdown="span">click to reveal</summary>

It's important to realize that while transforming '??????' into 'python' is cool, it is not necessary to complete this little algorithm. 'ababab' is also a valid answer.

In fact, you only need 3 distinct letters to never repeat an adjacent character. In the solution we use a, b and c, but it could be any combination of 3 letters.
eg:

```python
'a?a' # aba works
'a?b' # acb works
'a?c' # abc works
``` 

The algorithm simply becomes:
- Everytime you encounter a '?'
  - Get the character before and after
  - For each character in the list a, b c:
    - if char before and character after are not equal to the character, pick it and replace the '?'

</details>