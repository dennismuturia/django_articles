from django.shortcuts import render


# Create your views here. Creating now!!
def hello(request):
    my_variable = "Dennis"
    years = 23
    cities_array = ['Nairobi', 'Meru', 'Nyahururu']
    return render(request, 'hello.html', {'my_var':my_variable, 'years':years, 'cities':cities_array})
