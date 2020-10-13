import unittest
import csv
from data import *

class TESTS(unittest.TestCase):

    def setUp(self):
        self.d1 = data()
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
                self.d1.add_satellite(OrbitClass,OrbitType,LifeTime,purpose,name,operator,user)
        
           
    def test_count(self):
        self.assertEqual(284,self.d1.count_elements())

    def test_remove(self):
        self.assertEqual('1HOPSAT',self.d1.remove_by_name('1HOPSAT'))
    
    def test_by_purpose(self):
        self.assertEqual(91,self.d1.count_by_purpose('Communications'))
    
    def test_max_lifetime(self):
        self.assertEqual(25,self.d1.max_lifetime())

    def test_by_orbit_type(self):
        l = self.d1.all_satellites_by_OrbitType('Elliptical')
        self.assertEqual(5,len(l))

    def test_bw_liferange(self):
        self.assertEqual(196,self.d1.count_bw_life_range(2,10))

if __name__ == '__main__':
    unittest.main()


