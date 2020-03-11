from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import Stock
from .forms import StockForm


# Create your views here.



def home(request):
    

    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&interval=5min&apikey=yourapikey'

    

    if request.method == "POST":
        form = StockForm(request.POST)
        form.save()

    form = StockForm()    
    

    all_stock = Stock.objects.all()
    stock_data = []
 
    for each_stock in all_stock:
        r = requests.get(url.format(each_stock)).json()
        dataForAllDays = r['Time Series (Daily)']
        DATE =each_stock.date
        DS = dataForAllDays[DATE]
        print(DS)
        stocks = {
            'Name': each_stock.code,
            'Open': DS['1. open'],
            'High': DS['2. high'],
            'Low': DS['3. low'],
            'Close': DS['4. close'],
            'Volume': DS['5. volume'],
        }

        stock_data.append(stocks)
    
    print(stock_data)
    context = {'stock_data':stock_data, 'form' : form}
    
    return render(request, 'scraper/index.html',context)
    


