student_marks = [85, 92, 78, 95, 88, 73, 91, 67]

print(f"\nAll Student Marks : {student_marks}")
print(f"Total Students    : {len(student_marks)}")


first_three = student_marks[:3]
print(f"\nFirst 3 Marks     : {first_three}")

last_three = student_marks[-3:]
print(f"Last 3 Marks      : {last_three}")

highest_mark = max(student_marks)
lowest_mark = min(student_marks)
total_marks = sum(student_marks)
average_mark = total_marks / len(student_marks)

print(f"  Highest Mark    : {highest_mark}")
print(f"  Lowest Mark     : {lowest_mark}")
print(f"  Sum of Marks    : {total_marks}")
print(f"  Average Mark    : {average_mark:.2f}")
