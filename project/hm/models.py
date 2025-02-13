from django.db import models

# Create your models here.

class hm_guest_profile(models.Model):
    guest_profile_id = models.AutoField(primary_key=True)
    org_id = models.ForeignKey('hr.hr_org_profile', on_delete=models.CASCADE)
    loc_id = models.ForeignKey('hr.hr_org_location', on_delete=models.CASCADE)
    guest_code = models.CharField(max_length=20)
    guest_identifier = models.CharField(max_length=30)    #From Lookup Table as IDENTIFIER
    identifier_number = models.CharField(max_length=30)
    solutation = models.CharField(max_length=30)    #From Lookup Table
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mobile_no = models.CharField(max_length=20)
    address_line = models.CharField(max_length=300)
    country_code = models.ForeignKey('fnd.fnd_territories', on_delete=models.CASCADE)
    state_province_id = models.ForeignKey('fnd.fnd_state_province', on_delete=models.CASCADE)
    city_id = models.ForeignKey('fnd.fnd_cities', on_delete=models.CASCADE)
    gender = models.CharField(max_length=30)    #From Lookup Table
    profession = models.CharField(max_length=30)    #From Lookup Table
    nationality = models.CharField(max_length=30)    #From Lookup Table
    language = models.CharField(max_length=30)    #From Lookup Table
    party_id = models.ForeignKey('inv.inv_parties', on_delete=models.CASCADE)    #Company
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()

