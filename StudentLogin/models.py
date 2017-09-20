from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from multiselectfield import MultiSelectField


# Create your models here.
ELIGIBILITY_CHOICES = (
    ('Y','Eligible'),
    ('N','Not Eligible'),
    ('NI','Not Interested'),
    ('NR','Not Recommended'),
)
COURSE_CHOICES = (
    ('BTech','BTech'),
    ('MTech','MTech'),
)
BRANCHES = (
    ('Btech_CSE','Btech_CSE'),
    ('ECE','ECE'),
    ('MECH','MECH'),
    ('EEE','EEE'),
    ('Civil','Civil'),
    ('Chem','Chem'),
    ('EIE','EIE'),
    ('AeroSpace','AeroSpace'),
    ('Mtech_CSE','Mtech_CSE'),
    ('Control & Instrumentation Engineering','Control & Instrumentation Engineering'),
    ('Cyber Security Systems & Networks','Cyber Security Systems & Networks'),
    ('Power & Energy','Power & Energy'),
    ('Robotics & Automation','Robotics & Automation'),
    ('Thermal & Fluids','Thermal & Fluids'),
    ('VLSI Design','VLSI Design'),
    ('Wireless Networks & Applications','Wireless Networks & Applications'),
    ('Communication Engineering & Signal Processing','Communication Engineering & Signal Processing'),
    ('Computer Science & Engineering - Data Science','Computer Science & Engineering - Data Science'),
    ('Embedded Systems','Embedded Systems'),
    ('Power Electronics','Power Electronics'),
    ('Thermal Science & Energy Systems','Thermal Science & Energy Systems'),
    ('Automotive Engineering','Automotive Engineering'),
    ('Biomedical Engineering','Biomedical Engineering'),
    ('Communication Engineering & Signal Processing','Communication Engineering & Signal Processing'),
    ('Computational Engineering & Networking','Computational Engineering & Networking'),
    ('Control & Instrumentation Engineering','Control & Instrumentation Engineering'),
    ('Cyber Security','Cyber Security'),
    ('Engineering Design','Engineering Design'),
    ('Manufacturing Engineering','Manufacturing Engineering'),
    ('Material Science','Material Science'),
    ('Remote Sensing & Wireless Sensor Networks','Remote Sensing & Wireless Sensor Networks'),
    ('Renewable Energy Technologies','Renewable Energy Technologies'),
    ('Structural & Construction Engineering','Structural & Construction Engineering')
)
STATUS = (
    ('Applied','Applied'),
    ('Placed','Placed'),
    ('Not Placed', 'Not Placed'),
)
GENDER = (
    ('M','Male'),
    ('F','Female')
)
STAY_CHOICES = (
    ('H','Hosteler'),
    ('D','DayScholar')
)
JOB_CHOICES = (
    ('IT','IT sector'),
    ('CORE','Core engg'),
    ('others','others')
)
BOARD = (
    ('state','state'),
    ('CBSE','CBSE'),
    ('ICSC','ICSC')
)


class Student_details(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    middleName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    eligibility = models.CharField(choices=ELIGIBILITY_CHOICES, max_length=50)
    course = models.CharField(choices=COURSE_CHOICES, max_length=50)
    branch = models.CharField(choices=BRANCHES, max_length=50)
    rollno = models.CharField(max_length=50)
    massOffer = models.IntegerField(default=0)
    PlacementStatus = models.CharField(choices=STATUS,max_length=50)
    PlacementStatusFinal = models.BooleanField(default=True)
    campus = models.CharField(max_length=50)
    gender = models.CharField(choices=GENDER, max_length=50)
    DOB = models.DateField()
    tenth_percentage = models.IntegerField(default=0)
    twelth_percentage = models.IntegerField(default=0)
    s1 = models.IntegerField(default=0)
    s2 = models.IntegerField(default=0)
    s3 = models.IntegerField(default=0)
    s4 = models.IntegerField(default=0)
    s5 = models.IntegerField(default=0)
    s5 = models.IntegerField(default=0)
    s6 = models.IntegerField(default=0)
    CGPA = models.IntegerField(default=0)
    no_of_current_Arrears = models.IntegerField()
    no_of_history_Arrears = models.IntegerField()
    stay = models.CharField(choices=STAY_CHOICES, max_length=50)
    Internship_details = models.TextField()
    job_Interest = models.CharField(choices=JOB_CHOICES, max_length=50)
    tenth_board = models.CharField(choices=BOARD, max_length=50)
    tenth_year_of_passing = models.IntegerField()
    twelth_board = models.CharField(choices=BOARD, max_length=50)
    twelth_year_of_passing = models.IntegerField()
    gap_in_studies_with_reason = models.TextField()
    permanent_address = models.TextField()
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    pin = models.IntegerField()
    contact = models.IntegerField()
    email_id = models.EmailField()
    UG_marks = models.IntegerField()
    UG_aggr = models.IntegerField()
    course_PG = models.CharField(max_length=50)
    UG_specialiazation = models.CharField(max_length=50)
    UG_college = models.CharField(max_length=50)
    UG_year_of_passing = models.IntegerField()
    gate_score = models.IntegerField()
    Applicable_to_PG = models.CharField(max_length=50)
    ob_profile = models.CharField(max_length=50)
    expr = models.CharField(max_length=50)

def __str__(self):
    return self.user
