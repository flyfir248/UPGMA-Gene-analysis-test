# Importing necessary libraries

from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
from Bio import AlignIO
from flask import Flask
from flask import render_template
import matplotlib.pyplot as plt

app = Flask(__name__)


@app.route("/")
def generate_tree():

    # Read the sequences and align
    align = AlignIO.read('msa.phy', 'phylip')

    # Calculate the distance matrix
    calculator = DistanceCalculator('identity')
    distMatrix = calculator.get_distance(align)

    # Creating a DistanceTreeConstructor object
    constructor = DistanceTreeConstructor()

    ####################################################
    #  UPGMA
    ####################################################

    # Construct the phlyogenetic tree using UPGMA algorithm
    UPGMATree = constructor.upgma(distMatrix)

    # Draw the phlyogenetic tree
    Phylo.draw(UPGMATree)

    # Printing the phlyogenetic tree using terminal
    Phylo.draw_ascii(UPGMATree)

    ####################################################
    #  NJ
    ####################################################

    # Construct the phlyogenetic tree using NJ algorithm
    NJTree = constructor.nj(distMatrix)

    # Draw the phlyogenetic tree
    Phylo.draw(NJTree)

    # Printing the phlyogenetic tree using terminal
    Phylo.draw_ascii(NJTree)
    #return Phylo.draw_ascii(UPGMATree)

    return render_template('result.html', tree=UPGMATree)

if __name__ == "__main__":
    app.run(debug=True)