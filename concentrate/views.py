from django.shortcuts import render, redirect
from . import player

player = player.player0()

def concentrate(request):
    return render(request, 'concentrate/concentrate.html', {'board':""})

def search(request):
    board = request.POST['board']
    need = request.POST['need']
    notl = request.POST['not']
    colors = request.POST['colors']
    if len(board) < 25:
        return render(request, 'concentrate/concentrate.html', {'board':board, 'need':need, 'not':notl})
    if (not need and not notl):
        return redirect('results/'+board.lower())    
    elif (not need and notl):
        return redirect('results1/'+board.lower()+'/'+notl.lower())
    elif (need and not notl):
        return redirect('results2/'+board.lower()+'/'+need.lower())
    elif (need and notl):
        return redirect('results3/'+board.lower()+'/'+need.lower()+'/'+notl.lower())
    

def results(request, board):
    word_list = sorted(player.concentrate(board, "", "", ""))
    return render(request, 'concentrate/concentrate.html', {'word_list':word_list,'board':board, 'need':"", 'not':""})

def results1(request, board, notl):
    word_list = sorted(player.concentrate(board, "", notl, ""))
    return render(request, 'concentrate/concentrate.html', {'word_list':word_list,'board':board, 'need':"", 'not':notl})

def results2(request, board, need):
    word_list = sorted(player.concentrate(board, need, "", ""))
    return render(request, 'concentrate/concentrate.html', {'word_list':word_list,'board':board, 'need':need, 'not':""})

def results3(request, board, need, notl):
    word_list = sorted(player.concentrate(board, need, notl, ""))
    return render(request, 'concentrate/concentrate.html', {'word_list':word_list,'board':board, 'need':need, 'not':notl})