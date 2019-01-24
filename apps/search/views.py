from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from apps.index.models import Shop


@csrf_exempt
def search(request):
    q = request.GET.get('keywords')
    if q:
        shops = Shop.objects.filter(name__icontains=q)
        if shops:
            for shop in shops:
                shop.img = shop.shopimage_set.values_list('img_url', flat=True).first()
            return render(request, 'page_search.html', {'shops': shops})
        else:
            return HttpResponse(404)
    else:
        return HttpResponse(404)
