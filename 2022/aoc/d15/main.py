from typing import IO

from collections import defaultdict

class Beacon:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def manhattan_distance(self, sensor):
        return abs(self.x - sensor.x) + abs(self.y - sensor.y)

class Sensor:
    def __init__(self, x, y, closest_beacon):
        self.x = x
        self.y = y
        self.closest_beacon = closest_beacon
    
    def manhattan_distance(self, beacon):
        return abs(self.x - beacon.x) + abs(self.y - beacon.y)

def p_1(input_file: IO,
        debug=False): # pylint: disable=unused-argument
    
    y, sensorSet = input_file.read().strip().split('\n\n')
    y = int(y.split('=')[1])
    xs = set()
    input = sensorSet.split('\n')
    # Initialize a hash map to store the beacons and their counts
    beacon_counts = defaultdict(int)
    
    # Initialize a set to store the coordinates of the beacons not detected by any sensor
    undetected_beacons = set()
    
    # Parse the input and create a list of sensors and beacons
    sensors = []
    beacons = []
    manhattan_distances = []
    for line in input:
        parts = line.split()
        coords = parts[2], parts[3], parts[8], parts[9]
        sensorX, sensorY, beaconX, beaconY = [int(coord.strip().strip(',').strip(':').split('=')[1]) for coord in coords]
        xs.add(sensorX)
        xs.add(beaconX)
        beacon = Beacon(beaconX, beaconY)
        sensor = Sensor(sensorX, sensorY, beacon)
        sensors.append(sensor)
        beacons.append(beacon)
        manhattan_distances.append(sensor.manhattan_distance(beacon))
    
    beacons_on_y = [beacon for beacon in beacons if beacon.y == y]
    
    # Find the minimum and maximum x coordinates
    minX = min(xs)
    maxX = max(xs)
    
    distressNot = 0
    for x in range(minX - max(manhattan_distances), maxX + max(manhattan_distances) + 1):
        beacon = Beacon(x, y)
        found = False
        for sensor in sensors:
            if sensor.manhattan_distance(beacon) <= sensor.manhattan_distance(sensor.closest_beacon):
                found = True
                break
        for beacon in beacons_on_y:
            if beacon.x == x:
                found = False
                break
        if found:
            distressNot += 1
    
    return distressNot




def p_2(input_file: IO,
        debug=False): # pylint: disable=unused-argument
    pass
