from django.db import models

# Create your models here.

class hr_org_profile(models.Model):
    org_id = models.AutoField(primary_key=True)
    org_code = models.CharField(max_length=30)
    org_name = models.CharField(max_length=60)
    local_currency_code = models.ForeignKey('fnd.fnd_currencies', on_delete=models.CASCADE)
    reporting_currency_code = models.ForeignKey('fnd.fnd_currencies', on_delete=models.CASCADE)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()

class hr_org_location(models.Model):
    loc_id = models.AutoField(primary_key=True)
    org_id = models.ForeignKey(hr_org_profile, on_delete=models.CASCADE)
    loc_code = models.CharField(max_length=20)
    loc_name = models.CharField(max_length=60)
    local_currency_code = models.CharField(max_length=3)
    reporting_currency_code = models.CharField(max_length=3)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()

class hr_org_taxes_applicable(models.Model):
    tax_id = models.AutoField(primary_key=True)
    org_id = models.ForeignKey(hr_org_profile, on_delete=models.CASCADE)
    loc_id = models.ForeignKey(hr_org_location, on_delete=models.CASCADE)
    territory_tax_id = models.ForeignKey(fnd_territory_taxes, on_delete=models.CASCADE
    tax_number = models.CharField(max_length=30)
    description = models.CharField(max_length=60)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()
    
class hr_org_address(models.Model):
    org_add_id = models.AutoField(primary_key=True)
    org_id = models.ForeignKey(hr_org_profile, on_delete=models.CASCADE)
    loc_id = models.ForeignKey(hr_org_location, on_delete=models.CASCADE)
    address_line = models.CharField(max_length=300)
    country_code = models.ForeignKey('fnd.fnd_territories', on_delete=models.CASCADE)
    state_province_id = models.ForeignKey('fnd.fnd_state_province', on_delete=models.CASCADE)
    city_id = models.ForeignKey('fnd.fnd_cities', on_delete=models.CASCADE)
    address_type = models.CharField(max_length=30)    #Select from Lookup table
    active_date = models.DateField()
    inactive_date = models.DateField()
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()
    
class hr_org_contacts(models.Model):
    contact_id = models.AutoField(primary_key=True)
    org_id = models.ForeignKey(hr_org_profile, on_delete=models.CASCADE)
    loc_id = models.ForeignKey(hr_org_location, on_delete=models.CASCADE)
    contact_person = models.CharField(max_length=30)
    designation = models.CharField(max_length=30)
    active_date = models.DateField()
    inactive_date = models.DateField()
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()
    
class hr_org_contact_phones(models.Model):
    contact_phone_id = models.AutoField(primary_key=True)
    org_contacts = models.ForeignKey(hr_org_contacts, on_delete=models.CASCADE)
    land_line_1 = models.CharField(max_length=20)
    land_line_2 = models.CharField(max_length=20)
    mobile_1 = models.CharField(max_length=20)
    mobile_2 = models.CharField(max_length=20)
    personal_email = models.CharField(max_length=30)
    personal_email = models.CharField(max_length=30)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()
    
class hr_roles(models.Model):
    role_id = models.AutoField(primary_key=True)
    org_id = models.ForeignKey(hr_org_profile, on_delete=models.CASCADE)
    loc_id = models.ForeignKey(hr_org_location, on_delete=models.CASCADE)
    application_id = models.ForeignKey('fnd.fnd_applications', on_delete=models.CASCADE)
    role_name = models.CharField(max_length=30)    #select from Lookup Table
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()    
    
class hr_role_previleges(models.Model):
    role_priv_id = models.AutoField(primary_key=True)
    role_id = models.ForeignKey(hr_roles, on_delete=models.CASCADE)
    role_previleges = models.CharField(max_length=30)   #select from Lookup Table 
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()

class hr_role_functions(models.Model):
    role_function_id = models.AutoField(primary_key=True)
    role_previleges_id = models.ForeignKey(hr_role_previleges, on_delete=models.CASCADE)
    table_id = models.ForeignKey('fnd.fnd_tables', on_delete=models.CASCADE)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()

class hr_role_responsibilities(models.Model):
    role_resp_id = models.AutoField(primary_key=True)
    role_previleges_id = models.ForeignKey(hr_role_previleges, on_delete=models.CASCADE)
    menu_id = models.ForeignKey('fnd.d_fnmenus', on_delete=models.CASCADE)
    sub_menu_id = models.ForeignKey('fnd.fnd_sub_menus', on_delete=models.CASCADE)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()

class hr_user_category(models.Model):
    user_cat_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('fnd.fnd_users', on_delete=models.CASCADE)
    org_id = models.ForeignKey(hr_org_profile, on_delete=models.CASCADE)
    loc_id = models.ForeignKey(hr_org_location, on_delete=models.CASCADE)
    cost_center_id = models.ForeignKey('fa.fa_cost_centers', on_delete=models.CASCADE)
    user_category = models.CharField(max_length=30)    #select from Lookup Table
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()

class hr_user_previleges(models.Model):
    user_prev_id = models.AutoField(primary_key=True)
    user_category_id = models.ForeignKey(hr_user_category, on_delete=models.CASCADE)
    role_id = models.ForeignKey(hr_roles, on_delete=models.CASCADE)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()    
