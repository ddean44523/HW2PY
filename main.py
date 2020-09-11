# Author: Daniel Dean dpd5518@psu.edu

def getLetterGrade(grade):
  if grade == 'A':
     grade = 4.0
  elif grade =='A-':
      grade = 3.67
  elif grade == 'B+': 
      grade = 3.33
  elif grade == 'B':
      grade = 3.0
  elif grade == 'B-':
      grade = 2.67
  elif grade == 'C+':
      grade = 2.33
  elif grade == 'C':
      grade = 2.0
  elif grade == 'D':
      grade = 1.0
  else:
      grade = 0.0
  return grade

if __name__ == '__main__':
  gradeOne = getLetterGrade(input("Enter your course 1 letter grade: "))
  creditOne = int(input("Enter your course 1 credit: "))
  print(f"Grade point for course 1 is: {gradeOne}")
  gradeTwo = getLetterGrade(input("Enter your course 2 letter grade: "))
  creditTwo = int(input("Enter your course 2 credit: "))
  print(f"Grade point for course 1 is: {gradeTwo}")
  gradeThree = getLetterGrade(input("Enter your course 3 letter grade: "))
  creditThree = int(input("Enter your course 3 credit: "))
  print(f"Grade point for course 3 is: {gradeThree}")
  print (f"Your GPA is: {(gradeOne * creditOne + gradeTwo * creditTwo + gradeThree * creditThree) / (creditOne + creditTwo + creditThree)}")