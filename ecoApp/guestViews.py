
# def custom_login(request):
#     # Capture the current page URL (or the referer page where the user was before accessing the login page)
#     redirect_to = request.GET.get('next', request.META.get('HTTP_REFERER', '/'))
#
#     if request.method == 'POST':
#         # Get the username and password from the POST request
#         username = request.POST['username']
#         password = request.POST['password']
#
#         # Authenticate the user
#         user = authenticate(request, username=username, password=password)
#
#         if user is not None and user.is_staff:
#             login(request, user)
#             return redirect('admin_page')
#
#         elif user is not None and user.is_customer:
#             # If the user is valid, log them in
#             login(request, user)
#             messages.success(request, "Login successful.")
#             # Modify the URL: if the user was on /shirt_view, redirect them to /user_shirt_view
#             if '/shirt_view' in redirect_to:
#                 redirect_to = '/user_shirt_view'
#                 return HttpResponseRedirect(redirect_to)  # Redirect to the updated page
#
#             elif '/tshirt_view' in redirect_to:
#                 redirect_to = '/user_tshirt_view'
#                 return HttpResponseRedirect(redirect_to)
#
#             elif '/mjeans_view' in redirect_to:
#                 redirect_to = '/user_mjeans_view'
#                 return  HttpResponseRedirect(redirect_to)
#
#             elif 'sher_view' in redirect_to:
#                 redirect_to = '/user_sher_view'
#                 return HttpResponseRedirect(redirect_to)
#
#             elif 'track_view' in redirect_to:
#                 redirect_to = '/user_track_view'
#                 return HttpResponseRedirect(redirect_to)
#
#             elif 'wallet_view' in redirect_to:
#                 redirect_to = '/user_wallet_view'
#                 return HttpResponseRedirect(redirect_to)
#
#             elif 'watch_view' in redirect_to:
#                 redirect_to = '/user_watch_view'
#                 return HttpResponseRedirect(redirect_to)
#
#             elif 'shoe_view' in redirect_to:
#                 redirect_to = '/user_shoe_view'
#                 return HttpResponseRedirect(redirect_to)
#
#             elif 'saree_view' in redirect_to:
#                 redirect_to = '/user_saree_view'
#                 return HttpResponseRedirect(redirect_to)
#
#             elif 'kurta_view' in redirect_to:
#                 redirect_to = '/user_kurta_view'
#                 return HttpResponseRedirect(redirect_to)
#
#             elif 'gown_view' in redirect_to:
#                 redirect_to = '/user_gown_view'
#                 return HttpResponseRedirect(redirect_to)
#
#             elif 'top_view' in redirect_to:
#                 redirect_to = '/user_top_view'
#                 return HttpResponseRedirect(redirect_to)
#
#             elif 'wjeans_view' in redirect_to:
#                 redirect_to = '/user_wjeans_view'
#                 return HttpResponseRedirect(redirect_to)
#
#             elif 'wfoot_view' in redirect_to:
#                 redirect_to = '/user_wfoot_view'
#                 return HttpResponseRedirect(redirect_to)
#
#         else:
#             # If the user is not valid, show an error message
#             messages.error(request, "Invalid username or password.")
#
#     # Render the login form on GET request
#     return render(request, 'userHome.html', {'next': redirect_to})
#
#
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render


def custom_login(request):
    # Capture the current page URL (or the referer page where the user was before accessing the login page)
    redirect_to = request.GET.get('next', request.META.get('HTTP_REFERER', '/'))

    if request.method == 'POST':
        # Get the username and password from the POST request
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # If the user is valid, log them in
            login(request, user)
            messages.success(request, "Login successful.")

            # Modify the URL: if the user was on /shirt_view, redirect them to /user_shirt_view
            if '/gown_view' in redirect_to:
                redirect_to = '/user_gown_view'
            elif '/saree_view' in redirect_to:
                redirect_to = '/user_saree_view'
            elif '/kurta_view' in redirect_to:
                redirect_to = '/user_kurta_view'
            elif '/top_view' in redirect_to:
                redirect_to = '/user_top_view'
            elif '/shirt_view' in redirect_to:
                redirect_to = '/user_shirt_view'
            elif '/mjeans_view' in redirect_to:
                redirect_to = '/user_mjeans_view'
            elif '/tshirt_view' in redirect_to:
                redirect_to = '/user_tshirt_view'
            elif '/wjeans_view' in redirect_to:
                redirect_to = '/user_wjeans_view'
            elif '/footwear_view' in redirect_to:
                redirect_to = '/user_footwear_view'
            elif '/sher_view' in redirect_to:
                redirect_to = '/user_sher_view'
            elif '/track_view' in redirect_to:
                redirect_to = '/user_track_view'
            elif '/wallet_view' in redirect_to:
                redirect_to = '/user_wallet_view'
            elif '/watch_view' in redirect_to:
                redirect_to = '/user_watch_view'
            elif '/wfoot_view' in redirect_to:
                redirect_to = '/user_wfoot_view'
            elif '/shoe_view' in redirect_to:
                redirect_to = '/user_shoe_view'
            elif '/kidFrock_view' in redirect_to:
                redirect_to = '/user_kidFrock_view'
            elif '/gold_view' in redirect_to:
                redirect_to = '/user_gold_view'
            elif '/neck_view' in redirect_to:
                redirect_to = '/user_neck_view'
            elif '/earring_view' in redirect_to:
                redirect_to = '/user_earring_view'
            elif '/ring_view' in redirect_to:
                redirect_to = '/user_ring_view'
            elif '/chain_view' in redirect_to:
                redirect_to = '/user_chain_view'

            return HttpResponseRedirect(redirect_to)  # Redirect to the updated page
        else:
            # If the user is not valid, show an error message
            messages.error(request, "Invalid username or password.")

    # Render the login form on GET request
    return render(request, 'login.html', {'next': redirect_to})
