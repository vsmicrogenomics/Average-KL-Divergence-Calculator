import os
import math
from collections import Counter
from Bio import SeqIO

# Define input and output file paths
input_dir = "input"
output_dir = "output"

def kl_divergence(sequence):
    # Get tetramers and observed frequencies
    tetramers = [sequence[i:i+4] for i in range(len(sequence)-3)]
    obs_freqs = Counter(tetramers)

    # Calculate total tetramers and observed probabilities
    total_tetramers = sum(obs_freqs.values())
    obs_probs = {k: v/total_tetramers for k, v in obs_freqs.items()}

    # Calculate expected probabilities under a zero-order Markov model
    exp_probs = {k: 0.25**4 for k in obs_freqs.keys()}

    # Calculate the KL divergence
    kl_div = sum(obs_probs[k] * (math.log(obs_probs[k]/exp_probs[k]) if exp_probs[k] != 0 else 0)
                 for k in obs_probs.keys())

    return kl_div

# Get the list of filenames from the input directory
filename_list = [os.path.join(input_dir, f) for f in os.listdir(input_dir) if f.endswith(".fasta")]

# Create an empty list to store the average KL divergences for each input file
kl_div_list = []

# Calculate the average KL divergence for each file and write it to a separate output file
for filename in filename_list:
    kl_divs = []
    for record in SeqIO.parse(filename, "fasta"):
        kl = kl_divergence(str(record.seq))
        kl_divs.append(kl)
    avg_kl_div = sum(kl_divs) / len(kl_divs)
    # Create the output file path using the input filename
    output_file = os.path.join(output_dir, os.path.basename(filename).replace('.fasta','_kl_divergence.txt'))
    # Write the KL divergence result to the output file
    with open(output_file, "w") as outfile:
        # Write the header of the table to the output file
        outfile.write("Filename\tAverage KL Divergence\n")
        # Write the average KL divergence to the output file
        outfile.write(f"{os.path.basename(filename).replace('.fasta','')}\t{avg_kl_div}\n")
    # Append the average KL divergence to the kl_div_list
    kl_div_list.append(avg_kl_div)

# Calculate the overall average KL divergence
overall_avg_kl_div = sum(kl_div_list) / len(kl_div_list)

# Create the output file path for the combined results
combined_output_file = os.path.join(output_dir, "combined_kl_divergence.txt")

# Write the headers and the results to the combined output file
with open(combined_output_file, "w") as outfile:
    # Write the header of the table to the output file
    outfile.write("Filename\tAverage KL Divergence\n")
    # Write the average KL divergences for each input file to the output file
    for filename, avg_kl_div in zip(filename_list, kl_div_list):
        outfile.write(f"{os.path.basename(filename).replace('.fasta','')}\t{avg_kl_div}\n")
    # Write the overall average KL divergence to the output file
    outfile.write(f"Overall\t{overall_avg_kl_div}\n")
