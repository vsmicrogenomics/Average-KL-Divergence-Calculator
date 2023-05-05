Average KL Divergence Calculator

average-KL-divergence-calculator.py script calculates the average Kullback-Leibler (KL) divergence for each FASTA file in a given directory and produces a separate output file for each file with the calculated KL divergence. Additionally, it produces a combined output file with the average KL divergence for all input files.

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

Test Samples

Test samples and outputs are provided in the "test" directory of this repository. These can be used to test the script and verify that it is working correctly. The input files are located in the "test/input" directory, and the expected output files are located in the "test/output" directory. The test files have been named using the same format as the regular input and output files, and should produce the expected results when run through the script.

To cite this code in Github, you can use the following citation statement:

Vikas Sharma. 2023. Average KL Divergence Calculator [Software]. Github. Available from: https://github.com/vsmicrogenomics/Average-KL-Divergence-Calculator

Acknowledgement

This script uses the concept of Kullback-Leibler (KL) divergence, which is a measure of the relative entropy between two probability distributions. The KL divergence was first introduced by Kullback and Leibler in 1951, and has since been applied in various fields, including genomics. The method used to calculate the KL divergence in this script is based on the work by Bohlin et al. (2012), who applied the method to study the differences in genomic features between different bacterial elements. Their paper can be found here:

Bohlin J., van Passel M.W., Snipen L., Kristoffersen A.B., Ussery D., Hardy S.P. Relative entropy differences in bacterial chromosomes, plasmids, phages and genomic islands. BMC Genom. 2012;13:66. doi: 10.1186/1471-2164-13-66.
