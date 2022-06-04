from django.http import HttpResponse

class StripeWH_Handler:
    """Handle Stripe Webhooks"""

    def __init__(self, request):
        self.request = request

    def handel_event(self, event):
        """
        Handle a generic/unknowen/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandeled webhook recived: {event["type"]}',
            status=200
        )

    def handel_payment_intent_succeeded(self, event):
        """
        Handle the paymet_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        print(intent)
        return HttpResponse(
            content=f'Webhook recived: {event["type"]}',
            status=200
        )
    
    def handel_payment_intent_failed(self, event):
        """
        Handle the paymet_intent.payment_failed webhook from Stripe
        """

        return HttpResponse(
            content=f'Webhook recived: {event["type"]}',
            status=200
        )