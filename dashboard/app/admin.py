from django.contrib import admin

# Register your models here.
from django.contrib.admin import AdminSite, models
from django.shortcuts import render
from .models import Bottle, Order, Employee, Client, Revenue


class AdminDashboard(AdminSite):
    site_header = 'Water Delivery Dashboard'

    def index(self, request, extra_context=None):
        bottle_quantity = Bottle.objects.aggregate(models.Sum('quantity'))['quantity__sum'] or 0
        current_orders = Order.objects.filter(status='processing')
        completed_orders = Order.objects.filter(status='completed')
        busy_employees = Employee.objects.filter(status='busy')
        free_employees = Employee.objects.filter(status='free')
        clients = Client.objects.all()
        daily_revenue = Revenue.objects.filter(date='2023-12-10').aggregate(models.Sum('amount'))['amount__sum'] or 0
        weekly_revenue = Revenue.objects.filter(date__week='49').aggregate(models.Sum('amount'))['amount__sum'] or 0
        monthly_revenue = Revenue.objects.filter(date__month='12').aggregate(models.Sum('amount'))['amount__sum'] or 0

        context = {
            'bottle_quantity': bottle_quantity,
            'current_orders': current_orders,
            'completed_orders': completed_orders,
            'busy_employees': busy_employees,
            'free_employees': free_employees,
            'clients': clients,
            'daily_revenue': daily_revenue,
            'weekly_revenue': weekly_revenue,
            'monthly_revenue': monthly_revenue,
        }

        return render(request, 'admin/dashboard.html', context)


admin_site = AdminDashboard(name='admin_dashboard')

admin_site.register(Bottle)
admin_site.register(Order)
admin_site.register(Employee)
admin_site.register(Client)
admin_site.register(Revenue)
