import datetime
from django.shortcuts import render, redirect, reverse
from main.forms import joshShopEntryForm
from main.models import joshItem
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


@login_required(login_url='/login')
def show_main(request):
    products = [
    {'name': 'lipgloss', 'price': 1000000, 'description': 'sun glaze lipgloss', 'quantity': 100},
    {'name': 'blush on', 'price': 1000000, 'description': 'sugar plum blush on', 'quantity': 89},
    ]
    context = {
        'name': request.user.username,
        'products': products,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def create_item_entry(request):
    form = joshShopEntryForm(request.POST or None)
    if (form.is_valid() and request.method == "POST"):
        josh_item_entry = form.save(commit=False)
        josh_item_entry.user = request.user
        josh_item_entry.save()
        return redirect('main:show_main')
    context = {'form': form}
    return render(request,'create_item_entry.html', context)

@csrf_exempt
@require_POST
def add_item_entry_ajax(request):
    name = request.POST.get("name")
    price = request.POST.get("price")
    description = request.POST.get("description")
    quantity = request.POST.get("quantity")
    user = request.user

    new_item = joshItem(
        name=name, 
        price=price,
        description=description,
        quantity=quantity,
        user=user
    )
    new_item.save()

    return HttpResponse(b"CREATED", status=201)

def edit_item(request, id):
    # Get mood entry berdasarkan id
    mood = joshItem.objects.get(pk = id)

    # Set mood entry sebagai instance dari form
    form = joshShopEntryForm(request.POST or None, instance=mood)
    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    context = {'form': form}
    return render(request, "edit_item.html", context)

def delete_item(request,id):
    item = joshItem.objects.get(id=id)
    item.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def show_xml(request):
    data = joshItem.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = joshItem.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type ="application/json")

def show_xml_by_id(request, id):
    data = joshItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = joshItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.error(request, "Invalid username or password. Please try again.")
   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response