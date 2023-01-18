import requests

# URL to download the gene family data
url = "https://www.genenames.org/cgi-bin/download/custom?col=gd_hgnc_id&col=gd_app_sym&col=gd_app_name&col=gd_status&col=gd_locus_type&col=md_eg_id&col=md_mim_id&status=Approved&hgnc_dbtag=on&order_by=gd_app_sym_sort&format=text&submit=submit"

# search for the gene family
params = {"search": "HOX"}

# send GET request and save the response
response = requests.get(url, params=params)

# write the response content to a file
with open("HOX_gene_families.csv", "w") as file:
    file.write(response.text)

print("Data downloaded successfully!")