class res_reservation(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    org_id = models.ForeignKey('hr.hr_org_profile', on_delete=models.CASCADE)
    loc_id = models.ForeignKey('hr.hr_org_location', on_delete=models.CASCADE)
    reservation_number = models.IntegerField() #Unique Key
    reservation_date = models.DateField()
    reservation_status = models.CharField(max_length=30)    #From Lookup Table
    reservation_guarantees = models.CharField(max_length=30)    #From Lookup Table
    source_group = models.CharField(max_length=30)    #From Lookup Table
    source_codes = models.CharField(max_length=30)    #From Lookup Table
    turnaway_group = models.CharField(max_length=30)    #From Lookup Table
    turnaway_reasons = models.CharField(max_length=30)    #From Lookup Table
    no_of_room = models.IntegerField()
    no_of_events = models.IntegerField()
    block_required = models.CharField(max_length=30)
    payment_term = models.CharField(max_length=30)
    reserved_by = models.CharField(max_length=30)
    contact_number = models.CharField(max_length=20)
    email_address = models.CharField(max_length=60)
    parties_profile_id = models.ForeignKey('inv.inv_parties_profile', on_delete=models.CASCADE)
    remarks = models.CharField(max_length=60)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()

class res_reservation_status(models.Model):
    reservation_id = models.ForeignKey(res_reservation, on_delete=models.CASCADE)
    reservation_status = models.CharField(max_length=30)    #Update from res_reservation table
    status_updation_date = models.DateTimeField()
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    
class evt_event_order(models.Model):
    event_order_id = models.AutoField(primary_key=True)
    reservation_id = models.ForeignKey(hm_reservation, on_delete=models.CASCADE)
    inv_category_id = models.ForeignKey('inv.inv_category', on_delete=models.CASCADE)    #Example in Lookup Table EVENT_TYPE
    inv_category_set_id = models.ForeignKey('inv.inv_category_sets', on_delete=models.CASCADE)    #Example in Lookup Table EVENTS
    inventory_id = models.ForeignKey('inv.inv_inventory', on_delete=models.CASCADE)
    description = models.CharField(max_length=250)
    event_date_from = models.DateField()
    event_date_to = models.DateField()
    event_time_from = models.CharField(max_length=10)
    event_time_to = models.CharField(max_length=10)
    expected_participant_number = models.IntegerField()
    actual_participant_number = models.IntegerField()
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()

class evt_event_schedule(models.Model):
    event_schedule_id = models.AutoField(primary_key=True)
    event_order_id = models.ForeignKey(hm_event_order, on_delete=models.CASCADE)
    schedule_date = models.DateField()
    schedule_time = models.CharField(max_length=10)
    inv_category_id = models.ForeignKey('inv.inv_category', on_delete=models.CASCADE)    #Example word ENTERTAINMENT
    inv_category_set_id = models.ForeignKey('inv.inv_category_sets', on_delete=models.CASCADE)    #Entered by user or already selected default from fnd_entertainment_type Table in inv_category table
    inventory_id = models.ForeignKey('inv.inv_inventory', on_delete=models.CASCADE)    #Entered by user or already selected default from fnd_entertainments Table in inv_inventory table
    entertainment_rate = models.IntegerField()
    inventory_packing_id = models.ForeignKey('inv.inv_inventory_packing', on_delete=models.CASCADE)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()

class evt_event_food(models.Model):
    event_food_id = models.AutoField(primary_key=True)
    event_schedule_id = models.ForeignKey(hm_event_schedule, on_delete=models.CASCADE)
    inv_category_id = models.ForeignKey('inv.inv_inventory_categories', on_delete=models.CASCADE)
    inv_category_set_id = models.ForeignKey('inv.inv_category_sets', on_delete=models.CASCADE)
    inventory_id = models.ForeignKey('inv.inv_inventory', on_delete=models.CASCADE)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()

class res_complementory_services(models.Model):
    complementory_services_id = models.AutoField(primary_key=True)
    reservation_id = models.ForeignKey(hm_reservation, on_delete=models.CASCADE)
    inv_category_id = models.ForeignKey('inv.inv_inventory_categories', on_delete=models.CASCADE)
    inv_category_set_id = models.ForeignKey('inv.inv_category_sets', on_delete=models.CASCADE)
    inventory_id = models.ForeignKey('inv.inv_inventory', on_delete=models.CASCADE)    
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()

class res_raservation_block(models.Model):
    reservation_block_id = models.AutoField(primary_key=True)
    reservation_id = models.ForeignKey(hm_reservation, on_delete=models.CASCADE)
    block_code = models.CharField(max_length=30)
    block_name = models.CharField(max_length=60)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()

class res_reservation_detail(models.Model):
    reservation_detail_id = models.AutoField(primary_key=True)
    reservation_id = models.ForeignKey(hm_reservation, on_delete=models.CASCADE)
    guest_profile_id = models.ForeignKey(hm_guest_profile, on_delete=models.CASCADE)
    no_of_adults = models.IntegerField()
    no_of_childs = models.IntegerField()
    no_below_5_childs = models.IntegerField()
    no_below_10_childs = models.IntegerField()
    no_below_18_childs = models.IntegerField()
    no_of_pets = models.IntegerField()
    expected_nights = models.IntegerField()
    reservation_block_id = models.ForeignKey(hm_reservation_block, on_delete=models.CASCADE)
    pickup_flag = models.CharField(max_length=30)
    expected_arrival_date = models.DateField()
    expected_arrival_time = models.CharField(max_length=10)
    travelling_mode = models.CharField(max_length=30)    #From Lookup Table
    transportation = models.CharField(max_length=30)    #From Lookup Table
    transportation_no = models.CharField(max_length=20)
    reservation_status = models.CharField(max_length=30)
    reservation_status_date = models.DateTimeField()
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()

class ci_guest_arrival(models.Model):
    guest_arrival_id = models.AutoField(primary_key=True)
    reservation_id = models.ForeignKey(reservation, on_delete=models.CASCADE)
    check_in_flag = models.CharField(max_length=30)
    check_in_date = models.DateTimeField()
    inv_category_id = models.ForeignKey('inv.inv_inventory_categories', on_delete=models.CASCADE)
    inv_category_set_id = models.ForeignKey('inv.inv_category_sets', on_delete=models.CASCADE)
    inventory_id = models.ForeignKey('inv.inv_inventory', on_delete=models.CASCADE)
    amenity_type = models.CharField(max_length=30)
    amenity_rate = models.ImageField()
    currency_id = models.ForeignKey('fnd.fnd_currencies', on_delete=models.CASCADE)
    remarks = models.CharField(max_length=60)
    check_out_flag = models.CharField(max_length=30)
    check_out_date = models.DateTimeField()
    drop_flag = models.CharField(max_length=30)
    departure_date = models.DateField()
    departure_time = models.CharField(max_length=10)
    travelling = models.CharField(max_length=30)
    transportation = models.CharField(max_length=30)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()

class ci_guest_ledger(models.Model):
    guest_ledger_id = models.AutoField(primary_key=True)
    guest_arrival_id = models.ForeignKey(hm_guest_arrival, on_delete=models.CASCADE)
    entry_date = models.DateField()
    coa_code_combination = models.CharField(max_length=100)
    local_ledger_id = models.ForeignKey('fa.fa_local_ledger_coa', on_delete=models.CASCADE)
    amount_type = models.CharField(max_length=30)
    mode_of_payment = models.CharField(max_length=30)
    amount_without_taxes = models.ImageField()
    taxes_amount = models.ImageField()
    amount_with_taxes = models.ImageField()
    local_currency_amount = models.IntegerField()
    reporting_currency_amount = models.IntegerField()
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()    
