import GPFToBackbonePoints
import GPFToResidueCenters
from scipy.spatial import ConvexHull


def in_hull(p, hull):
    """
    Test if points in `p` are in `hull`

    `p` should be a `NxK` coordinates of `N` points in `K` dimensions
    `hull` is either a scipy.spatial.Delaunay object or the `MxK` array of the
    coordinates of `M` points in `K`dimensions for which Delaunay triangulation
    will be computed
    """
    from scipy.spatial import Delaunay
    if not isinstance(hull, Delaunay):
        hull = Delaunay(hull)

    return hull.find_simplex(p) >= 0


def make_convex_hull(protein_name):
    backbone_points = GPFToBackbonePoints.main(protein_name)
    return ConvexHull(backbone_points)


def main(protein_name):
    residue_identities = ["A", "V", "F", "P", "M", "I", "L", "D", "E", "K", "R", "S", "T", "Y", "H", "C", "N", "Q", "W"]
    outside_dict = {}
    for residue in residue_identities:
        outside_dict[residue] = 0
    convex_hull = make_convex_hull(protein_name)
    residue_points = GPFToResidueCenters.main(protein_name, desired_residues=residue_identities)
    hull_vertex_indices = convex_hull.vertices
    vertices_array = []
    for index in hull_vertex_indices:
        vertices_array.append(convex_hull.points[index])
    in_hull_array = in_hull(residue_points[0], vertices_array)
    # print(format(in_hull_array))
    for i in range(len(in_hull_array)):
        # print(in_hull_array[i])
        if not in_hull_array[i]:
            # print("Ding!")
            outside_residue = residue_points[1][i]
            #print(outside_residue)
            outside_dict[outside_residue] += 1
    return outside_dict
