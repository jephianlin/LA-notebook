#!/bin/bash


sed \
    -e 's/\^\\\\top/\\\\trans/g' \
    -e 's/\^{\\\\rm adj}/\\\\adj/g' \
    -e 's/\^{\\\\rm cof}/\\\\cof/g' \
    -e 's/\\\\mathbf{0}/\\\\bzero/g' \
    -e 's/\\\\mathbf{1}/\\\\bone/g' \
    -e 's/\\\\mathbf{a}/\\\\ba/g' \
    -e 's/\\\\mathbf{b}/\\\\bb/g' \
    -e 's/\\\\mathbf{c}/\\\\bc/g' \
    -e 's/\\\\mathbf{d}/\\\\bd/g' \
    -e 's/\\\\mathbf{e}/\\\\be/g' \
    -e 's/\\\\mathbf{h}/\\\\bh/g' \
    -e 's/\\\\mathbf{p}/\\\\bp/g' \
    -e 's/\\\\mathbf{q}/\\\\bq/g' \
    -e 's/\\\\mathbf{r}/\\\\br/g' \
    -e 's/\\\\mathbf{x}/\\\\bx/g' \
    -e 's/\\\\mathbf{y}/\\\\by/g' \
    -e 's/\\\\mathbf{z}/\\\\bz/g' \
    -e 's/\\\\mathbf{u}/\\\\bu/g' \
    -e 's/\\\\mathbf{v}/\\\\bv/g' \
    -e 's/\\\\mathbf{w}/\\\\bw/g' \
    -e 's/\\\\operatorname{tr}/\\\\tr/g' \
    -e 's/\\\\operatorname{null}/\\\\nul/g' \
    -e 's/\\\\operatorname{rank}/\\\\rank/g' \
    -e 's/\\\\operatorname{ker}/\\\\ker/g' \
    -e 's/\\\\operatorname{range}/\\\\range/g' \
    -e 's/\\\\operatorname{Col}/\\\\Col/g' \
    -e 's/\\\\operatorname{Row}/\\\\Row/g' \
    -e 's/\\\\operatorname{spec}/\\\\spec/g' \
    -e 's/\\\\operatorname{span}/\\\\vspan/g' \
    -e 's/\\\\operatorname{Vol}/\\\\Vol/g' \
    -e 's/\\\\operatorname{sgn}/\\\\sgn/g' \
    -e 's/\\\\operatorname{id}/\\\\idmap/g' \
    -e 's/\\\\operatorname{am}/\\\\am/g' \
    -e 's/\\\\operatorname{gm}/\\\\gm/g' \
    -e 's/\\\\operatorname{mult}/\\\\mult/g' \
    -e 's/\\\\operatorname{iner}/\\\\iner/g' \
    $1 > output.ipynb

mv output.ipynb $1

# $\newcommand{\trans}{^\top}
# \newcommand{\adj}{^{\rm adj}}
# \newcommand{\cof}{^{\rm cof}}
# \newcommand{\inp}[2]{\left\langle#1,#2\right\rangle}
# \newcommand{\dunion}{\mathbin{\dot\cup}}
# \newcommand{\bzero}{\mathbf{0}}
# \newcommand{\bone}{\mathbf{1}}
# \newcommand{\ba}{\mathbf{a}}
# \newcommand{\bb}{\mathbf{b}}
# \newcommand{\bc}{\mathbf{c}}
# \newcommand{\bd}{\mathbf{d}}
# \newcommand{\be}{\mathbf{e}}
# \newcommand{\bh}{\mathbf{h}}
# \newcommand{\bp}{\mathbf{p}}
# \newcommand{\bq}{\mathbf{q}}
# \newcommand{\br}{\mathbf{r}}
# \newcommand{\bx}{\mathbf{x}}
# \newcommand{\by}{\mathbf{y}}
# \newcommand{\bz}{\mathbf{z}}
# \newcommand{\bu}{\mathbf{u}}
# \newcommand{\bv}{\mathbf{v}}
# \newcommand{\bw}{\mathbf{w}}
# \newcommand{\tr}{\operatorname{tr}}
# \newcommand{\nul}{\operatorname{null}}
# \newcommand{\rank}{\operatorname{rank}}
# %\newcommand{\ker}{\operatorname{ker}}
# \newcommand{\range}{\operatorname{range}}
# \newcommand{\Col}{\operatorname{Col}}
# \newcommand{\Row}{\operatorname{Row}}
# \newcommand{\spec}{\operatorname{spec}}
# \newcommand{\vspan}{\operatorname{span}}
# \newcommand{\Vol}{\operatorname{Vol}}
# \newcommand{\sgn}{\operatorname{sgn}}
# \newcommand{\idmap}{\operatorname{id}}
# \newcommand{\am}{\operatorname{am}}
# \newcommand{\gm}{\operatorname{gm}}
# \newcommand{\mult}{\operatorname{mult}}
# \newcommand{\iner}{\operatorname{iner}}$
