sum  = 0.0
nocount = 0

while True:
  number = float(input("Enter a number : "))
  sum += number
  nocount += 1

  choice = input("Add another number ? (y/n) : ")
  if choice.casefold() == 'n':
      break

average = sum / nocount

print(f"sum : {sum}")
print(f"average : {average}")

