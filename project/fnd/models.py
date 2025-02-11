from django.db import models

# Create your models here.

class fnd_users(models.Model):
    users_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_address = models.CharField(max_length=60)
    contact_no = models.CharField(max_length=20)
    user_name = models.CharField(max_length=30)    #Unique Key
    encrypted_password = models.CharField(max_length=30)
    activation_flag = models.CharField(max_length=30)
    start_date = models.DateField()
    validation_days = models.IntegerField()
    expiry_date = models.DateField()
    last_passw_updation_date = models.DateTimeFielf()
    passw_updation_count = models.IntegerField()
    forget_password_count = models.IntegerField()
    last_inactivation_date = models.DateTimeField()
    last_reactivation_date = models.DateTimeField()
    reactivation_count = models.IntegerField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()

class fnd_users_passw_recovery(models.Model):
    users_id = models.ForeignKey(fnd_users, on_delete=models.CASCADE)
    password = models.CharField(max_length=30)
    confirm_password = models.CharField(max_length=30)
    recovery_code = models.CharField(max_length=30)    #Select from Lookup Table
    enter_recovery_code = models.CharField(max_length=30)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    
class fnd_applications(models.Model):
    application_id = models.AutoField(primary_key=True)
    application_code = models.CharField(max_length=10)
    description = models.CharField(max_length=60)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()

class fnd_tables(models.Model):
    tables_id = models.AutoField(primary_key=True)
    application_id = models.ForeignKey(fnd_applications, on_delete=models.CASCADE)
    table_name = models.CharField(max_length=60)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()

class fnd_menus(models.Model):
    menu_id = models.AutoField(primary_key=True)
    application_id = models.ForeignKey(fnd_applications, on_delete=models.CASCADE)
    menu_name = models.CharField(max_lenth=60)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()

class fnd_sub_menus(models.Model):
    sub_menu_id = models.AutoField(primary_key=True)
    menu_id = models.ForiegnKey(fnd_menus, on_delete=models.CASCADE)
    sub_menu_name = models.CharField(max_length=60)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()    

class fnd_lookup_type(models.Model):
    lookup_type = models.CharField(max_length=30)    #Unique Key
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()  

class fnd_lookup_values(models.Model):
    lookup_type = models.CharField(max_length=30)
    lookup_value = models.CharField(max_length=30)    #Composite Primary key of (lookup_type and lookup_value)
    description = models.CharField(max_length=60)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()
    
class fnd_territories(models.Model):
    territory_id = models.AutoField(primary_key=True)
    country_code = models.IntegerField()
    country_name = models.CharField(max_length=60)
    alfa_2 = models.CharField(max_length=2)
    alfa_3 = models.CharField(max_length=3)
    iso_3166_2 = models.CharField(max_length=13)
    region = models.CharField(max_length=10)
    sub_region = models.CharField(max_length=35)
    intermediate_region = models.CharField(max_length=20)
    region_code = models.IntegerField()
    sub_region_code = models.IntegerField()
    intermediate_region_code = models.IntegerField()
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()  

class fnd_state_province(models.Model):
    state_id = models.AutoField(primary_key=True)
    territories_id = models.ForeignKey(fnd_territories, on_delete=models.CASCADE)
    state_province_name = models.CharField(max_length=60)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()  

class fnd_cities(models.Model):
    city_id = models.AutoField(primary_key=True)
    state_province_id = models.ForeignKey(fnd_state_province, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=60)
    postal_code = models.CharField(max_length=30)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()

class fnd_territory_taxes(models.Model):
    territory_tax_id = models.AutoField(primary_key=True)
    territories_id = models.ForeignKey(fnd_territories, on_delete=models.CASCADE)
    territory_tax_code = models.CharField(max_length=10)
    description = models.CharField(max_length=60)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()  

class fnd_currencies(models.Model):
    id = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=60)
    currency_code = models.CharField(max_length=3)
    numeric_code = models.IntegerField()
    currency_name = models.CharField(max_length=60)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()
    
class fnd_unit_of_measure(models.Model):
    uom_id = models.AutoField(primary_key=True)
    uom_code = models.CharField(max_length=3)
    uom_name = models.CharField(max_length=60)
    description = models.CharField(max_length=300)
    level_category = models.CharField(max_length=6)
    symbol = models.CharField(max_length=30)
    conversion_factor = models.CharField(max_length=60)
    status = models.CharField(max_length=3)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()

class fnd_transaction_type(models.Model):
    application_id = models.ForeignKey(fnd_applications, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=20) (primary_key=True)
    transaction_value = models.CharField(max_length=30)
    description = models.CharField(max_length=250)
   created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()    

class fnd_inv_category(models.Model):
    category_code = models.CharField(max_length=30) (Unique_key=True)
    category_name = models.CharField(max_length=60)
    description = models.CharField(max_length=250)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()

class fnd_party_class(models.Model):
    party_class = models.CharField(max_length=30)    #Unique Key
    description = models.CharField(max_length=250)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()

class fnd_party_subclass(models.Model):
    party_class = models.CharField(max_length=30)
    party_subclass = models.CharField(max_length=30)    #Unique Key
    description = models.CharField(max_length=250)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()

class fnd_regions(models.Model):
    region_code = models.AutoField(primary_key=True)
    region = models.CharField(max_length=30)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()

class fnd_subregions(models.Model):
    region_code = models.ForeignKey(fnd_regions, on_delete=models.CASCADE)
    subregion_code = models.AutoField(primary_key=True)
    subregion = models.CharField(max_length=30)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()

class fnd_territories(models.Model):
    country_code = models.AutoField(primary_key=True)
    alpha_2 = models.CharField(max_length=2)
    alpha_3 = models.CharField(max_length=3)
    iso_3166-2 = models.CharField(max_length=15)
    country_name = models.CharField(max_length=60)
    region_code = models.ForeignKey(fnd_regions, on_delete=models.CASCADE)
    subregion_code = models.AutoField(primary_key=True)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()
    
