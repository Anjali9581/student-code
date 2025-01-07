from django.shortcuts import render, redirect
# Create your views here.

# def index(req):
#     data = "happy children's day"
#     context = {
#         'data':data
#     }
#     # return render(req,'index.html',context)
#     return render(req,'index.html',{'data':data})


# student =[
#         {'name':'swetha','qualification':"b.tech",'gender':'female','age':'22','yop':'2024','course':'pyspiders','skills':'django','mock_rating':'*','dob':'02-1-2002','address':'pungajutta'},
#         {'name':'bhavani','qualification':"b.tech",'gender':'female','age':'21','yop':'2024','course':'pyspiders','skills':'django','mock_rating':'*','dob':'9-7-2003','address':'pungajutta'},
#         {'name':'anjali','qualification':"degree",'gender':'female','age':'19','yop':'2024','course':'pyspiders','skills':'django','mock_rating':'*','dob':'02-12-2004','address':'pungajutta'},
#         {'name':'venamadhuri','qualification':"degree",'gender':'female','age':'24','yop':'2024','course':'pyspiders','skills':'django','mock_rating':'*','dob':'02-1-2000','address':'pungajutta'},
#         {'name':'shiva','qualification':"b.tech",'gender':'male','age':'21','yop':'2024','course':'pyspiders','skills':'puthon','mock_rating':'*','dob':'15-08-2003','address':'pungajutta'},
#         {'name':'akhil','qualification':"degree",'gender':'male','age':'22','yop':'2024','course':'pyspiders','skills':'communication','mock_rating':'*','dob':'10-09-2002','address':'pungajutta'},
#         {'name':'anju','qualification':"degree",'gender':'female','age':'19','yop':'2024','course':'pyspiders','skills':'django','mock_rating':'*','dob':'02-1-2004','address':'pungajutta'},
#         {'name':'uday','qualification':"degree",'gender':'female','age':'19','yop':'2024','course':'pyspiders','skills':'django','mock_rating':'*','dob':'20-1-2004','address':'pungajutta'},
#         {'name':'navya','qualification':"degree",'gender':'female','age':'19','yop':'2024','course':'pyspiders','skills':'django','mock_rating':'*','dob':'02-1-1004','address':'pungajutta'},
#         {'name':'prashanth','qualification':"degree",'gender':'male','age':'24','yop':'2020','course':'pyspiders','skills':'sales','mock_rating':'*','dob':'02-1-2000','address':'pungajutta'},
#         {'name':'srikanth','qualification':"b.tech",'gender':'male','age':'24','yop':'2020','course':'jspiders','skills':'java','mock_rating':'*','dob':'02-1-2000','address':'pungajutta'},
#         {'name':'thriveni','qualification':"degree",'gender':'female','age':'19','yop':'2024','course':'jspiders','skills':'sql','mock_rating':'*','dob':'02-12-2004','address':'pungajutta'},
#         {'name':'swathi','qualification':"b.tech",'gender':'female','age':'22','yop':'2024','course':'jspiders','skills':'web','mock_rating':'*','dob':'02-1-2002','address':'pungajutta'},
#         {'name':'harika','qualification':"b.tech",'gender':'female','age':'21','yop':'2024','course':'jspiders','skills':'java','mock_rating':'*','dob':'9-7-2003','address':'pungajutta'},
#         {'name':'soumya','qualification':"degree",'gender':'female','age':'24','yop':'2024','course':'jspiders','skills':'adv java','mock_rating':'*','dob':'02-1-2000','address':'pungajutta'},
#         {'name':'sagar','qualification':"b.tech",'gender':'male','age':'21','yop':'2024','course':'jspiders','skills':'java','mock_rating':'*','dob':'15-08-2003','address':'pungajutta'},
#         {'name':'malli','qualification':"degree",'gender':'male','age':'22','yop':'2024','course':'jspiders','skills':'communication','mock_rating':'*','dob':'10-09-2002','address':'pungajutta'},
#         {'name':'deepika','qualification':"degree",'gender':'female','age':'19','yop':'2024','course':'jspiders','skills':'django','mock_rating':'*','dob':'02-1-2004','address':'pungajutta'},
#         {'name':'shirisha','qualification':"degree",'gender':'female','age':'19','yop':'2024','course':'jspiders','skills':'django','mock_rating':'*','dob':'20-1-2004','address':'pungajutta'},
#         {'name':'nandhu','qualification':"degree",'gender':'female','age':'19','yop':'2024','course':'jspiders','skills':'django','mock_rating':'*','dob':'02-1-1004','address':'pungajutta'},
#         {'name':'ganesh','qualification':"degree",'gender':'male','age':'24','yop':'2020','course':'jspiders','skills':'sales','mock_rating':'*','dob':'02-1-2000','address':'pungajutta'},
#         {'name':'ram','qualification':"b.tech",'gender':'male','age':'24','yop':'2020','course':'jspiders','skills':'django','mock_rating':'*','dob':'02-1-2000','address':'pungajutta'},
#         {'name':'shyany','qualification':"degree",'gender':'female','age':'19','yop':'2024','course':'prospiders','skills':'sale','mock_rating':'*','dob':'02-12-2004','address':'pungajutta'},
#         {'name':'sharanya','qualification':"b.tech",'gender':'female','age':'22','yop':'2024','course':'prospiders','skills':'communication','mock_rating':'*','dob':'02-1-2002','address':'pungajutta'},
#         {'name':'shoba','qualification':"b.tech",'gender':'female','age':'21','yop':'2024','course':'prospiders','skills':'communication','mock_rating':'*','dob':'9-7-2003','address':'pungajutta'},
#         {'name':'rani','qualification':"degree",'gender':'female','age':'24','yop':'2024','course':'prospiders','skills':'sales','mock_rating':'*','dob':'02-1-2000','address':'pungajutta'},
#         {'name':'rana','qualification':"b.tech",'gender':'male','age':'21','yop':'2024','course':'prospiders','skills':'communication','mock_rating':'*','dob':'15-08-2003','address':'pungajutta'},
#         {'name':'kumar','qualification':"degree",'gender':'male','age':'22','yop':'2024','course':'prospiders','skills':'communication','mock_rating':'*','dob':'10-09-2002','address':'pungajutta'},
#         {'name':'rajitha','qualification':"degree",'gender':'female','age':'19','yop':'2024','course':'prospiders','skills':'communication','mock_rating':'*','dob':'02-1-2004','address':'pungajutta'},
#         {'name':'shivanjali','qualification':"degree",'gender':'female','age':'19','yop':'2024','course':'prospiders','skills':'salec','mock_rating':'*','dob':'20-1-2004','address':'pungajutta'},
#         {'name':'geethanjali','qualification':"degree",'gender':'female','age':'19','yop':'2024','course':'prospiders','skills':'sales','mock_rating':'*','dob':'02-1-1004','address':'pungajutta'},
#         {'name':'prasad','qualification':"degree",'gender':'male','age':'24','yop':'2020','course':'prospiders','skills':'sales','mock_rating':'*','dob':'02-1-2000','address':'pungajutta'},
#         {'name':'rakesh','qualification':"b.tech",'gender':'male','age':'24','yop':'2020','course':'qspiders','skills':'business develop','mock_rating':'*','dob':'02-1-2000','address':'pungajutta'},
#         {'name':'rana','qualification':"b.tech",'gender':'male','age':'21','yop':'2024','course':'qspiders','skills':'communication','mock_rating':'*','dob':'15-08-2003','address':'pungajutta'},
#         {'name':'kumar','qualification':"degree",'gender':'male','age':'22','yop':'2024','course':'qspiders','skills':'communication','mock_rating':'*','dob':'10-09-2002','address':'pungajutta'},
#         {'name':'rajitha','qualification':"degree",'gender':'female','age':'19','yop':'2024','course':'qspiders','skills':'communication','mock_rating':'*','dob':'02-1-2004','address':'pungajutta'},
#         {'name':'shivanjali','qualification':"degree",'gender':'female','age':'19','yop':'2024','course':'qspiders','skills':'salec','mock_rating':'*','dob':'20-1-2004','address':'pungajutta'},
#         {'name':'geethanjali','qualification':"degree",'gender':'female','age':'19','yop':'2024','course':'qspiders','skills':'sales','mock_rating':'*','dob':'02-1-1004','address':'pungajutta'},
#         {'name':'prasad','qualification':"degree",'gender':'male','age':'24','yop':'2020','course':'qspiders','skills':'sales','mock_rating':'*','dob':'02-1-2000','address':'pungajutta'},
#         {'name':'rakesh','qualification':"b.tech",'gender':'male','age':'24','yop':'2020','course':'qspiders','skills':'business develop','mock_rating':'*','dob':'02-1-2000','address':'pungajutta'},
     
