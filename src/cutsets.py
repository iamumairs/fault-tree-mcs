#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FT-MCS: Fault Tree Minimal Cutsets Library

This module provides an implementation of the MOCUS (Method of Obtaining Cut Sets)
algorithm for computing minimal cutsets from fault trees.

Author: Umair Siddique
License: MIT
Repository: https://github.com/iamumairs/fault-tree-mcs
"""
import os
import itertools
import csv


class ErrorMsg(Exception):
    """Custom exception for FT-MCS errors."""
    pass

def get_ft(name):
    """
    Load a fault tree from a CSV file.
    
    CSV Format:
        GateName,GateType,ChildrenSpace-Separated
        Example:
            TOP,Or,E1 E2
            E1,And,A B
    
    Args:
        name (str): Path to the CSV file
        
    Returns:
        list: List of tuples (gate_name, gate_type, children_list)
        
    Raises:
        ErrorMsg: If gate types other than 'And' or 'Or' are used
    """
    ft = []
    with open(name, newline='') as file:
        reader = csv.reader(file)
        ftt = list(map(tuple, reader))
    for i in ftt:
        if (i[1] == 'And' or i[1] == 'Or'):
            ft.append((i[0], i[1], i[2].split()))
        else:
            raise ErrorMsg(
                "Exception: Only And/Or gates are accepted in the Fault Tree")
    return(ft)


And = "And"
Or = "Or"


def rewrite_and(e, r, l):
    r.remove(e)
    for i in l:
        r.append(i)
    r.reverse()


def rewrite_or(e, r, l):
    new_rows = []
    x = r
    x.remove(e)
    for i in l:
        new_rows = new_rows + [([i] + x)]
    return (new_rows)

def top_to_init_path(te):
    path = []
    if te[0] == And:
        path = path + [te[1]]
    else:
        for x in te[1]:
            path = path + [[x]]
    return(path)


def cs_helper(i, j, p, dic_ft):
    updated_paths = p
    e = p[i][j]
    row = p[i]
    gate, inputs = dic_ft[e]
    if gate == And:
        rewrite_and(e, row, inputs)

    else:
        updated_paths.remove(p[i])
        new_rows = rewrite_or(e, row, inputs)
        updated_paths = updated_paths + new_rows
    return(updated_paths)


def find_element_to_expand(paths, d):
    for row in paths:
        for e in row:
            try:
                x = d[e]  # Optional -- we can return x as well
                return (paths.index(row), row.index(e))
            except KeyError:
                continue


def mocus_init(ft):
    dic_ft = dict([(k, [v, w]) for k, v, w in ft])
    tope = dic_ft['TOP']
    ps = top_to_init_path(tope)

    while True:
        try:
            i, j = find_element_to_expand(ps, dic_ft)
            ps = cs_helper(i, j, ps, dic_ft)
        except BaseException:
            break
    return(ps)

def mocus(fault_tree):
    """
    Compute minimal cutsets from a fault tree using the MOCUS algorithm.
    
    The MOCUS algorithm recursively expands gates according to Boolean logic
    and identifies minimal combinations of events that cause system failure.
    
    Args:
        fault_tree (list): Fault tree as list of tuples (gate_name, gate_type, children)
                          Gate types must be 'And' or 'Or'
                          
    Returns:
        list: List of minimal cutsets, each cutset is a list of basic events
        
    Example:
        >>> ft = [("TOP", "Or", ["E1", "E2"]),
        ...       ("E1", "And", ["A", "B"])]
        >>> mocus(ft)
        [['A', 'B'], ['E2']]
    
    References:
        - Fussell & Vesely (1972): "A New Methodology for Obtaining Cut Sets for Fault Trees"
        - Limnios & Ziani (1986): "An Algorithm for Reducing Cut Sets in Fault-Tree Analysis"
    """
    cs = []
    cs = mocus_init(fault_tree)
    css = list(map(lambda x: list(set(x)), cs))
    css.sort(key=len)
    for a, b in itertools.combinations(css, 2):
        if set(a) <= set(b):
            try:
                css.remove(b)
            except BaseException:
                continue
    return(css)