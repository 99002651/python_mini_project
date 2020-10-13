class details:
    def __init__(self,OrbitClass,OrbitType,LifeTime,Purpose):
        self.OrbitClass = OrbitClass
        self.OrbitType = OrbitType
        self.LifeTime = LifeTime
        self.Purpose = Purpose

class orbit:
    def __init__(self,perigee,apogee,eccentricity,inclination):
        self.perigee = perigee
        self.apogee = apogee
        self.eccentricity = eccentricity
        self.inclination = inclination

class Satellite(orbit,details):
    def __init__(self,OrbitClass,OrbitType,LifeTime,Purpose,perigee,apogee,eccentricity,inclination,Name,Operator,User):
        details.__init__(self,OrbitClass,OrbitType,LifeTime,Purpose)
        orbit.__init__(self,perigee,apogee,eccentricity,inclination)
        self.Name = Name
        self.Operator = Operator
        self.User = User

