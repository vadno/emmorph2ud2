#!/usr/bin/env python3
# -*- coding: utf-8, vim: expandtab:ts=4 -*-

####################
# SZÓFAJ SZABÁLYOK #
####################

POS_RULES = {
    '/Adj': 'ADJ',
    '/Adj|Abbr': 'ADJ',
    '/Adj|Attr': 'ADJ',
    '/Adj|Attr|Abbr': 'ADJ',
    '/Adj|Attr|Pro': 'ADJ_PRON',
    '/Adj|Pro': 'ADJ_PRON',
    '/Adj|Pro|Rel': 'PRON',
    '/Adj|Pro|Int': 'PRON',
    '/Adj|Pred': 'ADJ',
    '/Adj|Unit': 'ADJ',
    '/Adj|col': 'ADJ',
    '/Adj|nat': 'ADJ',

    '/Adv': 'ADV',
    '/Adv|(Adj)': 'ADV',
    '/Adv|(Num)': 'ADV',
    '/Adv|Abbr': 'ADV',
    '/Adv|Acronx': 'ADV',
    '/Adv|AdjMod': 'ADV',
    '/Adv|Pro': 'PRON',
    '/Adv|Pro|Rel': 'PRON',
    '/Adv|Pro|Int': 'PRON',

    '/Cnj': 'CCONJ',
    '/Cnj|Abbr': 'CCONJ',
    '/CmpdPfx': 'X',
    '/Det': 'DET',
    '/Det|Art.Def': 'DET',
    '/Det|Art.NDef': 'DET',
    '/Det|Pro': 'DET_PRON',
    '/Det|Pro|Int': 'PRON',
    '/Det|Pro|Rel': 'PRON',
    '/Det|Pro|(Post)': 'DET_PRON',
    '/Det|Pro|def': 'DET_PRON',
    '/Det|Q.NDef': 'DET',
    '/Det|Q|indef': 'DET',
    '/Det|Q': 'DET',

    '/Inj-Utt': 'INTJ',
    '/N': 'NOUN',
    '/N|Abbr': 'NOUN',
    '/N|Abbr|ChemSym': 'NOUN',
    '/N|Acron': 'NOUN',
    '/N|Acronx': 'NOUN',
    '/N|Ltr': 'NOUN',
    '/N|Pro': 'NOUN_PRON',
    '/N|Pro|Int': 'PRON',
    '/N|Pro|Rel': 'PRON',
    '/N|Pro|(Post)': 'NOUN_PRON',
    '/N|Pro|Abbr': 'NOUN_PRON',

    '/N|Unit': 'NOUN',
    '/N|Unit|Abbr': 'NOUN',
    '/N|lat': 'NOUN',
    '/N|mat': 'NOUN',
    '/Num': 'NUM',
    '/Num|Abbr': 'NUM',
    '/Num|Attr': 'NUM',
    '/Num|Digit': 'NUM',
    '/Num|Pro': 'NUM_PRON',
    '/Num|Pro|Int': 'PRON',
    '/Num|Pro|Rel': 'PRON',
    '/Num|Roman': 'NUM',

    '/Post': 'ADP',
    '/Post|(Abl)': 'ADP',
    '/Post|(All)': 'ADP',
    '/Post|(Ela)': 'ADP',
    '/Post|(Ins)': 'ADP',
    '/Post|(N0)': 'ADP',
    '/Post|(Poss)': 'ADP',
    '/Post|(Subl)': 'ADP',
    '/Post|(Supe)': 'ADP',
    '/Post|(Ter)': 'ADP',
    '/Prep': 'ADP',
    '/Prev': 'ADV',     # meg -> PART
    '/QPtcl': 'ADV',    # DONE PronType=Int (kérdőpartikula)
    '/S|Abbr': 'X',
    '/V': 'VERB',
    '/X': 'X',
    '/X|Abbr': 'X',

    # 'Hyph:Dash': 'PUNCT',
    # 'Hyph:Hyph': 'PUNCT',
    # 'Hyph:Slash': 'PUNCT',
}

###################
# DERIV SZABÁLYOK #
###################

