from django.contrib.auth.models import User
from django.views.generic import ListView, FormView, TemplateView


# Create your views here.
from SmartDATE.forms.register import FormRegister
from SmartDATE.models import Personne


class IndexView(TemplateView):
    template_name='index.html'


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = FormRegister

    def form_valid(self, form):
        email = form.cleaned_data['username']
        password_1 = form.cleaned_data['password_1']
        password_2 = form.cleaned_data['password_2']
        user = User.objects.create_user(email=email,
                                 password=password_1)
        # raise ValidationError() "Leve une erreur de validation / Mais pas conseillé"
        person = Personne.object.create(user=user)
        person.save
        return super().form_valid(form)