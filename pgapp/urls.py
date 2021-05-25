from django.urls import path
from .views import *
from .staffviews import *
from .roomtypeviews import *
from .preferenceviews import *
from .visitorviews import *
from .roomviews import *
from .studentviews import *
from .feeviews import *

urlpatterns = [
    path('',homepageview,name = "homepage"),
    path('login/',loginview,name = "loginpage"),
    path('login/authenticate/',authenticateuser,name = "authenticateuser"),
    path('signup/',signupview,name = "signuppage"),
    path('signup/register/',registeruser,name = "signup"),
    path('logout/',logoutuser,name = "logoutuser"),

    # staff
    path('staff/',staffview,name="staffpage"),
    path('staff/add/save/',addstaff),
    path('staff/add/',addstaffview,name = "addstaffpage"),
    path('staff/<int:id>/delete/',staffdelete),
    path('staff/<int:id>/edit/',staffeditview),
    path('staff/<int:id>/edit/save/',staffedit),

    # room type
    path('roomtype/',roomtypeview,name="roomtypepage"),
    path('roomtype/add/save/',addroomtype),
    path('roomtype/add/',addroomtypeview,name = "addroomtypepage"),
    path('roomtype/<int:id>/delete/',roomtypedelete),

    # preference
    path('preference/',preferenceview,name="preferencepage"),
    path('preference/add/save/',addpreference),
    path('preference/add/',addpreferenceview,name = "addpreferencepage"),
    path('preference/<int:id>/delete/',preferencedelete),

    # room
    path('room/',roomview,name="roompage"),
    path('room/add/save/',addroom),
    path('room/add/',addroomview,name = "addroompage"),
    path('room/<int:id>/delete/',roomdelete),

    # student

    path('student/add/save/',addstudent),
    path('student/add/',addstudentview,name = "addstudentpage"),
    path('student/<int:id>/delete/',studentdelete),
    path('student/<int:id>/edit/',studenteditview),
    path('student/<int:id>/edit/save/',studentedit),
    path('student/<int:id>/detail/',studentdetailview,name = "studentdetailpage"),
    path('student/<int:studentid>/addvisitor/',addvisitor),
    path('visitor/<int:visitorid>/delete/',deletevisitor),
    path('student/<int:studentid>/addfee/',addfee),
    path('fee/<int:feeid>/delete/',deletefee),
    path('student/<int:studentid>/addmessfee/',addmessfee),
    path('messfee/<int:messfeeid>/delete/',deletemessfee),




]