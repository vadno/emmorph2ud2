#!/usr/bin/env python3
# -*- coding: utf-8, vim: expandtab:ts=4 -*-

from .converterdata import mappings as mp
from .converterdata import lex_lists as ls
from .converterdata import remove_feats as rm


class EmMorph2UD2:
    pass_header = True

    def __init__(self, source_fields=None, target_fields=None):

        # Field names for e-magyar TSV
        if source_fields is None:
            source_fields = set()

        if target_fields is None:
            target_fields = []

        self.source_fields = source_fields
        self.target_fields = target_fields

    @staticmethod
    def _feats_to_dict(univfeature, univfeature_dict):
        """
        elrendezi a meglévő jegyeket a jegy-érték struktúrába
        :param univfeature: a jegy-érték sztringek listája
        :param univfeature_dict: dictonary-be rendezve
        """

        for inflex_feat in univfeature:
            key, attribute = inflex_feat.split('=')
            univfeature_dict[key] = attribute
        del univfeature[:]

    @staticmethod
    def _print_feats(featdict):
        """
        a megfelelő formátumba nyomtatja a jegy-érték párokat
        ábécé sorrendbe, pipe-pal elválasztva, egyenlőségjelekkel
        :param featdict: a jegy-érték párok dictionary-je
        :return: nyomtatáshoz formázott sztring
        """
        if featdict:
            return '|'.join([feat + '=' + featdict[feat] for feat in sorted(featdict, key=str.lower)])

        return '_'

    def parse(self, token, lemma, emmorph):
        """
        az emmorph címke feldolgozása
        :param token: szóalak
        :param lemma: tő
        :param emmorph: az emmorph címke
        :return: ud szófajcímke és formázott ud jegy-érték párok
        """

        # az emmorph kód szétvágása szófajra, derivációs és inflexiós jegyekre
        emmorph_features = emmorph.rstrip(']').lstrip('[').split('][')
        pos_feats = [feat for feat in emmorph_features if feat.startswith('/') or feat in ('OTHER', 'Punct')]
        deriv_feats = [feat for feat in emmorph_features if feat.startswith('_')]
        infl_feats = [feat for feat in emmorph_features if feat not in pos_feats + deriv_feats]

        # punktuáció önmagában, vagy szóra tapadó punct
        punct_feat = False
        if emmorph_features[-1] == 'Punct':
            if len(emmorph_features) > 1:
                punct_feat = True
            else:
                return 'PUNCT', '_'

        # a felsőfok jele szófaj volt, átkerül az inflexiós jegyek közé
        for feat in pos_feats:
            if feat in mp.POS_TO_INFL_FEAT:
                pos_feats.remove(feat)
                infl_feats.append(feat)

        # a középfok jele és az ige néhány jegye (műveltető, gyakoritó, ható)
        # és az igenevek jegyei átkerülnek az inflexiós jegyek közé
        # de megmaradnak a deriv jegyek között is a megfelelő szófaj miatt
        for feat in deriv_feats:
            if feat in mp.DERIV_TO_INFL_FEAT:
                infl_feats.append(feat)

        if not pos_feats:
            # ha egyáltalán nincs szófajcímke, akkor se akad el, majd a deriváció megoldja
            pos_feats.append('DERIV')

        # POS tagek feldolgozása
        pos_feat = pos_feats[0]
        univpos = ''
        if pos_feat in mp.POS_RULES:
            univpos = mp.POS_RULES[pos_feat]

        # derivációs jegyek feldolgozása
        for deriv_feat in deriv_feats:
            if deriv_feat in mp.DERIV_RULES:
                univpos = mp.DERIV_RULES[deriv_feat]

        # feature-ök feldolgozása
        univfeature = []
        univfeature_dict = {}

        if not univpos:
            univpos = 'X'

        # kötőszók a lex_listből
        if univpos == 'CCONJ':
            if lemma in ls.SCONJ:
                return 'SCONJ', '_'
            else:
                return univpos, '_'

        elif univpos in ('INTJ', 'X'):
            return univpos, '_'

        # a 'meg' igekötő kezelése
        elif univpos == 'ADV' and lemma == ls.PART:
            return 'PART', '_'

        elif univpos == 'VERB':

            # ige default jegyek
            univfeature_dict['Voice'] = 'Act'
            univfeature_dict['VerbForm'] = 'Fin'

            if not infl_feats:
                univfeature_dict['Definite'] = 'Ind'
                univfeature_dict['Mood'] = 'Cnd'
                univfeature_dict['Number'] = 'Sing'
                univfeature_dict['Person'] = '3'
                univfeature_dict['Tense'] = 'Pres'
                univfeature_dict['VerbForm'] = 'Fin'
                univfeature_dict['Voice'] = 'Act'

            else:
                # jegyek a mappingsből
                for infl_feat in infl_feats:
                    if '.' in infl_feat:
                        subfeats = infl_feat.split('.')
                        for subfeat in subfeats:
                            if subfeat in mp.VERBAL_INFL_RULES:
                                univfeature.extend(mp.VERBAL_INFL_RULES[subfeat])

                    elif infl_feat in mp.VERBAL_INFL_RULES:
                        univfeature.extend(mp.VERBAL_INFL_RULES[infl_feat])

            self._feats_to_dict(univfeature, univfeature_dict)

            # ha az infinitívusz ragozott, akkor tense jegye is van
            if 'VerbForm' in univfeature_dict:
                if univfeature_dict['VerbForm'] == 'Inf' and 'Person' in univfeature_dict and \
                        'Number' in univfeature_dict:
                    univfeature_dict['Tense'] = 'Pres'

            # Pot móddal (hatóképzővel) is kombinálódó módok kezelése
            if 'Pot' in univfeature_dict:
                # infeknél, ahol nem volt mód
                if 'Mood' not in univfeature_dict:
                    univfeature_dict['Mood'] = 'Pot'
                # kijelentő mód, jelen idő
                elif univfeature_dict['Mood'] == 'Ind':
                    univfeature_dict['Mood'] = 'Pot'
                # feltételes és felszólító mód
                else:
                    univfeature_dict['Mood'] += ',Pot'
                rm.del_feat('Pot', univfeature_dict)

        # maradékok névszók és határozószók
        else:

            # vonatkozó és kérdőnévmások
            if pos_feat in mp.REL_PRON:
                univfeature_dict['PronType'] = 'Rel'
                univpos = univpos.split('_')[0]
            elif pos_feat in mp.INT_PRON:
                univfeature_dict['PronType'] = 'Int'
                univpos = univpos.split('_')[0]

            # névmástípusok a lex_listből, az ud szófaj is ez alapján lesz Pron
            if 'PRON' in univpos:
                if lemma in ls.PRON_IND:
                    univpos = 'PRON'
                    univfeature_dict['PronType'] = 'Ind'
                elif lemma in ls.PRON_PRS:
                    univpos = 'PRON'
                    univfeature_dict['PronType'] = 'Prs'
                elif lemma == ls.PRON_RCP:
                    univpos = 'PRON'
                    univfeature_dict['PronType'] = 'Rcp'
                elif lemma in ls.PRON_DEM:
                    univpos = 'PRON'
                    univfeature_dict['PronType'] = 'Dem'
                elif lemma in ls.PRON_TOT:
                    univpos = 'PRON'
                    univfeature_dict['PronType'] = 'Tot'
                elif lemma in ls.PRON_REFL:
                    univpos = 'PRON'
                    univfeature_dict['Reflex'] = 'Yes'
                    rm.del_feat('PronType', univfeature_dict)

                elif univpos != 'PRON':
                    univpos = univpos.split('_')[0]
                    rm.del_feat('PronType', univfeature_dict)

                if univpos == 'PRON':
                    if lemma == ls.PRON_POSS:
                        univfeature_dict['Poss'] = 'Yes'
                    if 'Number[psed]' in univfeature_dict:
                        univfeature_dict['Poss'] = 'Yes'
                        rm.del_feat('Number[psed]', univfeature_dict)
                    if 'Person' not in univfeature_dict:
                        univfeature_dict['Person'] = '3'
                    if 'PronType' not in univfeature_dict and 'Reflex' not in univfeature_dict:
                        univfeature_dict['PronType'] = 'Prs'

            # determinánsok
            if univpos == 'DET':
                univfeature_dict['PronType'] = 'Art'
                if lemma in ls.PRON_DEF_ART:
                    univfeature_dict['Definite'] = 'Def'
                elif lemma == ls.PRON_INDEF_ART:
                    univfeature_dict['Definite'] = 'Ind'
                else:
                    univpos = 'ADV'

            # határozószói névmások
            elif univpos == 'ADV':
                if lemma in ls.PRON_IND:
                    univfeature_dict['PronType'] = 'Ind'
                elif lemma in ls.NEG:
                    univfeature_dict['PronType'] = 'Neg'
                elif lemma in ls.PRON_TOT:
                    univfeature_dict['PronType'] = 'Tot'
                elif lemma in ls.PRON_DEM:
                    univfeature_dict['PronType'] = 'Dem'
                elif lemma in ls.QPTCL:
                    univfeature_dict['PronType'] = 'Int'

            # névszók
            if univpos in ('NOUN', 'ADJ', 'NUM', 'PRON'):
                # default jegyek
                univfeature_dict['Case'] = 'Nom'
                univfeature_dict['Number'] = 'Sing'

                # tulajdonnév
                if univpos == 'NOUN':
                    if len(lemma) > 0 and lemma[0].isupper():
                        univpos = 'PROPN'

                # default alapfok a fokozás jegyének
                if univpos == 'ADJ':
                    univfeature_dict['Degree'] = 'Pos'

                # számnevek default sorszámnevek
                elif univpos == 'NUM':
                    univfeature_dict['NumType'] = 'Card'
                    # felszíni tulajdonságok alapján disztributív számnevek
                    if lemma.count('-') == 1:
                        dist1, dist2 = lemma.split('-')
                        if dist1 == dist2:
                            univfeature_dict['NumType'] = 'Dist'

            if univpos in ('NOUN', 'ADJ', 'NUM', 'PRON', 'PROPN', 'ADV'):
                # jegyek a mappingsből
                for infl_feat in infl_feats:
                    if infl_feat in mp.NOMINAL_INFL_RULES:
                        univfeature.extend(mp.NOMINAL_INFL_RULES[infl_feat])

                # ha felsőfok, akkor a középfok jegye már nem kell
                if 'Degree=Sup' in univfeature:
                    while 'Degree=Cmp' in univfeature:
                        univfeature.remove('Degree=Cmp')
                    # ronda megoldás a 'legesleg' kezelésére
                    if token.startswith('legesleg'):
                        univfeature.remove('Degree=Sup')
                        univfeature.append('Degree=Abs')

            self._feats_to_dict(univfeature, univfeature_dict)
            # fölösleges jegyek törlése szófajonként
            rm.remove_feats(univpos, univfeature_dict)

            # a számnév jeggyel rendelkező melléknevek nem fokozhatók
            if univpos == 'ADJ' and 'NumType' in univfeature_dict:
                rm.del_feat('Degree', univfeature_dict)

            # ha olyan sorszámnév, amit az emmorph nem sorszámnévnek elemzett
            if univpos == 'NUM' and punct_feat:
                univpos = 'ADJ'
                univfeature_dict['NumType'] = 'Ord'

        return univpos, self._print_feats(univfeature_dict)

    def process_sentence(self, sen, field_names):
        for tok in sen:
            tok.extend(self.parse(tok[field_names[0]], tok[field_names[1]], tok[field_names[2]]))
        return sen

    @staticmethod
    def prepare_fields(field_names):
        return [field_names['form'], field_names['lemma'], field_names['xpostag']]
