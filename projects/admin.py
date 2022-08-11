from django.contrib import admin
from .models import (TypeProjects, Projects)
from clients.models import (Contacts, Payment, Status, Clients)
from creators.models import (Positions, PaymentType, Creators)

admin.site.register(TypeProjects)
admin.site.register(Projects)

admin.site.register(Contacts)
admin.site.register(Payment)
admin.site.register(Status)
admin.site.register(Clients)

admin.site.register(Positions)
admin.site.register(PaymentType)
admin.site.register(Creators)