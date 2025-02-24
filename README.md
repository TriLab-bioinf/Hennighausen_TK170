# Hennighausen_TK170
## convert go-basic.obo to 3 columns format
```
python convert_obo_to_columns.py
```

## retrieve GO terms for each gene
```
## retrieve GO information from gff file
cat Wikim_166_afdsc_consensus.pgap.gff |awk 'BEGIN{FS="\t"}{if($3=="CDS")print $9}'|sed 's/^.*locus_tag=//g'|sed 's/;product=.*$//g'|sed 's/;note=.*\./\t/g'|sed 's/GO_[a-z]*: //g'|sed 's/  /\t/g'|sed 's/\t /\t/g' >Wikim_166_afdsc.GO.txt
## extract the necessary information
python Wikim_166_afdsc.py
## reformat
awk '{n=split($2,a,","); for (i=1; i<=n; i++) print $1"\t"a[i]}' Wikim_166_afdsc.GO.formatted.txt|sort -k2,2|join -t$'\t' -1 2 - -2 1 <(sort -k1,1 database/go_basic_3_columns.txt)|cut -f1,2,4 >Wikim_166_afdsc.GO.formatted2.txt
```

## for transmembrane related genes in DE level1 lists
```
## retrieve all transmembrane related genes in DE_level1 lists and get the related GO terms for these genes
grep "transmembrane" go_basic_3_columns.txt|sort -k1,1|join -t$'\t' -1 1 - -2 1 <(sort -k1,1 Wikim_166.GO.formatted2.txt)|sort -t$'\t' -k4,4 |join -t$'\t' -1 4 - -2 1 <(sort -k1,1 DE_level1.id)|cut -f1|sort -u|join -t$'\t' -1 1 - -2 2 <(sort -k2,2 Wikim_166.GO.formatted2.txt) |sed '1i gene\tGO\tOntology' >DE_level1.transmembrane.network.txt

## annotate GO terms and genes for cytoscape input
sort -k2,2 DE_level1.transmembrane.network.txt|join -t$'\t' -1 2 - -2 1 <(sort -k1,1 go_basic_3_columns.txt) |cut -f1,4,5 >DE_level1.transmembrane.network.anno1
awk '{print $1"\t"$1"\t""gene"}' DE_level1.transmembrane.network.txt |sed 1d> DE_level1.transmembrane.network.anno2
cat DE_level1.transmembrane.network.anno1 DE_level1.transmembrane.network.anno2 |sed '1i source\tanno\ttype'>DE_level1.transmembrane.network.anno.txt
```

## for all Level 1 genes
```
## retrieve all related GO terms for DE_level1 genes
sort -k1,1 DE_level1.id| join -t$'\t' -1 1 - -2 2 <(sort -k2,2 Wikim_166.GO.formatted2.txt) |sed '1i gene\tGO\tOntology' >DE_level1.network.txt

## annotate GO terms and genes for cytoscape input
sort -k2,2 DE_level1.network.txt|join -t$'\t' -1 2 - -2 1 <(sort -k1,1 go_basic_3_columns.txt) |cut -f1,4,5 >DE_level1.network.anno1
awk '{print $1"\t"$1"\t""gene"}' DE_level1.network.txt |sed 1d> DE_level1.network.anno2
cat DE_level1.network.anno1 DE_level1.network.anno2 |sort -u|sed '1i source\tanno\ttype'>DE_level1.network.anno.txt
```

## cytoscape
File -> Import -> Network from File (choose DE_level1.network.txt, gene as source, GO as target)

File -> Import -> Table from File (choose DE_level1.network.anno.txt)

style: 

**Fill Color**: 

![image](https://github.com/user-attachments/assets/bbd42a6b-ac44-4eba-914f-625ad3a37b34)

**Shape**:

![image](https://github.com/user-attachments/assets/fb356a1b-6b10-4b72-8910-fa60502b2cbc)

**Layout**: yFiles Organic Layout