DERIV_RULES = {
    '_Abe/Adj': 'ADJ',                      # "-A?tlAn, -tAlAn" abessivus = melléknévképző (fosztóképző)
    '_AdjVbz_Ntr/V': 'VERB',                # "-Vs?Odik, -Ul" denominális (melléknévből) intranzitívige-képző
    '_AdjVbz_Tr/V': 'VERB',                 # "-ít" denominális (melléknévből) tranzitívige-képző
    '_Adjz:i/Adj': 'ADJ',                   # "-i" melléknévképző
    '_Adjz:s/Adj': 'ADJ',                   # "-Vs" melléknévképző
    '_Adjz:Ó/Adj': 'ADJ',                   # "-Ó" melléknévképző, mély hangrendű magánhangzók ragozott alakjaiban
    '_Adjz:Ú/Adj': 'ADJ',                   # "-Ú" melléknévképző
    '_Adjz_Hab/Adj': 'ADJ',                 # "-Ós" melléknévképző: habituális
    '_Adjz_Loc:beli/Adj': 'ADJ',            # "-beli" melléknévképző (helyjelölő)
    '_Adjz_Ord:VdlAgOs/Adj': 'ADJ',         # "-VdlAgOs" melléknévképző (számnévből)
    '_Adjz_Quant/Adj': 'NUM',               # "-nyi" mennyiségnévképző
    '_Adjz_Type:fajta/Adj': 'ADJ',          # "-fajta" melléknévképző (típusjelölő)
    '_Adjz_Type:forma/Adj': 'ADJ',          # "-forma" melléknévképző (típusjelölő)
    '_Adjz_Type:féle/Adj': 'ADJ',           # "-féle" melléknévképző (típusjelölő)
    '_Adjz_Type:szerű/Adj': 'ADJ',          # "-szerű" melléknévképző (típusjelölő)
    '_AdvPerfPtcp/Adv': 'ADV',              # "-vÁn" határozói igenév
    '_AdvPtcp/Adv': 'ADV',                  # "-vA" határozói igenév
    '_AdvPtcp:ttOn/Adv': 'ADV',             # "-ttOn" határozói igenév
    '_AdvPtcp:vÁst/Adv': 'ADV',             # "-vÁst" határozói igenév
    '_Advz:rét/Adv': 'ADV',                 # "-rét" számnévi határozóképző
    '_Advz_LocDistr:szerte/Adv': 'ADV',     # "-szerte" határozóképző (térbeli fedés)
    '_Advz_Quant:szám/Adv': 'ADV',          # "-szám" határozóképző mennyiségekre
    '_Aggreg/Adv': 'NUM',                   # "-An" csoportszámosság-határozó
    # '_Caus/V': 'VERB',                    # "-t?At" műveltetőige-képző                       #  nem módosít szófajt
    # '_Com:stUl/Adv': 'ADV',               # "-stUl" comitativusi (társhatározói) esetrag     #  nem módosít szófajt
    # '_Comp/Adj': 'ADJ',                   # "-bb" középfok                                   #  nem módosít szófajt
    # '_Comp/Adv': 'ADV',                   # "-bb" középfok                                   #  nem módosít szófajt
    # '_Comp/Adv|Pro': 'ADV',               # "-bb" középfok                                   #  nem módosít szófajt
    # '_Comp/Num': 'NUM',                   # "-bb" középfok                                   #  nem módosít szófajt
    # '_Comp/Post|(Abl)': 'ADV',            # "-bb" középfok                                   #  nem módosít szófajt
    '_Des/N': 'NOUN',                       # "-hatnék" desiderativus
    # '_Design/Adj': 'ADJ',                 # "-(bb)ik" kijelölő                               #  nem módosít szófajt
    # '_Dim:cskA/Adj': 'ADJ',               # "-VcskA" kicsinyítő képző                        #  nem módosít szófajt
    # '_Dim:cskA/N': 'NOUN',                # "-VcskA" kicsinyítő képző                        #  nem módosít szófajt
    '_Distr:nként/Adv': 'ADV',              # "-Vnként" disztributív
    '_DistrFrq:ntA/Adv': 'ADV',             # "-VntA" gyakorisághatározó
    # '_Freq/V': 'VERB',                    # "-O?gAt" gyakorítóképző                          #  nem módosít szófajt
    '_Frac/Num': 'NUM',                     # "-Vd" törtszámnév
    '_FutPtcp/Adj': 'ADJ',                  # "-AndÓ" „beálló" melléknévi igenév
    '_Ger/N': 'NOUN',                       # "-Ás" nomen actionis igenominalizáló
    '_Ger:tA/N': 'NOUN',                    # "-tA" birtokos igenominalizáló
    '_ImpfPtcp/Adj': 'ADJ',                 # "-Ó" folyamatos melléknévi igenév
    # '_Manner/Adv': 'ADJ',                 # "-An, -Ul" határozóképző: módhatározó            #  nem módosít szófajt
    '_Manner:0/Adv': 'ADJ',               # határozóképző: módhatározó ha zéró toldalékként realizálódik
                                            # a fosztóképző "-A?tlAn/-tAlAn" után              #  nem módosít szófajt
    # '_MedPass/V': 'VERB',                 # "-Ódik" mediális ige                             #  nem módosít szófajt
    # '_Mlt-Iter/Adv': 'ADV',               # "-szOr" multiplikatív/iteratív                   #  nem módosít szófajt
    # '_MltComp/Adv': 'NUM',                # "-szOrtA" összehasonlító multiplikatív           #  nem módosít szófajt
    # '_Mod/V': 'VERB',                     # -hAt" modális („ható") igeképző                  #  nem módosít szófajt
    '_ModPtcp/Adj': 'ADJ',                  # "-hAtÓ" modális melléknévi igenév
    '_Mrs/N': 'NOUN',                       # "-né" asszonynévképző
    '_NAdvz:ilAg/Adv': 'ADJ',               # "-ilAg" denominális (főnévből) határozóképző
    '_NVbz_Ntr:zik/V': 'VERB',              # "-zik" intranzitív igeképző
    '_NVbz_Tr:z/V': 'VERB',                 # "-z" denominális (főnévből) tranzitívige-képző
    '_NegModPtcp/Adj': 'ADJ',               # "-hAtAtlAn" tagadó modális melléknévi igenév
    '_NegPtcp/Adj': 'ADJ',                  # "-AtlAn" tagadó passzív melléknévi igenév (igei fosztóképző)
    '_Nz:s/N': 'NOUN',                      # "-Vs" főnévképző
    '_Nz_Abstr/N': 'NOUN',                  # "-sÁg" főnévképző absztraktfőnév-képző
    # '_Nz_Type:féleség/N': 'NOUN',         # "-féleség" főnévképző (típusjelölő)              #  nem módosít szófajt
    # '_Nz_Type:szerűség/N': 'NOUN',        # "-szerűség" főnévképző (típusjelölő)             #  nem módosít szófajt
    '_Ord/Adj': 'ADJ',                      # "-Vdik" sorszámnév
    '_OrdDate/N': 'NOUN',                   # "-Vdika" dátumokban a nap sorszámnévképzője
    # '_Pass/V': 'VERB',                    # "-t?Atik" passzív                                #  nem módosít szófajt
    '_PerfPtcp/Adj': 'ADJ',                 # "-O?tt" befejezett melléknévi igenév
    '_PerfPtcp_Subj=tA/Adj': 'ADJ',         # "-tA" befejezett melléknévi igenév
    '_Tmp_Ante/Adv': 'ADV',                 # "-jA" időbeli megelőzés
    '_Tmp_Loc/Adv': 'ADV',                  # "-vAl, -0" időhatározói végződés
                                            # (különböző (lexikalizált) megjelenési formákban)
    '_VAdvz:ÓlAg/Adv': 'ADV',               # "-ÓlAg" határozóképző: igéből
    '_VAdjz:nivaló/Adj': 'ADJ',             # HIÁNYZIK A HONLAPRÓL!!!
    '_VNz:nivaló/N': 'NOUN',                # "-nivaló" főnévképző
    '_Vbz:kOd/V': 'VERB'                    # "-s?kOdik" denominális igeképző
}

