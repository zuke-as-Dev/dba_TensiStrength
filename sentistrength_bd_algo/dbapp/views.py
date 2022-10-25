from django.shortcuts import render
from .dbalgo_logic import single_function

def index(request):
    return render(request, 'index.html')

def counter(request):
    text = request.POST['text']
    new_words_rated = single_function.super_function(str(text))
    new_words = single_function.word(text)
    psy_words = single_function.psy_f(text)
    context={
        'db_list':new_words_rated,
        'db_words':new_words,
        'psy':psy_words,
        'dl_len':len(new_words_rated),
        'dw_len':len(new_words)
    }
    return render(request, 'output.html',context)
# Create your views here.
