from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html', {'on_render': "Hey That is Amazing!"})


def count(request):
    return render(request, "count.html")


def result(request):
    sentence = request.GET['fulltext']
    word_list = sentence.split()
    length_of_sentence = len(word_list)

    word_dict = dict()
    for word in word_list:
        if word not in word_dict.keys():
            word_dict[word] = 1
        else:
            word_dict[word] += 1

    max_used_item = max(word_dict.items(), key=lambda k: k[1])
    print(max_used_item)
    max_used_word = max_used_item[0]
    max_used = max_used_item[1]
    return render(request, "result.html", {'sentence': sentence, 'length_of_sentence': length_of_sentence,
                                           "max_used_word": max_used_word, 'max_used': max_used})
