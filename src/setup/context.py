from setup.models import SiteSetup

def site_setup(request):
    setup = SiteSetup.objects.first()
    return {
        "site_setup": setup
    }