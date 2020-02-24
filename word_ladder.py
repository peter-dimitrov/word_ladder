#!/bin/python3


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    from collections import deque
    import copy
    if start_word == end_word:
        return [start_word]
    with open(dictionary_file) as dictionary_file:
        dictionary = dictionary_file.readlines()
    new_dic = []
    for nword in dictionary:
        new_dic.append(nword.strip('\n'))
    s = []
    s.append(start_word)
    q = deque()
    q.appendleft(s)
    while len(q) != 0:
        top = q.pop()
        for word in new_dic:
            if _adjacent(word,top[-1]):    
                if word == end_word:
                    top.append(word)
                    for i in range(1,len(top)-2):
                        if _adjacent(top[i-1],top[i+1]):
                            top.pop(i)
                    return top
                sc = copy.deepcopy(top)
                sc.append(word)
                q.appendleft(sc)
                new_dic.remove(word)
    return None

def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.
    '''
    if len(ladder) == 0:
        return False
    if len(ladder) == 1:
        return True
    for index in range(len(ladder)-1):
            if not _adjacent(ladder[index],ladder[index+1]):
                return False
    return True            

def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    if len(word1) != len(word2):
        return False
    x = 0
    for index in range(len(word1)):
        if word1[index] != word2[index]:
            x += 1
    if x == 1:
        return True
    else:
        return False
       
