

# Troubleshooting

### Docker only has the dependencies it is born with
When your tools require old versions of software,
```
conda install pandas
```
Will grab the newest version of pandas and possibly cause problems

### Methylation data has different formats
[BED](https://genome.ucsc.edu/FAQ/FAQformat.html#format1) is not the same as [BEDRBS](https://github.com/ENCODE-DCC/encValData/blob/master/as/bedRrbs.as)


### [Nvidia-Docker](https://github.com/NVIDIA/nvidia-docker) and [JHiccup](https://github.com/giltene/jHiccup)
May demand different versions of CUDA






Good luck.
