#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 11:03:09 2025

@author: rene
"""

import numpy as np



def paths_to_LaTeX_table(paths, fheader):

    outfile_name = f"{fheader}path_table.txt"

    with open(outfile_name, "w") as f:

        print('\\begin{table} [ht!] ', file=f)
        print('\\renewcommand{\\arraystretch}{1.3}', file=f)
        print('\\caption{Set of simple paths for graph in fig. \\ref{fig:ExampleGraph}} ', file=f)
        print('\\label{tab:SimplePathsExample}', file=f)
        print('\t\\centering', file=f)
        print('\t\\begin{tabular} {c  c  c} \\toprule', file=f)
        print('\t\t\\textbf{Path ID} & \\textbf{Route} & \\textbf{Length} \\\ \\midrule', file=f)

        index=1
        for path in paths:
            pathstr = "-".join(str(node) for node in path)
            if (index % 4) == 0:
                print(f'\t\t\t{index} & {pathstr} & {len(path)-1} \\\ \\midrule', file=f)
            else:
                print(f'\t\t\t{index} & {pathstr} & {len(path)-1} \\\ ', file=f)
            index += 1
        print('\\bottomrule', file=f)

        print('\t\end{tabular}', file=f)
        print('\end{table}', file=f)

        print(f"File {outfile_name} completed")
