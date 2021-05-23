def practice_assert(arg):
  assert arg, f"arg == {arg!r}"


print("this will pass")
practice_assert("abc")

print("this will raise an exception")
practice_assert([])