#########################
# POS helyett INFL jegy #
#########################

POS_TO_INFL_FEAT = ('/Supl',)

###########################
# DERIV helyett INFL jegy #
###########################

DERIV_TO_INFL_FEAT = (
    '_Freq/V',                              # "-O?gAt" gyakorítóképző
    '_Mod/V',                               # -hAt" modális („ható") igeképző
    '_Caus/V',                              # "-t?At" műveltetőige-képző
    '_Comp/Adj',                            # "-bb" középfok
    '_Comp/Adv|Pro',                        # "-bb" középfok
    '_Comp/Adv',                            # "-bb" középfok
    '_Comp/Num',                            # "-bb" középfok
    '_Design/Adj',                          # "-(bb)ik" kijelölő
    '_Distr:nként/Adv',                     # "-Vnként" disztributív
    '_AdvPtcp/Adv',                         # "-vA" határozói igenév (a többi határozói igenevet nem kezeli)
    '_FutPtcp/Adj',                         # "-AndÓ" „beálló" melléknévi igenév
    '_ImpfPtcp/Adj',                        # "-Ó" folyamatos melléknévi igenév
    '_PerfPtcp/Adj',                        # "-O?tt" befejezett melléknévi igenév
    '_Frac/Num',                            # "-Vd" törtszámnév
    '_Ord/Adj',                             # "-Vdik" sorszámnév
    '_Adjz_Hab/Adj',
    '_Adjz:Ó/Adj',
    '_Manner/Adv',
    '_Manner:0/Adv',
    '_NAdvz:ilAg/Adv',
    '_VAdvz:ÓlAg/Adv',
    '_ModPtcp/Adj'
)

