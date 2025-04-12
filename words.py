word1 = input("Enter first word: ")
word2 = input("Enter second word: ")


set1 = set(word1)
set2 = set(word2)

common_chars = set1.intersection(set2)
different_in_word1 = set1.difference(set2)
different_in_word2 = set2.difference(set1)
union_chars = set1.union(set2)

print(f"First word: {word1}")
print(f"Second word: {word2}")
print(f"Common characters: {common_chars}")
print(f"Different Characters in first word: {different_in_word1}")
print(f"Different Characters in second word: {different_in_word2}")
print(f"Union characters: {union_chars}")
