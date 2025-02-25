import logging

import stripe
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.utils.http import urlencode
from django.views import View
from stripe import SignatureVerificationError

from ecoApp import cart
from ecoApp.models import Cart
from ecoApp.models import Product, Order, OrderItem, Payment
from ecoProject import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


# class CreateStripeCheckoutSessionView(LoginRequiredMixin, View):
#     def post(self, request, *args, **kwargs):
#         # Get the total price from the POST data
#         total_price = request.POST.get('total_price')
#
#         if not total_price:
#             return redirect('cart_detail')
#
#         try:
#             total_price = float(total_price)
#         except ValueError:
#             return redirect('cart_detail')
#
#         # Get the cart associated with the user
#         try:
#             cart = Cart.objects.get(user=request.user)
#         except Cart.DoesNotExist:
#             return redirect('cart_detail')
#
#         # Create Stripe checkout session with metadata
#         checkout_session = stripe.checkout.Session.create(
#             payment_method_types=["card"],
#             line_items=[
#                 {
#                     "price_data": {
#                         "currency": "inr",
#                         "unit_amount": int(total_price * 100),
#                         "product_data": {
#                             "name": "Cart Total",
#                             "description": "Total items in your cart",
#                         },
#                     },
#                     "quantity": 1,
#                 }
#             ],
#             mode="payment",
#             billing_address_collection="required",
#             shipping_address_collection={"allowed_countries": ["IN"]},
#             metadata={
#                 "user_id": request.user.id,
#                 "cart_id": cart.id,
#                 "total_price": total_price,
#             },
#             success_url=f"{settings.PAYMENT_SUCCESS_URL}?{urlencode({'order_id': order.id})}",
#             cancel_url=settings.PAYMENT_CANCEL_URL,
#         )
#
#         return redirect(checkout_session.url)


class CreateStripeCheckoutSessionView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        total_price = request.POST.get('total_price')

        if not total_price:
            return redirect('cart_detail')

        try:
            total_price = float(total_price)
        except ValueError:
            return redirect('cart_detail')

        try:
            cart = Cart.objects.get(user=request.user)
        except Cart.DoesNotExist:
            return redirect('cart_detail')

        # Create Stripe checkout session with metadata
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": "inr",
                        "unit_amount": int(total_price * 100),
                        "product_data": {
                            "name": "Cart Total",
                            "description": "Total items in your cart",
                        },
                    },
                    "quantity": 1,
                }
            ],
            mode="payment",
            billing_address_collection="required",
            shipping_address_collection={"allowed_countries": ["US","DE","FR","GB","CA"]},
            metadata={
                "user_id": request.user.id,
                "cart_id": cart.id,
                "total_price": total_price,
            },
            # success_url=f"{settings.PAYMENT_SUCCESS_URL}?session_id={{CHECKOUT_SESSION_ID}}",
            success_url = request.build_absolute_uri(reverse('SuccessView')) + '?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=settings.PAYMENT_CANCEL_URL,
        )

        return redirect(checkout_session.url)


def clear_cart(user):
    from .models import CartItem  # Import your CartItem model
    CartItem.objects.filter(cart__user=user).delete()


logger = logging.getLogger(__name__)


class SuccessView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        session_id = request.GET.get('session_id')

        if not session_id:
            logger.error("Missing session_id in request.")
            return redirect('cart_detail')

        try:
            # Retrieve the session details from Stripe
            session = stripe.checkout.Session.retrieve(session_id)
            logger.info(f"Stripe session retrieved: {session}")

            if session.get('payment_status') != 'paid':
                logger.warning("Payment status is not 'paid'.")
                return redirect('cart_detail')

            # Extract metadata
            user_id = session.metadata.get('user_id')
            cart_id = session.metadata.get('cart_id')
            total_price = float(session.metadata.get('total_price'))
            logger.info(f"Metadata: user_id={user_id}, cart_id={cart_id}, total_price={total_price}")

            # Validate user
            if int(user_id) != request.user.id:
                logger.error("Logged-in user does not match session metadata.")
                return redirect('cart_detail')

            # Retrieve the cart
            cart = Cart.objects.get(id=cart_id, user=request.user)
            logger.info(f"Cart retrieved: {cart}")

            # Create the order
            order = Order.objects.create(user=request.user, total_price=total_price)
            logger.info(f"Order created: {order.id}")

            # Add items to the order
            for item in cart.items.all():
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    unit_price=item.unit_price,
                    total_price=item.unit_price * item.quantity,
                )

            # Clear the cart
            cart.items.all().delete()
            logger.info(f"Cart cleared for user: {request.user.id}")

            # Retrieve billing and shipping addresses from Stripe session
            billing_address = session.get('customer_details', {}).get('address', {})
            shipping_address = session.get('shipping', {}).get('address', {})

            # Pass the addresses to the template
            return render(request, 'admin_view.html', {
                'order': order,
                'billing_address': billing_address,
                'shipping_address': shipping_address
            })

        except stripe.error.StripeError as e:
            logger.error(f"Stripe error: {e}")
            return render(request, 'error.html', {'message': "Payment verification failed."})

        except Cart.DoesNotExist:
            logger.error("Cart does not exist for the user.")
            return redirect('cart_detail')

        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return render(request, 'error.html', {'message': "An error occurred during order processing."})



def CancelView(request):
    return render(request, 'cancel.html')


def choosePay(request, pk):
    product = get_object_or_404(Product, id=pk)
    return render(request, 'choosePay.html', {'product': product})


def place_order(request):
    if request.method == 'POST':
        payment_method = request.POST.get('payment_method')
        total_price = request.POST.get('total_price')

        # Create the order object
        order = Order.objects.create(
            user=request.user,
            total_price=total_price
        )

        # Get the cart associated with the user
        cart, created = Cart.objects.get_or_create(user=request.user)

        # Loop through each cart item and create an OrderItem
        for item in cart.cartitem_set.all():
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                unit_price=item.unit_price,
                total_price=item.unit_price * item.quantity
            )

        # Create a Payment instance
        Payment.objects.create(
            order=order,
            user=request.user,
            payment_method=payment_method,
            amount=total_price,  # Assuming the total price is in decimal format
            status='P'  # Status as 'Pending'
        )

        # Optionally clear the cart after placing the order
        cart.cartitem_set.all().delete()

        # Redirect to an order confirmation page or similar
        return redirect('SuccessView', order_id=order.order_id)

    return render(request, 'place_order.html')


def order_confirmation(request, order_id):
    order = get_object_or_404(Order, order_id=order_id)
    return render(request, 'order_confirmation.html', {'order': order})




def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    endpoint_secret = 'whsec_maaVP94zNW5laPDHeGlYXVSeDU0XvMcP'

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        return HttpResponse(status=400)

    # Handle checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        # Retrieve the shipping details
        shipping_details = session.get('shipping', {})
        address = shipping_details.get('address', {})
        shipping_address = (
            f"{address.get('line1', '')}, {address.get('city', '')}, "
            f"{address.get('state', '')}, {address.get('postal_code', '')}, {address.get('country', '')}"
        )

        # Update the corresponding order with the shipping address
        order = Order.objects.get(order_id=session['client_reference_id'])
        order.shipping_address = shipping_address
        order.save()

    return HttpResponse(status=200)







