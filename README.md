# emmorph2ud2

The script converts the output tag of emMorph morphological analyzer to the corresponding UD v2 tag.

# What's in this repo?

* the main script of the converter: `__main__.py` (run it with `python3 -m emmorph2ud2`)
* auxiliary files in folder `converterdata`
* license
* this readme

# The tagsets :hungary:

A detailed description of the tagsets is available [here](https://github.com/dlt-rilmta/panmorph).

## emMorph

[emMorph](https://github.com/dlt-rilmta/emMorph) is the current morphological analyzer for Hungarian and it is integrated into the [e-magyar](http://e-magyar.hu/en) language processing toolchain. The list of emMorph tags is from [here](http://e-magyar.hu/en/textmodules/emmorph_codelist).

## UD v2

UD follows [Universal Dependencies](http://universaldependencies.org/), a framework for cross-linguistically consistent grammatical annotation.

# How to use the converter?

* standard input: token, lemma, emmorph tag separated by tab
* standard output: ud v2 tag (POS and feats)

# Dependencies

`Python3`

# License

GNU General Public License v3.0

# Our converters

* [emmorph2ud](https://github.com/vadno/emmorph2ud)
* [emmorph2msd](https://github.com/vadno/emmorph2msd)
* [emmorph2conll](https://github.com/vadno/emmorph2conll)
