from Bio import GenBank

gbk = "insulin.gbk"
fasta = "insulin_converted.fasta"

input_handle = open(gbk, "r")
output_handle = open(fasta, "w")

for seq_record in SeqIO.parse(input_handle, "genbank"):
	print ("dealing with GenBank record %s" % seq_record.id)
	for seq_feature in seq_record.features :
		if seq_feature.type == "ACCESSION":
			output_handle.write(">%s form %s\n%s\n" % (seq_feature.id)
		elif seq_feature.type == "ORGANISM":
			output_handle.write(">%s form %s\n%s\n" % (seq_feature.qualifiers['organism_name'])
		elif seq_feature.type == "ORIGIN":
			assert len(seq_feature.qualifiers['ORIGIN']) ==1
			output_handle.write(">%s form %s\n%s\n" % (seq_feature.qualifiers['translation'])

output_handle.close()
input_handle.close()
print ("Done")
