# Hennighausen_TK170
## for transmembrane
### retrieve all transmembrane related genes in DE_level1 lists and get the related GO terms for these genes
```
grep "transmembrane" go_basic_3_columns.txt|sort -k1,1|join -t$'\t' -1 1 - -2 1 <(sort -k1,1 Wikim_166.GO.formatted2.txt)|sort -t$'\t' -k4,4 |join -t$'\t' -1 4 - -2 1 <(sort -k1,1 DE_level1.id)|cut -f1|sort -u|join -t$'\t' -1 1 - -2 2 <(sort -k2,2 Wikim_166.GO.formatted2.txt) |sed '1i gene\tGO\tOntology' >DE_level1.transmembrane.network.txt
```

### annotate GO terms and genes for cytoscape input
```
sort -k2,2 DE_level1.transmembrane.network.txt|join -t$'\t' -1 2 - -2 1 <(sort -k1,1 go_basic_3_columns.txt) |cut -f1,4,5 >DE_level1.transmembrane.network.anno1
awk '{print $1"\t"$1"\t""gene"}' DE_level1.transmembrane.network.txt |sed 1d> DE_level1.transmembrane.network.anno2
cat DE_level1.transmembrane.network.anno1 DE_level1.transmembrane.network.anno2 |sed '1i source\tanno\ttype'>DE_level1.transmembrane.network.anno.txt
```

## for all Level 1 id
### retrieve all related GO terms for DE_level1 genes
```
sort -k1,1 DE_level1.id| join -t$'\t' -1 1 - -2 2 <(sort -k2,2 Wikim_166.GO.formatted2.txt) |sed '1i gene\tGO\tOntology' >DE_level1.network.txt
```

### annotate GO terms and genes for cytoscape input
```
sort -k2,2 DE_level1.network.txt|join -t$'\t' -1 2 - -2 1 <(sort -k1,1 go_basic_3_columns.txt) |cut -f1,4,5 >DE_level1.network.anno1
awk '{print $1"\t"$1"\t""gene"}' DE_level1.network.txt |sed 1d> DE_level1.network.anno2
cat DE_level1.network.anno1 DE_level1.network.anno2 |sort -u|sed '1i source\tanno\ttype'>DE_level1.network.anno.txt
```
