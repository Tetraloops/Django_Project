from django.db import models

# Create your models here.

class inv_warehouse(models.Model):
    warehouse_id = models.AutoField(primary_key=True)
    org_id = models.ForeignKey('hr.hr_org_profile', on_delete=models.CASCADE)
    loc_id = models.ForeignKey('hr.hr_org_location', on_delete=models.CASCADE)
    warehouse_code = models.CharField(max_length=30)
    warehouse_name = models.CharField(max_length=60)
    location_id = models.ForeignKey(hr_org_location, on_delete=models.CASCADE)
    shipping_address_line = models.CharField(max_length=300)
    city_id = models.ForeignKey('fnd.fnd_cities', on_delete=models.CASCADE)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()
    
class hr_warehouse_zone(models.Model):
    warehouse_zone_id = models.AutoField(primary_key=True)
    warehouse_id = models.ForeignKey(inv_warehouse, on_delete=models.CASCADE)
    warehouse_zone_code = models.CharField(max_length=30)
    zone_name = models.CharField(max_length=60)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()
    
class inv_warehouse_shelf(models.Model):
    warehouse_shelf_id = models.AutoField(primary_key=True)
    warehouse_zone_id = models.ForeignKey(inv_warehouse_zone, on delete=models.CASCADE)
    shelf_code = models.CharField(max_length=30)
    shelf_name = models.CharField(max_length=60)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()
    
class inv_inventory_categories(models.Model):
    inv_category_id = models.AutoField(primary_key=True)
    org_id = models.ForeignKey('hr.hr_org_profile', on_delete=models.CASCADE)
    loc_id = models.ForeignKey('hr.hr_org_location', on_delete=models.CASCADE)
    inv_category_code = models.CharField(max_length= 30)
    inv_category_name = models.CharField(max_length= 60)
    parent_inv_category_id = models.CharField(max_length=30)    #Recursive Table
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()
    
class inv_inventory(models.Model):
    inv_id = models.AutoField(primary_key=True)
    org_id = models.ForeignKey('hr.hr_org_profile', on_delete=models.CASCADE)
    loc_id = models.ForeignKey('hr.hr_org_location', on_delete=models.CASCADE)
    inv_category_id = models.ForeignKey(inv_inventory_categories, on_delete=models.CASCADE)
    inventory_code = models.CharField(max_length=30)
    inventory_name = models.CharField(max_length= 60)
    inventory_type = models.CharField(max_length=30)    #Inventory Type or Item Type - Select from Lookup Table
    stock_type = models.CharField(max_length=30)    #Select from Lookup Table
    inventory_status = models.CharField(max_length=30)    #Select from Lookup Table
    subinventories = models.CharField(max_length=30)    #Select from Lookup Table
    warehouse_id = models.ForeignKey(inv_warehouse, on_delete=models.CASCADE) #For example locator of item
    warehouse_zone_id = models.ForeignKey(inv_warehouse_zone, on_delete=models.CASCADE)
    warehouse_shelf_id = models.ForeignKey(inv_warehouse_shelf, on_delete=models.CASCADE)
    costing_method = models.CharField(max_length=30)    #Select from Lookup Table
    minimum_order_qty = models.IntegerField()    #The smallest quantity of an item that can be ordered.
    maximum_order_qty = models.IntegerField()    #The largest quantity of an item that can be ordered.
    safety_stock = models.IntegerField()        #The minimum level of inventory that must be maintained to prevent stockouts.
    manufacturing_date = models.DateTimeField()
    expiry_date = models.DateField()
    base_unit_qty = models.IntegerField()
    base_uom_id = models.ForeignKey('fnd.fnd_unit_of_measure', on_delete=models.CASCADE)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()
    
class inv_inventory_coa_codes(models.Model):
    inv_coa_codes_id = models.AutoField(primary_key=True)
    inventory_id = models.ForeignKey(hr_inventory, on_delete=models.CASCADE)
    coa_code_combination = models.CharField(max_length=100)
    local_ledger_id = models.ForeignKey('fa.fa_local_ledger_coa', on_delete=models.CASCADE)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()
    
class inv_inventory_taxes_applicable(models.Model):
    inv_taxes_app_id = models.AutoField(primary_key=True)
    inventory_id = models.ForeignKey(inv_inventory, on_delete=models.CASCADE)
    tax_setup_line_id = models.ForeignKey('fa.fa_tax_setup_line', on_delete=models.CASCADE)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()
    
class inv_inventory_packing(models.Model):
    inv_packing_id = models.AutoField(primary_key=True)
    org_id = models.ForeignKey('hr.hr_org_profile', on_delete=models.CASCADE)
    loc_id = models.ForeignKey('hr.hr_org_location', on_delete=models.CASCADE)
    packing_code = models.CharField(max_length=30)
    packing_name = models.CharField(max_length=60)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()
    
class inv_packing_conversion(models.Model):
    packing_conversion_id = models.AutoField(primary_key=True)
    inv_category_id = models.ForeignKey(inv_inventory_categories, on_delete=models.CASCADE)
    inventory_id = models.ForeignKey(inv_inventory, on_delete=models.CASCADE)
    inventor_packing_id = models.ForeignKey(inv_inventory_packing, on_delete=models.CASCADE)
    contained_qty = models.IntegerField()
    contained_uom_id = models.ForeignKey('fnd.fnd_unit_of_measure', on_delete=models.CASCADE)
    base_unit_qty = models.IntegerField()
    base_uom_id = models.ForeignKey('fnd.fnd_unit_of_measure', on_delete=models.CASCADE)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()


