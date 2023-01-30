def reverseWords(s):
    s = s.strip()
    words = s.split()
    return " ".join(words[::-1])
s = "the sky is blue"
print("Reversed string:", reverseWords(s))
s = " hello world "
print("Reversed string:", reverseWords(s))
s ="a good example"
print("Reversed string:", reverseWords(s))
s ="apple is red"
print("Reversed string:", reverseWords(s))
s = "Red rose"
print("Reversed string:", reverseWords(s))
