from django.shortcuts import render
from django.views.generic import TemplateView
from .api import tracking_dummy,tracking

# Create your views here.
class Tracking(TemplateView):
    template_name= 'tracking/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        resi = self.request.GET.get('resi')
        kurir = self.request.GET.get('courier')
        
        print(f'resi={resi}')
        print(f'kurir={kurir}')
        
        
        if resi and kurir:
            data= tracking_dummy(resi, kurir)
            print(data)
            if data['meta']['code']==200:
                context['data'] =data
                print('ada')
            
                
        return context
    
