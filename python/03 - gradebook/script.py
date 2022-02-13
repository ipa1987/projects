last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
subjects = ['physics', 'calculus', 'poetry', 'history']
grades = [98, 97, 85, 88]

gradebook = list(zip(subjects, grades))

gradebook.append(['computer science', 100])
gradebook.append(['visual arts', 93])

#assign new tuple to the element at index -1
#it contains the values from the original tuple
#with 5 added to the last element
gradebook[-1] = (gradebook[-1][0], gradebook[-1][-1] +5)

#how do i remove the value of 85 from poetry and append "pass"
gradebook[2] = (gradebook[2][0], "pass") #again, a new tuple

print(gradebook)

full_gradebook = last_semester_gradebook + gradebook

print(full_gradebook)


