from django.shortcuts import render

# Create your views here.
def prices(request, thing, cnt):
    product_price = {"라면":980,"홈런볼":1500,"칙촉":2300, "식빵":1800}
    if product_price.get(thing):
        result = product_price[thing] * cnt
    else:
        result = "/는 없어용"
    context = {
        "product_price" : product_price,
        "thing" : thing,
        "cnt" : cnt,
        "result" : result
    }
    return render(request, "prices/price.html", context)
