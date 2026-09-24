from django.shortcuts import render
from .models import Contact


def contact_list(request):
    contacts = Contact.objects.all().order_by("name")
    return render(request, "contacts/contact_list.html", {"contacts": contacts})
