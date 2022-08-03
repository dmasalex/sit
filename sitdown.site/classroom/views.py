import ast
from datetime import datetime

from django.contrib.auth import login, logout
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .forms import SchoolboyForm, UserLoginForm
from .functions import create_lst_boys
from .models import Classroom, Location, Schoolboy, Teacher


def print_location(request, pk):
    location = Location.objects.get(id=pk)
    dict_boy = {}
    dict_loc = eval(location.position)

    for key, value in dict_loc.items():
        lst = []
        for row in value:
            boy = Schoolboy.objects.get(slug=row)
            lst.append(boy.name)
        dict_boy[key] = lst

    return render(request, "classroom/print_location.html", dict_boy)


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("schoolboy")
    else:
        form = UserLoginForm()
    return render(request, "classroom/login.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("login")


def location(request, slug):
    classroom = Classroom.objects.get(slug=slug)
    teachers = Teacher.objects.filter(classroom__slug=slug)
    dict_loc = {}

    boys_one_plus = list(
        Schoolboy.objects.filter(
            classroom__slug=slug, gender__name="Мальчик", requirement__name="1+"
        )
    )
    girls_one_plus = list(
        Schoolboy.objects.filter(
            classroom__slug=slug, gender__name="Девочка", requirement__name="1+"
        )
    )
    boys_one = list(
        Schoolboy.objects.filter(
            classroom__slug=slug, gender__name="Мальчик", requirement__name="1"
        )
    )
    girls_one = list(
        Schoolboy.objects.filter(
            classroom__slug=slug, gender__name="Девочка", requirement__name="1"
        )
    )
    boys_two_plus = list(
        Schoolboy.objects.filter(
            classroom__slug=slug, gender__name="Мальчик", requirement__name="2+"
        )
    )
    girls_two_plus = list(
        Schoolboy.objects.filter(
            classroom__slug=slug, gender__name="Девочка", requirement__name="2+"
        )
    )
    boys_two = list(
        Schoolboy.objects.filter(
            classroom__slug=slug, gender__name="Мальчик", requirement__name="2"
        )
    )
    girls_two = list(
        Schoolboy.objects.filter(
            classroom__slug=slug, gender__name="Девочка", requirement__name="2"
        )
    )
    boys_three_plus = list(
        Schoolboy.objects.filter(
            classroom__slug=slug, gender__name="Мальчик", requirement__name="3+"
        )
    )
    girls_three_plus = list(
        Schoolboy.objects.filter(
            classroom__slug=slug, gender__name="Девочка", requirement__name="3+"
        )
    )
    boys_three = list(
        Schoolboy.objects.filter(
            classroom__slug=slug, gender__name="Мальчик", requirement__name="3"
        )
    )
    girls_three = list(
        Schoolboy.objects.filter(
            classroom__slug=slug, gender__name="Девочка", requirement__name="3"
        )
    )
    boys = list(
        Schoolboy.objects.filter(
            classroom__slug=slug, gender__name="Мальчик", requirement__name="-"
        )
    )
    girls = list(
        Schoolboy.objects.filter(
            classroom__slug=slug, gender__name="Девочка", requirement__name="-"
        )
    )

    desk_1, desk_2, desk_3, desk_4, desk_5, desk_6 = create_lst_boys(
        boys_one,
        girls_one,
        boys_one_plus,
        girls_one_plus,
        boys_two,
        girls_two,
        boys_two_plus,
        girls_two_plus,
        boys_three,
        girls_three,
        boys_three_plus,
        girls_three_plus,
        boys,
        girls,
    )

    context = {
        "desk_1": desk_1,
        "desk_2": desk_2,
        "desk_3": desk_3,
        "desk_4": desk_4,
        "desk_5": desk_5,
        "desk_6": desk_6,
        "classroom": classroom,
        "teachers": teachers,
    }
    d_1, d_2, d_3, d_4, d_5, d_6 = [], [], [], [], [], []
    for name in desk_1:
        d_1.append(str(name.slug))
    dict_loc["desk_1"] = d_1

    for name in desk_2:
        d_2.append(str(name.slug))
    dict_loc["desk_2"] = d_2

    for name in desk_3:
        d_3.append(str(name.slug))
    dict_loc["desk_3"] = d_3

    for name in desk_4:
        d_4.append(str(name.slug))
    dict_loc["desk_4"] = d_4

    for name in desk_5:
        d_5.append(str(name.slug))
    dict_loc["desk_5"] = d_5

    for name in desk_6:
        d_6.append(str(name.slug))
    dict_loc["desk_6"] = d_6

    location = Location(classroom=classroom, position=dict_loc)
    location.save()
    context["pk"] = location.pk

    return render(request, "classroom/location.html", context=context)


def boy_location_update(request, slug):
    boy = Schoolboy.objects.get(slug=slug)
    classroom = Classroom.objects.get(name=boy.classroom)
    # location = Location.objects.filter()
    print(classroom)
    # найти локацию последнюю

    context = {}
    return render(request, "classroom/location_update.html", context=context)


def location_update(request, pk):
    context = {}
    classroom = Location.objects.get(pk=pk)
    context["classroom"] = classroom
    dict_location = ast.literal_eval(classroom.position)
    context["pk"] = pk
    for key, value in dict_location.items():
        tmp = []
        for name in value:
            boy = Schoolboy.objects.get(slug=name)
            tmp.append(boy)
        context[key] = tmp

    return render(request, "classroom/location_update.html", context=context)


def location_now(request, pk):
    location = Location.objects.get(pk=pk)
    dict_location = ast.literal_eval(location.position)
    context = {}
    for key, value in dict_location.items():
        tmp = []
        for name in value:
            boy = Schoolboy.objects.get(slug=name)
            tmp.append(boy)
        context[key] = tmp
    context["teachers"] = Teacher.objects.filter(classroom__slug=boy.classroom.slug)
    context["classroom"] = Classroom.objects.get(slug=boy.classroom.slug)
    context["pk"] = pk

    return render(request, "classroom/location_now.html", context=context)


def location_save(request, slug):
    now = datetime.now()
    try:
        location_last = Location.objects.filter(
            classroom__slug=slug, save_bd=True
        ).latest("create_data")
        location_last.end_data = now
        location_last.save()
    except Exception as e:
        print(e)
    location = Location.objects.filter(classroom__slug=slug).latest("create_data")
    location.save_bd = True
    location.save()
    Location.objects.filter(classroom__slug=slug, save_bd=False).delete()
    return redirect("schoolboy")


class TeacherDetail(DetailView):
    model = Teacher
    template_name = "classroom/teacher_detail.html"


class SchoolboyCreate(CreateView):
    form_class = SchoolboyForm
    template_name = "classroom/schoolboy_create.html"


class SchoolboyUpdate(UpdateView):
    model = Schoolboy
    form_class = SchoolboyForm
    template_name = "classroom/schoolboy_update.html"


class SchoolboyDelete(DeleteView):
    model = Schoolboy
    template_name = "classroom/schoolboy_delete.html"
    success_url = reverse_lazy("schoolboy")


class SchoolboyListView(ListView):
    model = Location
    template_name = "classroom/index.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        rooms = Classroom.objects.all()
        classroom_lst = []
        classroom_last = Location.objects.filter(save_bd=True)
        try:
            for room in rooms:
                classroom_lst.append(
                    Location.objects.filter(save_bd=True, classroom__name=room).latest(
                        "create_data"
                    )
                )
        except Exception as e:
            print("exception", e)
        context["classroom"] = classroom_lst
        context["classroom_last"] = classroom_last
        return context


class ClassroomDetailView(DetailView):
    model = Classroom
    template_name = "classroom/classroom_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["teachers"] = Teacher.objects.filter(classroom=self.object.id)
        context["schoolboy"] = Schoolboy.objects.filter(classroom=self.object.id)
        return context


class ClassroomListView(ListView):
    model = Classroom
    template_name = "classroom/classroom.html"
    allow_empty = False


class SchoolboyDetailView(DetailView):
    model = Schoolboy
    template_name = "classroom/schoolboy_detail.html"
