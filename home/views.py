from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
#def home(request):
#    return HttpResponse("<h1>Hey iam a Django server.</h1>")

#def home(request):
#    return render(request, "index.html")

def home(request):

    peoples =[
        {'name' : 'Likhith' , 'age' :19},
        {'name' : 'Mahesh Babu' , 'age' :47},
        {'name' : 'Ram Charan' , 'age' :38},
        {'name' : 'MSD' , 'age' :45},
    ]

    text = """👨‍💻 About Me:
                Embarking on my 2nd-year journey in B-Tech Computer Science and Engineering with a focus on Artificial Intelligence and Machine Learning. I thrive on exploring, learning, and innovating in the dynamic world of technology.
                """
    
    vegetables = ['potato','brinjal','tomato','onion']




    return render(request, "index.html" ,context={'page':'Home page','peoples' : peoples , 'text' : text , 'vegetables' : vegetables} )

#def success_page(request):
#    return HttpResponse("""<h1>This is success page!</h1>
#    <p>djkcndsjcnjdsncjsdnciusdncdjcbnudbcudsbc hdsc</p>
#    <hr>
#    <p>dhbcnjdncuidncdncmomcicniweucn</p>
#    """)

def about(request):
    context={'page':'About'}
    return render(request, "about.html",context)

def contact(request):
    context={'page':'Contact'}
    return render(request, "contact.html",context)


