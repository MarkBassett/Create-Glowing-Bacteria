complimentary = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
def complenentary(strand):
    return ''.join([complimentary[letter] for letter in strand])

file_name = input()
with open(file_name, 'r') as data:
    raw_data = data.read()
dna_info = raw_data.split()
strand = dna_info[0]
strand_comp = complenentary(strand)
restricted_site = dna_info[1]
restricted_site_comp = complenentary(restricted_site)
gfp_strand = dna_info[2]
gfp_strand_comp = complenentary(gfp_strand)
gfp1_res_site = dna_info[3]
gfp1_res_site_comp = complenentary(gfp1_res_site)
gfp2_res_site = dna_info[4]
gfp2_res_site_comp = complenentary(gfp2_res_site)

strand_split = strand[:strand.index(restricted_site) + 1] + ' ' + strand[strand.index(restricted_site) + 1:]
strand_comp_split = strand_comp[:strand_comp.index(restricted_site_comp) + 5] +\
                    ' ' + strand_comp[strand_comp.index(restricted_site_comp) + 5:]

gfp_strand_split = gfp_strand[gfp_strand.index(gfp1_res_site) + 1: gfp_strand.rindex(gfp2_res_site) + 1]
gfp_strand_comp_split = gfp_strand_comp[gfp_strand_comp.index(gfp1_res_site_comp)
                                    + 5: gfp_strand_comp.rindex(gfp2_res_site_comp) + 5]
ligation = strand_split.replace(' ', gfp_strand_split)
ligation_comp = strand_comp_split.replace(' ', gfp_strand_comp_split)
print(ligation)
print(ligation_comp)
