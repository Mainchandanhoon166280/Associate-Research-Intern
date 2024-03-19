from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    season = request.form.get('season')
    location = request.form.get('location')
    crop_type = request.form.get('crop_type')
    field_size = float(request.form.get('field_size'))
    unit = request.form.get('unit')

    # Convert field size to square meters based on the selected unit
    if unit == 'hectares':
        field_size *= 10000  # 1 hectare = 10,000 square meters
    elif unit == 'acres':
        field_size *= 4046.86  # 1 acre = 4046.86 square meters

    # Calculate CO2 emissions
          # Additional information based on location and crop type
              # for solar effeciency and sunlight duration based on location
    if location == 'Andhra Pradesh':
        if season == 'Autumn':
            solar_efficiency = 0.25 # in percentage
            sunlight_duration = 6.5 # in hours
        elif season == 'Spring':
            solar_efficiency = 0.25 
            sunlight_duration = 6.5     
        elif season == 'Summer':
            solar_efficiency = 0.25 
            sunlight_duration = 7.5 
        elif season == 'Winter':
            solar_efficiency = 0.25 
            sunlight_duration = 5.5 
        elif season == 'Kharif':
            solar_efficiency = 0.25 
            sunlight_duration = 5.5     
        elif season == 'Rabi':
            solar_efficiency = 0.25 
            sunlight_duration = 8.5 
        elif season == 'Zaid':
            solar_efficiency = 0.25 
            sunlight_duration = 7.5 
        else:
            solar_efficiency = 0.25 
            sunlight_duration = 4.5 
    elif location == 'Arunachal Pradesh':
        if season == 'Autumn':
            solar_efficiency = 0.15 # in percentage
            sunlight_duration = 4.5 # in hours
        elif season == 'Spring':
            solar_efficiency = 0.15 
            sunlight_duration = 5.5     
        elif season == 'Summer':
            solar_efficiency = 0.15 
            sunlight_duration = 6.5 
        elif season == 'Winter':
            solar_efficiency = 0.15 
            sunlight_duration = 3.5 
        elif season == 'Kharif':
            solar_efficiency = 0.15 
            sunlight_duration = 4.5     
        elif season == 'Rabi':
            solar_efficiency = 0.15 
            sunlight_duration = 6.5 
        elif season == 'Zaid':
            solar_efficiency = 0.15 
            sunlight_duration = 5.5 
        else:
            solar_efficiency = 0.25 
            sunlight_duration = 4.5 
    elif location == 'Assam':
        if season == 'Autumn':
            solar_efficiency = 0.15 # in percentage
            sunlight_duration = 5.5 # in hours
        elif season == 'Spring':
            solar_efficiency = 0.15 
            sunlight_duration = 6.5     
        elif season == 'Summer':
            solar_efficiency = 0.15 
            sunlight_duration = 7.5 
        elif season == 'Winter':
            solar_efficiency = 0.15 
            sunlight_duration = 4.5 
        elif season == 'Kharif':
            solar_efficiency = 0.15 
            sunlight_duration = 4.5     
        elif season == 'Rabi':
            solar_efficiency = 0.15 
            sunlight_duration = 6.5 
        elif season == 'Zaid':
            solar_efficiency = 0.15 
            sunlight_duration = 5.5 
        else:
            solar_efficiency = 0.25 
            sunlight_duration = 4.5 
    elif location == 'Bihar':
        if season == 'Autumn':
            solar_efficiency = 0.15 # in percentage
            sunlight_duration = 5.5 # in hours
        elif season == 'Spring':
            solar_efficiency = 0.15 
            sunlight_duration = 6.5     
        elif season == 'Summer':
            solar_efficiency = 0.15 
            sunlight_duration = 7.5 
        elif season == 'Winter':
            solar_efficiency = 0.15 
            sunlight_duration = 4.5 
        elif season == 'Kharif':
            solar_efficiency = 0.15 
            sunlight_duration = 5.5     
        elif season == 'Rabi':
            solar_efficiency = 0.15 
            sunlight_duration = 7.5 
        elif season == 'Zaid':
            solar_efficiency = 0.15 
            sunlight_duration = 6.5 
        else:
            solar_efficiency = 0.25 
            sunlight_duration = 4.5 
    elif location == 'Chhattisgarh':
        if season == 'Autumn':
            solar_efficiency = 0.15 # in percentage
            sunlight_duration = 6.5 # in hours
        elif season == 'Spring':
            solar_efficiency = 0.15 
            sunlight_duration = 6.5     
        elif season == 'Summer':
            solar_efficiency = 0.15 
            sunlight_duration = 7.5 
        elif season == 'Winter':
            solar_efficiency = 0.15 
            sunlight_duration = 4.5 
        elif season == 'Kharif':
            solar_efficiency = 0.15 
            sunlight_duration = 5.5     
        elif season == 'Rabi':
            solar_efficiency = 0.15 
            sunlight_duration = 8.5 
        elif season == 'Zaid':
            solar_efficiency = 0.15 
            sunlight_duration = 7.5 
        else:
            solar_efficiency = 0.25 
            sunlight_duration = 4.5 
    elif location == 'Goa':
        if season == 'Autumn':
            solar_efficiency = 0.15 # in percentage
            sunlight_duration = 6.5 # in hours
        elif season == 'Spring':
            solar_efficiency = 0.15 
            sunlight_duration = 6.5     
        elif season == 'Summer':
            solar_efficiency = 0.15 
            sunlight_duration = 7.5 
        elif season == 'Winter':
            solar_efficiency = 0.15 
            sunlight_duration = 5.5 
        elif season == 'Kharif':
            solar_efficiency = 0.15 
            sunlight_duration = 7.5     
        elif season == 'Rabi':
            solar_efficiency = 0.15 
            sunlight_duration = 8.5 
        elif season == 'Zaid':
            solar_efficiency = 0.15 
            sunlight_duration = 9.5 
        else:
            solar_efficiency = 0.25 
            sunlight_duration = 4.5 
    elif location == 'Gujarat':
        if season == 'Autumn':
            solar_efficiency = 0.25 # in percentage
            sunlight_duration = 7.5 # in hours
        elif season == 'Spring':
            solar_efficiency = 0.25 
            sunlight_duration = 7.5     
        elif season == 'Summer':
            solar_efficiency = 0.25 
            sunlight_duration = 8.5 
        elif season == 'Winter':
            solar_efficiency = 0.25 
            sunlight_duration = 5.5 
        elif season == 'Kharif':
            solar_efficiency = 0.25 
            sunlight_duration = 7.5     
        elif season == 'Rabi':
            solar_efficiency = 0.25 
            sunlight_duration = 8.5 
        elif season == 'Zaid':
            solar_efficiency = 0.25 
            sunlight_duration = 9.5 
        else:
            solar_efficiency = 0.25 
            sunlight_duration = 4.5 
    elif location == 'Haryana':
        if season == 'Autumn':
            solar_efficiency = 0.20 # in percentage
            sunlight_duration = 7.5 # in hours
        elif season == 'Spring':
            solar_efficiency = 0.20 
            sunlight_duration = 7.5     
        elif season == 'Summer':
            solar_efficiency = 0.20 
            sunlight_duration = 8.5 
        elif season == 'Winter':
            solar_efficiency = 0.20 
            sunlight_duration = 5.5 
        elif season == 'Kharif':
            solar_efficiency = 0.20 
            sunlight_duration = 6.5     
        elif season == 'Rabi':
            solar_efficiency = 0.20
            sunlight_duration = 7.5 
        elif season == 'Zaid':
            solar_efficiency = 0.20
            sunlight_duration = 8.5 
        else:
            solar_efficiency = 0.25
            sunlight_duration = 4.5   
    elif location == 'Himachal Pradesh':
        if season == 'Autumn':
            solar_efficiency = 0.15 # in percentage
            sunlight_duration = 5.5 # in hours
        elif season == 'Spring':
            solar_efficiency = 0.15 
            sunlight_duration = 6.5     
        elif season == 'Summer':
            solar_efficiency = 0.15 
            sunlight_duration = 7.5 
        elif season == 'Winter':
            solar_efficiency = 0.15 
            sunlight_duration = 4.5 
        elif season == 'Kharif':
            solar_efficiency = 0.15 
            sunlight_duration = 6.5     
        elif season == 'Rabi':
            solar_efficiency = 0.15 
            sunlight_duration = 7.5 
        elif season == 'Zaid':
            solar_efficiency = 0.15 
            sunlight_duration = 8.5 
        else:
            solar_efficiency = 0.25 
            sunlight_duration = 4.5 
    elif location == 'Jammu and Kashmir':
        if season == 'Autumn':
            solar_efficiency = 0.15 # in percentage
            sunlight_duration = 5.5 # in hours
        elif season == 'Spring':
            solar_efficiency = 0.15 
            sunlight_duration = 6.5     
        elif season == 'Summer':
            solar_efficiency = 0.15 
            sunlight_duration = 7.5 
        elif season == 'Winter':
            solar_efficiency = 0.15 
            sunlight_duration = 4.5 
        elif season == 'Kharif':
            solar_efficiency = 0.15 
            sunlight_duration = 6.5     
        elif season == 'Rabi':
            solar_efficiency = 0.15 
            sunlight_duration = 7.5 
        elif season == 'Zaid':
            solar_efficiency = 0.15 
            sunlight_duration = 7.5 
        else:
            solar_efficiency = 0.25 
            sunlight_duration = 4.5 
    elif location == 'Jharkhand':
        if season == 'Autumn':
            solar_efficiency = 0.25 # in percentage
            sunlight_duration = 5.5 # in hours
        elif season == 'Spring':
            solar_efficiency = 0.25 
            sunlight_duration = 6.5     
        elif season == 'Summer':
            solar_efficiency = 0.25 
            sunlight_duration = 7.5 
        elif season == 'Winter':
            solar_efficiency = 0.25 
            sunlight_duration = 4.5 
        elif season == 'Kharif':
            solar_efficiency = 0.25 
            sunlight_duration = 5.5     
        elif season == 'Rabi':
            solar_efficiency = 0.25 
            sunlight_duration = 6.5 
        elif season == 'Zaid':
            solar_efficiency = 0.25 
            sunlight_duration = 7.5 
        else:
            solar_efficiency = 0.25 
            sunlight_duration = 4.5 
    elif location == 'Karnataka':
        if season == 'Autumn':
            solar_efficiency = 0.20 # in percentage
            sunlight_duration = 6.5 # in hours
        elif season == 'Spring':
            solar_efficiency = 0.20 
            sunlight_duration = 6.5     
        elif season == 'Summer':
            solar_efficiency = 0.20 
            sunlight_duration = 7.5 
        elif season == 'Winter':
            solar_efficiency = 0.20
            sunlight_duration = 5.5 
        elif season == 'Kharif':
            solar_efficiency = 0.20 
            sunlight_duration = 6.5     
        elif season == 'Rabi':
            solar_efficiency = 0.20
            sunlight_duration = 8.5 
        elif season == 'Zaid':
            solar_efficiency = 0.20 
            sunlight_duration = 9.5 
        else:
            solar_efficiency = 0.25 
            sunlight_duration = 4.5 
    elif location == 'Kerala':
        if season == 'Autumn':
            solar_efficiency = 0.15 # in percentage
            sunlight_duration = 6.5 # in hours
        elif season == 'Spring':
            solar_efficiency = 0.15 
            sunlight_duration = 6.5     
        elif season == 'Summer':
            solar_efficiency = 0.15 
            sunlight_duration = 7.5 
        elif season == 'Winter':
            solar_efficiency = 0.15 
            sunlight_duration = 5.5 
        elif season == 'Kharif':
            solar_efficiency = 0.15 
            sunlight_duration = 5.5     
        elif season == 'Rabi':
            solar_efficiency = 0.15 
            sunlight_duration = 6.5 
        elif season == 'Zaid':
            solar_efficiency = 0.15 
            sunlight_duration = 7.5 
        else:
            solar_efficiency = 0.25 
            sunlight_duration = 4.5 
    elif location == 'Madhya Pradesh':
        if season == 'Autumn':
            solar_efficiency = 0.20 # in percentage
            sunlight_duration = 6.5 # in hours
        elif season == 'Spring':
            solar_efficiency = 0.20 
            sunlight_duration = 6.5     
        elif season == 'Summer':
            solar_efficiency = 0.20 
            sunlight_duration = 7.5 
        elif season == 'Winter':
            solar_efficiency = 0.20 
            sunlight_duration = 5.5 
        elif season == 'Kharif':
            solar_efficiency = 0.20
            sunlight_duration = 5.5     
        elif season == 'Rabi':
            solar_efficiency = 0.20 
            sunlight_duration = 6.5 
        elif season == 'Zaid':
            solar_efficiency = 0.20 
            sunlight_duration = 7.5 
        else:
            solar_efficiency = 0.25 
            sunlight_duration = 4.5 
    elif location == 'Maharashtra':
        if season == 'Autumn':
            solar_efficiency = 0.20 # in percentage
            sunlight_duration = 6.5 # in hours
        elif season == 'Spring':
            solar_efficiency = 0.20 
            sunlight_duration = 6.5     
        elif season == 'Summer':
            solar_efficiency = 0.20 
            sunlight_duration = 7.5 
        elif season == 'Winter':
            solar_efficiency = 0.20
            sunlight_duration = 5.5 
        elif season == 'Kharif':
            solar_efficiency = 0.20
            sunlight_duration = 6.5     
        elif season == 'Rabi':
            solar_efficiency = 0.20 
            sunlight_duration = 7.5 
        elif season == 'Zaid':
            solar_efficiency = 0.20 
            sunlight_duration = 8.5 
        else:
            solar_efficiency = 0.25 
            sunlight_duration = 4.5 
    elif location == 'Manipur':
        if season == 'Autumn':
            solar_efficiency = 0.15 # in percentage
            sunlight_duration = 5.5 # in hours
        elif season == 'Spring':
            solar_efficiency = 0.15 
            sunlight_duration = 6.5     
        elif season == 'Summer':
            solar_efficiency = 0.15 
            sunlight_duration = 7.5 
        elif season == 'Winter':
            solar_efficiency = 0.15 
            sunlight_duration = 4.5 
        elif season == 'Kharif':
            solar_efficiency = 0.15 
            sunlight_duration = 5.5     
        elif season == 'Rabi':
            solar_efficiency = 0.15 
            sunlight_duration = 6.5 
        elif season == 'Zaid':
            solar_efficiency = 0.15 
            sunlight_duration = 7.5 
        else:
            solar_efficiency = 0.25 
            sunlight_duration = 4.5 
    elif location == 'Meghalaya':
        if season == 'Autumn':
            solar_efficiency = 0.15 # in percentage
            sunlight_duration = 5.5 # in hours
        elif season == 'Spring':
            solar_efficiency = 0.15 
            sunlight_duration = 6.5     
        elif season == 'Summer':
            solar_efficiency = 0.15 
            sunlight_duration = 7.5 
        elif season == 'Winter':
            solar_efficiency = 0.15 
            sunlight_duration = 4.5 
        elif season == 'Kharif':
            solar_efficiency = 0.15 
            sunlight_duration = 5.5     
        elif season == 'Rabi':
            solar_efficiency = 0.15 
            sunlight_duration = 6.5 
        elif season == 'Zaid':
            solar_efficiency = 0.15 
            sunlight_duration = 7.5
        else:
            solar_efficiency = 0.25 
            sunlight_duration = 4.5 
    elif location == 'Mizoram':
        if season == 'Autumn':
            solar_efficiency = 0.15 # in percentage
            sunlight_duration = 5.5 # in hours
        elif season == 'Spring':
            solar_efficiency = 0.15 
            sunlight_duration = 6.5     
        elif season == 'Summer':
            solar_efficiency = 0.15 
            sunlight_duration = 7.5 
        elif season == 'Winter':
            solar_efficiency = 0.15 
            sunlight_duration = 4.5 
        elif season == 'Kharif':
            solar_efficiency = 0.15 
            sunlight_duration = 5.5     
        elif season == 'Rabi':
            solar_efficiency = 0.15 
            sunlight_duration = 6.5 
        elif season == 'Zaid':
            solar_efficiency = 0.15 
            sunlight_duration = 7.5
        else:
            solar_efficiency = 0.25 
            sunlight_duration = 4.5 
    elif location == 'Nagaland':
        if season == 'Autumn':
            solar_efficiency = 0.15 # in percentage
            sunlight_duration = 5.5 # in hours
        elif season == 'Spring':
            solar_efficiency = 0.15 
            sunlight_duration = 6.5     
        elif season == 'Summer':
            solar_efficiency = 0.15 
            sunlight_duration = 7.5 
        elif season == 'Winter':
            solar_efficiency = 0.15 
            sunlight_duration = 4.5 
        elif season == 'Kharif':
            solar_efficiency = 0.15 
            sunlight_duration = 5.5     
        elif season == 'Rabi':
            solar_efficiency = 0.15 
            sunlight_duration = 6.5 
        elif season == 'Zaid':
            solar_efficiency = 0.15 
            sunlight_duration = 7.5
        else:
            solar_efficiency = 0.25 
            sunlight_duration = 4.5 
    elif location == 'Odisha':
        if season == 'Autumn':
            solar_efficiency = 0.15 # in percentage
            sunlight_duration = 6.5 # in hours
        elif season == 'Spring':
            solar_efficiency = 0.15 
            sunlight_duration = 6.5     
        elif season == 'Summer':
            solar_efficiency = 0.15 
            sunlight_duration = 7.5 
        elif season == 'Winter':
            solar_efficiency = 0.15 
            sunlight_duration = 5.5 
        elif season == 'Kharif':
            solar_efficiency = 0.15 
            sunlight_duration = 6     
        elif season == 'Rabi':
            solar_efficiency = 0.15 
            sunlight_duration = 8 
        elif season == 'Zaid':
            solar_efficiency = 0.15 
            sunlight_duration = 9
        else:
            solar_efficiency = 0.25 
            sunlight_duration = 4.5 
    elif location == 'Punjab':
        if season == 'Autumn':
            solar_efficiency = 0.25 # in percentage
            sunlight_duration = 7.5 # in hours
        elif season == 'Spring':
            solar_efficiency = 0.25 
            sunlight_duration = 7.5     
        elif season == 'Summer':
            solar_efficiency = 0.25 
            sunlight_duration = 8.5 
        elif season == 'Winter':
            solar_efficiency = 0.25 
            sunlight_duration = 5.5 
        elif season == 'Kharif':
            solar_efficiency = 0.25 
            sunlight_duration = 6.5     
        elif season == 'Rabi':
            solar_efficiency = 0.25 
            sunlight_duration = 7.5 
        elif season == 'Zaid':
            solar_efficiency = 0.25 
            sunlight_duration = 8.5
        else:
            solar_efficiency = 0.25 
            sunlight_duration = 4.5 
    elif location == 'Rajasthan':
        if season == 'Autumn':
            solar_efficiency = 0.25 # in percentage
            sunlight_duration = 7.5 # in hours
        elif season == 'Spring':
            solar_efficiency = 0.25 
            sunlight_duration = 7.5     
        elif season == 'Summer':
            solar_efficiency = 0.25 
            sunlight_duration = 8.5 
        elif season == 'Winter':
            solar_efficiency = 0.25 
            sunlight_duration = 5.5 
        elif season == 'Kharif':
            solar_efficiency = 0.25 
            sunlight_duration = 7.5     
        elif season == 'Rabi':
            solar_efficiency = 0.25 
            sunlight_duration = 8.5 
        elif season == 'Zaid':
            solar_efficiency = 0.25 
            sunlight_duration = 9.5
        else:
            solar_efficiency = 0.25 
            sunlight_duration = 4.5 
    elif location == 'Sikkim':
        if season == 'Autumn':
            solar_efficiency = 0.15 # in percentage
            sunlight_duration = 5.5 # in hours
        elif season == 'Spring':
            solar_efficiency = 0.15 
            sunlight_duration = 6.5     
        elif season == 'Summer':
            solar_efficiency = 0.15 
            sunlight_duration = 7.5 
        elif season == 'Winter':
            solar_efficiency = 0.15 
            sunlight_duration = 4.5 
        elif season == 'Kharif':
            solar_efficiency = 0.15 
            sunlight_duration = 5.5     
        elif season == 'Rabi':
            solar_efficiency = 0.15 
            sunlight_duration = 6.5 
        elif season == 'Zaid':
            solar_efficiency = 0.15 
            sunlight_duration = 7.5
        else:
            solar_efficiency = 0.25 
            sunlight_duration = 4.5 
    elif location == 'Tamil Nadu':
        if season == 'Autumn':
            solar_efficiency = 0.25 # in percentage
            sunlight_duration = 6.5 # in hours
        elif season == 'Spring':
            solar_efficiency = 0.25 
            sunlight_duration = 6.5     
        elif season == 'Summer':
            solar_efficiency = 0.25 
            sunlight_duration = 7.5 
        elif season == 'Winter':
            solar_efficiency = 0.25 
            sunlight_duration = 5.5 
        elif season == 'Kharif':
            solar_efficiency = 0.25 
            sunlight_duration = 6.5     
        elif season == 'Rabi':
            solar_efficiency = 0.25 
            sunlight_duration = 7.5 
        elif season == 'Zaid':
            solar_efficiency = 0.25 
            sunlight_duration = 8.5
        else:
            solar_efficiency = 0.25 
            sunlight_duration = 4.5 
    elif location == 'Telangana':
        if season == 'Autumn':
            solar_efficiency = 0.25 # in percentage
            sunlight_duration = 6.5 # in hours
        elif season == 'Spring':
            solar_efficiency = 0.25 
            sunlight_duration = 6.5     
        elif season == 'Summer':
            solar_efficiency = 0.25 
            sunlight_duration = 7.5 
        elif season == 'Winter':
            solar_efficiency = 0.25 
            sunlight_duration = 5.5 
        elif season == 'Kharif':
            solar_efficiency = 0.25 
            sunlight_duration = 6.5     
        elif season == 'Rabi':
            solar_efficiency = 0.25 
            sunlight_duration = 7.5 
        elif season == 'Zaid':
            solar_efficiency = 0.25 
            sunlight_duration = 8.5
        else:
            solar_efficiency = 0.25 
            sunlight_duration = 4.5 
    elif location == 'Tripura':
        if season == 'Autumn':
            solar_efficiency = 0.15 # in percentage
            sunlight_duration = 5.5 # in hours
        elif season == 'Spring':
            solar_efficiency = 0.15 
            sunlight_duration = 6.5     
        elif season == 'Summer':
            solar_efficiency = 0.15 
            sunlight_duration = 7.5 
        elif season == 'Winter':
            solar_efficiency = 0.15 
            sunlight_duration = 4.5 
        elif season == 'Kharif':
            solar_efficiency = 0.15 
            sunlight_duration = 5.5     
        elif season == 'Rabi':
            solar_efficiency = 0.15 
            sunlight_duration = 6.5 
        elif season == 'Zaid':
            solar_efficiency = 0.15 
            sunlight_duration = 7.5
        else:
            solar_efficiency = 0.25 
            sunlight_duration = 4.5 
    elif location == 'Uttar Pradesh':
        if season == 'Autumn':
            solar_efficiency = 0.20 # in percentage
            sunlight_duration = 5.5 # in hours
        elif season == 'Spring':
            solar_efficiency = 0.20 
            sunlight_duration = 6.5     
        elif season == 'Summer':
            solar_efficiency = 0.20 
            sunlight_duration = 7.5 
        elif season == 'Winter':
            solar_efficiency = 0.20 
            sunlight_duration = 4.5 
        elif season == 'Kharif':
            solar_efficiency = 0.20 
            sunlight_duration = 6.5     
        elif season == 'Rabi':
            solar_efficiency = 0.20
            sunlight_duration = 7.5 
        elif season == 'Zaid':
            solar_efficiency = 0.250
            sunlight_duration = 8.5
        else:
            solar_efficiency = 0.25 
            sunlight_duration = 4.5 
    elif location == 'West Bengal':
        if season == 'Autumn':
            solar_efficiency = 0.25 # in percentage
            sunlight_duration = 5.5 # in hours
        elif season == 'Spring':
            solar_efficiency = 0.25 
            sunlight_duration = 5.5     
        elif season == 'Summer':
            solar_efficiency = 0.25 
            sunlight_duration = 6.5 
        elif season == 'Winter':
            solar_efficiency = 0.25 
            sunlight_duration = 4.5 
        elif season == 'Kharif':
            solar_efficiency = 0.25 
            sunlight_duration = 6    
        elif season == 'Rabi':
            solar_efficiency = 0.25 
            sunlight_duration = 8
        elif season == 'Zaid':
            solar_efficiency = 0.25 
            sunlight_duration = 9
        else:
            solar_efficiency = 0.25 
            sunlight_duration = 4.5 
    else:
        # Default values in case the location is not listed
        solar_efficiency = 0.25
        sunlight_duration = 5.5
    
         # Additional code for crop life cycle based on location and crop type
            # for solar effeciency and sunlight duration based on location
    if location == 'Andhra Pradesh':
        if crop_type == 'Cotton':
            crop_lifecycle = 165
        elif crop_type == ' Groundnut':
            crop_lifecycle = 135
        elif crop_type == 'Rice':
            crop_lifecycle = 150
        elif crop_type == 'Wheat':
            crop_lifecycle = 135
        else:
            crop_lifecycle = 90
    elif location == 'Arunachal Pradesh':
        if crop_type == 'Millets':
            crop_lifecycle = 75
        elif crop_type == 'Rice':
            crop_lifecycle = 135
        elif crop_type == 'Wheat':
            crop_lifecycle = 135
        else:
            crop_lifecycle = 90
    elif location == 'Assam':
        if crop_type == 'Rice':
            crop_lifecycle = 135
        elif crop_type == 'Wheat':
            crop_lifecycle = 135
        else:
            crop_lifecycle = 90
    elif location == 'Bihar':
        if crop_type == 'Maize':
            crop_lifecycle = 105
        elif crop_type == 'Rice':
            crop_lifecycle = 135
        elif crop_type == 'Wheat':
            crop_lifecycle = 135
        else:
            crop_lifecycle = 90
    elif location == 'Chhattisgarh':
        if crop_type == 'Maize':
            crop_lifecycle = 105
        elif crop_type == 'Rice':
            crop_lifecycle = 135
        elif crop_type == 'Soyabean':
            crop_lifecycle = 105
        elif crop_type == 'Wheat':
            crop_lifecycle = 135
        else:
            crop_lifecycle = 90
    elif location == 'Goa':
        if crop_type == 'Rice':
            crop_lifecycle = 135
        elif crop_type == 'Wheat':
            crop_lifecycle = 135
        else:
            crop_lifecycle = 90
    elif location == 'Gujarat':
        if crop_type == 'Cotton':
            crop_lifecycle = 165
        elif crop_type == ' Groundnut':
            crop_lifecycle = 135
        elif crop_type == ' Groundnut':
            crop_lifecycle = 105
        elif crop_type == 'Rice':
            crop_lifecycle = 135
        elif crop_type == 'Wheat':
            crop_lifecycle = 135
        else:
            crop_lifecycle = 90
    elif location == 'Haryana':
        if crop_type == 'Rice':
            crop_lifecycle = 105
        elif crop_type == 'Rice':
            crop_lifecycle = 135
        elif crop_type == 'Wheat':
            crop_lifecycle = 135
        else:
            crop_lifecycle = 90
    elif location == 'Himachal Pradesh':
        if crop_type == 'Rice':
            crop_lifecycle = 135
        elif crop_type == 'Vegetables':
            crop_lifecycle = 105
        elif crop_type == 'Wheat':
            crop_lifecycle = 135
        else:
            crop_lifecycle = 90
    elif location == 'Jharkhand':
        if crop_type == 'Maize':
            crop_lifecycle = 105
        elif crop_type == 'Pulses':
            crop_lifecycle = 100
        elif crop_type == 'Rice':
            crop_lifecycle = 140
        elif crop_type == 'Wheat':
            crop_lifecycle = 145
        else:
            crop_lifecycle = 90
    elif location == 'Karnataka':
        if crop_type == 'Coffee':
            crop_lifecycle = 315 #per harvesting cycle
        elif crop_type == 'Rice':
            crop_lifecycle = 135
        elif crop_type == 'Sugarcane':
            crop_lifecycle = 450
        elif crop_type == 'Wheat':
            crop_lifecycle = 135
        else:
            crop_lifecycle = 90
    elif location == 'Kerala':
        if crop_type == 'Rice':
            crop_lifecycle = 135
        elif crop_type == 'Wheat':
            crop_lifecycle = 135
        else:
            crop_lifecycle = 90
    elif location == '>Madhya Pradesh':
        if crop_type == 'Gram':
            crop_lifecycle = 105
        elif crop_type == 'Rice':
            crop_lifecycle = 135
        elif crop_type == 'Soyabean':
            crop_lifecycle = 105
        elif crop_type == 'Wheat':
            crop_lifecycle = 135
        else:
            crop_lifecycle = 90
    elif location == 'Maharashtra':
        if crop_type == 'Cotton':
            crop_lifecycle = 165
        elif crop_type == 'Rice':
            crop_lifecycle = 135
        elif crop_type == 'Sugarcane':
            crop_lifecycle = 450
        elif crop_type == 'Wheat':
            crop_lifecycle = 135
        else:
            crop_lifecycle = 90
    elif location == 'Manipur':
        if crop_type == 'Maize':
            crop_lifecycle = 105
        elif crop_type == 'Rice':
            crop_lifecycle = 135
        elif crop_type == 'Wheat':
            crop_lifecycle = 135
        else:
            crop_lifecycle = 90
    elif location == 'Meghalaya':
        if crop_type == 'Maize':
            crop_lifecycle = 105
        elif crop_type == 'Rice':
            crop_lifecycle = 135
        elif crop_type == 'Vegetables':
            crop_lifecycle = 105
        elif crop_type == 'Wheat':
            crop_lifecycle = 135
        else:
            crop_lifecycle = 90
    elif location == 'Mizoram':
        if crop_type == 'Maize':
            crop_lifecycle = 105
        elif crop_type == 'Rice':
            crop_lifecycle = 135
        elif crop_type == 'Wheat':
            crop_lifecycle = 135
        else:
            crop_lifecycle = 90
    elif location == 'Nagaland':
        if crop_type == 'Maize':
            crop_lifecycle = 105
        elif crop_type == 'Millets':
            crop_lifecycle = 75
        elif crop_type == 'Rice':
            crop_lifecycle = 135
        elif crop_type == 'Wheat':
            crop_lifecycle = 135
        else:
            crop_lifecycle = 90
    elif location == 'Odisha':
        if crop_type == 'Rice':
            crop_lifecycle = 135
        elif crop_type == 'Wheat':
            crop_lifecycle = 135
        else:
            crop_lifecycle = 90
    elif location == 'Punjab':
        if crop_type == 'Maize':
            crop_lifecycle = 105
        elif crop_type == 'Rice':
            crop_lifecycle = 135
        elif crop_type == 'Wheat':
            crop_lifecycle = 135
        else:
            crop_lifecycle = 90
    elif location == 'Rajasthan':
        if crop_type == 'Barley':
            crop_lifecycle = 105
        elif crop_type == 'Mustard':
            crop_lifecycle = 105
        elif crop_type == 'Rice':
            crop_lifecycle = 135
        elif crop_type == 'Wheat':
            crop_lifecycle = 135
        else:
            crop_lifecycle = 90
    elif location == 'Sikkim':
        if crop_type == 'Rice':
            crop_lifecycle = 135
        elif crop_type == 'Wheat':
            crop_lifecycle = 135
        else:
            crop_lifecycle = 90
    elif location == 'Tamil Nadu':
        if crop_type == 'Cotton':
            crop_lifecycle = 165
        elif crop_type == 'Groundnut':
            crop_lifecycle = 135
        elif crop_type == 'Rice':
            crop_lifecycle = 135
        if crop_type == 'Sugarcane':
            crop_lifecycle = 450
        elif crop_type == 'Wheat':
            crop_lifecycle = 135
        else:
            crop_lifecycle = 90
    elif location == 'Telangana':
        if crop_type == 'Rice':
            crop_lifecycle = 135
        elif crop_type == 'Wheat':
            crop_lifecycle = 135
        else:
            crop_lifecycle = 90
    elif location == 'Tripura':
        if crop_type == 'Rice':
            crop_lifecycle = 135
        elif crop_type == 'Wheat':
            crop_lifecycle = 135
        else:
            crop_lifecycle = 90
    elif location == 'Uttar Pradesh':
        if crop_type == 'Rice':
            crop_lifecycle = 135
        elif crop_type == 'Sugarcane':
            crop_lifecycle = 450
        elif crop_type == 'Vegetables':
            crop_lifecycle = 105
        elif crop_type == 'Wheat':
            crop_lifecycle = 135
        else:
            crop_lifecycle = 90
    elif location == 'Uttarakhand':
        if crop_type == 'Rice':
            crop_lifecycle = 135
        elif crop_type == 'Wheat':
            crop_lifecycle = 135
        else:
            crop_lifecycle = 90
    elif location == 'West Bengal':
        if crop_type == 'Rice':
            crop_lifecycle = 135
        elif crop_type == 'Wheat':
            crop_lifecycle = 135
        else:
            crop_lifecycle = 90
    else:
        crop_lifecycle = 90  # Default crop lifecycle value

    solar_panel_energy_capacity = 365 * solar_efficiency * sunlight_duration * crop_lifecycle # 365W
    average_energy_consumption = field_size * ((10 * 0.001) * 25 * 1000 * 9.81 * (2.7778 * 10**-4)) # energy required to lift the water 25 meter = Volume * height * density * gravity, volume = field size * (depth volume = 10mm per day), in watt-hr
    total_energy_consumption = average_energy_consumption * 5.5 * 90 * 0.6 # effeciency 60 percentage
    solar_emissions = 41 * (total_energy_consumption/1000) # 41 is in gram, A 1 kW or 1 unit rooftop system generally requires 12 sq. metres (130 square feet) 
    dg_emissions = 1144 * (total_energy_consumption/1000)  #  1144 is in gram for 1 unit or 1000watt
    co2_emissions_difference = dg_emissions - solar_emissions
    co2_emissions_difference_kg = co2_emissions_difference / 1000  # Convert grams to kilograms

    if co2_emissions_difference > 0:
        co2_emissions_difference_str = 'Reduced by {:.2f} kg (Compared to conventional DG_set)'.format(co2_emissions_difference_kg)
    elif co2_emissions_difference == 0:
        co2_emissions_difference_str = 'No difference in emissions'
    else:
        co2_emissions_difference_str = 'Increased by {:.2f} kg'.format(co2_emissions_difference_kg)

    # Calculate solar installation 
    average_energy_consumption = field_size * ((10 * 0.001) * 25 * 1000 * 9.81 * (2.7778 * 10**-4))
    total_energy_consumption = average_energy_consumption * 5.5 * 90 * 1.67 # effeciency 60 percentage
    panels_required = total_energy_consumption / solar_panel_energy_capacity

    # Calculate solar panel capacity
    total_solar_panel_energy_capacity =  solar_panel_energy_capacity * panels_required
    formatted_total_solar_panel_energy_capacity ="{:.2f} W".format(total_solar_panel_energy_capacity)


    # Calculate installation cost
    solar_cost = panels_required * 15000
    formatted_solar_cost = "INR {:.2f}".format(solar_cost)

    # Calculate loan and subsidy availability based on location
    loan_subsidy_avail = 'No' if location in ['Assam', 'Goa', 'Himachal Pradesh', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Sikkim', 'Tripura', 'Jammu and Kashmir', 'Uttarakhand'] else 'Yes'

    # Calculate feasibility score...
    # 1st, 1 marks for co2 emission
    if  co2_emissions_difference > 0:
         co2_score = 1
    elif  co2_emissions_difference == 0:
           co2_score = 0.5 
    else:
        co2_score = 0

    # 2nd, 1 marks for area needed on land
    area_of_one_solar_panel = (1755 / 1000) * (1040 / 1000)  # Convert mm to meters
    area_needed = panels_required * area_of_one_solar_panel * (1 + 0.05)  # 5% added for mounting structure and civil work
    tilt_angle_degrees = 20  # Standard tilt angle used in North India in degrees
    tilt_angle_radians = tilt_angle_degrees * (math.pi / 180)
    area_needed_on_land = area_needed * abs(math.cos(tilt_angle_radians))

    if area_needed_on_land < (field_size * 0.25):
        area_score = 1
    elif area_needed_on_land < (field_size * 0.4):
        area_score = 0.5
    else:
        area_score = 0

    # 3rd, 1 marks for price difference
    government_crop_price = 2200  # Standard price rate of the crop type per ton for the government in INR
    government_diesel_price = (92 * 5.5 * 90) + 5000  # Replace with the actual price of diesel with all setup in INR
    solar_plate_life_span = 100  # Lifespan of solar panels in years = 25 * 4
    total_cost_of_solar_plate = solar_cost / solar_plate_life_span
    price_difference = government_crop_price - total_cost_of_solar_plate
    diesel_price_difference = government_crop_price - government_diesel_price
    price_score = 1 if price_difference < diesel_price_difference else 0

    # 4th, 1 marks for breakeven
    crop_yield_per_sq_meter = 14  # gm
    government_crop_price_per_kg = 22  # INR
    total_money_required_for_crop = (crop_yield_per_sq_meter * field_size) * government_crop_price_per_kg / 1000
    if total_money_required_for_crop / 4 >= total_cost_of_solar_plate:  # One-fourth of total money required, total_cost_of_solar_plate per season
        break_even_score = 1
    else:
        break_even_score = 0

    # 5th, 1 marks for loan and subsidy
    if loan_subsidy_avail == 'No':
        marks = 0
    else:
        marks = 1

    # 6th, 1 marks for ROI
    crop_yield_per_sq_meter = 14  # gm
    total_crop_yield_per_kg = (crop_yield_per_sq_meter * field_size) / 1000
    gain_from_investment = (total_crop_yield_per_kg * (government_crop_price_per_kg / 100))
    ROI = ((gain_from_investment - total_cost_of_solar_plate) / total_cost_of_solar_plate)
    if ROI == 1:
        ROI_marks = 1
    else:
        ROI_marks = 0

    total_score = co2_score + area_score + price_score + break_even_score + marks + ROI_marks

    # Determine feasibility
    if total_score >= 3.5:
        feasibility = 'Good'
    elif total_score >= 2.5:
        feasibility = 'Moderate'
    else:
        feasibility = 'Poor'

    # Calculations for profitibility Index
    Profitibility_Index = ((((gain_from_investment + ((solar_cost) * 20 / 100) + total_cost_of_solar_plate) / total_cost_of_solar_plate) -21) * 1000)
         # Profitability Index = (Net Present value + Initial investment) / Initial investment
         # overheads =((solar_cost)*20/100)
    formatted_Profitibility_Index ="{:.4f}".format(Profitibility_Index)

    # Calcutions for effective Pricing
    
    # Discount_price= 
    if location == 'Andhra Pradesh':
            subsidy_cost = (50/100) * solar_cost
    elif location == 'Arunachal Pradesh':
            subsidy_cost = (32.5/100) * solar_cost
    elif location == 'Assam':
            subsidy_cost = (40/100) * solar_cost
    elif location == 'Bihar':
            subsidy_cost = (37.5/100) * solar_cost
    elif location == 'Chhattisgarh':
            subsidy_cost = (42.5/100) * solar_cost
    elif location == 'Goa':
            subsidy_cost = (32.5/100) * solar_cost
    elif location == 'Gujarat':
            subsidy_cost = (32.5/100) * solar_cost
    elif location == 'Haryana':
            subsidy_cost = (57.5/100) * solar_cost
    elif location == 'Himachal Pradesh':
            subsidy_cost = (50/100) * solar_cost
    elif location == 'Jharkhand':
            subsidy_cost = (40/100) * solar_cost
    elif location == 'Karnataka':
            subsidy_cost = (40/100) * solar_cost
    elif location == 'Kerala':
            subsidy_cost = (40/100) * solar_cost
    elif location == 'Madhya Pradesh':
            subsidy_cost = (45/100) * solar_cost
    elif location == 'Maharashtra':
            subsidy_cost = (32.5/100) * solar_cost
    elif location == 'Manipur':
            subsidy_cost = (32.5/100) * solar_cost
    elif location == 'Meghalaya':
            subsidy_cost = (32.5/100) * solar_cost
    elif location == 'Mizoram':
            subsidy_cost = (32.5/100) * solar_cost
    elif location == 'Nagaland':
            subsidy_cost = (32.5/100) * solar_cost
    elif location == 'Odisha':
            subsidy_cost = (40/100) * solar_cost
    elif location == 'Punjab':
            subsidy_cost = (62.5/100) * solar_cost
    elif location == 'Rajasthan':
            subsidy_cost = (42.5/100) * solar_cost
    elif location == 'Sikkim':
            subsidy_cost = (45/100) * solar_cost
    elif location == 'Tamil Nadu':
            subsidy_cost = (50/100) * solar_cost
    elif location == 'Telangana':
            subsidy_cost = (50/100) * solar_cost
    elif location == 'Tripura':
            subsidy_cost = (40/100) * solar_cost
    elif location == 'Uttar Pradesh':
            subsidy_cost = (40/100) * solar_cost
    elif location == 'Uttarakhand':
            subsidy_cost = (50/100) * solar_cost
    elif location == 'West Bengal':
            subsidy_cost = (40/100) * solar_cost
    else:
        subsidy_cost = (40/100) * solar_cost
    
    Maintenance_charges = (10/100) * solar_cost
    EMI = (11/100) * solar_cost # In all states aproximately 10 to 12 percentage

    Effective_Pricing = (solar_cost - subsidy_cost) + EMI + Maintenance_charges  # Effective Price = Gross Price - Discount Price
    formatted_Effective_Pricing = "INR {:.2f}".format(Effective_Pricing)  # assuming downpayment zero due to variablity

    return render_template(
        'results.html',
        co2_emissions=co2_emissions_difference_str,
        solar_cost=formatted_solar_cost,
        feasibility=feasibility,
        loan_subsidy_avail=loan_subsidy_avail,
        Profitibility_Index=formatted_Profitibility_Index,
        Solar_Panel_Capacity=formatted_total_solar_panel_energy_capacity,
        Effective_Pricing=formatted_Effective_Pricing
    )

if __name__ == '__main__':
    app.run(debug=True)
