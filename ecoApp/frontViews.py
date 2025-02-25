from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from ecoApp.models import Product


def saree_view(request):
    sarees = Product.objects.filter(Sub_Category='Sarees')
    context = {
        'sarees': sarees
    }
    return render(request, 'saree_list.html', context)


def saree_detail(request, pk):
    saree = get_object_or_404(Product, pk=pk)
    context = {
        'saree': saree
    }
    return render(request, 'saree_detail.html', context)


def kurta_view(request):
    kurtas = Product.objects.filter(Sub_Category='Kurta&Kurtis')
    context = {
        'kurtas': kurtas
    }
    return render(request, 'kurta_list.html', context)

def kurta_detail(request, pk):
    kurtas = get_object_or_404(Product, pk=pk)
    context = {
        'kurtas': kurtas
    }
    return render(request, 'kurta_detail.html', context)

def gown_view(request):
    gowns = Product.objects.filter(Sub_Category='Gowns')
    context = {
        'gowns': gowns
    }
    return render(request, 'gown_list.html', context)


def gown_detail(request, pk):
    gowns = get_object_or_404(Product, pk=pk)
    context = {
        'gown': gowns
    }
    return render(request, 'gown_detail.html', context)



def top_view(request):
    top = Product.objects.filter(Sub_Category='Topwear')
    context = {
        'top': top
    }
    return render(request, 'top_list.html', context)

def top_detail(request, pk):
    top = get_object_or_404(Product, pk=pk)
    context = {
        'top': top
    }
    return render(request, 'top_detail.html', context)

def shirt_view(request):
    shirts = Product.objects.filter(Q(Sub_Category = 'CShirts') | Q(Sub_Category = 'FShirts'))
    context = {
        'shirts': shirts
    }
    return render(request, 'shirt_list.html', context)


def shirt_detail(request, pk):
    shirts = get_object_or_404(Product, pk=pk)
    context = {
        'shirts': shirts
    }
    return render(request, 'shirt_detail.html', context)



def mjeans_view(request):
    jeans = Product.objects.filter(Sub_Category='MJeans')
    context = {
        'jeans': jeans
    }
    return render(request, 'mjeans_list.html', context)

def mjeans_detail(request,pk):
    jeans = get_object_or_404(Product, pk=pk)
    context = {
        'jeans': jeans
    }
    return render(request, 'mjeans_detail.html', context)


def sher_view(request):
    sherwani = Product.objects.filter(Sub_Category='Sherwanis')
    context = {
        'sherwani' : sherwani
    }
    return render(request,'sherwani_list.html',context)


def sher_detail(request,pk):
    sherwani = get_object_or_404(Product, pk=pk)
    context = {
        'sherwani':sherwani
    }
    return render(request,'sherwani_detail.html',context)

def tshirt_view(request):
    tshirts = Product.objects.filter(Sub_Category='T-shirts')
    context = {
        'tshirts': tshirts
    }
    return render(request, 'tshirt_list.html', context)

def tshirt_detail(request, pk):
    tshirts = get_object_or_404(Product, pk=pk)
    context = {
        'tshirts': tshirts
    }
    return render(request, 'tshirt_detail.html', context)


def wjeans_view(request):
    wjeans = Product.objects.filter(Sub_Category='WJeans')
    context = {
        'wjeans': wjeans
    }
    return render(request, 'wjeans_list.html', context)


def wjeans_detail(request, pk):
    wjeans = get_object_or_404(Product, pk=pk)
    context = {
        'wjeans': wjeans
    }
    return render(request, 'wjeans_detail.html', context)


def footwear_view(request):
    wfoot = Product.objects.filter(Sub_Category='Flats')
    context = {
        'wfoot': wfoot
    }
    return render(request, 'footwear.html', context)




def tshirt_detail(request, pk):
    sherwanis = get_object_or_404(Product, pk=pk)
    context = {
        'sherwanis': sherwanis
    }
    return render(request, 'tshirt_detail.html', context)


def track_view(request):
    track = Product.objects.filter(Sub_Category='trackpant')
    context = {
        'track': track
    }
    return render(request, 'track_list.html', context)

def track_detail(request, pk):
    track = get_object_or_404(Product, pk=pk)
    context = {
        'track': track
    }
    return render(request, 'track_detail.html', context)

def wallet_view(request):
    wallet = Product.objects.filter(Sub_Category='Wallet')
    context = {
        'wallet': wallet
    }
    return render(request, 'wallet_list.html', context)


def wallet_detail(request, pk):
    wallet = get_object_or_404(Product, pk=pk)
    context = {
        'wallet': wallet
    }
    return render(request, 'wallet_detail.html', context)

