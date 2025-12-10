from django.shortcuts import render
from .models import ItemRanking

def curriculo_spiff(request):
    dados = {
        "nome": "Eduardo Ruthiele",
        "cargo": "Estudante de Ciência da Computação",
        "email": "eduardo@email.com",
        "cidade": "São Paulo - SP",
        "sobre": "Sou estudante de Ciência da Computação, com interesse em desenvolvimento web e programação.",
        "habilidades": [
            "Python",
            "Django",
            "HTML",
            "CSS",
            "Git e GitHub"
        ],
        "experiencias": [
            "Projeto acadêmico com Django",
            "Desenvolvimento de páginas web",
            "Lógica de programação"
        ]
    }
    return render(request, "curriculo/curriculo-v1.html", dados)


def curriculo_spiff_v2(request):
    return render(request, "curriculo/curriculo-v2.html")


def ranking(request):
    itens = ItemRanking.objects.all()
    return render(request, "curriculo/ranking.html", {
        "itens": itens
    })
