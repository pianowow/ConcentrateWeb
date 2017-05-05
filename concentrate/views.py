from django.shortcuts import render, redirect
from . import player

player = player.player0()

def concentrate(request):
    return render(request, 'concentrate/concentrate.html', {'board':"", 'colors':'W'*25})

def search(request):
    board = request.POST['board']
    need = request.POST['need']
    notl = request.POST['not']
    colors = request.POST['colors']
    if len(board) < 25:
        return render(request, 'concentrate/concentrate.html', {'board':board, 'colors':colors, 'need':need, 'not':notl})
    if (not need and not notl):
        return redirect('results/'+board.lower() + '/' + colors.lower())    
    elif (not need and notl):
        return redirect('results1/'+board.lower()+ '/' + colors.lower() +'/'+notl.lower())
    elif (need and not notl):
        return redirect('results2/'+board.lower()+ '/' + colors.lower() +'/'+need.lower())
    elif (need and notl):
        return redirect('results3/'+board.lower()+ '/' + colors.lower() +'/'+need.lower()+'/'+notl.lower())
    

def results(request, board, colors):
    plays = player.decide(board, colors, "", "", 1)
    plays.sort(reverse=True, key=lambda x: (x[0],len(x[1])))
    return render(request, 'concentrate/concentrate.html', {'plays':plays,'board':board, 'colors':colors, 'need':"", 'not':""})

def results1(request, board, colors, notl):
    plays = player.decide(board, colors, "", notl, 1)
    plays.sort(reverse=True, key=lambda x: (x[0],len(x[1])))
    return render(request, 'concentrate/concentrate.html', {'plays':plays,'board':board, 'colors':colors, 'need':"", 'not':notl})

def results2(request, board, colors, need):
    plays = player.decide(board, colors, need, "", 1)
    plays.sort(reverse=True, key=lambda x: (x[0],len(x[1])))
    return render(request, 'concentrate/concentrate.html', {'plays':plays,'board':board, 'colors':colors, 'need':need, 'not':""})

def results3(request, board, colors, need, notl):
    plays = player.decide(board, colors, need, notl, 1)
    plays.sort(reverse=True, key=lambda x: (x[0],len(x[1])))
    return render(request, 'concentrate/concentrate.html', {'plays':plays,'board':board, 'colors':colors, 'need':need, 'not':notl})