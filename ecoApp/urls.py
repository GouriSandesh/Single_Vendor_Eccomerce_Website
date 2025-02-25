from django.urls import path
from ecoApp import views, adminViews, frontViews, userFrontViews, wishlistViews, cartViews, guestViews, checkoutViews
urlpatterns = [
    # Home
    path('', views.homepage, name="homepage"),
    path('user_home', views.user_home, name="user_home"),
    path('admin', views.admin, name="admin"),
    path('admin_dash', adminViews.admin_dash, name="admin_dash"),

    # Admin
    path('admin1', views.admin, name="admin_page"),
    path('custView', adminViews.custView, name="custView"),
    path('product_add', adminViews.product_add, name='product_add'),  # Product Add
    path('product_view', adminViews.product_view, name='product_view'),  # Product View
    path('delete_product/<int:id>/', adminViews.delete_product, name="delete_product"),  # Delete Product
    path('update_product/<int:id>/', adminViews.update_product, name="update_product"),  # Update Product

    # Login # Signup # Logout
    path('login_page', views.login_page, name="login_page"),
    path('custom_login', guestViews.custom_login, name="custom_login"),
    path('signup', views.signup, name="signup"),
    path('signout', views.signout, name='signout'),

    # Customer
    path('custdash_view', views.custdash_view, name="custdash_view"),  # Dashboard
    path('cust_base', views.cust_base, name="cust_base"),  # Dashboard
    path('profile_view', userFrontViews.profile_view, name="profile_view"),  # Profile
    path('cust_detail/<int:pk>/', adminViews.cust_detail, name="cust_detail"),
    path('product_detail/<int:pk>/', adminViews.product_detail, name="product_detail"),


    # Men
    path('men', views.men, name="men"),
    path('user_men', views.user_men, name="user_men"),

    # Shirt Page
    path('shirt_view', frontViews.shirt_view, name="shirt_view"),
    path('shirts/<int:pk>/', frontViews.shirt_detail, name='shirt_detail'),
    path('user_shirt_view', userFrontViews.user_shirt_view, name="user_shirt_view"),
    path('user_shirt_detail/<int:pk>/', userFrontViews.user_shirt_detail, name='user_shirt_detail'),

    # Tshirt Page
    path('tshirt_view', frontViews.tshirt_view, name="tshirt_view"),
    path('tshirt_detail/<int:pk>/', frontViews.tshirt_detail, name='tshirt_detail'),
    path('user_tshirt_view', userFrontViews.user_tshirt_view, name="user_tshirt_view"),
    path('user_tshirt_detail/<int:pk>/', userFrontViews.user_tshirt_detail, name='user_tshirt_detail'),



    # Jeans Page
    path('mjeans_view', frontViews.mjeans_view, name="mjeans_view"),
    path('mjeans_detail/<int:pk>/', frontViews.mjeans_detail, name='mjeans_detail'),
    path('user_mjeans_view', userFrontViews.user_mjeans_view, name="user_mjeans_view"),
    path('user_mjeans_detail/<int:pk>/', userFrontViews.user_mjeans_detail, name="user_mjeans_detail"),


    # Sherwani Page
    path('sher_view', frontViews.sher_view, name="sher_view"),
    path('sher_detail/<int:pk>/', frontViews.sher_detail, name='sher_detail'),
    path('user_sher_view', userFrontViews.user_sher_view, name="user_sher_view"),
    path('user_sher_detail/<int:pk>/', userFrontViews.user_sher_detail, name="user_sher_detail"),


    # Track Pant Page
    path('track_view', frontViews.track_view, name="track_view"),
    path('track_detail/<int:pk>/', frontViews.track_detail, name="track_detail"),
    path('user_track_view', userFrontViews.user_track_view, name="user_track_view"),
    path('user_track_detail/<int:pk>/', userFrontViews.user_track_detail, name="user_track_detail"),

    # Wallet Page
    path('wallet_view', frontViews.wallet_view, name="wallet_view"),
    path('wallet_detail/<int:pk>/', frontViews.wallet_detail, name="wallet_detail"),
    path('user_wallet_view', userFrontViews.user_wallet_view, name="user_wallet_view"),
    path('user_wallet_detail/<int:pk>/', userFrontViews.user_wallet_detail, name="user_wallet_detail"),

    # Watch Page
    path('watch_view', frontViews.watch_view, name="watch_view"),
    path('watch_detail/<int:pk>/', frontViews.watch_detail, name="watch_detail"),
    path('user_watch_view', userFrontViews.user_watch_view, name="user_watch_view"),
    path('user_watch_detail/<int:pk>/', userFrontViews.user_watch_detail, name="user_watch_detail"),

    # Shoe Page
    path('shoe_view',frontViews.shoe_view, name="shoe_view"),
    path('shoe_detail/<int:pk>/',frontViews.shoe_detail,name="shoe_detail"),
    path('user_shoe_view', userFrontViews.user_shoe_view, name="user_shoe_view"),
    path('user_shoe_detail/<int:pk>/', userFrontViews.user_shoe_detail, name="user_shoe_detail"),

    # Women
    path('women', views.women, name="women"),
    path('user_women', views.user_women, name="user_women"),

    # Saree Page
    path('saree_view', frontViews.saree_view, name="saree_view"),
    path('saree_detail/<int:pk>/', frontViews.saree_detail, name='saree_detail'),
    path('user_saree_view', userFrontViews.user_saree_view, name="user_saree_view"),
    path('user_saree/<int:pk>/', userFrontViews.user_saree_detail, name='user_saree_detail'),

    # Kurta Page
    path('kurta_view', frontViews.kurta_view, name="kurta_view"),
    path('kurtas/<int:pk>/', frontViews.kurta_detail, name='kurta_detail'),
    path('user_kurta_view', userFrontViews.user_kurta_view, name="user_kurta_view"),
    path('user_kurta/<int:pk>/', userFrontViews.user_kurta_detail, name='user_kurta_detail'),

    # Dresses Page
    path('gown_view', frontViews.gown_view, name="gown_view"),
    path('gown/<int:pk>/', frontViews.gown_detail, name='gown_detail'),
    path('user_gown_view', userFrontViews.user_gown_view, name="user_gown_view"),
    path('user_gown/<int:pk>/', userFrontViews.user_gown_detail, name='user_gown_detail'),

    # Top Page
    path('top_view', frontViews.top_view, name="top_view"),
    path('top/<int:pk>/', frontViews.top_detail, name='top_detail'),
    path('user_top_view', userFrontViews.user_top_view, name="user_top_view"),
    path('user_top/<int:pk>/', frontViews.top_detail, name='user_top_detail'),

    # Jeans Women
    path('wjeans_view', frontViews.wjeans_view, name="wjeans_view"),
    path('wjeans/<int:pk>/', frontViews.wjeans_detail, name='wjeans_detail'),
    path('user_wjeans_view', userFrontViews.user_wjeans_view, name="user_wjeans_view"),
    path('user_wjeans/<int:pk>/', userFrontViews.user_wjeans_detail, name='user_wjeans_detail'),

    # Women Footwear
    path('wfoot_view', frontViews.wfoot_view, name='wfoot_view'),
    path('wjeans/<int:pk>/', frontViews.wjeans_detail, name='wjeans_detail'),
    path('user_wfoot_view', userFrontViews.user_wfootwear_view, name="user_wfoot_view"),
    path('user_wfoot_detail/<int:pk>/', userFrontViews.user_wfootwear_detail, name='user_wfoot_detail'),

    # Kids
    path('kids', views.kids, name="kids"),
    path('user_kids', views.user_kids, name="user_kids"),
    path('kidFrock_view', frontViews.kidFrock_view, name="kidFrock_view"),
    path('kidsFrock_detail/<int:pk>/', frontViews.kidsFrock_detail, name='kidsFrock_detail'),
    path('kidDungrs_view', frontViews.kidDungrs_view, name="kidDungrs_view"),
    path('useer_kidDung_view', userFrontViews.useer_kidDung_view, name="useer_kidDung_view"),
    path('kidDung_detail/<int:pk>/', frontViews.kidDung_detail, name='kidDung_detail'),
    path('user_kkidDung_detail/<int:pk>/', userFrontViews.user_kkidDung_detail, name='user_kkidDung_detail'),
    path('boyShirts_view', frontViews.boyShirts_view, name="boyShirts_view"),
    path('boyShirts_Detail/<int:pk>/', frontViews.boyShirts_Detail, name='boyShirts_Detail'),
    path('girlsTops_view', frontViews.girlsTops_view, name="girlsTops_view"),
    path('girlsTops_Detail/<int:pk>/', frontViews.girlsTops_Detail, name='girlsTops_Detail'),
    path('user_girlsTop_view', userFrontViews.user_girlsTop_view, name="user_girlsTop_view"),
    path('user_girlsTop_detail/<int:pk>/', userFrontViews.user_girlsTop_detail, name='user_girlsTop_detail'),
    path('kidTshirts_view',frontViews.kidTshirts_view,name='kidTshirts_view'),
    path('kidTshirts_detail/<int:pk>/', frontViews.kidTshirts_detail, name='kidTshirts_detail'),
    path('user_Ktshirts_view',userFrontViews.user_Ktshirts_view,name='user_Ktshirts_view'),
    path('user_Ktshirts_detail/<int:pk>/', userFrontViews.user_Ktshirts_detail, name='user_Ktshirts_detail'),
    path('user_kidJack_view', userFrontViews.user_kidJack_view, name='user_kidJack_view'),
    path('kidJack_view', frontViews.kidJack_view, name='kidJack_view'),
    path('user_kidJack_detail/<int:pk>/', userFrontViews.user_kidJack_detail, name='user_kidJack_detail'),
    path('kidJack_detail/<int:pk>/', frontViews.kidJack_detail, name='kidJack_detail'),
    path('bcloth_view', frontViews.bcloth_view, name='bcloth_view'),
    path('bcloth_detail/<int:pk>/', frontViews.bcloth_detail, name='bcloth_detail'),
    path('user_bcloth_view', userFrontViews.user_bcloth_view, name='user_bcloth_view'),
    path('user_bcloth_detail/<int:pk>/', userFrontViews.user_bcloth_detail, name='user_bcloth_detail'),
    path('gcloth_view', frontViews.gcloth_view, name='gcloth_view'),
    path('user_gcloth_view', userFrontViews.user_gcloth_view, name='user_gcloth_view'),
    path('gcloth_detail/<int:pk>/', frontViews.gcloth_detail, name='gcloth_detail'),
    path('user_gcloth_detail/<int:pk>/', userFrontViews.user_gcloth_detail, name='user_gcloth_detail'),

    # Jewellery
    path('jewel', views.jewel, name="jewel"),
    path('user_jewel', views.user_jewel, name="user_jewel"),


    path('gold_view', frontViews.gold_view, name="gold_view"),
    path('user_gold_view', userFrontViews.user_gold_view, name="user_gold_view"),
    path('gold_detail/<int:pk>/', frontViews.gold_detail, name='gold_detail'),
    path('user_gold_detail/<int:pk>/', userFrontViews.user_gold_detail, name='user_gold_detail'),
    path('neck_view', frontViews.neck_view, name="neck_view"),
    path('user_neck_view', userFrontViews.user_neck_view, name="user_neck_view"),
    path('neck_detail/<int:pk>/', frontViews.neck_detail, name='neck_detail'),
    path('user_neck_detail/<int:pk>/', userFrontViews.user_neck_detail, name='user_neck_detail'),
    path('earring_view', frontViews.earring_view, name="earring_view"),
    path('user_earring_view', userFrontViews.user_earring_view, name="user_earring_view"),
    path('earring_detail/<int:pk>/', frontViews.earring_detail, name='earring_detail'),
    path('user_earring_detail/<int:pk>/', userFrontViews.user_earring_detail, name='user_earring_detail'),
    path('ring_view', frontViews.ring_view, name="ring_view"),
    path('user_ring_view', userFrontViews.user_ring_view, name="user_ring_view"),
    path('user_ring_detail/<int:pk>/', userFrontViews.user_ring_detail, name='user_ring_detail'),
    path('ring_detail/<int:pk>/', frontViews.ring_detail, name='ring_detail'),
    path('chain_view', frontViews.chain_view, name="chain_view"),
    path('user_chain_view', userFrontViews.user_chain_view, name="user_chain_view"),
    path('chain_detail/<int:pk>/', frontViews.chain_detail, name='chain_detail'),
    path('user_chain_detail/<int:pk>/', userFrontViews.user_chain_detail, name='user_chain_detail'),
    path('bangle_view', frontViews.bangle_view, name="bangle_view"),
    path('bangle_detail/<int:pk>/', frontViews.bangle_detail, name='bangle_detail'),
    path('user_bangle_view', userFrontViews.user_bangle_view, name="user_bangle_view"),
    path('user_bangle_detail/<int:pk>/', userFrontViews.user_bangle_detail, name='user_bangle_detail'),
    path('silver_view', frontViews.silver_view, name="silver_view"),
    path('silver_detail/<int:pk>/', frontViews.silver_detail, name='silver_detail'),
    path('user_silver_detail/<int:pk>/', userFrontViews.user_silver_detail, name='user_silver_detail'),
    path('user_silver_view', userFrontViews.user_silver_view, name="user_silver_view"),
    path('pendant_view', frontViews.pendant_view, name="pendant_view"),
    path('pendant_detail/<int:pk>/', frontViews.pendant_detail, name='pendant_detail'),
    path('user_pendant_view', userFrontViews.user_pendant_view, name="user_pendant_view"),
    path('user_pendant_detail/<int:pk>/', userFrontViews.user_pendant_detail, name='user_pendant_detail'),
    path('hand_view',frontViews.hand_view,name='hand_view'),
    path('hand_detail',frontViews.hand_detail,name='hand_detail'),
    path('user_hand_view',userFrontViews.user_hand_view,name='user_hand_view'),
    path('user_hand_detail',userFrontViews.user_hand_detail,name='user_hand_detail'),


    # Bag
    path('bags', views.bags, name="bags"),
    path('user_bag', views.user_bag, name="user_bag"),
    path('tote_view', frontViews.tote_view, name='tote_view'),

    # Footwear
    path('foot', views.foot, name="foot"),
    path('user_foot', views.user_foot, name="user_foot"),


    # Wishlist
    path('add_to_wishlist/<int:product_id>/', wishlistViews.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist_detail', wishlistViews.wishlist_detail, name='wishlist_detail'),
    path('remove_from_wishlist/<int:product_id>/', wishlistViews.remove_from_wishlist, name='remove_from_wishlist'),

    # Cart
        path('cart_detail', cartViews.cart_detail, name='cart_detail'),
        path('add_to_cart/<int:product_id>/', cartViews.add_to_cart, name='add_to_cart'),
        path('remove_from_cart/<int:product_id>/', cartViews.remove_from_cart, name='remove_from_cart'),
        path('increase_quantity/<int:product_id>/', cartViews.increase_quantity, name='increase_quantity'),
        path('decrease_quantity/<int:product_id>/', cartViews.decrease_quantity, name='decrease_quantity'),



    path('address_view', userFrontViews.address_view, name="address_view"),
    # path('add_address', userFrontViews.add_address, name="add_address"),
    # path('show_address', userFrontViews.show_address, name="show_address"),


    path('CreateStripeCheckoutSessionView', checkoutViews.CreateStripeCheckoutSessionView.as_view(),name="CreateStripeCheckoutSessionView"),
    # path('stripe_webhook', checkoutViews.stripe_webhook,name="stripe_webhook"),
    path('SuccessView',checkoutViews.SuccessView.as_view(),name="SuccessView"),
    path('CancelView',checkoutViews.CancelView,name="CancelView"),
    path('choosePay/<int:pk>/',checkoutViews.choosePay,name="choosePay"),


    path('orders_view',views.orders_view,name="orders_view"),    #Customer viewing
    path('delete_order/<int:pk>/',views.delete_order,name="delete_order"),


    path('admin_order_detail_view/<str:order_id>/',adminViews.admin_order_detail_view,name="admin_order_detail_view"),
    path('admin_orders_view>/',adminViews.admin_orders_view,name="admin_orders_view"),
    path('place_order',checkoutViews.place_order,name="place_order"),
    path('order_confirmation',checkoutViews.order_confirmation,name="order_confirmation"),
















]

