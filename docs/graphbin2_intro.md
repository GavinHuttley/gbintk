# GraphBin2: Refined and Overlapped Binning of Metagenomic Contigs Using Assembly Graphs

**GraphBin2** is an extension of [GraphBin](https://github.com/Vini2/GraphBin) which refines the binning results obtained from existing tools and, more importantly, is able to assign contigs to multiple bins. GraphBin2 uses the connectivity and coverage information from assembly graphs to adjust existing binning results on contigs and to infer contigs shared by multiple 
species.

You can find more details about GraphBin2 at [https://github.com/metagentools/GraphBin2](https://github.com/metagentools/GraphBin2).

If you use GraphBin2 in your work, please cite the two publications as follows.

```bibtex
@InProceedings{mallawaarachchi_et_al:LIPIcs:2020:12797,
  author =	{Vijini G. Mallawaarachchi and Anuradha S. Wickramarachchi and Yu Lin},
  title =	{{GraphBin2: Refined and Overlapped Binning of Metagenomic Contigs Using Assembly Graphs}},
  booktitle =	{20th International Workshop on Algorithms in Bioinformatics (WABI 2020)},
  pages =	{8:1--8:21},
  series =	{Leibniz International Proceedings in Informatics (LIPIcs)},
  ISBN =	{978-3-95977-161-0},
  ISSN =	{1868-8969},
  year =	{2020},
  volume =	{172},
  editor =	{Carl Kingsford and Nadia Pisanti},
  publisher =	{Schloss Dagstuhl--Leibniz-Zentrum f{\"u}r Informatik},
  address =	{Dagstuhl, Germany},
  URL =		{https://drops.dagstuhl.de/opus/volltexte/2020/12797},
  URN =		{urn:nbn:de:0030-drops-127974},
  doi =		{10.4230/LIPIcs.WABI.2020.8},
  annote =	{Keywords: Metagenomics binning, contigs, assembly graphs, overlapped binning}
}

@Article{Mallawaarachchi2021,
  author={Mallawaarachchi, Vijini G. and Wickramarachchi, Anuradha S. and Lin, Yu},
  title={Improving metagenomic binning results with overlapped bins using assembly graphs},
  journal={Algorithms for Molecular Biology},
  year={2021},
  month={May},
  day={04},
  volume={16},
  number={1},
  pages={3},
  abstract={Metagenomic sequencing allows us to study the structure, diversity and ecology in microbial communities without the necessity of obtaining pure cultures. In many metagenomics studies, the reads obtained from metagenomics sequencing are first assembled into longer contigs and these contigs are then binned into clusters of contigs where contigs in a cluster are expected to come from the same species. As different species may share common sequences in their genomes, one assembled contig may belong to multiple species. However, existing tools for binning contigs only support non-overlapped binning, i.e., each contig is assigned to at most one bin (species).},
  issn={1748-7188},
  doi={10.1186/s13015-021-00185-6},
  url={https://doi.org/10.1186/s13015-021-00185-6}
}
```