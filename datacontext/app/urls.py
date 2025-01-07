from django.urls import path
from . import views
# from .views import *
# from .views import index

urlpatterns = [
    path('',views.index,name='home'),
    path('py',views.py,name='py'),
    path('j',views.j,name='j'),
    path('pro',views.pro,name='pro'),
    path('q',views.q,name='q'),
    path('cards',views.card,name='cards'),
    path('pycards',views.pycards,name='pycards'),
    path('jcards',views.jcards,name='jcards'),
    path('procards',views.procards,name='procards'),
    path('qcards',views.qcards,name='qcards'),

    path('1/<int:pk>',views.details,name='display'),
    path('2/<int:jk>',views.update,name='edit'),
    path('add',views.create,name="add")

]