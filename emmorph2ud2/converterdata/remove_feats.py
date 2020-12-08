#!/usr/bin/env python3
# -*- coding: utf-8, vim: expandtab:ts=4 -*-


def del_feat(featname, feats):
    """
    kitölri az adott jegyet a jegy-érték párok dictionary-jéből
    :param featname: a törlendő jegy
    :param feats: a jegy-érték párok dictionary-je
    """

    try:
        del feats[featname]
    except KeyError:
        pass


def remove_feats(pos, feats):
    """
    kitölri a fölösleges jegyeket a szófaj alapján
    :param pos: a törlendő jegy
    :param feats: a jegy-érték párok dictionary-je
    """

    if pos == 'NOUN':
        del_feat('Definite', feats)
        del_feat('NumType', feats)
        del_feat('PronType', feats)
        del_feat('Person', feats)

    elif pos == 'NUM':
        del_feat('Definite', feats)
        del_feat('PronType', feats)
        del_feat('Degree', feats)

    elif pos == 'ADJ':
        del_feat('Definite', feats)

    elif pos == 'ADV':
        del_feat('Case', feats)
        del_feat('Number', feats)
        del_feat('NumType', feats)
        del_feat('Definite', feats)
        del_feat('Number[psor]', feats)
        del_feat('Person[psor]', feats)

    elif pos == 'DET':
        del_feat('Case', feats)
        del_feat('Number', feats)

    elif pos == 'PRON':
        del_feat('Definite', feats)
