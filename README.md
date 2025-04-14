

# Assignment Overview

In this assignment, you will implement two classic sorting algorithms
— **Merge Sort** and **Quick Sort** — and use them to sort student
records. This will help reinforce your understanding of recursion,
conditionals, and working with structured data like tuples and
dictionaries.


# Learning Objectives

-   Implement Merge Sort and Quick Sort in Python
-   Sort a list of student records by name and by GPA
-   Understand stability and differences in sorting algorithms
-   Practice working with tuples and dictionaries


# Requirements

You must:

1.  Implement \`merge<sub>sort</sub>()\` and \`quick<sub>sort</sub>()\` to sort lists of:
    -   Student **tuples**: \`("Name", GPA)\`
    -   Student **dicts**: \`{"name": "Alice", "gpa": 3.9}\`
2.  Sort students by:
    -   Name (alphabetically)
    -   GPA (descending)


# 📁 Suggested File Structure

    .
    ├── merge_sort.py         ← Your merge sort implementation
    ├── quick_sort.py         ← Your quick sort implementation
    ├── sort_demo.py          ← Test script to demonstrate sorting
    ├── students.py           ← Sample data and utility functions
    └── student_sort_assignment.org  ← This assignment


# 🧮 Example Student Data

    students_tuples = [
        ("Alice", 3.9),
        ("Bob", 3.4),
        ("Charlie", 3.6),
        ("Diana", 3.4)
    ]
    
    students_dicts = [
        {"name": "Alice", "gpa": 3.9},
        {"name": "Bob", "gpa": 3.4},
        {"name": "Charlie", "gpa": 3.6},
        {"name": "Diana", "gpa": 3.4}
    ]


# 🚀 Starter Code for Merge Sort

    def merge_sort(data, key=lambda x: x):
        if len(data) <= 1:
            return data
        mid = len(data) // 2
        left = merge_sort(data[:mid], key)
        right = merge_sort(data[mid:], key)
        return merge(left, right, key)
    
    def merge(left, right, key):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if key(left[i]) <= key(right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result


# 🚀 Starter Code for Quick Sort

    def quick_sort(data, key=lambda x: x):
        if len(data) <= 1:
            return data
        pivot = data[0]
        lesser = [x for x in data[1:] if key(x) <= key(pivot)]
        greater = [x for x in data[1:] if key(x) > key(pivot)]
        return quick_sort(lesser, key) + [pivot] + quick_sort(greater, key)


# 🧪 Demonstration Script

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


# 📌 Notes

-   You can use \`key\` functions to control sort criteria (like in \`sorted()\`).
-   Try adding new student entries and test again.
-   Consider testing the stability of your sort on repeated GPAs.


# ✅ What to Submit

-   Your \`.py\` files: \`merge<sub>sort.py</sub>\`, \`quick<sub>sort.py</sub>\`, \`students.py\`, \`sort<sub>demo.py</sub>\`
-   A short reflection: Which sort is easier to write and why?


# 💡 Bonus Challenge

Compare runtime for large randomly generated student lists (e.g.,
1000+ entries). Use the \`time\` module.

