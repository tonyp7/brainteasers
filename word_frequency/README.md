# word_frequency

Write an algorithm that given a list of words returns the total count of each individual word in an array, in alphabetical order.

example:

```python
example = ['the', 'dog', 'got', 'the', 'bone']
solution(example) #[1, 1, 1, 2]

# here the output is [1, 1, 1, 2] because we have:
# bone:1, dog:1, got:1, the: 2 
```


# solution

This problem would actually be harder if we were asked to simply output the count of words in the order that they were found.
But because we are being asked to output in alphabetical order, this is a tremendous help that will simplify our lives.

So the first part of the algorithm is simply to order the list. That way:

```python
example = ['the', 'dog', 'got', 'the', 'bone']
#becomes:
sorted(example) #['bone', 'dog', 'got', 'the', 'the']
```

Then, we just need to iterate through this sorted list. Every time you encounter a word that is different than the current
word being counted, all we have to do is to flush the current count to an output list.