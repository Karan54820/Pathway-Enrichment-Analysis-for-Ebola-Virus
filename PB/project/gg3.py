import pandas as pd

df3 = pd.read_csv('ebola_pIC50.csv')

# df3


selection = ['canonical_smiles','molecule_chembl_id']
df3_selection = df3[selection]
df3_selection.to_csv('molecule.smi', sep='\t', index=False, header=False)

# print(molecule.smi | wc -l)
# ! cat molecule.smi | wc -l
# ! cat padel.sh
# ! bash padel.sh
# ! ls -l


df3_X = pd.read_csv('descriptors_output.csv')

# df3_X


df3_X = df3_X.drop(columns=['Name'])
# df3_X


df3_Y = df3['pIC50']
# df3_Y

dataset3 = pd.concat([df3_X,df3_Y], axis=1)
# dataset3

dataset3.to_csv('ebola_pIC50.csv', index=False)