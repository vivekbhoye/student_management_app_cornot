from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Book,School,Student
from django.views.generic import CreateView,ListView,DetailView
from django.db.models import Q
# Create your views here.
# class HomeView(CreateView)

# class StudentCreateView(ListView):
#     model = Student
#     fields = ['first_name','last_name','email','gender','school','books']
#     template_name = "studentmanagementapp/home.html"

def homeview(request):
    # student = Student.objects.all()

    # context ={
    #     'student' : student
    # }

    return render(request,'studentmanagementapp/home.html')


class StudentDetailView(DetailView):
    model = Student
    template_name = "studentmanagementapp/student_detail.html"


class StudentCreateView(CreateView):
    model = Student
    fields ='__all__'
    template_name = "studentmanagementapp/student_create.html"
    # success_url = reverse_lazy('student-detail')

class SchoolCreateView(CreateView):
    model = School
    fields ='__all__'
    template_name = "studentmanagementapp/school_create.html"


class BookCreateView(CreateView):
    model = Book
    fields ='__all__'
    template_name = "studentmanagementapp/book_create.html"

class Search(ListView):
    model = Student
    template_name = "studentmanagementapp/search.html"
    context_object_name = 'all_search_results'

    def get_queryset(self) :
        result = super(Search,self).get_queryset()
        name_query = self.request.GET.get('search_student_name')
        id_query = self.request.GET.get('search_student_id')
        if id_query:
            id_result = Student.objects.filter(id=id_query)
            if id_result:
                # print("id")
                # print(id_result)
                return id_result

        elif name_query:
            name_result = Student.objects.filter(Q(first_name__contains=name_query) | Q(last_name__contains=name_query))
            if name_result:
                # print("name")
                # print(name_result)
                return name_result

        else:
            # print("postresult 22")
            result = None
            return result

    
