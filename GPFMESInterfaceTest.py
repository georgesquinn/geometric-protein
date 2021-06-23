import GPFMESInterface

sphere = GPFMESInterface.main("2BKF", "default")
print("Sphere radius is: " + format(sphere[0]))
print("Sphere center is: " + format(sphere[1]))