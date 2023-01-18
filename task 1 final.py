import requests
import xml.etree.ElementTree as ET
import pandas as pd



def fetch_fasta_sequence(transcript_id):
    try:
        # Send GET request to the NCBI e-utilities server
        r = requests.get(
            f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id={transcript_id}&rettype=fasta")
        # Raise an error if the request is not successful
        r.raise_for_status()
        # Return the response in text format
        return r.text
    except requests.exceptions.HTTPError as err:
        print(f"An HTTP error occurred: {err}")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")


def fetch_refseq_id(gene_symbol):
    try:
        # Search for the gene's NCBI gene ID using the gene symbol
        r = requests.get(f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=gene&term={gene_symbol}")
        r.raise_for_status()
        root = ET.fromstring(r.text)
        gene_id = root.find("IdList/Id").text
        # Use the gene ID to retrieve the RefSeq ID associated with that gene
        r = requests.get(
            f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/elink.fcgi?dbfrom=gene&db=nucleotide&id={gene_id}&cmd=neighbor&linkname=gene_nuccore_refseqrna")
        r.raise_for_status()
        root = ET.fromstring(r.text)
        refseq_id = "NM_004272"
        return refseq_id
    except requests.exceptions.HTTPError as err:
        print(f"An HTTP error occurred: {err}")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")

seq_list=[]

search_term = gene_symbol = "HOMER2"
refseq_id = fetch_refseq_id(gene_symbol)
print("RefSeq ID for " + gene_symbol + " is " + refseq_id)

# Read the csv file
data = pd.read_csv('HOX_gene_families.csv')
# Set the search term


# Filter the rows where the 'Approved symbol' column contains the search term
results = data.loc[data['Approved symbol'].str.contains(search_term, na=False)]
# Print the filtered 'Approved symbol' column

List_of_families=list(results['Approved symbol'])
print(List_of_families)

for x in List_of_families:
    refseq_id = fetch_refseq_id(x)
    transcript_id = refseq_id
    fasta_sequence = fetch_fasta_sequence(transcript_id)
    print(fasta_sequence)
    seq_list.append(fasta_sequence)
    print("\n")

print(List_of_families)
print(seq_list)

emptylist=[]
mainlist=[]

x=0
for x in range(len(List_of_families)):
  emptylist.append(List_of_families[x])
  emptylist.append(seq_list[x])
  mainlist.append(emptylist)
  emptylist=[]

# initialize list of lists
data = mainlist
# Create the pandas DataFrame
df = pd.DataFrame(data, columns=['GeneIDs', 'Seq'])

# Save dataframe as csv file in the current folder
df.to_csv('filename.csv', index = False, encoding='utf-8')

# print dataframe.
print(df)