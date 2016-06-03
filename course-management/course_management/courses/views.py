from django.shortcuts import render
from .models import Course, Lecture
from .helpers import calc_duration


def lectures(request):
    lectures = []
    for elem in Lecture.objects.all():
        lectures.append(elem)
    return render(request, "lectures.html", locals())


def get_lecture(request):
    request_lect_id = int(request.path.split('/')[-1])
    if request.method == "GET":
        lectures = [Lecture.objects.get(lection_id=request_lect_id)]
        return render(request, "lectures.html", locals())


def has_course(course_name):
    return Course.objects.filter(name=course_name)


def change_lecture(request):
    course = request.POST.get('course')
    if not has_course(course):
        error = "We don't have such course!!"
        return render(request, 'new_lecture.html', locals())
    lecture = Lecture(name=request.POST.get('name'),
                      week=request.POST.get('week'),
                      course=Course.objects.get(name=course),
                      url=request.POST.get('url'))
    lecture.save()
    return lecture


def edit_lecture(request):
    request_lect_id = int(request.path.split('/')[-1])
    lecture = Lecture.objects.get(lection_id=request_lect_id)
    if request.method == 'GET':
        return render(request, "edit_lecture.html", locals())
    if request.method == 'POST':
        new_lecture = change_lecture(request)
        lecture.delete()
        return render(request, "editted_lecture.html", locals())


def new_lecture(request):
    if request.method == 'POST':
        lecture = change_lecture(request)
    return render(request, 'new_lecture.html', locals())


def home(request):
    list_with_fields = []
    for elem in Course.objects.all():
        list_with_fields.append(elem)
    return render(request, 'home.html', locals())


def go_to_course(request):
    req_name = request.path.split('/')[-1]
    list_with_fields = Course.objects.filter(name=req_name)
    return render(request, 'home.html', locals())


def get_POST_attributes(request):
    name = request.POST.get('name')
    description = request.POST.get('description')
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')
    approximation = calc_duration(start_date, end_date)

    return name, description, start_date, end_date, approximation


def course_edit(request):
    req_name = request.path.split('/')[-1]
    field = Course.objects.get(name=req_name)
    if request.method == "GET":
        return render(request, 'edit_course.html', locals())
    if request.method == "POST":
        name, description, start_date, end_date, approximation = get_POST_attributes(request)
        Course.objects.filter(name=req_name).\
            update(name=name,
                   description=description,
                   start_date=start_date,
                   end_date=end_date,
                   approximation=approximation)
        return home(request)


def create_new_course(request):
    if request.method == 'POST':
        name, description, start_date, end_date, approximation = get_POST_attributes(request)
        u = Course(name=name,
                   description=description,
                   start_date=start_date,
                   end_date=end_date,
                   approximation=approximation)
        u.save()
    return render(request, 'new_course.html', locals())