######################
# vonatkozó névmások #
######################

REL_PRON = {
    '/Adj|Pro|Rel',
    '/Adv|Pro|Rel',
    '/Det|Pro|Rel',
    '/N|Pro|Rel',
    '/Num|Pro|Rel'
}

##################
# kérdő névmások #
##################

INT_PRON = {
    '/Adj|Pro|Int',
    '/Adv|Pro|Int',
    '/Det|Pro|Int',
    '/N|Pro|Int',
    '/Num|Pro|Int'
}

##########################
# inflexiós jegyek: igei #
##########################

VERBAL_INFL_RULES = {
    '_Caus/V': ['Voice=Cau'],               # "-t?At" műveltetőige-képző
    '_Freq/V': ['Aspect=Iter'],             # "-O?gAt" gyakorítóképző
    '_Mod/V': ['Pot=Pot'],                  # ez itt nem hiba, későb a Pot=Pot tovább módosul!

    'Inf': ['VerbForm=Inf'],
    
    'Sbjv': ['Mood=Imp', 'Tense=Pres'],
    'Cond': ['Mood=Cnd', 'Tense=Pres'],
    'Prs': ['Mood=Ind', 'Tense=Pres'],
    'Pst': ['Mood=Ind', 'Tense=Past'],

    '1Sg': ['Number=Sing', 'Person=1'],
    '1Sg›2': ['Definite=2', 'Number=Sing', 'Person=1'],
    '2Sg': ['Number=Sing', 'Person=2'],
    '3Sg': ['Number=Sing', 'Person=3'],
    '1Pl': ['Number=Plur', 'Person=1'],
    '1Pl*': ['Number=Plur', 'Person=1'],
    '2Pl': ['Number=Plur', 'Person=2'],
    '3Pl': ['Number=Plur', 'Person=3'],
    '3Pl*': ['Number=Plur', 'Person=3'],
    'Def': ['Definite=Def'],
    'NDef': ['Definite=Ind']
}

#############################
# inflexiós jegyek: névszói #
#############################

