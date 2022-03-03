from django.views.generic import CreateView

from sauth.forms import ShopUserCreateForm
from sauth.models import ShopUser


class ShopUserCreateView(CreateView):
    model = ShopUser
    template_name = 'user/shopuser_form.html'
    success_url = '/user/login'
    form_class = ShopUserCreateForm
