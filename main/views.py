from django.shortcuts import render

# Create your views here.
def show_main(request):

    products = [
    {'name': 'lipgloss', 'price': 1000000, 'description': 'sun glaze lipgloss', 'quantity': 100},
    {'name': 'blush on', 'price': 1000000, 'description': 'sugar plum blush on', 'quantity': 89}
    ]

    return render(request, "main.html", {'products': products})

    # products = [{
    #     'name': 'lipgloss',
    #     'price': 10000000,
    #     'description': 'hellooo',
    #     'quantity': 1
    # },
    # {
    #     'name': 'blush on',
    #     'price': 10000000,
    #     'description': 'lol',
    #     'quantity': 1
    # }]

    # return render(request, "main.html", products)
