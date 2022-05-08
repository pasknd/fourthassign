from django.shortcuts import render,redirect
from django.http import HttpResponse
import pymongo
connection=pymongo.MongoClient("localhost",27017)
database=connection["myDB"]
collection=database["myCollect"]


def home(request):
    return render(request,'registerr.html')


def add(request):



    hname=request.GET['name']
    hpasscode=request.GET['passcode']
    tpasscode=int(hpasscode)
    info=collection.find_one({'username':hname})



    for i in info:

        print(i)



    if hname==info['username'] and tpasscode==info['passcode']:
            id, username, passcode, amount = info['_id'], info['username'], info['passcode'], info['amount']
            return render(request,'login.html',{'id':id,'username':username,'passcode':passcode,'amount':amount})
    else:
        return render(request,'registerr.html')










def register(request):
    lname = request.POST['username']
    passcode1 = request.POST['passcode']
    passcode2 = request.POST['passcode2']
    if passcode1==passcode2:
        passcode=int(passcode1)
        data={'username':lname,'passcode':passcode,'amount':30000}
        content=collection.insert_one(data)
        return render(request, 'home.html')

        #return render(request, 'result.html',{'username':lname,'passcode':passcode,'passcode2':passcode,'amount':30000})

    if passcode1!=passcode2:
        return HttpResponse('confirm password again')














