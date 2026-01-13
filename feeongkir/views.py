from django.shortcuts import render
from django.views.generic import TemplateView
import requests
from django.http import JsonResponse
from .models import Province, City
from .api import get_cost
import math

class Ongkir(TemplateView):
    template_name = 'feeongkir/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        provinces = Province.objects.all()
        
        # Ambil Data      
        asal_prov_id = self.request.GET.get("asal-prov")
        asal_city_id = self.request.GET.get("asal-city")
        tujuan_prov_id = self.request.GET.get("tujuan-prov")
        tujuan_city_id = self.request.GET.get("tujuan-city")
        weight = int(self.request.GET.get("weight", 0)) 
        panjang= int(self.request.GET.get("panjang",0))
        lebar= int(self.request.GET.get("lebar",0))
        tinggi= int(self.request.GET.get("tinggi",0))
        couriers = self.request.GET.getlist("couriers")
        
        # Hitung Ongkir by Volume
        ongkir_volume= math.ceil(panjang * lebar * tinggi /6000)
        print(f'ongkir_volume : {ongkir_volume}')
        print(f'ongkir_berat : {weight}')
        
        # Inisialisasi form_id
        asal_prov = None
        asal_city = None
        tujuan_prov = None
        tujuan_city = None
        
        if asal_prov_id:
            asal_prov = Province.objects.get(id=asal_prov_id)
        if asal_city_id:
            asal_city = City.objects.get(id=asal_city_id)
        if tujuan_prov_id:
            tujuan_prov = Province.objects.get(id=tujuan_prov_id)
        if tujuan_city_id:
            tujuan_city = City.objects.get(id=tujuan_city_id)
            
        # Pengecekan Berat Paket
        if weight > ongkir_volume:
            weight_taken = weight
        else:
            weight_taken = ongkir_volume
            
        weight_taken_gr = weight_taken * 1000
        
        cost_price=[]
        
        cost_price_json = get_cost(asal_city_id,tujuan_city_id,weight_taken_gr,couriers)
        if cost_price_json.get("meta", {}).get("code") == 200:
            cost_price = cost_price_json.get("data", [])
            
        context["provinces"] = provinces
        context["asal_prov"] = asal_prov
        context['asal_city'] = asal_city
        context['tujuan_prov'] = tujuan_prov
        context['tujuan_city'] = tujuan_city
        context['weight'] = weight_taken
        context['cost_price']= cost_price

        return context


def ajax_get_cities(request):
    province_id= request.GET.get('province_id')
    cities = City.objects.filter(province_id=province_id)
    return JsonResponse({
        "cities": [
            {"id": c.id, "name": c.name}
            for c in cities
        ]
    })







