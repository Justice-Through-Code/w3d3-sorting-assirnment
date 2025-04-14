

# 📚 Assignment Overview

In this assignment, you will implement two classic sorting algorithms
— **Merge Sort** and **Quick Sort** — and use them to sort student
records. This will help reinforce your understanding of recursion,
conditionals, and working with structured data like tuples and
dictionaries.


# 🎯 Learning Objectives

-   Implement Merge Sort and Quick Sort in Python
-   Sort a list of student records by name and by GPA
-   Understand stability and differences in sorting algorithms
-   Practice working with tuples and dictionaries


# 🔧 Requirements

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


# 🧑‍🎓 Example Student Data

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
        """Sort the data using merge sort.
        Args:
            data (list): The list to sort.
            key (function): A function that returns a value to compare.
        Returns:
            list: A sorted list.
        """
        # TODO: Implement merge sort
        pass


# 🚀 Starter Code for Quick Sort

    def quick_sort(data, key=lambda x: x):
        """Sort the data using quick sort.
        Args:
            data (list): The list to sort.
            key (function): A function that returns a value to compare.
        Returns:
            list: A sorted list.
        """
        # TODO: Implement quick sort
        pass


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
-   A short reflection: Which sort was easier to write and why?


# 🧪 Testing Your Code

-   From your project root directory, run:
    
        python -m unittest discover -s tests


# 💡 Bonus Challenge

Compare runtime for large randomly generated student lists (e.g.,
1000+ entries). Use the \`time\` module and compare Merge Sort and Quick Sort performance.