def watch_view(request):
    watch = Product.objects.filter(Sub_Category='Watch')
    context = {
        'watch': watch
    }
    return render(request, 'watch_list.html', context)

def watch_detail(request, pk):
    watch = get_object_or_404(Product, pk=pk)
    context = {
        'watch': watch
    }
    return render(request, 'watch_detail.html', context)


def wfoot_view(request):
    wfoot = Product.objects.filter(Q(Sub_Category='Flats') | Q(Sub_Category='Heels'))
    context = {
        'wfoot': wfoot
    }
    return render(request, 'wfootwear_list.html', context)


def wfoot_detail(request, pk):
    wfoot = get_object_or_404(Product, pk=pk)
    context = {
        'wfoot': wfoot
    }
    return render(request, 'wfootwear_detail.html', context)


def shoe_view(request):
    shoe = Product.objects.filter(Q(Sub_Category='CShoes') | Q(Sub_Category='SShoes'))
    context = {
        'shoe': shoe
    }
    return render(request, 'shoe_list.html', context)


def shoe_detail(request, pk):
    shoe = get_object_or_404(Product, pk=pk)
    context = {
        'shoe': shoe
    }
    return render(request, 'shoe_detail.html', context)


# Kids Sections


def kidFrock_view(request):
    frocks = Product.objects.filter(Sub_Category='Gfrocks')
    context = {
        'frocks': frocks
    }
    return render(request, 'kid_frock_list.html', context)


def kidsFrock_detail(request, pk):
    frocks = get_object_or_404(Product, pk=pk)
    context = {
        'frocks': frocks
    }
    return render(request, 'kid_frock_detail.html', context)


def kidDungrs_view(request):
    dungs = Product.objects.filter(Sub_Category='Gdung')
    context = {
        'dungs': dungs
    }
    return render(request, 'kidDung_list.html', context)

def kidDung_detail(request,pk):
    dungs = get_object_or_404(Product,pk=pk)
    context = {
        'dungs' : dungs
    }
    return  render(request,'kidDung_Detail.html',context)

def boyShirts_view(request):
    shirts = Product.objects.filter(Sub_Category='Bshirts')
    context = {
        'shirts' : shirts
    }
    return render(request,'boysShirts_list.html',context)

def boyShirts_Detail(request,pk):
    shirts = get_object_or_404(Product,pk=pk)
    context = {
        'shirts' : shirts
    }
    return render(request,'boysShirts_Detail.html',context)

def girlsTops_view(request):
    tops = Product.objects.filter(Sub_Category='Gtops')
    context ={
        'tops':tops
    }
    return render(request,'girlsTops_list.html',context)

def girlsTops_Detail(request,pk):
    tops = get_object_or_404(Product,pk=pk)
    context={
        'tops':tops
    }
    return render(request,'girlsTops_Detail.html',context)


def kidTshirts_view(request):
    tshirts=Product.objects.filter(Sub_Category='KTshirts')
    context={
        'tshirts':tshirts
    }
    return render(request,'kidsTshirts_list.html',context)


def kidTshirts_detail(request,pk):
    tshirts=get_object_or_404(Product,pk=pk)
    return render(request,'kidsTshirts_Detail.html',{'tshirts':tshirts})


def kidJack_view(request):
    jackets = Product.objects.filter(Sub_Category='Jackets')
    return render(request,'kidJacket_list.html',{'jackets':jackets})


def kidJack_detail(request,pk):
    jackets=get_object_or_404(Product,pk=pk)
    return render(request,'kidJacket_detail.html',{'jackets':jackets})


def bcloth_view(request):
    bcloth=Product.objects.filter(Sub_Category='BoysClothing')
    return render(request,'bcloth_list.html',{'bcloth':bcloth})


def bcloth_detail(request,pk):
    bcloth=get_object_or_404(Product,pk=pk)
    return render(request,'bcloth_detail.html',{'bcloth':bcloth})


def gcloth_view(request):
    gcloth=Product.objects.filter(Sub_Category='GirlsClothing')
    return render(request,'gcloth_list.html',{'gcloth':gcloth})


def gcloth_detail(request,pk):
    gcloth=get_object_or_404(Product,pk=pk)
    return render(request,'gcloth_detail.html',{'gcloth':gcloth})







def gold_view(request):
    gold = Product.objects.filter(Sub_Category='Gold')
    context = {
        'gold': gold
    }
    return render(request, 'gold_list.html', context)

def gold_detail(request, pk):
    gold = get_object_or_404(Product, pk=pk)
    context = {
        'gold': gold
    }
    return render(request, 'gold_detail.html', context)


def neck_view(request):
    neck = Product.objects.filter(Sub_Category='Necklace')
    context = {
        'neck': neck
    }
    return render(request, 'neck_list.html', context)


