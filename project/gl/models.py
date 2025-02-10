from django.db import models

# Create your models here.

class gl_natural_sub_coa(models.Model):
    natural_sub_coa_id = models.AutoField(primary_key=True)
    org_id = models.ForeignKey('hr.hr_org_profile', on_delete=models.CASCADE)
    natural_acc_code = models.CharField(max_length=30)
    natural_sub_code = models.CharField(max_length=10)
    natural_sub_title = models.CharField(max_length=30)
    natural_accounts = models.CharField(max_length=30)    #select from Lookup Table
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()
    
class gl_main_ledger_coa(models.Model):
    main_ledger_id = models.AutoField(primary_key=True)
    org_id = models.ForeignKey('hr.hr_org_profile', on_delete=models.CASCADE)
    natural_sub_id = models.ForeignKey(gl_natural_sub_coa, on_delete=models.CASCADE)
    main_ledger_code = models.CharField(max_length=10)
    main_ledger_title = models.CharField(max_length=40)
    accounting_method = models.CharField(max_length=30)    #select from Lookup Table
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()
    
class gl_sub_ledger_coa(models.Model):
    sub_ledger_coa_id = models.AutoField(primary_key=True)
    org_id = models.ForeignKey('hr.hr_org_profile', on_delete=models.CASCADE)
    main_ledger_id = models.ForeignKey(gl_main_ledger_coa, on_delete=models.CASCADE)
    sub_ledger_code = models.CharField(max_length=10)
    sub_ledger_title = models.CharField(max_length=50)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()
    
class gl_local_ledger_coa(models.Model):
    local_ledger_coa_id = models.AutoField(primary_key=True)
    org_id = models.ForeignKey('hr.hr_org_profile', on_delete=models.CASCADE)
    loc_id = models.ForeignKey('hr.hr_org_location', on_delete=models.CASCADE)
    sub_ledger_id = models.ForeignKey(gl_sub_ledger_coa, on_delete=models.CASCADE)
    local_ledger_code = models.CharField(max_length=10)
    local_ledger_title = models.CharField(max_length=60)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()
    
class gl_cost_centers(models.Model):
    cost_centers_id = models.AutoField(primary_key=True)
    org_id = models.ForeignKey('hr.hr_org_profile', on_delete=models.CASCADE)
    loc_id = models.ForeignKey('hr.hr_org_location', on_delete=models.CASCADE)
    cost_center_code = models.CharField(max_length=20)
    cost_center_name = models.CharField(max_length=60)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()
    
class gl_tax_setup_line(models.Model):
    tax_setup_line_id = models.AutoField(primary_key=True)
    org_id = models.ForeignKey('hr.hr_org_profile', on_delete=models.CASCADE)
    loc_id = models.ForeignKey('hr.hr_org_location', on_delete=models.CASCADE)
    org_taxes_applicable_id = models.ForeignKey('hr.hr_org_taxes_applicable', on_delete=models.CASCADE)
    taxation_type = models.CharField(max_length=30)    #select from Lookup Table
    effective_date = models.DateField()
    ineffective_date = models.DateField()
    coa_code_combination = models.CharField(max_length=100)
    local_ledger_id = models.ForeignKey(gl_local_ledger_coa, on_delete=models.CASCADE)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()
    
class gl_tax_setup_detail(models.Model):
    tax_setup_detail_id = models.AutoField(primary_key=True)
    tax_setup_line_id = models.ForeignKey(gl_tax_setup_line, on_delete=models.CASCADE)
    range_from = models.IntegerField()
    range_to = models.IntegerField()
    tax_glctor = models.CharField(max_length=30)    #select from Lookup Table
    tax_multiplier = models.IntegerField()
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()
    
class gl_business_deals_line(models.Model):
    business_deals_line_id = models.AutoField(primary_key=True)
    org_id = models.ForeignKey('hr.hr_org_profile', on_delete=models.CASCADE)
    loc_id = models.ForeignKey('hr.hr_org_location', on_delete=models.CASCADE)
    business_deal_name = models.CharField(max_length=30)
    discount_glctor = models.CharField(max_length=30)        #select from Lookup Table
    discount_multiplier = models.IntegerField()
    effective_date = models.DateField()
    ineffective_date = models.DateField()
    coa_code_combination = models.CharField(max_length=100)
    local_ledger_id = models.ForeignKey(gl_local_ledger_coa, on_delete=models.CASCADE)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()
    
class gl_business_deals_detail(models.Model):
    business_deals_detail_id = models.AutoField(primary_key=True)
    business_deal_line_id = models.ForeignKey(gl_business_deals_line, on_delete=models.CASCADE)
    range_from = models.IntegerField()
    range_to = models.IntegerField()
    discount_glctor = models.CharField(max_length=30)    #select from Lookup Table
    discount_multiplier = models.IntegerField()
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()

class gl_business_deals_container(models.Model):
    business_deals_container_id = models.AutoField(primary_key=True)
    business_deal_detail_id = models.ForeignKey(gl_business_deals_detail, on_delete=models.CASCADE)
#    inventory_category_id = models.ForeignKey('inv.inventory_categories', on_delete=models.CASCADE)
#    inventory_id = models.ForeignKey('inv.inventory', on_delete=models.CASCADE)
    inventory_qty = models.IntegerField()
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()
    
