from django.shortcuts import render
from .models import Portfolio

def portfolio_view(request):
    portfolios = Portfolio.objects.all()
    return render(request, 'portfolio.html', {'portfolios': portfolios})
