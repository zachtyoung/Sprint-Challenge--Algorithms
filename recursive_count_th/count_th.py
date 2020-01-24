'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if len(word) == 0: return 0
    if len(word) < 2: return 0
    total = 0
    if word[0] == 't' and word[1] == 'h': total += 1
    if len(word) > 2:
        total += count_th(word[1:])
    return total
