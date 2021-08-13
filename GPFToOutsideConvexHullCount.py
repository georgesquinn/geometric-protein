import GPFToBackbonePoints
import GPFToResidueCenters
from scipy.spatial import ConvexHull


def make_convex_hull(protein_name):
    backbone_points = GPFToBackbonePoints.main(protein_name)
    return ConvexHull(backbone_points)


def main(protein_name):
    convex_hull = make_convex_hull(protein_name)
    residue_points = GPFToResidueCenters.main(protein_name)
    
    print(format(convex_hull))
