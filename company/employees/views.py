from django.shortcuts import render

def employee_list(request):
    
    employees = [
        {"name": "vishnu", "title": "Software Engineer", "salary": 60000, "full_time": True},
        {"name": "adhi", "title": "Designer", "salary": 40000, "full_time": False},
        {"name": "ashik", "title": "Manager", "salary": 80000, "full_time": True},
    ]


    return render(request, 'employee_list.html', {'employees': employees})
