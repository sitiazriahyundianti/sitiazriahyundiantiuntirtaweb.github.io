from django.shortcuts import render

# Create your views here.
def faperta(request):
    judul = "Akademik"
    s1 = ["Program Studi S-1", "Program Studi S-2"]

    konteks = {
        'title': judul,
        's1': s1,
    }
    return render(request, 'faperta.html', konteks)
