from django.shortcuts import render, redirect
from main.forms import joshShopEntryForm
from main.models import joshItem
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):
    josh_item_entries = joshItem.objects.all()
    products = [
    {'name': 'lipgloss', 'price': 1000000, 'description': 'sun glaze lipgloss', 'quantity': 100},
    {'name': 'blush on', 'price': 1000000, 'description': 'sugar plum blush on', 'quantity': 89},
    ]
    context = {
        'products': products,
        'josh_item_entries': josh_item_entries
    }

    return render(request, "main.html", context)

def create_item_entry(request):
    form = joshShopEntryForm(request.POST or None)
    if (form.is_valid() and request.method == "POST"):
        form.save()
        return redirect('main:show_main')
    context = {'form': form}
    return render(request,'create_item_entry.html', context)

def show_xml(request):
    data = joshItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = joshItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type ="application/json")

def show_xml_by_id(request, id):
    data = joshItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = joshItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")