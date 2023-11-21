from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .models import Contact
from .form import ContactForm

# Create your views here.
def contact_us(request):
    form = ContavtForm(request.POST or None)
    if form_is_valid():
        save_form = form.save(commit=False)
        save_form.save()

    return render(request, 'contacts/contact_us.html')
