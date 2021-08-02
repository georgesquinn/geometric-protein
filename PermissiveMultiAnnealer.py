import PermissiveAnnealSphereFinder


def main(points_array, exemption_constant):
    sphere = PermissiveAnnealSphereFinder.main(points_array, exemption_constant)
    for _ in range(9):
        other_sphere = PermissiveAnnealSphereFinder.main(points_array, exemption_constant)
        if other_sphere[0] < sphere[0]:
            sphere = other_sphere
    return sphere
