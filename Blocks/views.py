from django.shortcuts import render
from . import block

def index(request):
    if request.method == 'POST':
        lender = request.POST['lender']
        amount =  request.POST['amount']
        borrower =  request.POST['borrower']
        block.create_block(name=lender, amount=amount, to=borrower)
        print("good")
    return render(request, "index.html")

def check(request):
    result = block.check_integrity()
    print(result)
    return render(request, "index.html", { 'results': result })