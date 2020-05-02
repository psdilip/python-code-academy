vowels = ['a','e','i','o','u','A','E','I','O','U']
def anti_vowel(text):
  for i in vowels:
    if i in text:
        text = text.replace(i,"")
  print(text)

anti_vowel("sai")