class gl_agent_commission_line(models.Model):
    agent_comm_line_id = models.AutoField(primary_key=True)
    org_id = models.ForeignKey('hr.hr_org_profile', on_delete=models.CASCADE)
    loc_id = models.ForeignKey('hr.hr_org_location', on_delete=models.CASCADE)
    commission_code = models.CharField(max_length=30)    #select from Lookup Table
    description = models.CharField(max_length=60)
    effective_date = models.DateField()
    ineffective_date = models.DateField()
    coa_code_combination = models.CharField(max_length=100)
    local_ledger_id = models.ForeignKey(hr_local_ledger_coa, on_delete=models.CASCADE)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()
    
class gl_agent_commission_detail(models.Model):
    agent_comm_detail_id = models.AutoField(primary_key=True)
    agent_commission_line_id = models.ForeignKey(gl_agent_commission_line, on_delete=models.CASCADE)
    range_from = models.IntegerField()
    range_to = models.IntegerField()
    commission_glctor = models.CharField(max_length=30)    #select from Lookup Table
    commission_multiplier = models.IntegerField()
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()
    
class gl_period_codes(models.Model):
    period_codes_id = models.AutoField(primary_key=True)
    org_id = models.ForeignKey('hr.hr_org_profile', on_delete=models.CASCADE)
    period_code = models.CharField(max_length=30)    #Example Q1 for first quarter, Q2 or M1 for first month, M2 etc
    period_name = models.CharField(max_length=60)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()
    
class gl_periods(models.Model):
    periods_id = models.AutoField(primary_key=True)
    period_codes_id = models.ForeignKey(gl_period_codes, on_delete=models.CASCADE)
    period_types = models.CharField(max_length=30)    #select from Lookup Table
    period_start_date = models.DateField()
    period_end_date = models.DateField()
    combination_of_period = models.CharField(max_length=30)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()
    
class gl_period_status(models.Model):
    period_status_id = models.AutoField(primary_key=True)
    periods_id = models.ForeignKey(gl_periods, on_delete=models.CASCADE)
    combination_of_period = models.CharField(max_length=60)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.CharField(max_length=10)
    end_time = models.CharField(max_length=10)
    combination_of_period_status = models.CharField(max_length=100)
    mode = models.CharField(max_length=30)
    period_status = models.CharField(max_length=30)    #select from Lookup Table
    reopen_date = models.DateTimeField()
    extend_start_date = models.DateField()
    extend_end_date = models.DateField()
    extend_start_time = models.CharField(max_length=10)
    extend_end_time = models.CharField(max_length=10)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()
    
class gl_transaction_batch(models.Model):
    trans_batch_id = models.AutoField(primary_key=True)
    org_id = models.ForeignKey('hr.hr_org_profile', on_delete=models.CASCADE)
    loc_id = models.ForeignKey('hr.hr_org_location', on_delete=models.CASCADE)
    period_status_id = models.ForeignKey(gl_period_status, on_delete=models.CASCADE)
    trans_batch_code = models.CharField(max_length=150)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()
    
class gl_currency_conversion(models.Model):
    currency_conversion_id = models.AutoField(primary_key=True)
    org_id = models.ForeignKey('hr.hr_org_profile', on_delete=models.CASCADE)
    loc_id = models.ForeignKey('hr.hr_org_location', on_delete=models.CASCADE)
    period_status_id = models.ForeignKey(period_status, on_delete=models.CASCADE)
    conversion_date = models.DateField()
    from_currency = models.ForeignKey('fnd.fnd_currencies', on_delete=models.CASCADE)
    to_currency = models.ForeignKey('fnd.fnd_currencies', on_delete=models.CASCADE)
    conversion_rate = models.IntegerField()
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()
    
class gl_transaction_line(models.Model):
    trans_line_id = models.AutoField(primary_key=True)
    org_id = models.ForeignKey('hr.hr_org_profile', on_delete=models.CASCADE)
    loc_id = models.ForeignKey('hr.hr_org_location', on_delete=models.CASCADE)
    transaction_batch_id = models.ForeignKey(gl_transaction_batch, on_delete=models.CASCADE)
    trans_line_date = models.DateField()
    transaction_type = models.CharField(max_length=20)    #select from fnd_transaction_type Table
    currency_id = models.ForeignKey('fnd.fnd_currencies', on_delete=models.CASCADE)
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()
    
class gl_transaction_detail(models.Model):
    trans_detail_id = models.AutoField(primary_key=True)
    trans_line = models.ForeignKey(gl_transaction_line, on_delete=models.CASCADE)
    coa_code_combination = models.CharField(max_length=100)
    cost_center_id = models.ForeignKey(gl_cost_centers, on_delete=models.CASCADE)
    local_ledger_id = models.ForeignKey(gl_local_ledger_coa, on_delete=models.CASCADE)
    description = models.models.CharField(max_length=60)
    debit_amount = models.IntegerField()
    credit_amount = models.IntegerField()
    local_currency_amount = models.IntegerField()
    reporting_currency_amount = models.IntegerField()
    created_by = models.CharField(max_length=30)
    creation_date = models.dateTimeField()
    last_updated_by = models.CharField(max_length=30)
    last_updation_date = models.DateTimeField()    
