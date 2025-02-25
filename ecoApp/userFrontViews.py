
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from ecoApp.forms import profile_info_form, UserReg, Customer_reg, userform, add_address_form, ProfileForm
from ecoApp.models import Product, Customers, addressBook


def user_saree_view(request):
    sarees = Product.objects.filter(Sub_Category='Sarees')
    context = {
        'sarees': sarees
    }
    return render(request, 'user_saree_list.html', context)


def user_saree_detail(request, pk):
    saree = get_object_or_404(Product, pk=pk)
    context = {
        'saree': saree
    }
    return render(request, 'user_saree_detail.html', context)

def user_kurta_view(request):
    kurtas = Product.objects.filter(Sub_Category='Kurta&Kurtis')
    context = {
        'kurtas': kurtas
    }
    return render(request, 'user_kurta_list.html', context)


def user_kurta_detail(request, pk):
    kurtas = get_object_or_404(Product, pk=pk)
    context = {
        'kurtas': kurtas
    }
    return render(request, 'user_kurta_detail.html', context)


def user_gown_view(request):
    gowns = Product.objects.filter(Sub_Category='Gowns')
    context = {
        'gowns': gowns
    }
    return render(request, 'user_gown_list.html', context)


def user_gown_detail(request, pk):
    gowns = get_object_or_404(Product, pk=pk)
    context = {
        'gown': gowns
    }
    return render(request, 'user_gown_detail.html', context)


def user_mjeans_view(request):
    jeans = Product.objects.filter(Sub_Category='MJeans')
    context = {
        'jeans': jeans
    }
    return render(request, 'user_mjeans_list.html', context)


def user_mjeans_detail(request, pk):
    jeans = get_object_or_404(Product, pk=pk)
    context = {
        'jeans': jeans
    }
    return render(request, 'user_mjeans_detail.html', context)

def user_sher_view(request):
    sherwani = Product.objects.filter(Sub_Category='Sherwanis')
    context = {
        'sherwani':sherwani
    }
    return render(request,'user_sherwani_list.html',context)


def user_sher_detail(request,pk):
    sherwani = get_object_or_404(Product,pk=pk)
    context={
        'sherwani':sherwani
    }
    return render(request,'user_sherwani_detail.html',context)

def user_tshirt_view(request):
    tshirts = Product.objects.filter(Sub_Category='T-shirts')
    context = {
        'tshirts': tshirts
    }
    return render(request, 'user_tshirt_list.html', context)

def user_tshirt_detail(request, pk):
    tshirts = get_object_or_404(Product, pk=pk)
    context = {
        'tshirts': tshirts
    }
    return render(request, 'user_tshirt_detail.html', context)


def user_top_view(request):
    top = Product.objects.filter(Sub_Category='Topwear')
    context = {
        'top': top
    }
    return render(request, 'user_top_list.html', context)


def user_top_detail(request,pk):
    top=get_object_or_404(Product,pk=pk)
    context={
        'top':top
    }
    return render(request,'user_top_detail.html',context)


def user_girlsTop_view(request):
    tops=Product.objects.filter(Sub_Category='Gtops')
    context={
        'tops':tops
    }
    return render(request,'user_girlsTop_list.html',context)


def user_girlsTop_detail(request,pk):
    tops=get_object_or_404(Product,pk=pk)
    context={
        'tops':tops
    }
    return render(request,'user_girlsTop_detail.html',context)


def user_Ktshirts_view(request):
    tshirts=Product.objects.filter(Sub_Category='KTshirts')
    return render(request,'user_kidTshirts_list.html',{'tshirts':tshirts})


def user_Ktshirts_detail(request,pk):
    tshirts=get_object_or_404(Product,pk=pk)
    return render(request,'user_kidTshirts_detail.html',{'tshirts':tshirts})


def user_kidJack_view(request):
    jackets = Product.objects.filter(Sub_Category='Jackets')
    return render(request,'user_kidJacket_list.html',{'jackets':jackets})