class inv_parties_profile(models.Model):
    parties_profile_id = models.AutoField(primary_key=True)
    org_id = models.ForeignKey('hr.hr_org_profile', on_delete=models.CASCADE)
    loc_id = models.ForeignKey('hr.hr_org_location', on_delete=models.CASCADE)
    party_code = models.CharField(max_length=30)
    party_name = models.CharField(max_length=60)
    party_classification = models.Char_Field(max_length=30)
    address_line = models.CharField(max_length=300)
    city_id = models.ForeignKey('fnd.fnd_cities', on_delete=models.CASCADE)
    active_flag = models.CharField(max_length=30)
    vat_numbers = models.CharField(max_length=60)
    currency_id = models.ForeignKey('fnd.fnd_currencies', on_delete=models.CASCADE)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()

class inv_parties_contacts(models.Model):
    parties_contacts_id = models.AutoField(primary_key=True)
    party_id = models.ForeignKey(inv_parties_profile, on_delete=models.CASCADE)
    contact_person = models.CharField(max_length=30)
    contact_designation = models.CharField(max_length=30)
    landline1 = models.CharField(max_length=30)
    landline2 = models.CharField(max_length=30)
    mobile1 = models.CharField(max_length=30)
    mobile1 = models.CharField(max_length=30)
    email_address = models.CharField(max_length=60)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()

class inv_parties_shipping(models.Model):
    parties_shipping_id = models.AutoField(primary_key=True)
    party_id = models.ForeignKey(inv_parties_profile, on_delete=models.CASCADE)
    shipping_address_line = models.CharField(max_length=300)
    city_id = models.ForeignKey('fnd.fnd_cities', on_delete=models.CASCADE)
    business_terms = models.CharField(max_length=30)
    payment_terms = models.CharField(max_length=30)
    tax_flag = models.CharField(max_length=30)
    discount_flag = models.CharField(max_length=30)
    commission_flag = models.CharField(max_length=30)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()   

class inv_parties_taxes(models.Model):
    parties_taxes_id = models.AutoField(primary_key=True)
    party_id = models.ForeignKey(inv_parties_profile, on_delete=models.CASCADE)
    tax_setup_line_id = models.ForeignKey('fa.fa_tex_setup_line', on_delete=models.CASCADE)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()

class inv_parties_business_deals(models.Model):
    parties_business_deals_id = models.AutoField(primary_key=True)
    party_id = models.ForeignKey(inv_parties_profile, on_delete=models.CASCADE)
    business_deal_line_id = models.ForeignKey('fa.fa_business_deal_line', on_delete=models.CASCADE)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()

class inv_parties_commission(models.Model):
    parties_comm_id = models.AutoField(primary_key=True)
    party_id = models.ForeignKey(inv_parties_profile, on_delete=models.CASCADE)
    agent_commission_line_id = models.ForeignKey('fa.fa_agent_commission_line', on_delete=models.CASCADE)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()

class inv_parties_bank_account(models.Model)
    parties_bank_acc_id = models.AutoField(primary_key=True)
    party_id = models.ForeignKey(inv_parties_profile, on_delete=models.CASCADE)
    bank_account = models.CharField(max_length=30)
    branch_code = models.CharField(max_length=20)
    bank_name = models.CharField(max_length=60)
    address_line = models.CharField(max_length=300)
    city_id = models.ForeignKey('fnd.fnd_cities', on_delete=models.CASCADE)
    active_flag = models.CharField(max_length=30)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()        

class inv_wh_transaction_line(models.Model):
    wh_trans_line_id = models.AutoField(primary_key=True)
    org_id = models.ForeignKey('hr.hr_org_profile', on_delete=models.CASCADE)
    loc_id = models.ForeignKey('hr.hr_org_location', on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=20)    #select from fnd_transaction_type Table
    transaction_date = models.DateField()
    party_id = models.ForeignKey(inv_parties, on_delete=models.CASCADE)
    invoice_number = models.IntegerField()
    invoice_date = models.DateField()
    vehicle_number = models.CharField(max_length=20)
    driver_name = models.CharField(max_length=30)
    driver_mobile_number = models.CharField(max_length=20)
    currency_id = models.ForeignKey('fnd.fnd_currencies', on_delete=models.CASCADE)
    agent_commission_party_id = models.ForeignKey(inv_parties, on_delete=models.CASCADE)
    description = models.CharField(max_length=60)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()

class inv_wh_transaction_detail(models.Model):
    wh_trans_detail_id = models.AutoField(primary_key=True)
    wh_transaction_line_id = models.ForeignKey(inv_wh_transaction_line, on_delete=models.CASCADE)
    inventory_category_id = models.ForeignKey(inv_inventory_categories, on_delete=models.CASCADE)
    inventory_id = models.ForeignKey(inv_inventory, on_delete=models.CASCADE)
    inventory_qty = models.IntegerField()
    inventory_rate = models.IntegerField()
    business_deal_line_id = models.ForeignKey('fa.fa_business_deals_line', on_delete=models.CASCADE)
    amount_without_taxes = models.IntegerField()
    taxs_amount = models.IntegerField()
    amount_with_taxes = models.IntegerField()
    local_currency_amount = models.IntegerField()
    reporting_currency_amount = models.IntegerField()
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()    
