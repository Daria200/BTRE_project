from django.shortcuts import render, get_object_or_404
from .models import Realtor
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def index(request):
    realtors = Realtor.objects.order_by('-hire_date')
    paginator = Paginator(realtors, 3)
    page = request.GET.get('page')
    page_realtors = paginator.get_page(page)
    context = {'realtors': page_realtors}
    return render(request, 'realtors/realtors.html', context)

def realtor(request,realtor_id):
    realtor=get_object_or_404(Realtor, pk=realtor_id )
    context = {'realtor': realtor}
    return render(request, 'realtors/realtor.html', context)



