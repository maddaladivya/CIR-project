from __future__ import unicode_literals

from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.


ELIGIBILITY_CHOICES = (
    ('BTech','BTech'),
    ('MTech','MTech'),
)
BRANCHES = (
    ('BT-CSE','BT-CSE'),
    ('ECE','ECE'),
    ('MECH','MECH'),
    ('EEE','EEE'),
    ('Civil','Civil'),
    ('Chem','Chem'),
    ('EIE','EIE'),
    ('AeroSpace','AeroSpace'),
    ('MT-CSE','MT-CSE'),
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

class Company_details(models.Model):
    comp_name = models.CharField(max_length=50)
    comp_ctc = models.IntegerField(default=0)
    comp_date = models.DateField(default=0)
    eligibility = MultiSelectField(choices=ELIGIBILITY_CHOICES)
    branch = MultiSelectField(choices=BRANCHES)

    def __str__(self):
        return self.comp_name

