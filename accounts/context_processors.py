
from vendor.models import Vendor

def get_vendor(request):
    if request.user.is_authenticated:
        vendor = Vendor.objects.get(user=request.user)
        return {'vendor': vendor}
    return {}

