from classes import * 

class data():

    def __init__(self):
        self.info = []
        self.dist = []

    
    def add_satellite(self,OrbitClass,OrbitType,LifeTime,Purpose,perigee,apogee,eccentricity,inclination,Name,Operator,User):
        s1 = Satellite(OrbitClass,OrbitType,LifeTime,Purpose,perigee,apogee,eccentricity,inclination,Name,Operator,User)
        self.info.append(s1)
    
    def add_orbit(self,perigee,apogee,eccentricity,inclination):
        s2 = orbit(perigee,apogee,eccentricity,inclination)
        self.dist.append(s2)
    
    def remove_by_name(self,name):
        x=0
        for obj in self.info:
            if obj.Name==name:
                index = self.info.index(obj)
                var = self.info.pop(index)
                x = var.Name
        return x

   
    def count_elements(self):
        return len(self.info)

  
    def display(self):
        for element in self.info:
            print(element.Name,element.Purpose)



    #Details class related functions

    def count_by_purpose(self,purpose):
        count = 0
        for obj in self.info:
            if obj.Purpose == purpose:
                count = count + 1
        return count

    def max_lifetime(self):
        max = 0.0
        for obj in self.info:
            x = float(obj.LifeTime)
            if(max < x):
                max = x
        return max

    def all_satellites_by_OrbitType(self,Type):
        sats = []
        for obj in self.info:
            if obj.OrbitType == Type:
                sats.append(obj.Name)
        return sats

    def count_by_user_operator(self,user,operator):
        count=0
        for obj in self.info:
            if obj.User==user and obj.Operator==operator:
                count = count+1
        return count

    def count_bw_life_range(self,min,max):
        count=0
        for obj in self.info:
            x = float(obj.LifeTime)
            if x>min and x<max:
                count = count+1
        return count

    #orbit class related functions

    def MaxPerigee(self):
        max = 0.0
        #print("In max func:")
        for i in self.dist:
            m = float(i.perigee)
            if(max < m):
                max = m
        return max

    def MinPerigee(self):
        min = 0
        for i in self.dist:
            if(min > float(i.perigee)):
                min = i.perigee
        return min

    def AvgPerigee(self):
        sum_perigee = 0
        cnt=0
        for i in self.dist:
            sum_perigee = sum_perigee + float(i.perigee)
            cnt = cnt + 1
        return (sum_perigee/cnt)


    def MaxApogee(self):
        max = 0.0
        for i in self.dist:
            m = float(i.apogee)
            if(max < m):
                max = m
        return max

    def MinApogee(self):
        min = 0.0
        for i in self.dist:
            m = float(i.apogee)
            if(min > m):
                min = m
        return min

    def AvgApogee(self):
        sum_apogee = 0
        cnt=0
        for i in self.dist:
            sum_apogee = sum_apogee + float(i.apogee)
            cnt = cnt + 1
        return (sum_apogee/cnt)

    def AvgEcentricity(self):
        sum_e = 0
        cnt=0
        for i in self.dist:
            sum_e = sum_e + float(i.eccentricity)
            cnt = cnt + 1
        return (sum_e/cnt)

    def AvgInclination(self):   
        sum_i = 0
        cnt = 0
        for j in self.dist:
            sum_i = sum_i + float(j.inclination)
            cnt = cnt + 1
        return (sum_i/cnt)

    def count_elements_orbit(self):
        return len(self.dist)
# Regular Expressions

# Regular Expressions
    