from students import students_tuples, students_dicts
from merge_sort import merge_sort
from quick_sort import quick_sort

# Sort tuples by GPA
sorted_by_gpa = merge_sort(students_tuples, key=lambda x: -x[1])
print("Merge sort by GPA (tuples):", sorted_by_gpa)

# Sort tuples by name
sorted_by_name = quick_sort(students_tuples, key=lambda x: x[0])
print("Quick sort by name (tuples):", sorted_by_name)

# Sort dicts by GPA
sorted_dicts_by_gpa = merge_sort(students_dicts, key=lambda x: -x["gpa"])
print("Merge sort by GPA (dicts):", sorted_dicts_by_gpa)

# Sort dicts by name
sorted_dicts_by_name = quick_sort(students_dicts, key=lambda x: x["name"])
print("Quick sort by name (dicts):", sorted_dicts_by_name)
