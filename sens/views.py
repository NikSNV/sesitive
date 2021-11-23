from django.shortcuts import render
from random import randint

from sens.forms import SensForm


def get_sens(request):
    if request.method == 'POST':
        form = SensForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)

            if 'number' in request.session:
                request.session['number'] = f"{request.session['number']}, {form.cleaned_data['number']}"
            else:
                request.session['number'] = ''

            if 'sens1True' not in request.session:
                request.session['sens1True'] = 0
            if 'sens1' in request.session:
                if int(request.session['sens1'][-2:]) == form.cleaned_data['number']:
                    request.session['sens1True'] += 1
                else:
                    request.session['sens1True'] -= 1

            if 'sens2True' not in request.session:
                request.session['sens2True'] = 0
            if 'sens1' in request.session:
                if int(request.session['sens2'][-2:]) == form.cleaned_data['number']:
                    request.session['sens2True'] += 1
                else:
                    request.session['sens2True'] -= 1

    else:
        print(f'Это сессия: {request.session}')
        print(request.user)
        if 'sens1' in request.session:
            request.session['sens1'] = f"{request.session['sens1']}, {randint(10, 99)}"
            sens1 = request.session['sens1']
            request.session['sens2'] = f"{request.session['sens2']}, {randint(10, 99)}"
        else:
            print('empty!!!')
            request.session['sens1'] = ''
            request.session['sens2'] = ''

        if 'number' not in request.session:
            request.session['number'] = ''
        if 'sens1True' not in request.session:
            request.session['sens1True'] = 0
        if 'sens2True' not in request.session:
            request.session['sens2True'] = 0

        # print(f"Это последнее число sens1: {int(request.session['sens1'][-2:])}")
        form = SensForm()

    return render(request, 'sens/sens_houm.html',
                  {'title': 'Загадайте 2-х значное число и нажмите "Я загадал!":', 'sens1': request.session['sens1'][1:],
                   'sens2': request.session['sens2'][1:], 'number': request.session['number'][1:],
                   'sens1True': request.session['sens1True'], 'sens2True': request.session['sens2True'], 'form': form})