#     ]
from .models import Student
students=Student.objects.all()
def index(req):
    # students=Student.objects.all()
    context = {
        # 'name':name,'qualification':qualification,'gendor':gendor,'age':age,'yop':yop,'cours':cours,'skills':skills,'mock_rating':mock_rating,'dob':dob,'address':address,
        'student':students
    }
    return render(req,'index1.html',context)

def py(req):
    context = {
        'student' : students
    }
    return render(req,'py.html',context)

def j(req):
    context = {
        'student' : students
    }
    return render(req,'j.html',context)

def pro(req):
    context = {
        'student' : students
    }
    return render(req,'pro.html',context)

def q(req):
    context = {
        'student' : students
    }
    return render(req,'q.html',context)


def card(req):
    context = {
        'student' : students
    }
    return render(req,'card.html',context)

def pycards(req):
    context = {
        'student' : students
    }
    return render(req,'py_card.html',context)

def jcards(req):
    context = {
        'student' : students
    }
    return render(req,'jcards.html',context)


def procards(req):
    context = {
        'student' : students
    }
    return render(req,'procard.html',context)

def qcards(req):
    context = {
        'student' : students
    }
    return render(req,'qcard.html',context)




def details(req,pk):
    student1 = Student.objects.get(id=pk)
    if req.method == "POST":
        data1.delete()
        return redirect("home")
    context = {
        'student1' : student1
    }
    return render(req,'singledetails.html',context)

