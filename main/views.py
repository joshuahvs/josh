from django.shortcuts import render

# Create your views here.
def show_main(request):

    products = [
    {'name': 'lipgloss', 'price': 1000000, 'description': 'sun glaze lipgloss', 'quantity': 100},
    {'name': 'blush on', 'price': 1000000, 'description': 'sugar plum blush on', 'quantity': 89}
    ]

    return render(request, "main.html", {'products': products})
