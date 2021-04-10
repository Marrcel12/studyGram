from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import SearchForm
# query
from marketplace.models import product, raiting_products, raitings_to_product
from profiles.models import profile, raitings_to_users


def index(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
    else:
        form = SearchForm()

    context = {"form":form}
    # products
    ids_best_review = raiting_products.objects.order_by(
        "value_number").values('id_raiting')[::-1]
    # change here number of best products
    ids_best_review = ids_best_review[:6]

    ids_best_products = []
    for i in ids_best_review:
        ids_best_products.append(
            raitings_to_product.objects.filter(
                id_raiting=i['id_raiting']).values("id_product")[0]["id_product"])

    context["best_products"] = []
    for i in ids_best_products:
        tmp_product = product.objects.filter(product_id=i).values()[0]
        tmp_product['description'] = tmp_product['description'][:300]
        context["best_products"] .append(tmp_product)

    # best 6 products

    # profiles
    id_profiles = raitings_to_users.objects.values()
    uniq_ids = list(set([i["profile_id"] for i in id_profiles.values(
        "profile_id") if i["profile_id"]]))
    ids_number_of_reviews = {}

    for id_user in uniq_ids:
        ids_number_of_reviews[id_user] = id_profiles.filter(
            profile_id=id_user).count()

        # last number in this code means how much users do we need
    ids_popular_users = list(dict(sorted(ids_number_of_reviews.items(),
                                         key=lambda item: item[1], reverse=True)).keys())[:3]

    context["popular_profiles"] = []
    for i in ids_popular_users:
        # TODO: Do we need to check if it is creator??? like is_creator = True in filter?
        tmp_profile = profile.objects.filter(profile_id=i).values()[0]
        tmp_profile['description'] = tmp_profile['description'][:180]
        context["popular_profiles"].append(tmp_profile)

    return render(request, 'landing.html', context)
