from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'index.html')


def result(request):
    print(request)
    student_name = request.GET['name']
    department = request.GET['department']
    blood_group = request.GET['blood_group']
    mobile_number = request.GET['mobile_number']

    student_arr = [{
        "student_name": "praveenkumars",
        "department": "BSc - computerscience",
        "blood_group": "A1B + ve",
        "mobile_number": 123456789
    }, {
        "student_name": "Nirmalkumars",
        "department": 'BSc - computerscience',
        "blood_group": 'B + ve',
        "mobile_number": 1334456789
    }, {
        "student_name": 'Dhoni',
        "department": 'BSc - computerscience',
        "blood_group": 'A1B - ve',
        "mobile_number": 123498787789
    }, {
        "student_name": 'Ramkumar',
        "department": 'BSc - computerscience',
        "blood_group": 'O + ve',
        "mobile_number": 10998560436789
    }, {
        "student_name": student_name,
        "department": department,
        "blood_group": blood_group,
        "mobile_number": mobile_number
    }]

    print(student_arr)
    return render(request, 'result.html', {"result": student_arr})
