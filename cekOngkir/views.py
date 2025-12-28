from django.shortcuts import render
from django.views.generic import TemplateView
import requests
from .api import get_prov,get_cities
from django.http import JsonResponse


NAME_MAPPING = {
    "NANGGROE ACEH DARUSSALAM (NAD)": "Aceh",
    "NUSA TENGGARA BARAT (NTB)" :"NTB",
    "NUSA TENGGARA TIMUR (NTT)" :"NTT"
}

class Ongkir(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        response = get_prov()
        provinces = response.get("data", [])
        if provinces:
            print(provinces)
        else:
            print('data kosong')

        context["provinces"] = provinces
        

        return context



def ajax_get_cities(request):
    province_id = request.GET.get("province_id")

    if not province_id:
        return JsonResponse({"cities": []})

    response = get_cities(province_id)
    cities = response.get("data", [])

    return JsonResponse({"cities": cities})





