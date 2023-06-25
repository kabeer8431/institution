from django.db import models
from datetime import datetime
# Manually Imported Modules
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Institution(models.Model):
    # Default generated Fields
    modifiedOn = models.DateTimeField(default=datetime.now())
    
    # Basic Required Fields
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    address = models.TextField()
    city = models.CharField(max_length=100, default='bangalore')
    state = models.CharField(max_length=50, default='karnataka')
    postal_code = models.IntegerField(default=560045)
    country = models.CharField(max_length=100, default='india')
    
    # Principal Details
    principal_name = models.CharField(max_length=100)
    principal_email = models.CharField(max_length=100)
    principal_phone = models.CharField(max_length=10)
    password = models.CharField(max_length=100)
    
    # Chairman Details
    owner_name = models.CharField(max_length=100)
    owner_email = models.CharField(max_length=100)
    owner_phone = models.CharField(max_length=10)
    password = models.CharField(max_length=100)
    
    # Additional / Misc Fields
    website = models.CharField(max_length=100, null=True)
    logo = models.ImageField(upload_to='database/Logos', 
                    null=True)
    motto = models.TextField()
    mission_statement = models.TextField()
    visibility = models.BooleanField(default=True)

class Department(models.Model):
    # Default generated Fields
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50)
    institution = models.ForeignKey(Institution, 
                    on_delete=models.CASCADE)
    office_location = models.TextField()
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    
    # Head of the Department Details
    hod_name = models.CharField(max_length=100)
    hod_email = models.CharField(max_length=100)
    hod_phone = models.CharField(max_length=10)
    
    # Additional Misc Fields
    description = models.TextField()
    specialization_area = models.CharField(max_length=100)
    budget_allocation = models.BigIntegerField(null=True)
    facilities_available = ArrayField(models.CharField(max_length=100),
                    blank=True,null=True)
    research_areas = ArrayField(models.TextField(),
                    blank=True,null=True)
    visibility = models.BooleanField(default=True)

class Staff(models.Model):
    name = models.CharField(max_length=100)
    dob  = models.DateField()
    doj = models.DateField(default=datetime.now())
    postal_code = models.IntegerField(default=560045)
    gender = models.CharField(max_length=6,
                    choices=[('M', 'Male'),
                             ('F', 'Female'),
                             ('O', 'Others')])
    address = models.TextField()
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=100)
    total_salary = models.IntegerField()
    role = models.CharField(max_length=10, default='T',
                    choices=[('C', 'Chancellor'),
                            ('VC', 'Vice Chanecellor'),
                            ('S', 'Secretary'),
                            ('D', 'Dean'),
                            ('P', 'Principal'),
                            ('VP', 'Vice Principal'),
                            ('M', 'Management'),
                            ('L', 'Librarian'),
                            ('FDO', 'Front Desk Office'), # ServiceDesk
                            ('F', 'Finance Secretary'),
                            ('ITS', 'IT Support'),
                            ('T', 'Teachers'),
                            ('SS', 'Support Staff'),
                            ('EC', 'Election Commitee'),
                            ('TT', 'Time Table Commitee'),
                            ('AC', 'Alumni Coordinators'),
                            ('S', 'Security')])
    alloted_leave = models.IntegerField()
    available_leave = models.IntegerField()
    files = models.FileField(upload_to='media/files/StudentFiles',null=True)
    # Bank details (for Salary)
    account_name = models.CharField(max_length=100,null=True)
    bank_name = models.CharField(max_length=50,null=True)
    account_number = models.CharField(max_length=20,null=True)
    ifsc_code = models.CharField(max_length=20,null=True)
    # Teacher Files Zipped (Optional)
    files = models.FileField(upload_to='media/files/StudentFiles',null=True)
    photo = models.ImageField(upload_to='media/files/StudentFiles',null=True)

class Course(models.Model):
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department,
                    on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff,
                    on_delete=models.CASCADE)
    code = models.CharField(max_length=20)
    description = models.TextField(null=True)
    visibility = models.BooleanField(default=True)
    
class Class(models.Model):
    name = models.CharField(max_length=100)
    semester = models.IntegerField(null=True)
    start_date = models.DateField(default=datetime.now())
    end_date = models.DateField()
    room = models.CharField(max_length=20)
    # Fees details of the student
    tuition_fees = models.IntegerField(default=0)
    admission_fees = models.IntegerField(default=0)
    registration_fees = models.IntegerField(default=0) # It is a fees paid each semester or academic year to register for courses. 
    exam_fees = models.IntegerField(default=0) 
    lab_fees = models.IntegerField(default=0)
    library_fees = models.IntegerField(default=0)
    sports_fees = models.IntegerField(default=0) # Fees Associated with sport facilities.
    technology_fees = models.IntegerField(default=0) # Covers technology resources.
    student_association_fees = models.IntegerField(default=0) # Student club, extra curricular fees and etc.
    trip_fees = models.IntegerField(default=0)
    special_program_fees = models.IntegerField(default=0)
    # Set visibility to false if class needs to be deleted
    visibility = models.BooleanField(default=True)

class ClassLink(models.Model):
    _class = models.ForeignKey(Class, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)

class TeachingBook(models.Model):
    class_link = models.ForeignKey(ClassLink, on_delete=models.CASCADE)
    _datetime = models.DateTimeField(default=datetime.now())

class StaffAttendance(models.Model):
    staff = models.ForeignKey(Staff,on_delete=models.CASCADE)
    _date = models.DateField(default=datetime.today())
    attendance = models.CharField(max_length=20,choices=[
                    ('P','Present'),
                    ('A','Absent'),
                    ('PL', 'Paid Leave'),
                    ('EL', 'Emergency Leave'),
                    ('CL', 'Casual Leave'),
                    ('PAL', 'Paternity Leave'),
                    ('ML', 'Maternity Leave')])

