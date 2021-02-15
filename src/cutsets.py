#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
===============================================================================
    File name: cutsets.py
    Author: Umair Siddique
    Description: Accepts a fault tree and generates the minmal cutsets
    Licence: MIT
===============================================================================
'''
import os
import itertools
import csv


class ErrorMsg(Exception):
    pass

class ErrorMsg(Exception):
    """
    Taken from https://community.esri.com/thread/140022
    """
    pass

def get_ft(name):
    ft = []
    with open(name, newline='') as file:
        reader = csv.reader(file)
        ftt = list(map(tuple, reader))
    for i in ftt:
        if (i[1] == 'And' or i[1] == 'Or'):
            ft.append((i[0], i[1], i[2].split()))
        else:
            raise ErrorMsg(
                "Exceptiopn: Only And/OR gates are accepted in the Fault Tree")
    return(ft)


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