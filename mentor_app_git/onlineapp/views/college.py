from django.views import View
from django.shortcuts import render,get_object_or_404,redirect
from onlineapp.models import Colleges,Student,Marks
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from onlineapp.forms.colleges_forms import *
from onlineapp.forms.student_form import *
from onlineapp.forms.marks_form import *
from django.urls import *
from django.contrib.auth.mixins import LoginRequiredMixin


#django123

class CollegeView(LoginRequiredMixin,View):
    login_url = 'onlineapp:login'
    def get(self,request,*args,**kwargs):
        colleges = Colleges.objects.values('id' ,'Name', 'Acronym')
        #colleges = Colleges.objects.all()
        #import ipdb
        #ipdb.set_trace()
        pass

        return render(
            request,

            template_name='college.html',
            context = {
                'colleges': colleges,
                'user_permissions': self.request.user.get_all_permissions
            }
        )

class CollegeListView(LoginRequiredMixin,ListView):
    login_url = 'onlineapp:login'
    model=Colleges
    context_object_name='colleges'
    def get_context_data(self,*,object_list=None,**kwargs):
        c= super(CollegeListView,self).get_context_data(**kwargs)

        return c


class CollegeDetailView(LoginRequiredMixin,DetailView):
    login_url = 'onlineapp:login'
    model=Colleges
    context_object_name = 'colleges'
    template_name = 'student.html'

    def get_object(self,queryset=None):
        return get_object_or_404(Colleges,**self.kwargs)

    def get_context_data(self, **kwargs):
        context=super(CollegeDetailView,self).get_context_data(**kwargs)

        college=context.get('colleges')

        students = list(college.student_set.values('id','Name','Email_id','marks__Total').order_by("-marks__Total"))



        context.update({
        'colleges':students,
        'user_permission':self.request.user.get_all_permissions
        })

        return context

class CreateCollegeView(LoginRequiredMixin,CreateView):
    login_url = 'onlineapp:login'
    model = Colleges
    form_class = AddCollege
    template_name = 'college_form.html'
    success_url = reverse_lazy('onlineapp:colleges')




class CreateStudentView(LoginRequiredMixin,CreateView):
    login_url = 'onlineapp:login'
    model = Student
    form_class = StudentForm
    template_name = 'student_form.html'
    success_url = reverse_lazy('onlineapp:colleges')

    def get_context_data(self, **kwargs):
        context = super(CreateStudentView, self).get_context_data(**kwargs)
        test_form = MockTestForm()
        context.update({
            'student_form': context.get('form'),
            'test_form': test_form,
            'user_permission': self.request.user.get_all_permissions
        })
        return context

    def post(self, request, *args, **kwargs):


        priamry=Colleges.objects.values('id').order_by(kwargs.get('college_Acronym'))

        college = get_object_or_404(Colleges, pk=priamry[0])
        #college = get_object_or_404(Colleges, pk=kwargs.get('college_Acronym'))

        student_form = StudentForm(request.POST)
        test_form = MockTestForm(request.POST)

        if student_form.is_valid():
            student = student_form.save(commit=False)
            student.Colleges = college
            student.save()

            if test_form.is_valid():
                score = test_form.save(commit=False)
                score.Total = sum(test_form.cleaned_data.values())
                score.student = student
                score.save()


class DeleteCollegeView(LoginRequiredMixin,DeleteView):
    login_url = 'onlineapp:login'
    model=Colleges
    template_name="delete_college.html"
    success_url=reverse_lazy('onlineapp:colleges')



class DeleteStudentView(LoginRequiredMixin,DeleteView):
    login_url = 'onlineapp:login'
    model=Student
    template_name="delete_student.html"
    success_url=reverse_lazy('onlineapp:colleges')




class UpdateCollegeView(LoginRequiredMixin,UpdateView):
    login_url = 'onlineapp:login'
    model = Colleges
    form_class = UpdateCollegeForm
    template_name = 'updatecollege_form.html'
    success_url = reverse_lazy('onlineapp:colleges')


    def get_object(self, queryset=None):
        return get_object_or_404(Colleges, **{'pk': self.kwargs.get('pk')})


    def get_context_data(self, **kwargs):
        context = super(UpdateCollegeView, self).get_context_data(**kwargs)
        college = context.get('colleges')
        students = list(college.student_set.order_by('-marks__Total'))

        context.update({
            'students': students,
            'user_permission': self.request.user.get_all_permissions
        })
        return context




class UpdateStudentView(LoginRequiredMixin,UpdateView):
    login_url = 'onlineapp:login'
    model = Student
    form_class = UpdateStudentForm
    template_name = 'updatestudent_form.html'

    def get_context_data(self, **kwargs):
        context = super(UpdateStudentView, self).get_context_data(**kwargs)
        student_form = context.get('student')
        test_form = UpdateMockTestForm(instance=student_form.marks)
        context.update({
            'student_form': context.get('form'),
            'test_form': test_form,
            'user_permission': self.request.user.get_all_permissions
        })

        return context

    def post(self, request, *args, **kwargs):
        student = Student.objects.get(pk=kwargs.get('pk'))
        form = UpdateStudentForm(request.POST, instance=student)
        test_form = UpdateMockTestForm(request.POST, instance=student.marks)
        test = test_form.save(commit = False)
        test.Total = sum(test_form.cleaned_data.values())
        form.save()
        test.save()
        return redirect("onlineapp:colleges")

