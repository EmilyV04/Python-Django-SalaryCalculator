from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def result(request):
    salario            = int(request.POST.get("salario",False))
    otros_ingresos     = int(request.POST.get("otros_ingresos",False))
    aporte_pension     = int(request.POST.get("aporte_pension",False))
    pagos_salud        = int(request.POST.get("pagos_salud",False))
    
    if salario <= 2000000:
        subsidio_transporte = 117172
    else:
        subsidio_transporte = 0

    total_ingreso_mensual = salario + otros_ingresos
    aporte_fpv            = aporte_pension
    salud_obligatoria     = (float(salario) * 0.04) + (float(otros_ingresos) * 0.024)
    salud_prepagada       = pagos_salud
    pension_obligatoria   = (float(salario) * 0.04) + (float(otros_ingresos) * 0.024)
    compensacion         = (total_ingreso_mensual + subsidio_transporte) - (salud_obligatoria + salud_prepagada + aporte_fpv + pension_obligatoria)

    return render(request,"result.html", {"total_ingreso_mensual" : total_ingreso_mensual,
                                        "salud_obligatoria" : salud_obligatoria,
                                        "salud_prepagada" : salud_prepagada,
                                        "pension_obligatoria" : pension_obligatoria,
                                        "aporte_fpv" : aporte_fpv,
                                        "compensacion" : compensacion})
