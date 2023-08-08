from django.contrib import admin

# Manually Imported Modules
from home.models import *

# Register your models here.

# Basic Tables
admin.site.register(Institution)
admin.site.register(Department)
admin.site.register(Staff)
admin.site.register(Course)
admin.site.register(Class)
admin.site.register(ClassLink)
admin.site.register(TeachingBook)
admin.site.register(Student)

# Attendance Tables
admin.site.register(StaffAttendance)
admin.site.register(StudentAttendance)

# Financial Tables
admin.site.register(Fees)
admin.site.register(Fine)
admin.site.register(Salary)
admin.site.register(Transactions)
admin.site.register(FinancialReport)

# Examination Tables
admin.site.register(Examination)
admin.site.register(Marks)

# Library and Books
admin.site.register(Books)
admin.site.register(BookTransaction)

# Sports
admin.site.register(Sports)
admin.site.register(SportsTeam)
admin.site.register(SportsStudent)
admin.site.register(SportsCoach)
admin.site.register(SportsInventory)
admin.site.register(SportsInventoryTranasaction)

# Events
admin.site.register(Event)

# Hostel Management
admin.site.register(Hostel)
admin.site.register(HostelStudent)

# Inventory Management
admin.site.register(ClassInventory)
admin.site.register(DepartmentInventory)
admin.site.register(InstitutionInventory)
admin.site.register(HostelInventory)

# Scholarship Management
# Research, Development and Innovation