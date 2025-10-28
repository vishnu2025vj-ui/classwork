from django.shortcuts import render

# Hardcoded student data (no database)
STUDENTS = {
    'Alice': 'A+',
    'Bob': 'B',
    'Charlie': 'A',
    'David': 'C+',
}

def homepage(request):
    students = STUDENTS.keys()  # get all names
    return render(request, 'homepage.html', {'students': students})

def view_result(request, student_name):
    result = STUDENTS.get(student_name, 'Result not found')
    return render(request, 'result.html', {
        'student_name': student_name,
        'result': result
    })
