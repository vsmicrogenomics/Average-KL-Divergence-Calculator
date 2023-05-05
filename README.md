Average KL Divergence Calculator

This script calculates the average Kullback-Leibler (KL) divergence for each FASTA file in a given directory and produces a separate output file for each file with the calculated KL divergence. Additionally, it produces a combined output file with the average KL divergence for all input files.

Dependencies

This script requires the following dependencies:

Python 3.x
Biopython
You can install Biopython using pip:

Copy code

pip install biopython

Usage

Clone the repository to your local machine.

Navigate to the directory containing the script.

Place your input FASTA files in the "input" directory.

Run the script using the following command:

Copy code

python average_kl_divergence.py
The script will generate an "output" directory containing the separate output files for each input file, as well as a combined output file containing the average KL divergence for all input files.

Input

The input directory should contain one or more FASTA files. The script will process all files with a ".fasta" file extension.

Output

The script will generate an "output" directory containing the separate output files for each input file, as well as a combined output file named "combined_kl_divergence.txt". Each output file will have a ".txt" file extension and will be named based on the input file name. For example, if the input file is named "example.fasta", the output file will be named "example_kl_divergence.txt".

The output files will have two columns: "Filename" and "Average KL Divergence". The "Filename" column will contain the name of the input file, and the "Average KL Divergence" column will contain the calculated KL divergence for that file.

The combined output file will have the same format, with the addition of a row for the overall average KL divergence across all input files.

To cite this code in Github, you can use the following citation statement:

Vikas Sharma. 2023. Average KL Divergence Calculator [Software]. Github. Available from: https://github.com/vsmicrogenomics/Average-KL-Divergence-Calculator
