python2.7 stat_sents.py parall/beng.txt.shuf.piece  parall/gujr.txt.shuf.piece    parall/knda.txt.shuf.piece  parall/romn.txt.shuf.piece    parall/telu.txt.shuf.piece parall/cyrl.txt.shuf.piece  parall/guru.txt.shuf.piece    parall/mlym.txt.shuf.piece  parall/sinh.txt.shuf.piece    parall/thai.txt.shuf.piece parall/deva.txt.shuf.piece  parall/khmr.txt.shuf.piece    parall/mymr.txt.shuf.piece  parall/taml.txt.shuf.piece    parall/tibt.txt.shuf.piece 90

sh cut.sh

python2.7 merge.py

python2.7 stat_sents.py batch_align/all.deva  batch_align/all.khmr  batch_align/all.mymr    batch_align/all.taml  batch_align/all.tibt batch_align/all.beng  batch_align/all.gujr  batch_align/all.knda  batch_align/all.romn    batch_align/all.telu batch_align/all.cyrl  batch_align/all.guru  batch_align/all.mlym  batch_align/all.sinh    batch_align/all.thai 90


python split.py

python  sample.py
