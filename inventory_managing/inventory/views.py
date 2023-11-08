from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, CreateView
from .forms import CategoryForm
from .models import Category

class InputDataView( CreateView):
	model = Category
	form_class = CategoryForm
	template_name =  'inventory/input_data.html'
	success_url = redirect("dashboard")

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['categories'] = Category.objects.all()
		return context

	def form_valid(self, form):
		#form.instance.user = self.request.user
		return super().form_valid(form)
	

class DashboardView(View):
    template_name = 'inventory/dashboard.html'
    def get(self, request):
        return render(request, self.template_name)
    def post(self, request):
        pass
	

	