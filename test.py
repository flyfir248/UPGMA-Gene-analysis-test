import requests

# Define global constants
ENSEMBL_SERVER = "http://rest.ensembl.org/"
CONTENT_TYPE = "application/json"

def fetch_data(server, ext, content_type):
    try:
        # Send GET request to the Ensembl server
        r = requests.get(server + ext, headers={"Content-Type": content_type})
        # Raise an error if the request is not successful
        r.raise_for_status()
        # Return the response in JSON format
        return r.json()
    except requests.exceptions.HTTPError as err:
        print(f"An HTTP error occurred: {err}")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")

def get_gene_sequence(gene_name):
    try:
        # Look up the gene's ID using the symbol lookup endpoint
        ext = f"lookup/symbol/homo_sapiens/{gene_name}?"
        gene_data = fetch_data(ENSEMBL_SERVER, ext, CONTENT_TYPE)

        # Check if the gene name is not found in the database
        if "error" in gene_data:
            raise ValueError(gene_data["error"])

        # Retrieve the gene's sequence using the ID
        ext = f"sequence/id/{gene_data['id']}?"
        gene_sequence = fetch_data(ENSEMBL_SERVER, ext, "text/x-fasta")

        # Print the gene name, ID and sequence
        print(f"> {gene_name}\n{gene_sequence}")
    except ValueError as err:
        print(f"An error occurred: {err}")

gene_name = "CYP2D6"
get_gene_sequence(gene_name)
#gene_sequence(gene_name)