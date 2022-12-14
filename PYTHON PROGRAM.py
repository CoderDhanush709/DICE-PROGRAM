from random import randint

score = 0

while True:
  decision = input("Enter your desired number or enter 'q' to stop: ")
  if decision == 'q':
    break
  
  desired_number = int(decision)

  print('Now the die is being rolled....')
  top_face_number = randint(1, 6)

  print('The die says', top_face_number)

  matched = top_face_number == desired_number

  if matched:
    score += 1

  print('Congrats! you won the round' if matched else 'Sorry, better luck next time\n')

print('Your score is',score)
