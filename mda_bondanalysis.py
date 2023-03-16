# import importlib

# # check whether `MDAnalysis` package is installed or not
# package_name = 'MDAnalysis'
# OA
# spec = importlib.util.find_spec(package_name)
# if spec is None:
#     print(package_name +" is not installed")



import MDAnalysis as mda

u = mda.Universe("dump_10frames.xyz")
graphene = u.select_atoms("name C")
for ts in u.trajectory:
    #https://docs.mdanalysis.org/dev/documentation_pages/topology/guessers.html
    bonds=mda.topology.guessers.guess_bonds(atoms=graphene,coords=graphene.positions,box=u.dimensions)
    u.add_TopologyAttr('bonds', bonds)
	
from MDAnalysis.analysis.bat import BAT
#https://docs.mdanalysis.org/dev/documentation_pages/analysis/bat.html
r = BAT(graphene)
r.run()


#trajectory - https://www.mdanalysis.org/MDAnalysisTutorial/trajectories.html
#adding attributes - https://userguide.mdanalysis.org/stable/examples/constructing_universe.html


'''
grap1 = u.select_atoms("name C")
with mda.Writer("dump_modified.xyz", grap1.n_atoms) as W:
    for ts in u.trajectory:
        W.write(grap1)
'''
