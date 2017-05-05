from django.shortcuts import render, redirect
from . import player

player = player.player0()

def concentrate(request):
    return render(request, 'concentrate/concentrate.html', {'board':""})

def search(request):
    board = request.POST['board']
    need = request.POST['need']
    notl = request.POST['not']
    anyl = request.POST['any']
    colors = request.POST['colors']
    print(colors)
    if len(board) < 25:
        return render(request, 'concentrate/concentrate.html', {'board':board, 'need':need, 'not':notl, 'any':anyl})
    return redirect('results/'+board.lower()+'/'+need.lower()+'/'+notl.lower()+'/'+anyl.lower())

def results(request, board, need, notl, anyl):
    word_list = sorted(player.concentrate(board, need, notl, anyl))
    return render(request, 'concentrate/concentrate.html', {'word_list':word_list,'board':board, 'need':need, 'not':notl, 'any':anyl})
