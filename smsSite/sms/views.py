from django.core.exceptions import ValidationError
from django.shortcuts import HttpResponse
from django.shortcuts import render

# Create your views here.
from sms.forms import *
from sms.models import sms
from sms.serializer import SmsSerializer


def index(request):
    print(request.method)
    test = sms.objects.all()
    if request.method == 'POST':
        form = SendSmsForm(request.POST)
        form1 = DelSmsForm(request.POST)
        if form1.is_valid():
            for i in test:
                if i.message == form1.cleaned_data['message']:
                    del_sms = sms(i.id).delete()
        if form.is_valid():
            buff = form.cleaned_data
            flag = True
            for i in test:
                if i.message == form.cleaned_data['message']:
                    print(i.message)
                    flag = False
                    print(form.cleaned_data['message'])
            if flag:
                new_sms = sms(**buff).save()
        form = SendSmsForm()
        form1 = DelSmsForm()
    else:
        form = SendSmsForm()
        form1 = DelSmsForm()
    return render(request, 'sms/main.html',{'form1': form1,'form': form, 'content': test})

def get_single_sms (request):
    _id=request.GET.get('id',None)
    if not _id:
        raise ValidationError('ID not found')
    _id = int(_id)
    _sms = sms.objects.get(id=_id)
    serializer = SmsSerializer(_sms)
    return HttpResponse(str(serializer.serialize()))
