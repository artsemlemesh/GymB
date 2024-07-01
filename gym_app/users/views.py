import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.decorators import api_view

from rest_framework.response import Response
stripe.api_key = settings.STRIPE_SECRET_KEY

@csrf_exempt
@api_view(['POST'])
def create_payment_intent(request):
   
    try:
        amount = request.data.get('amount')

        # Assume stripe.PaymentIntent.create is properly set up
        payment_intent = stripe.PaymentIntent.create(
            amount=1099,
            currency='usd'
        )

        return Response({
            'clientSecret': payment_intent.client_secret
        })
    except Exception as e:
        return Response({'error': str(e)}, status=400)
    # if request.method == 'POST':
    #     data = json.loads(request.body)
    #     print(data, 'DJANGO DATA')
    #     try:
    #         # Create a PaymentIntent with the order amount and currency
    #         intent = stripe.PaymentIntent.create(
    #             amount=data['amount'],
    #             currency='usd',
    #             automatic_payment_methods={
    #                 'enabled': True,
    #             },
    #         )
    #         return JsonResponse({'clientSecret': intent['client_secret']})
    #     except Exception as e:
    #         return JsonResponse({'error': str(e)}, status=403)
