meal = 10
tax = 0.08
tip = 0.15

meal = meal + (meal*tax)
total = meal + (meal*tip)

print('$%.2f' % total)