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
from django.shortcuts import render, redirect
from .forms import ItemRankingForm

def adicionar_item(request):
    if request.method == "POST":
        form = ItemRankingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('curriculo:ranking')
    else:
        form = ItemRankingForm()

    return render(request, "curriculo/adicionar.html", {"form": form})

from django.shortcuts import get_object_or_404

def editar_item(request, id):
    item = get_object_or_404(ItemRanking, id=id)

    if request.method == "POST":
        form = ItemRankingForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("curriculo:ranking")
    else:
        form = ItemRankingForm(instance=item)

    return render(request, "curriculo/editar.html", {"form": form})
def remover_item(request, id):
    item = get_object_or_404(ItemRanking, id=id)

    if request.method == "POST":
        item.delete()
        return redirect("curriculo:ranking")

    return render(request, "curriculo/remover.html", {"item": item})
