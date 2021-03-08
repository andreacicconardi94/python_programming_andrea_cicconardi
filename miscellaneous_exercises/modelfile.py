#this script allows you to see what modeller reads from the pdb file before
#you launch the program.
from modeller import *
env = environ()
# If you also want to see HETATM residues, uncomment this line:
#env.io.hetatm = True
code = '1BY8'
mdl = model(env, file=code)
aln = alignment(env)
aln.append_model(mdl, align_codes=code)
aln.write(file=code+'.seq')