NOMINAL_INFL_RULES = {
    '/Supl': ['Degree=Sup'],                          # szófaji jegyből lett derivációs jegy
    '_Comp/Adj': ['Degree=Cmp'],
    '_Comp/Adv|Pro': ['Degree=Cmp'],
    '_Comp/Adv': ['Degree=Cmp'],
    '_Comp/Num': ['Degree=Cmp'],
    '_Design/Adj': ['Degree=Cmp'],

    '_AdvPtcp/Adv': ['VerbForm=Conv'],               # "-vA" határozói igenév

    '_FutPtcp/Adj': ['VerbForm=PartFut'],             # "-AndÓ" „beálló" melléknévi igenév
    '_ImpfPtcp/Adj': ['VerbForm=PartPres'],           # "-Ó" folyamatos melléknévi igenév
    '_PerfPtcp/Adj': ['VerbForm=PartPast'],           # "-O?tt" befejezett melléknévi igenév
    '_Adjz_Hab/Adj': ['VerbForm=PartPres'],
    '_Adjz:Ó/Adj': ['VerbForm=PartPres'],
    '_ModPtcp/Adj': ['VerbForm=PartPres'],

    '_Frac/Num': ['NumType=Frac'],                    # "-Vd" törtszámnév
    '_Ord/Adj': ['NumType=Ord'],                      # "-Vdik" sorszámnév

    '_Distr:nként/Adv': ['Case=Dis'],                 # "-Vnként" disztributív
    '_Manner/Adv': ['Case=Ess'],
    # '_Manner:0/Adv': ['Case=Ess'],                   # TODO kivettem kísérlet
    '_NAdvz:ilAg/Adv': ['Case=Ess'],
    '_VAdvz:ÓlAg/Adv': ['Case=Ess'],
    'Nom': ['Case=Nom'],
    'Acc': ['Case=Acc'],
    'Dat': ['Case=Dat'],
    'Ins': ['Case=Ins'],
    'Cau': ['Case=Cau'],
    'Ine': ['Case=Ine'],
    'Supe': ['Case=Sup'],
    'Ade': ['Case=Ade'],
    'Ill': ['Case=Ill'],
    'Ela': ['Case=Ela'],
    'Del': ['Case=Del'],
    'Subl': ['Case=Sub'],
    'Abl': ['Case=Abl'],
    'All': ['Case=All'],
    'Ter': ['Case=Ter'],
    'Temp': ['Case=Tem'],
    'Loc': ['Case=Loc'],
    'Inl': ['Case=Inl'],
    'Transl': ['Case=Tra'],
    'Ess': ['Case=Ess'],
    'EssFor:ként': ['Case=Ess'],
    'EssFor:képp': ['Case=Ess'],
    'EssFor:képpen': ['Case=Ess'],

    'Pl': ['Number=Plur'],
    'Fam.Pl': ['Number=Plur'],

    '1Sg': ['Number=Sing', 'Person=1'],
    '2Sg': ['Number=Sing', 'Person=2'],
    '3Sg': ['Number=Sing', 'Person=3'],
    '1Pl': ['Number=Plur', 'Person=1'],
    '2Pl': ['Number=Plur', 'Person=2'],
    '3Pl': ['Number=Plur', 'Person=3'],

    'Poss.1Sg': ['Number[psor]=Sing', 'Person[psor]=1'],
    'Poss.2Sg': ['Number[psor]=Sing', 'Person[psor]=2'],
    'Poss.3Sg': ['Number[psor]=Sing', 'Person[psor]=3'],
    'Poss.1Pl': ['Number[psor]=Plur', 'Person[psor]=1'],
    'Poss.2Pl': ['Number[psor]=Plur', 'Person[psor]=2'],
    'Poss.3Pl': ['Number[psor]=Plur', 'Person[psor]=3'],

    'Pl.Poss.1Sg': ['Number=Plur', 'Number[psor]=Sing', 'Person[psor]=1'],
    'Pl.Poss.2Sg': ['Number=Plur', 'Number[psor]=Sing', 'Person[psor]=2'],
    'Pl.Poss.3Sg': ['Number=Plur', 'Number[psor]=Sing', 'Person[psor]=3'],
    'Pl.Poss.1Pl': ['Number=Plur', 'Number[psor]=Plur', 'Person[psor]=1'],
    'Pl.Poss.2Pl': ['Number=Plur', 'Number[psor]=Plur', 'Person[psor]=2'],
    'Pl.Poss.3Pl': ['Number=Plur', 'Number[psor]=Plur', 'Person[psor]=3'],

    'AnP': ['Number[psed]=Sing'],
    'AnP.Pl': ['Number[psed]=Plur'],
}
