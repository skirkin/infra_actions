from django.http import HttpResponse


def index(request):
    return HttpResponse('РЈ РјРµРЅСЏ РїРѕР»СѓС‡РёР»РѕСЃСЊ!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