def user_kidJack_detail(request,pk):
    jackets=get_object_or_404(Product,pk=pk)
    return render(request,'user_kidJacket_detail.html',{'jackets':jackets})


def user_bcloth_view(request):
    bcloth=Product.objects.filter(Sub_Categoty='BoysClothing')
    return render(request,'user_bcloth_detail.html',{'bcloth':bcloth})


def user_bcloth_detail(request,pk):
    bcloth=get_object_or_404(Product,pk=pk)
    return render(request,'user_bcloth_detail.html',{'bcloth':bcloth})


def user_gcloth_view(request):
    gcloth=Product.objects.filter(Sub_Category='GirlsClothing')
    return render(request,'user_gcloth_list.html',{'gcloth':gcloth})


def user_gcloth_detail(request,pk):
    gcloth=get_object_or_404(Product,pk=pk)
    return render(request,'user_gcloth_detail.html',{'gcloth':gcloth})


def user_wjeans_view(request):
    wjeans = Product.objects.filter(Sub_Category='WJeans')
    context = {
        'wjeans': wjeans
    }
    return render(request, 'user_wjeans_list.html', context)

def user_wjeans_detail(request, pk):
    wjeans = get_object_or_404(Product, pk=pk)
    context = {
        'wjeans': wjeans
    }
    return render(request, 'user_wjeans_detail.html', context)


def user_wfootwear_view(request):
    wfoot = Product.objects.filter(Sub_Category='Flats')
    context = {
        'wfoot': wfoot
    }
    return render(request, 'user_wfootwear_list.html', context)


def user_wfootwear_detail(request, pk):
    wfoot = get_object_or_404(Product, pk=pk)
    context = {
        'woot': wfoot
    }
    return render(request, 'user_wfootwear_detail.html', context)

def user_shirt_view(request):
    shirts = Product.objects.filter(Q(Sub_Category = 'CShirts') | Q(Sub_Category = 'FShirts'))
    context = {
        'shirts': shirts
    }
    return render(request, 'user_shirt_list.html', context)

def user_shirt_detail(request, pk):
    shirts = get_object_or_404(Product, pk=pk)
    context = {
        'shirts': shirts
    }
    return render(request, 'user_shirt_detail.html', context)




def user_track_view(request):
    track = Product.objects.filter(Sub_Category='trackpant')
    context = {
        'track': track
    }
    return render(request, 'user_track_list.html', context)


def user_track_detail(request, pk):
    track = get_object_or_404(Product, pk=pk)
    context = {
        'track': track
    }
    return render(request, 'user_track_detail.html', context)

def user_wallet_view(request):
    wallet = Product.objects.filter(Sub_Category='Wallet')
    context = {
        'wallet': wallet
    }
    return render(request, 'user_wallet_list.html', context)

def user_wallet_detail(request, pk):
    wallet = get_object_or_404(Product, pk=pk)
    context = {
        'wallet': wallet
    }
    return render(request, 'user_wallet_detail.html', context)


def user_watch_view(request):
    watch = Product.objects.filter(Sub_Category='Watch')
    context = {
        'watch': watch
    }
    return render(request, 'user_watch_list.html', context)

def user_watch_detail(request, pk):
    watch = get_object_or_404(Product, pk=pk)
    context = {
        'watch': watch
    }
    return render(request, 'watch_detail.html', context)


def user_shoe_view(request):
    shoe = Product.objects.filter(Sub_Category='CShoes')
    context = {
        'shoe': shoe
    }
    return render(request, 'user_shoe_list.html', context)

def user_shoe_detail(request, pk):
    shoe = get_object_or_404(Product, pk=pk)
    context = {
        'shoe': shoe
    }
    return render(request, 'shoe_detail.html', context)



def user_kidFrock_view(request):
    frock = Product.objects.filter(Sub_Category='Sarees')
    context = {
        'frock': frock
    }
    return render(request, 'user_kid_frock_list.html', context)


