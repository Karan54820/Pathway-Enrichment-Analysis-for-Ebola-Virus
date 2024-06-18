import pandas as pd
from chembl_webresource_client.new_client import new_client

target = new_client.target
target_query = target.search('ebolavirus')
targets = pd.DataFrame.from_dict(target_query)
print(targets)

chembl_id = []
canonical_smiles = []
standard_value = []
bioactivity_class = []
for i in range(0,len(targets)):
    selected_target = targets.target_chembl_id[i]
    print(selected_target)

    activity = new_client.activity
    res = activity.filter(target_chembl_id=selected_target).filter(standard_type="IC50")

    df = pd.DataFrame.from_dict(res)
    if df.empty:
        continue
    else:
    # print(df.head(3))
        df1 = df[df.standard_value.notna()]

        for j in df1.molecule_chembl_id:
            chembl_id.append(j)

        for j in df1.canonical_smiles:
            canonical_smiles.append(j)

        for j in df1.standard_value:
            standard_value.append(j)

        
        for j in df1.standard_value:
            if float(j) >= 10000:
                bioactivity_class.append("inactive")
            elif float(j) <= 1000:
                bioactivity_class.append("active")
            else:
                bioactivity_class.append("intermediate")
        
        df1.to_csv('bioactivity_data'+str(i)+'.csv', index=False)

data_tuples = list(zip(chembl_id, canonical_smiles, bioactivity_class, standard_value))
df3 = pd.DataFrame( data_tuples,  columns=['molecule_chembl_id', 'canonical_smiles', 'bioactivity_class', 'standard_value'])
print(df3)
df3.to_csv('bioactivity_preprocessed_data.csv', index=False)