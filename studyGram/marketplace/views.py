import functools
from django.http import HttpResponse
from django.shortcuts import render
from .forms import SearchForm,FilterForm
from django.http import HttpResponseRedirect
from .models import *
from django.db.models import Q
# search


def best_products(number_to_retun, size_of_desc):
            ids_best_review = raiting_products.objects.order_by("value_number").values('id_raiting')[::-1]
            ids_best_review = ids_best_review[:number_to_retun]

            ids_best_products = []
            for i in ids_best_review:
                ids_best_products.append(
                    raitings_to_product.objects.filter(
                        id_raiting=i['id_raiting']).values("id_product")[0]["id_product"])
            to_return=[]
            for i in ids_best_products:
                tmp_product = product.objects.filter(product_id=i).values()[0]
                tmp_product['description'] = tmp_product['description'][:size_of_desc]
                to_return.append(tmp_product)
            return to_return
# Create your views here.
def start(request):
    context = {"search":None}
    context["levels"]=[i for i in level.objects.values('id_level','name')]
    # filter_subject=
    context["subjects"]=[i for i in subject.objects.values('id_subject','name')]
    # filter_topic=
    context["topics"]=[i for i in topic.objects.values('id_topic','name')]
    # phrase text search
    if request.method == 'GET':
        if request.GET['search']:
            search_value=request.GET['search']
            part_string=search_value[:int(len(search_value)/2)]
            search_res = product.objects.filter(
                (Q(title__trigram_similar=search_value)| Q(description__trigram_similar=search_value) | Q( description__contains=part_string) | Q( title__contains=part_string)| Q( tags__contains=part_string)))
            context["search_result"]=best_products(15, 150) #design purposes
            # context["search_result"]=search_res
        else:
            context["search_result"]= best_products(15, 100)
    elif request.method == 'POST':
        print("DEBUG ")
        search_value = request.POST['search']
        context["search_res"] = []
        sting_model= {"level":level,"subject":subject,"topic":topic}
        query={"level": request.POST['levels'] if request.POST['levels'] !="" else None,"subject":request.POST['subjects'] if request.POST['subjects'] !="" else None,"topic":request.POST['topics'] if request.POST['topics']!="" else None}
        
        # level
        product_ids=None
        if None not in list(query.values()):
            id_subject_topic_query=subject_topic.objects.filter(Q(id_topic=query["topic"])&Q(id_subject=query["subject"])).values("id_subject_topic")
            if id_subject_topic_query:
                product_ids_query_res = level_subject_topic_product.objects.filter(Q(id_level=query["level"])&Q(id_subject_topic=id_subject_topic_query[0]["id_subject_topic"])).values("id_product")
                product_ids=[]
                for i in product_ids_query_res:
                    for z in i:
                        product_ids.append(i[z])
            else:
                print("errr")
                context["warning"]="Nie mamy takich notatek"
                return render(request, 'index.html', context) 

            if search_value !="":
                part_string=search_value[:int(len(search_value)/2)]
                search_res = product.objects.filter(
                (Q(title__trigram_similar=search_value)| Q(description__trigram_similar=search_value) | Q( description__contains=part_string) | Q( title__contains=part_string)| Q( tags__contains=part_string)),product_id__in = product_ids)
                
            else:
                  search_res = product.objects.filter(product_id__in = product_ids)
        else:
            search_value=request.GET['search']
            part_string=search_value[:int(len(search_value)/2)]
            search_res = product.objects.filter(
                (Q(title__trigram_similar=search_value)| Q(description__trigram_similar=search_value) | Q( description__contains=part_string) | Q( title__contains=part_string)| Q( tags__contains=part_string)))
        context["search_result"]=search_res
    print(context)
        
      #    TODO: Give contnen  from search_res to contex
    return render(request, 'index.html', context)   
   

    
