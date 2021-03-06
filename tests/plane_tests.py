from project.plane_class import *


airbus1 = Plane("A321", "BA", 10001, 200)

# ----------------------------------------------------------
exp_flight_no = 10001
# Test 1: Get
print("Testing method: get_flight_no() ")
output1 = airbus1.get_flight_no()
print(f"Test result:  {output1}")
print(output1 == exp_flight_no)

# ----------------------------------------------------------
new_flight_no = 10100
# Test 2: Set
print("\nTesting method: set_flight_no()  ")
airbus1.set_flight_no(10100)
output2 = airbus1.get_flight_no()
print(f"Test result: {output2}")
print(output2 == new_flight_no)