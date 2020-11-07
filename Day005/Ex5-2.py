max_score = 0
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
  if n == 0:
      max_score = student_scores[n]
  else:
      if student_scores[n] > max_score:
          max_score = student_scores[n]
print('The highest score in the class is: '+str(max_score))