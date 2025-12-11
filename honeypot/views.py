

# Create your views here.
from django.http import HttpResponse
from django.utils import timezone


def fake_admin(request):
    ip = request.META.get("REMOTE_ADDR")
    time = timezone.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"[HONEYPOT] Fake admin accessed: IP={ip} TIME={time}")

    return HttpResponse(
        "<h2>Page not found</h2>",
        status=404
    )
