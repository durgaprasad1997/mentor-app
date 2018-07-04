from django.urls import path
from . import backup_views
from . import backup_views
from .views import *
from onlineapp.rest_views import rest_college,rest_student,rest_mark,rest_detailedStudents,rest_specificstudent
from onlineapp.views.auth import *
from django.conf.urls import url
from onlineapp import views
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import obtain_jwt_token,verify_jwt_token



app_name="onlineapp"

urlpatterns = [
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),


    path('api/v2/colleges/', rest_college.college_list),
    path('api/v2/colleges/<int:pk>/', rest_college.college_detail),
    path('api/v2/colleges/<int:pk>/students/',  rest_student.StudentList.as_view()),
    path('api/v2/colleges/<int:college_id>/students/<int:pk>/',  rest_student.StudentDetail.as_view()),


    path('api/v1/colleges/<int:id1>/students/<int:id2>/',rest_specificstudent.detailedstudents_list),


    path('api/v1/detailedstudents/<int:id>/', rest_detailedStudents.detailedstudents_list),
    url(r'^api/v1/marks/$', rest_mark.mark_list),
    url(r'^api/v1/marks/(?P<pk>[0-9]+)/$', rest_mark.mark_detail),

    url(r'^api/v1/students/$', rest_student.student_list),
    url(r'^api/v1/students/(?P<pk>[0-9]+)/$', rest_student.student_detail),

    url(r'^api/v1/colleges/$', rest_college.college_list),
    url(r'^api/v1/colleges/(?P<pk>[0-9]+)/$', rest_college.college_detail),

    path('logout/',logout_view, name="logout"),
    path('login/',LoginView.as_view(),name="login"),
    path('signup/',SignUpView.as_view(),name="signup"),

    path('colleges/',CollegeView.as_view(),name = 'colleges'),

    path('colleges/add_college/', CreateCollegeView.as_view(),name='add_college'),
    path('colleges/<str:Acronym>/add_student/', CreateStudentView.as_view(),name='add_student'),


    path('colleges/<str:Acronym>/',CollegeDetailView.as_view(),name='College_Acronym'),
    path('colleges/<int:pk>/delete/',DeleteCollegeView.as_view(),name='college_delete'),
    path('colleges/<int:pk>/edit/', UpdateCollegeView.as_view(), name='college_edit'),


    path('colleges/<str:Acronym>/<int:pk>/edit/', UpdateStudentView.as_view(), name='student_edit'),

    path('colleges/<str:Acronym>/<int:pk>/delete/',DeleteStudentView.as_view(),name='student_delete'),

    path('exceptionsession/', backup_views.exceptiontest),
    path('testsession/', backup_views.testSession),
    path('studentmarks/', backup_views.queryMarks),
    path('studentdetails/', backup_views.query3),
    path('studentdetails/<int:num>/', backup_views.query3_id),
    path('q2/', backup_views.query2),
    path('q1/', backup_views.query),
    path('game/', backup_views.index),
    path('greet/', backup_views.get),

]