def neck_detail(request, pk):
    neck = get_object_or_404(Product, pk=pk)
    context = {
        'neck': neck
    }
    return render(request, 'neck_detail.html', context)


def earring_view(request):
    ear = Product.objects.filter(Sub_Category='Earrings')
    context = {
        'ear': ear
    }
    return render(request, 'ear_list.html', context)


def earring_detail(request, pk):
    ear = get_object_or_404(Product, pk=pk)
    context = {
        'ear': ear
    }
    return render(request, 'ear_detail.html', context)


def ring_view(request):
    ring = Product.objects.filter(Sub_Category='Rings')
    context = {
        'ring': ring
    }
    return render(request, 'ring_list.html', context)


def ring_detail(request, pk):
    ring = get_object_or_404(Product, pk=pk)
    context = {
        'ring': ring
    }
    return render(request, 'ring_detail.html', context)


def chain_view(request):
    chain = Product.objects.filter(Sub_Category='Chains')
    context = {
        'chain': chain
    }
    return render(request, 'chain_list.html', context)


def chain_detail(request,pk):
    chain=get_object_or_404(Product,pk=pk)
    return render(request,'chain_detail.html',{'chain':chain})


def bangle_view(request):
    bangle=Product.objects.filter(Sub_Category='Bangles')
    return render(request,'bangles_list.html',{'bangle':bangle})


def bangle_detail(request,pk):
    bangle=get_object_or_404(Product,pk=pk)
    return render(request,'bangles_detail.html',{'bangle':bangle})


def silver_view(request):
    silver=Product.objects.filter(Sub_Category='SilverJewel')
    context={
        'silver':silver
    }
    return render(request,'silver_list.html',context)



def pendant_view(request):
    pen=Product.objects.filter(Sub_Category='Pendant')
    return render(request,'pendant_list.html',{'pen':pen})


def pendant_detail(request,pk):
    pen=get_object_or_404(Product,pk=pk)
    return render(request,'pendant_detail.html',{'pen':pen})



def silver_detail(request,pk):
    silver=get_object_or_404(Product,pk=pk)
    return render(request,'silver_detail.html',{'silver':silver})



def hand_view(request):
    hand=Product.objects.filter(Q(Sub_Category='SBags')|Q(Sub_Category='HandBags'))
    context={
        'hand':hand
    }
    return render(request,'hand_list.html',context)


def hand_detail(request,pk):
    hand=get_object_or_404(Product,pk=pk)
    return render(request,'hand_detail.html',{'hand':hand})


def tote_view(request):
    totes=Product.objects.filter(Sub_Category='Totes')
    context={
        'totes':totes
    }
    return render(request,'totes_list.html',context)


def totes_detail(request,pk):
    totes=get_object_or_404(Product,pk=pk)
    return render(request,'totes_detail.html',{'totes':totes})


def hobo_view(request):
    hobo = Product.objects.filter(Sub_Category='Sarees')
    context = {
        'hobo': hobo
    }
    return render(request, 'hobo_list.html', context)


def hobo_detail(request,pk):
    hobo=get_object_or_404(Product,pk=pk)
    return render(request,'hobo_detail.html',{'hobo':hobo})



def cross_view(request):
    cross = Product.objects.filter(Sub_Category='Sarees')
    context = {
        'cross': cross
    }
    return render(request, 'cross_list.html', context)



def cross_detail(request,pk):
    cross=get_object_or_404(Product,pk=pk)
    return render(request,'totes_detail.html',{'cross':cross})



def travel_view(request):
    travel = Product.objects.filter(Sub_Category='Sarees')
    context = {
        'travel': travel
    }
    return render(request, 'travel_list.html', context)


def travel_detail(request,pk):
    travel=get_object_or_404(Product,pk=pk)
    return render(request,'travel_detail.html',{'travel':travel})


def clutches_view(request):
    clutches = Product.objects.filter(Sub_Category='Clutches')
    context = {
        'clutches': clutches
    }
    return render(request, 'clutches_list.html', context)


def clutches_detail(request,pk):
    clutches=get_object_or_404(Product,pk=pk)
    return render(request,'clutches_detail.html',{'clutches':clutches})



def back_view(request):
    back = Product.objects.filter(Sub_Category='backpack')
    context = {
        'back': back
    }
    return render(request, 'back_list.html', context)


def back_detail(request,pk):
    back=get_object_or_404(Product,pk=pk)
    return render(request,'clutches_detail.html',{'back':back})


def mess_view(request):
    mess = Product.objects.filter(Sub_Category='backpack')
    context = {
        'mess': mess
    }
    return render(request, 'messanger_list.html', context)


def mess_detail(request,pk):
    mess=get_object_or_404(Product,pk=pk)
    return render(request,'messanger_detail.html',{'mess':mess})



