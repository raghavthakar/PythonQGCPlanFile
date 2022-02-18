import json

# useful for writing null into json
null = None

class QGCPlanFile:
    # Arguments: firmwaretype, hoverspeed (m/s), plannedHomePosition [lat, long, alt]
    def __init__(self, planned_home_position, firmware_type = 12, hover_speed = 7):
        self.mission = {
            "fileType": "Plan",
            "geoFence": {
                "circles": [
                ],
                "polygons": [
                ],
                "version": 2
            },
            "groundStation": "QGroundControl",
            "mission": {
                "firmwareType": firmware_type,
                "hoverSpeed": hover_speed,
                "items": [],
                "plannedHomePosition": planned_home_position,
                "vehicleType": 2,
                "version": 2
            },
            "rallyPoints": {
                "points": [
                ],
                "version": 2
            },
            "version": 1
        }
    
    def addTakeoffItem(self, latitude, longitude, altitude, pitch=0, yaw=0):
        takeoff_item = {
                "autoContinue": True,
                "command": 22,
                "frame": 3,
                "params": [
                    pitch,
                    0,
                    yaw,
                    null,
                    latitude,
                    longitude,
                    altitude
                ],
                "type": "SimpleItem"
            }
        self.mission["mission"]["items"].append(takeoff_item)
    
    def addWaypointItem(self, latitude, longitude, altitude, hold=0, accept_radius=0, pass_radius=0, yaw=0):
        waypoint_item = {
                "autoContinue": True,
                "command": 16,
                "frame": 3,
                "params": [
                    hold,
                    accept_radius,
                    pass_radius,
                    yaw,
                    latitude,
                    longitude,
                    altitude
                ],
                "type": "SimpleItem"
            }
        self.mission["mission"]["items"].append(waypoint_item)

    def addLandItem(self, latitude, longitude, altitude, abort_alt=0, precision_land_mode=0, yaw=0):
        land_item = {
                "autoContinue": True,
                "command": 21,
                "frame": 3,
                "params": [
                    abort_alt,
                    precision_land_mode,
                    0,
                    yaw,
                    latitude,
                    longitude,
                    altitude
                ],
                "type": "SimpleItem"
            }
        self.mission["mission"]["items"].append(land_item)

    def generateMissionFile(self):
        print(self.mission["mission"]["items"])
        with open("sample.plan", "w") as outfile:
            json.dump(self.mission, outfile)

plan_file = QGCPlanFile([47.3985099, 8.5451002, 50])

plan_file.addTakeoffItem(latitude=47.39851, longitude=8.5451002, altitude=50)
plan_file.addWaypointItem(latitude=47.39857, longitude=8.545109, altitude=50)
plan_file.addWaypointItem(latitude=47.39817, longitude=8.545109, altitude=50)
plan_file.addLandItem(latitude=47.39817, longitude=8.545109, altitude=-50)

plan_file.generateMissionFile()