import subprocess
import pandas as pd
from io import BytesIO

cols = ['locus','feature','class','assembly','genome','seq_type','chromosome','genomic_accession','start','end','strand','protein','non-redundant_refseq','related_accession','name','symbol','GeneID','tag','feature_interval_length','product_length','attributes']

with open('./RmlA.txt') as my_file:
    protein_listA = my_file.read().splitlines()
with open('./RmlB-ugd.txt') as my_file:
    protein_listB = my_file.read().splitlines()
with open('./RmlC.txt') as my_file:
    protein_listM = my_file.read().splitlines()
with open('./RmlD.txt') as my_file:
    protein_listD = my_file.read().splitlines()

# protein_list = protein_listA + protein_listB + protein_listM + protein_listD

found = subprocess.check_output("grep -E \"" + '|'.join(protein_listA) + "\" /home/toshi/Databases/Genomes_June22/Feature_table/modified/merged.txt", shell=True)
dfA = pd.read_csv(BytesIO(found), sep='\t', names=cols)
dfA = dfA.assign(protein_class= 'RmlA')
print(dfA.shape)

found = subprocess.check_output("grep -E \"" + '|'.join(protein_listB) + "\" /home/toshi/Databases/Genomes_June22/Feature_table/modified/merged.txt", shell=True)
dfB = pd.read_csv(BytesIO(found), sep='\t', names=cols)
dfB = dfB.assign(protein_class= 'RmlB-ugd')
print(dfB.shape)

# df = dfA.append(dfB)
found = subprocess.check_output("grep -E \"" + '|'.join(protein_listM) + "\" /home/toshi/Databases/Genomes_June22/Feature_table/modified/merged.txt", shell=True)
dfM = pd.read_csv(BytesIO(found), sep='\t', names=cols)
dfM = dfM.assign(protein_class= 'RmlC')
print(dfM.shape)

# df = df.append(dfM)
found = subprocess.check_output("grep -E \"" + '|'.join(protein_listD) + "\" /home/toshi/Databases/Genomes_June22/Feature_table/modified/merged.txt", shell=True)
dfD = pd.read_csv(BytesIO(found), sep='\t', names=cols)
dfD = dfD.assign(protein_class= 'RmlD')
print(dfD.shape)

#df = df.append(dfD)
import itertools
import re

genomes = list(dfA['assembly'].unique()) + list(dfB['assembly'].unique()) + list(dfM['assembly'].unique()) + list(dfD['assembly'].unique())
genomes[:5]
outs = []
for genome in genomes:
    gen_record = {}
    recordsA = dfA[dfA['assembly'] == genome]
    recordsB = dfB[dfB['assembly'] == genome]
    recordsM = dfM[dfM['assembly'] == genome]
    recordsD = dfD[dfD['assembly'] == genome]
    state = None
    locussesA = recordsA['locus'].tolist()
    locussesB = recordsB['locus'].tolist()
    locussesM = recordsM['locus'].tolist()
    locussesD = recordsD['locus'].tolist()
    gen_record['proteinA'] = recordsA['protein'].tolist()
    gen_record['proteinB'] = recordsB['protein'].tolist()
    gen_record['proteinM'] = recordsM['protein'].tolist()
    gen_record['proteinD'] = recordsD['protein'].tolist()
    for combination in itertools.product(locussesA, locussesB, locussesM, locussesD):
        # locusses = combination['locus'].tolist()
        locusses = [int(re.sub("[^\d]", "", locus)) for locus in combination]
        if state is None and sorted(locusses) == list(range(min(locusses), max(locusses)+1)):
            state = 'C'
        elif state is None and max(locusses) - min(locusses) <= 10:
            state = 'N'
    gen_record['genome'] = genome
    locusses = locussesA + locussesB + locussesM + locussesD
    if len(locusses) < 2:
        state = 'Null'
    if state is None:
        state = 'D'
    gen_record['locusRmlA'] = locussesA
    gen_record['locusRmlB-ugd'] = locussesB
    gen_record['locusRmlC'] = locussesM
    gen_record['locusRmlD'] = locussesD
    gen_record['state'] = state
    print(gen_record)
    outs.append(gen_record)

output = pd.DataFrame(outs)
output.to_csv('./out_RmlABCD.csv')
