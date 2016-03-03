class Wind:
    def __init__(self, direction=0, speed=0):
        self.direction = direction
        self.speed = speed

    def dict(self):
        return {"speed": self.speed, "dir": self.direction}


class Cyclone:
    def __init__(self):
        self.pressure_spread = 0.0
        self.centerZ = 0.0
        self.ellipticity = 0.0
        self.rotation = 0.0
        self.pressure_excess = 0
        self.centerX = 0.0

    def dict(self):
        d = {
            "pressure_spread": self.pressure_spread,
            "pressure_excess": self.pressure_excess,
            "centerZ": self.centerZ,
            "ellipticity": self.ellipticity,
            "rotation": self.rotation,
            "centerX": self.centerX
        }
        return d


class Weather:
    class Season:
        Summer = 1
        Winter = 2
        Spring = 3
        Fall = 4

    def __init__(self):
        self.atmosphere_type = 0
        self.wind_at_ground = Wind()
        self.wind_at_2000 = Wind()
        self.wind_at_8000 = Wind()
        self.enable_fog = False
        self.turbulence_at_ground = 0
        self.turbulence_at_2000 = 0
        self.turbulence_at_8000 = 0
        self.season_temperature = 20
        self.season_iseason = Weather.Season.Summer
        self.type_weather = 0
        self.qnh = 760
        self.cyclones = []
        self.name = "Summer, clean sky"
        self.fog_thickness = 0
        self.fog_visibility = 25
        self.fog_density = 7
        self.visibility_distance = 80000
        self.clouds_thickness = 200
        self.clouds_density = 0
        self.clouds_base = 300
        self.clouds_iprecptns = 0

    def load_from_dict(self, dict):
        self.atmosphere_type = dict["atmosphere_type"]
        wind = dict.get("wind", {})
        wind_at_ground = wind.get("atGround", {})
        wind_at_2000 = wind.get("at2000", {})
        wind_at_8000 = wind.get("at8000", {})
        self.wind_at_ground = Wind(wind_at_ground.get("dir", 0), wind_at_ground.get("speed", 0))
        self.wind_at_2000 = Wind(wind_at_2000.get("dir", 0), wind_at_2000.get("speed", 0))
        self.wind_at_8000 = Wind(wind_at_8000.get("dir", 0), wind_at_8000.get("speed", 0))
        self.enable_fog = dict["enable_fog"]
        turbulence = dict.get("turbulence", {})
        self.turbulence_at_ground = turbulence.get("atGround", 0)
        self.turbulence_at_2000 = turbulence.get("at2000", 0)
        self.turbulence_at_8000 = turbulence.get("at8000", 0)
        season = dict.get("season", {})
        self.season_temperature = season.get("temperature", 20)
        self.season_iseason = season.get("iseason", 1)
        self.type_weather = dict.get("type_weather", 0)
        self.qnh = dict.get("qnh", 760)
        cyclones = dict.get("cyclones", {})
        for x in cyclones:
            c = Cyclone()
            c.centerX = cyclones[x].get("centerX", 0)
            c.centerZ = cyclones[x].get("centerZ", 0)
            c.ellipticity = cyclones[x].get("ellipticity", 0)
            c.pressure_excess = cyclones[x].get("pressure_excess", 0)
            c.pressure_spread = cyclones[x].get("pressure_spread", 0)
            c.rotation = cyclones[x].get("rotation", 0)
            self.cyclones.append(c)
        self.name = dict.get("name", "Summer, clean sky")
        fog = dict.get("fog", {})
        self.fog_thickness = fog.get("thickness", 0)
        self.fog_visibility = fog.get("visibility", 25)
        self.fog_density = fog.get("density", 7)
        visibility = dict.get("visiblity", {})
        self.visibility_distance = visibility.get("distance", 80000)
        clouds = dict.get("clouds", {})
        self.clouds_thickness = clouds.get("thickness", 200)
        self.clouds_density = clouds.get("density", 0)
        self.clouds_base = clouds.get("base", 300)
        self.clouds_iprecptns = clouds.get("iprecptns", 0)

    def dict(self):
        d = {}
        d["atmosphere_type"] = self.atmosphere_type
        d["wind"] = {"atGround": self.wind_at_ground.dict(),
                     "at2000": self.wind_at_2000.dict(),
                     "at8000": self.wind_at_8000.dict()}
        d["enable_fog"] = self.enable_fog
        d["turbulence"] = {"atGround": self.turbulence_at_ground,
                           "at2000": self.turbulence_at_2000,
                           "at8000": self.turbulence_at_8000}
        d["season"] = {"iseason": self.season_iseason, "temperature": self.season_temperature}
        d["type_weather"] = self.type_weather
        d["qnh"] = self.qnh
        d["cyclones"] = {x: self.cyclones[x].dict() for x in range(0, len(self.cyclones))}
        d["name"] = self.name
        d["fog"] = {"thickness": self.fog_thickness, "visibility": self.fog_visibility, "density": self.fog_density}
        d["visibility"] = {"distance": self.visibility_distance}
        d["clouds"] = {"thickness": self.clouds_thickness,
                       "density": self.clouds_density,
                       "base": self.clouds_base,
                       "iprecptns": self.clouds_iprecptns}
        return d