def user_kidsFrock_detail(request, pk):
    frock = get_object_or_404(Product, pk=pk)
    context = {
        'frock': frock
    }
    return render(request, 'user_kid_frock_detail.html', context)




def useer_kidDung_view(request):
    dungs = Product.objects.filter(Sub_Category='Gdung')
    context = {
        'dungs': dungs
    }
    return render(request, 'user_kidDung_list.html', context)


def user_kkidDung_detail(request, pk):
    dungs = get_object_or_404(Product, pk=pk)
    context = {
        'dungs': dungs
    }
    return render(request, 'user_kidDung_detail.html', context)


def user_boyShirt_view(request):
    shirts = Product.objects.filter(Sub_Category='')
    context={
        'shirts':shirts
    }
    return render(request,'user_boysShirts_list.html',context)


def user_boyShirt_detail(request,pk):
    shirts=get_object_or_404(Product,pk=pk)
    context={
        'shirts':shirts
    }
    return render(request,'user_boysShirt_detail.html',context)



def user_gold_view(request):
    gold = Product.objects.filter(Sub_Category='Gold')
    context = {
        'gold': gold
    }
    return render(request, 'user_gold_list.html', context)



def user_gold_detail(request, pk):
    gold = get_object_or_404(Product, pk=pk)
    context = {
        'gold': gold
    }
    return render(request, 'user_gold_detail.html', context)



def user_neck_view(request):
    neck = Product.objects.filter(Sub_Category='Necklace')
    context = {
        'neck': neck
    }
    return render(request, 'user_neck_list.html', context)


def user_neck_detail(request, pk):
    neck = get_object_or_404(Product, pk=pk)
    context = {
        'neck': neck
    }
    return render(request, 'user_neck_detail.html', context)



def user_earring_view(request):
    ear = Product.objects.filter(Sub_Category='Earrings')
    context = {
        'ear': ear
    }
    return render(request, 'ear_list.html', context)


def user_earring_detail(request, pk):
    ear = get_object_or_404(Product, pk=pk)
    context = {
        'ear': ear
    }
    return render(request, 'ear_detail.html', context)



def user_ring_view(request):
    ring = Product.objects.filter(Sub_Category='Rings')
    context = {
        'ring': ring
    }
    return render(request, 'user_ring_list.html', context)


def user_ring_detail(request, pk):
    ring = get_object_or_404(Product, pk=pk)
    context = {
        'ring': ring
    }
    return render(request, 'user_ring_detail.html', context)


def user_chain_view(request):
    chain = Product.objects.filter(Sub_Category='Chains')
    context = {
        'chain': chain
    }
    return render(request, 'user_chain_list.html', context)


def user_chain_detail(request,pk):
    chain=get_object_or_404(Product,pk=pk)
    return render(request,'user_chain_detail.html',{'chain':chain})



def user_bangle_view(request):
    bangle=Product.objects.filter(Sub_Category='Bangles')
    return render(request,'user_bangles_list.html',{'bangle':bangle})


def user_bangle_detail(request,pk):
    bangle=get_object_or_404(Product,pk=pk)
    return render(request,'user_bangles_detail.html',{'bangle':bangle})


def user_silver_view(request):
    silver=Product.objects.filter(Sub_Category='SilverJewel')
    context={
        'silver':silver
    }
    return render(request,'user_silver_list.html',context)



def user_silver_detail(request,pk):
    silver=get_object_or_404(Product,pk=pk)
    return render(request,'user_silver_detail.html',{'silver':silver})


def user_pendant_view(request):
    pen=Product.objects.filter(Sub_Category='Pendant')
    return render(request,'user_pendant_list.html',{'pen':pen})


def user_pendant_detail(request,pk):
    pen=get_object_or_404(Product,pk=pk)
    return render(request,'user_pendant_detail.html',{'pen':pen})




def user_hand_view(request):
    hand=Product.objects.filter(Q(Sub_Category='SBags')|Q(Sub_Category='HandBags'))
    context={
        'hand':hand
    }
    return render(request,'user_hand_list.html',context)


