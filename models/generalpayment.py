# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 23:06:33 2023

@author: Sheila
"""

from app import db

class GeneralPayment(db.Model):
    __tablename__ = 'GeneralPayment'
    
    record_number = db.Column(db.String(30))
    change_type = db.Column(db.String(30))
    covered_recipient_type = db.Column(db.String(80))
    teaching_hospital_ccn = db.Column(db.String(30))
    teaching_hospital_id = db.Column(db.String(30))
    teaching_hospital_name = db.Column(db.String(80))
    covered_recipient_profile_id = db.Column(db.String(30))
    covered_recipient_npi = db.Column(db.String(30))
    covered_recipient_first_name = db.Column(db.String(80))
    covered_recipient_middle_name = db.Column(db.String(80))
    covered_recipient_last_name = db.Column(db.String(80))
    covered_recipient_name_suffix = db.Column(db.String(30))
    recipient_primary_business_street_address_line1 = db.Column(db.String(80))
    recipient_primary_business_street_address_line2 = db.Column(db.String(80))
    recipient_city = db.Column(db.String(30))
    recipient_state = db.Column(db.String(30))
    recipient_zip_code = db.Column(db.String(30))
    recipient_country = db.Column(db.String(30))
    recipient_province = db.Column(db.String(30))
    recipient_postal_code = db.Column(db.String(30))
    covered_recipient_primary_type_1 = db.Column(db.String(80))
    covered_recipient_primary_type_2 = db.Column(db.String(30))
    covered_recipient_primary_type_3 = db.Column(db.String(30))
    covered_recipient_primary_type_4 = db.Column(db.String(30))
    covered_recipient_primary_type_5 = db.Column(db.String(30))
    covered_recipient_primary_type_6 = db.Column(db.String(30))
    covered_recipient_specialty_1 = db.Column(db.String(200))
    covered_recipient_specialty_2 = db.Column(db.String(80))
    covered_recipient_specialty_3 = db.Column(db.String(80))
    covered_recipient_specialty_4 = db.Column(db.String(80))
    covered_recipient_specialty_5 = db.Column(db.String(80))
    covered_recipient_specialty_6 = db.Column(db.String(80))
    covered_recipient_license_state_code1 = db.Column(db.String(30))
    covered_recipient_license_state_code2 = db.Column(db.String(30))
    covered_recipient_license_state_code3 = db.Column(db.String(30))
    covered_recipient_license_state_code4 = db.Column(db.String(30))
    covered_recipient_license_state_code5 = db.Column(db.String(30))
    submitting_applicable_manufacturer_or_applicable_gpo_name = db.Column(db.String(80))
    applicable_manufacturer_or_applicable_gpo_making_payment_id = db.Column(db.String(30))
    applicable_manufacturer_or_applicable_gpo_making_payment_name = db.Column(db.String(80))
    applicable_manufacturer_or_applicable_gpo_making_payment_state = db.Column(db.String(30))
    applicable_manufacturer_or_applicable_gpo_making_payment_country = db.Column(db.String(30))
    total_amount_of_payment_usdollars = db.Column(db.String(80))
    date_of_payment = db.Column(db.String(30))
    number_of_payments_included_in_total_amount = db.Column(db.String(30))
    form_of_payment_or_transfer_of_value = db.Column(db.String(80))
    nature_of_payment_or_transfer_of_value = db.Column(db.String(150))
    city_of_travel = db.Column(db.String(30))
    state_of_travel = db.Column(db.String(30))
    country_of_travel = db.Column(db.String(30))
    physician_ownership_indicator = db.Column(db.String(30))
    third_party_payment_recipient_indicator = db.Column(db.String(30))
    name_of_third_party_entity_receiving_payment_or_transfer_of_ccfc = db.Column(db.String(80))
    charity_indicator = db.Column(db.String(30))
    third_party_equals_covered_recipient_indicator = db.Column(db.String(30))
    contextual_information = db.Column(db.String(500))
    delay_in_publication_indicator = db.Column(db.String(30))
    record_id = db.Column(db.String(80), primary_key=True)
    dispute_status_for_publication = db.Column(db.String(30))
    related_product_indicator = db.Column(db.String(30))
    covered_or_noncovered_indicator_1 = db.Column(db.String(30))
    indicate_drug_or_biological_or_device_or_medical_supply_1 = db.Column(db.String(80))
    product_category_or_therapeutic_area_1 = db.Column(db.String(100))
    name_of_drug_or_biological_or_device_or_medical_supply_1 = db.Column(db.String(80))
    associated_drug_or_biological_ndc_1 = db.Column(db.String(80))
    associated_device_or_medical_supply_pdi_1 = db.Column(db.String(80))
    covered_or_noncovered_indicator_2 = db.Column(db.String(80))
    indicate_drug_or_biological_or_device_or_medical_supply_2 = db.Column(db.String(80))
    product_category_or_therapeutic_area_2 = db.Column(db.String(80))
    name_of_drug_or_biological_or_device_or_medical_supply_2 = db.Column(db.String(80))
    associated_drug_or_biological_ndc_2 = db.Column(db.String(80))
    associated_device_or_medical_supply_pdi_2 = db.Column(db.String(80))
    covered_or_noncovered_indicator_3 = db.Column(db.String(80))
    indicate_drug_or_biological_or_device_or_medical_supply_3 = db.Column(db.String(80))
    product_category_or_therapeutic_area_3 = db.Column(db.String(80))
    name_of_drug_or_biological_or_device_or_medical_supply_3 = db.Column(db.String(80))
    associated_drug_or_biological_ndc_3 = db.Column(db.String(80))
    associated_device_or_medical_supply_pdi_3 = db.Column(db.String(80))
    covered_or_noncovered_indicator_4 = db.Column(db.String(80))
    indicate_drug_or_biological_or_device_or_medical_supply_4 = db.Column(db.String(80))
    product_category_or_therapeutic_area_4 = db.Column(db.String(80))
    name_of_drug_or_biological_or_device_or_medical_supply_4 = db.Column(db.String(80))
    associated_drug_or_biological_ndc_4 = db.Column(db.String(80))
    associated_device_or_medical_supply_pdi_4 = db.Column(db.String(80))
    covered_or_noncovered_indicator_5 = db.Column(db.String(80))
    indicate_drug_or_biological_or_device_or_medical_supply_5 = db.Column(db.String(80))
    product_category_or_therapeutic_area_5 = db.Column(db.String(80))
    name_of_drug_or_biological_or_device_or_medical_supply_5 = db.Column(db.String(80))
    associated_drug_or_biological_ndc_5 = db.Column(db.String(80))
    associated_device_or_medical_supply_pdi_5 = db.Column(db.String(80))
    program_year = db.Column(db.String(30))
    payment_publication_date = db.Column(db.String(30))

    def __repr__(self):
        return f'<GeneralPayment {self.record_id}>'

    def row2dict(row):
        d = {}
        for column in row.__table__.columns:
            d[column.name] = str(getattr(row, column.name))

        return d
    
    