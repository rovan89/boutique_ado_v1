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
            content=f'Webhook recived: {event["type"]}',
            status=200
        )