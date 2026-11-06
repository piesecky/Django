from django.shortcuts import render

def domace(request):
    ulohy = {
        "uloha1": "Dokončiť projekt z programovania",
        "uloha2": "Naučiť sa na test z matematiky",
        "uloha3": "Napísať referát z dejepisu",
    }
    return render(request, 'domace/domace.html', ulohy)
