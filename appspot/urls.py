"""appspot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

import appspot.auto_texts.scaffolding
import appspot.auto_text_fields.scaffolding
import appspot.addresses.scaffolding
import appspot.assignments.scaffolding
import appspot.case_contacts.scaffolding
import appspot.case_equipments.scaffolding
import appspot.case_expenses.scaffolding
import appspot.case_sequences.scaffolding
import appspot.case_status.scaffolding
import appspot.case_types.scaffolding
import appspot.case_videos.scaffolding
import appspot.companies.scaffolding
import appspot.contractor_rates.scaffolding

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

auto_text_crud = appspot.auto_texts.scaffolding.Auto_textCrudManager()
urlpatterns += auto_text_crud.get_url_patterns()
auto_text_field_crud = appspot.auto_text_fields.scaffolding.Auto_text_fieldCrudManager()
urlpatterns += auto_text_field_crud.get_url_patterns()
address_crud = appspot.addresses.scaffolding.AddressCrudManager()
urlpatterns += address_crud.get_url_patterns()
assignment_crud = appspot.assignments.scaffolding.AssignmentCrudManager()
urlpatterns += assignment_crud.get_url_patterns()
case_contact_crud = appspot.case_contacts.scaffolding.Case_contactCrudManager()
urlpatterns += case_contact_crud.get_url_patterns()
case_equipment_crud = appspot.case_equipments.scaffolding.Case_equipmentCrudManager()
urlpatterns += case_equipment_crud.get_url_patterns()
case_expenses_crud = appspot.case_expenses.scaffolding.Case_expenseCrudManager()
urlpatterns += case_expenses_crud.get_url_patterns()
case_sequences_crud = appspot.case_sequences.scaffolding.Case_sequenceCrudManager()
urlpatterns += case_sequences_crud.get_url_patterns()
case_status_crud = appspot.case_status.scaffolding.Case_statusCrudManager()
urlpatterns += case_status_crud.get_url_patterns()
case_type_crud = appspot.case_types.scaffolding.Case_typeCrudManager()
urlpatterns += case_type_crud.get_url_patterns()
company_crud = appspot.companies.scaffolding.CompanyCrudManager()
urlpatterns += company_crud.get_url_patterns()
contractor_rate_crud = appspot.contractor_rates.scaffolding.Contractor_rateCrudManager()
urlpatterns += contractor_rate_crud.get_url_patterns()











