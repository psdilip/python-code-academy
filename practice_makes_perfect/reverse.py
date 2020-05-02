def reverse(text):
  letters = ""
  for i in text:
    letters = i + letters
  return letters