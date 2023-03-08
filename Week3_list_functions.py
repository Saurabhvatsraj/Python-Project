# string variable can have special characters with escape or backslash (\) char
msg = 'Today\'s special event is at 5:30pm' 
print(msg)

# List of Students
student_names = ['Mike','Sarah','Joe','Smith','Melanie','Renu','Rahul','Harris','Guru','Jenna']

# print(f"Student List - {student_names}")
# print("Student List - " + str(student_names))
# print("Student List - " + student_names) # why this string concatenation is not working?

msg = f"Name of first student in the list is  {student_names[0].title()}."
print(msg)


students_average_score = [91.99,94.43,89,85.23,98.31,88,78.6,92,94.35,80.72]
print()

print (f"student score {students_average_score[0] * 2}")
print(len(student_names))
print(len(students_average_score))
print("\nList values : " + str(students_average_score)) # Print the entire list

print(students_average_score[2:]) # print from second element to last

formatted_str = "Index -2 (second last element) is {:.2f}"
print(formatted_str.format(students_average_score[-2])) # print from second last element

formatted_str = "Index -1 (last element) is {:.2f}"
print(formatted_str.format(students_average_score[-1])) # print from second element to end

formatted_str = "Index -3 (third last element) is {:.2f}"
print(formatted_str.format(students_average_score[-3])) # print from second element to end


formatted_str = "Index 2 (3rd element) is {:.2f}"
print(formatted_str.format(students_average_score[2])) # print second element

formatted_str = "Index 0 (first element in the list) is {:.2f}"
print(formatted_str.format(students_average_score[0])) # print second element

formatted_str = "Index 1 (second element in the list) is {:.2f}"
print(formatted_str.format(students_average_score[1])) # print second element

print("Type of item list is " + str(type(students_average_score)))
print()

# List can have different data types
item_list = ['Jino',98.99, 100]
print("item_list have different data types : " + str(item_list))

# set or change values of an element
print("3rd element in student_names list is " + student_names[2])
student_names[2] = "James"

print()
# add a new name to student_names list
print("Add a new student name and average score")
student_names.append('Jude')
students_average_score.append(80.99)

print (student_names)
print (students_average_score)

num_values = [34,23,54,67,12,45]
print(num_values)

print(type(item_list))


r_values = range(0,22,3)
print(list(r_values))
print(type(r_values))

r_values = range(0,22,2)
print(list(r_values))

# The following statement print the student_names in a reverse order:
print(sorted(student_names,reverse=True ))
print(sorted(student_names))
print (f"student name: {student_names}")
student_names.sort()
# print(student_names)
print (f"permanantly sorted student name: {student_names}")
student_names.sort(reverse=True)
print (f"permanantly sorted (reverse order) student name: {student_names}")
print (f"student name: {student_names}")
student_names.reverse()
print (f"student name: {student_names}")
student_names.reverse()
print (f"student name: {student_names}")