def update(req,jk):
    update = True
    student2=Student.objects.get(id=jk)
    if req.method == 'POST':
        name =req.POST.get('name')
        qualification=req.POST.get('qualification')
        gender =req.POST.get('gender')
        age =req.POST.get('age')
        course =req.POST.get('course')
        skills =req.POST.get('skills')
        mock_rating =req.POST.get('mock_rating')

        student2.name = name
        student2.qualification = qualification
        student2.gender = gender
        student2.age = age
        student2.course = course
        student2.skills = skills
        student2.mock_rating = mock_rating
        student2.save()
        print(name,qualification,gender,age,course,skills,mock_rating)
    context = {
        'student2' : student2,
        'update' : update
    }
    return render(req,'edit.html',context)

def create(req):
    update = False
    if req.method == 'POST':
        name =req.POST.get('name')
        qualification=req.POST.get('qualification')
        gender =req.POST.get('gender')
        age =req.POST.get('age')
        course =req.POST.get('course')
        skills =req.POST.get('skills')
        mock_rating =req.POST.get('mock_rating')
        a = Student.objects.create(name=name,qualification=qualification,gender=gender,age=age,course=course,skills=skills,mock_rating=mock_rating)
        print(name,qualification,gender,age,course,skills,mock_rating)
        return redirect("home")
    return render(req,'add.html',{'update':update})
    