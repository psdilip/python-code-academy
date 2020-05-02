grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
  total = 0
  for i in scores:
    total += i
  return total
print(grades_sum(grades))

def grades_average(grades_input):
  sum_total = grades_sum(grades_input)
  average = sum_total/float(len(grades_input))
  return average
print(grades_average(grades))

def grades_variance(scores):
  average = grades_average(scores)
  variance = 0
  for score in scores:
    variance += (average - score)**2
  variance = variance/len(scores)
  return variance
print(grades_variance(grades))