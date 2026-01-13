from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Analytics(TemplateView):
    template_name= 'analytics/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['deskripsi']='Menyajikan perbandingan performa layanan ekspedisi berdasarkan rating pelanggan, ulasan Google Maps, dan analisis masalah pengiriman di berbagai kota besar Indonesia.'
            
        return context