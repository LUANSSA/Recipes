from django.shortcuts import render

# Create your views here.

def Home(request):

    recipes = range(1, 5)

    return render(request, "recipes/pages/home.html", context={
        "numeros": recipes,
        "is_detail_page": False,
    })


def Recipes_Detalhe(request, id):
    
    return render(request, "recipes/pages/recipes_detalhe.html", context={
        "numeros" : "1",
        "is_detail_page": True,
    })