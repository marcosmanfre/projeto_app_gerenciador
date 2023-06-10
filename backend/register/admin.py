from django.contrib import admin
from register.models import Employees

@admin.register(Employees)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('EmployeeId', 'EmployeeName', 'Department', 'Role', 'DateOfJoining')
    list_filter = ('Department',)
    search_fields = ('EmployeeName', 'Department')