def user_hand_detail(request,pk):
    hand=get_object_or_404(Product,pk=pk)
    return render(request,'user_hand_detail.html',{'hand':hand})



def user_tote_view(request):
    totes=Product.objects.filter(Sub_Category='Totes')
    context={
        'totes':totes
    }
    return render(request,'user_totes_list.html',context)


def user_totes_detail(request,pk):
    totes=get_object_or_404(Product,pk=pk)
    return render(request,'user_totes_detail.html',{'totes':totes})



def user_hobo_view(request):
    hobo = Product.objects.filter(Sub_Category='Hobo')
    context = {
        'hobo': hobo
    }
    return render(request, 'user_hobo_list.html', context)


def user_hobo_detail(request,pk):
    hobo=get_object_or_404(Product,pk=pk)
    return render(request,'user_hobo_detail.html',{'hobo':hobo})





def user_cross_view(request):
    cross = Product.objects.filter(Sub_Category='Sarees')
    context = {
        'cross': cross
    }
    return render(request, 'user_cross_list.html', context)



def user_cross_detail(request,pk):
    cross=get_object_or_404(Product,pk=pk)
    return render(request,'user_cross_detail.html',{'cross':cross})



def user_back_view(request):
    back = Product.objects.filter(Sub_Category='backpack')
    context = {
        'back': back
    }
    return render(request, 'user_back_list.html', context)


def user_back_detail(request,pk):
    back=get_object_or_404(Product,pk=pk)
    return render(request,'user_back_detail.html',{'back':back})



def user_mess_view(request):
    mess = Product.objects.filter(Sub_Category='backpack')
    context = {
        'mess': mess
    }
    return render(request, 'user_messanger_list.html', context)


def user_mess_detail(request,pk):
    mess=get_object_or_404(Product,pk=pk)
    return render(request,'user_messanger_detail.html',{'mess':mess})



def user_cross_detail(request,pk):
    cross=get_object_or_404(Product,pk=pk)
    return render(request,'user_cross_detail.html',{'cross':cross})



def user_travel_view(request):
    travel = Product.objects.filter(Sub_Category='Sarees')
    context = {
        'travel': travel
    }
    return render(request, 'user_travel_list.html', context)


def user_travel_detail(request,pk):
    travel=get_object_or_404(Product,pk=pk)
    return render(request,'user_travel_detail.html',{'travel':travel})


def user_clutches_view(request):
    clutches = Product.objects.filter(Sub_Category='Clutches')
    context = {
        'clutches': clutches
    }
    return render(request, 'user_clutches_list.html', context)


def user_clutches_detail(request,pk):
    clutches=get_object_or_404(Product,pk=pk)
    return render(request,'user_clutches_detail.html',{'clutches':clutches})






def profile_view(request):
    # Load the current user's data
    customer = Customers.objects.get(user=request.user)  # Adjust this line if necessary

    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('profile_view')  # Replace with your redirect target
    else:
        form = ProfileForm(instance=customer)  # Pre-populate the form with existing data

    return render(request, 'cust_profile.html', {'form': form})



def update_profile(request):
    data = Customers.objects.get(user=request.user.customers)
    form = Customer_reg(instance=data)
    if request.method == 'POST':
        form = Customer_reg(request.POST,request.files,instance=data)
        if form.is_valid():
            form.save()
            return redirect(profile_view)
    return render(request,'update_profile.html', {'form': form})



def address_view(request):
    # Check if there are addresses in the database
    addresses = addressBook.objects.all()
    has_addresses = addresses.exists()

    # Handle the form submission if any
    if request.method == 'POST':
        form = add_address_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('address_view'))
    else:
        form = add_address_form()

    return render(request, 'add_address.html', {
        'form': form,
        'data': addresses,  # Pass the addresses to the template
        'has_addresses': has_addresses  # Boolean flag to control template logic
    })

def show_address(request):
    data = addressBook.objects.all()
    return render(request,'show_address.html',{'data':data})