class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=100, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    _class = models.ForeignKey(Class,on_delete=models.CASCADE)
    dob = models.DateField()
    gender = models.CharField(max_length=6,
                    choices=[('M', 'Male'),
                             ('F', 'Female'),
                             ('O', 'Others')])
    address = models.TextField()
    city = models.CharField(max_length=100)
    postal_code = models.IntegerField(default=560045)
    student_phone = models.CharField(max_length=10)
    parent_phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100,null=True)
    # Parents Details
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    # Bank details (for certificates)
    account_name = models.CharField(max_length=100,null=True)
    bank_name = models.CharField(max_length=50,null=True)
    account_number = models.CharField(max_length=20,null=True)
    ifsc_code = models.CharField(max_length=20,null=True)
    # Fees detials of the Student
    fees_current_year = models.IntegerField()
    fees_previous_year_due = models.IntegerField(default=0)
    fees_total = models.IntegerField()
    fees_paid = models.IntegerField()
    fees_balance = models.IntegerField()
    # Student Files Zipped
    files = models.FileField(upload_to='media/files/StudentFiles',null=True)
    photo = models.ImageField(upload_to='media/files/StudentFiles',null=True)

class StudentAttendance(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    _datetime = models.DateTimeField(default=datetime.now())
    attendance = models.CharField(max_length=20,choices=[
                    ('P','Present'),
                    ('A','Absent'),
                    ('L', 'Leave')])

##############################################################
#######    Finance Department ################################
##############################################################
class Fees(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    _date = models.CharField(max_length=50)
    due_date = models.DateField()
    total = models.IntegerField()
    received = models.IntegerField()
    balance = models.IntegerField()

class Fine(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    reason = models.TextField()
    amount = models.IntegerField()
    status = models.CharField(max_length=10,choices=[
                    ('P', 'Paid'),
                    ('U', 'Unpaid')])


class Salary(models.Model):
    staff = models.ForeignKey(Staff,on_delete=models.CASCADE)
    _date = models.DateField(default=datetime.now())
    paid_year = models.IntegerField()
    paid_month = models.IntegerField(choices=[
                    (1, 'January'),
                    (2, 'February'),
                    (3, 'March'),
                    (4, 'April'),
                    (5, 'May'),
                    (6, 'June'),
                    (7, 'July'),
                    (8, 'August'),
                    (9, 'September'),
                    (10, 'October'),
                    (11, 'November'),
                    (12, 'December')])
    total = models.IntegerField()
    received = models.IntegerField()
    balance = models.IntegerField()

class Transactions(models.Model):
    name = models.CharField(max_length=100)
    institution = models.ForeignKey(Institution,on_delete=models.CASCADE)
    _date = models.DateField(default=datetime.today())
    description = models.TextField()
    transaction_type = models.CharField(max_length=30,
                    choices=[('I', 'Income'),
                             ('E', 'Expense'),
                             ('R', 'Refund')])
    amount = models.IntegerField(default=datetime.today().year)
    payment_method = models.CharField(max_length=50)
    invoice_number = models.CharField(max_length=100)
    staff = models.ForeignKey(Staff,null=True,
                    on_delete=models.CASCADE)
    student = models.ForeignKey(Student,null=True,
                    on_delete=models.CASCADE)

class FinancialReport(models.Model):
    institution = models.ForeignKey(Institution,on_delete=models.CASCADE)
    _date = models.DateField(default=datetime.now())
    report_type = models.CharField(max_length=20,
                    choices=[('P', 'Profit and Loss Statement'),
                        ('B', 'Balance Sheet'),
                        ('C', 'Cash Flow Statement'),
                        ('B', 'Budgetary Report'),
                        ('R', 'Revenue and Expense Analysis')])
    generated_by = models.ForeignKey(Staff,on_delete=models.CASCADE)
    report_file = models.FileField(upload_to='media/files/FinancialReports')


##############################################################
#######    Examination Department ############################
##############################################################

class Examination(models.Model):
    subject = models.ForeignKey(ClassLink,on_delete=models.CASCADE)
    exam_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=100,null=True)
    _type = models.CharField(max_length=100,
                    choices=[
                        ('A', 'Aptitude Test'),
                        ('E', 'Entrance Test'),
                        ('F', 'Final Exam'),
                        ('M', 'Mid Term Examination'),
                        ('MO', 'Monthly Test'),
                        ('P', 'Preparatory Exam'),
                        ('PR', 'Practical Exam'),
                        ('Q', 'Quarterly Test'),
                        ('UT', 'Unit Test'),])
    max_marks = models.IntegerField()
    passing_marks = models.IntegerField()

class Marks(models.Model):
    examination = models.ForeignKey(Examination,
                    on_delete=models.CASCADE)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    obtained_marks = models.IntegerField()

# class Admissions(models.Model): # It is not needed, the admissions is handled in Student table only.
#     pass

##############################################################
##################   Library Department  #####################
##############################################################

class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100,null=True)
    publication_date = models.DateField(null=True)
    category = models.CharField(max_length=100)
    availability = models.BooleanField(default=True)

class BookBorrowing(models.Model):
    book = models.ForeignKey(Books,on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff,on_delete=models.CASCADE)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    borrowing_date = models.DateField(default=datetime.now())
    return_date = models.DateField(null=True)
    status = models.CharField(max_length=10,default='B',
                        choices=[('B', 'Borrowed'),
                                ('R', 'Returned')])

##############################################################
######### Sports, Events and Facilities  #####################
##############################################################

class Sports(models.Model):
    pass

class Events(models.Model):
    pass

class Facilities(models.Model):
    pass