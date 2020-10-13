import csv
from data import *
        
d1 = data()
with open('satellite.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        for i in range(len(row)):
            name = row[0]
            operator = row[1]
            user = row[2]
            purpose = row[3]
            OrbitClass = row[4]
            OrbitType = row[5]
            perigee = row[6]
            apogee = row[7]
            eccentricity = row[8]
            inclination = row[9]
            Mass = row[10]
            year = row[11]
            LifeTime = row[12]
            LaunchSite = row[13]
            LaunchVehicle = row[14]        
    
        d1.add_satellite(OrbitClass,OrbitType,LifeTime,purpose,perigee,apogee,eccentricity,inclination,name,operator,user)
        d1.add_orbit(perigee,apogee,eccentricity,inclination)

print(d1.count_elements())    
print(d1.remove_by_name('1HOPSAT')) 
print(d1.count_elements())  

print(d1.count_by_purpose('Communications'))
print(d1.max_lifetime())
print(d1.all_satellites_by_OrbitType('Elliptical'))

print(d1.count_bw_life_range(2,10))

print("max value:",d1.MaxPerigee())
print(d1.MinPerigee())
print(d1.AvgPerigee())
print(d1.MaxApogee())
print(d1.MinApogee())
print(d1.AvgApogee())
print(d1.AvgEcentricity())
print(d1.AvgInclination())
print(d1.count_elements_orbit())