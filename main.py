def practice_assert(arg):
  print(f"is {arg!r} True?", bool(arg))
  assert arg, f"arg == {arg!r}"


print("this will pass ".ljust(40, '='))
practice_assert("abc")
print('''I said "This will pass"''')


try:
  print("This will raise an exception ".ljust(40, '='))
  practice_assert('')
except AssertionError as e:
  print('''I told you "This will raise an exception" :''', e)
finally:
  print("end of try-except block")


print("this will raise an exception ".ljust(40, '='))
practice_assert([])
print('''This line will not show up''')
