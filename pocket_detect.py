#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Protein-ligand Docking Pipeline.

Author: Zheng Liangzhen
Contact: astrozheng@gmail.com
Date: Aug. 2021.

"""

import numpy as np
import mdtraj as mt
import os, sys


def read_pdb(filename):
    traj = mt.load_pdb(filename)

    table, bonds = traj.topology.to_dataframe()

    with open(filename) as lines:
        lines = [x for x in lines]
        try:
            bfactors = np.array([float(x.split()[-2]) for x in lines if "ATOM" in x])
        except:
            #print("Bfactors as zero")
            bfactors = np.zeros(table.shape[0]) 
            for i, l in enumerate(lines):
                try:
                    #print(l)
                    bfactors[i] = float(l.split()[-3])
                except:
                    bfactors[i] = 0.0
            

    assert table.shape[0] == bfactors.shape[0]

    table['bfactors'] = bfactors

    return table, traj


def mean_bfactors(bfactors):
    # in pointsite, some atoms have very large predicted scores, such as 9.9,
    # these predictions are not valid, should be aviod
    return np.mean([x for x in bfactors if (x < 1.0 and x >= 0.0)])


def close_to_res(resid, resid_list, nres_cutoff=5):
    
    n = [x for x in resid_list if abs(resid - x) < nres_cutoff]
    if len(n) > 0:
        return False
    else:
        return True


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("usage: pocket_detect.py input.pdb")
        sys.exit(0)

    inp = sys.argv[1]
    df, traj = read_pdb(inp)
    res = df['resSeq'].unique()

    bf_cutoff = 0.5
    nres_cutoff = 5

    mean_bf = []
    for rid in res:
        _bf = df[df['resSeq'] == rid]['bfactors']
        mean_bf.append([rid, mean_bfactors(_bf)])

    sorted_mean_bf = sorted(mean_bf, key=lambda x: x[1], reverse=True)

    res_ids = [x for x in sorted_mean_bf if x[1] >= bf_cutoff]

    keep_res = []
    
    if len(res_ids) > 0:
        for rid, mbf in res_ids:
            if close_to_res(rid, keep_res, nres_cutoff): 
                atm_ndx = df[df['resSeq'] == rid].index
                #xyz     = traj.xyz[0][atm_ndx].mean(axis=1) * 10.0
                # bug fix here 08.21.2021
                xyz     = traj.xyz[0][atm_ndx].mean(axis=0) * 10.0
                print("HIT {} {:.3f} {:.3f} {:.3f} {:.3f}".format(rid, mbf, xyz[0], xyz[1], xyz[2]))
                keep_res.append(rid)
            else:
                pass
    else:
        print("NOT-FOUND")


