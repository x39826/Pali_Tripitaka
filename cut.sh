batch=10000
max_len=90

python2.7 stat_sents.py parall/beng.txt.shuf.piece  parall/gujr.txt.shuf.piece    parall/knda.txt.shuf.piece  parall/romn.txt.shuf.piece    parall/telu.txt.shuf.piece parall/cyrl.txt.shuf.piece  parall/guru.txt.shuf.piece    parall/mlym.txt.shuf.piece  parall/sinh.txt.shuf.piece    parall/thai.txt.shuf.piece parall/deva.txt.shuf.piece  parall/khmr.txt.shuf.piece    parall/mymr.txt.shuf.piece  parall/taml.txt.shuf.piece    parall/tibt.txt.shuf.piece  $max_len

((python2.7 cut_sents.py parall/sinh.txt.shuf.piece batch/sinh $batch &); \
(python2.7 cut_sents.py parall/cyrl.txt.shuf.piece batch/cyrl $batch&); \
(python2.7 cut_sents.py parall/beng.txt.shuf.piece batch/beng $batch&); \
(python2.7 cut_sents.py parall/taml.txt.shuf.piece batch/taml $batch&); \
(python2.7 cut_sents.py parall/telu.txt.shuf.piece batch/telu $batch&); \
(python2.7 cut_sents.py parall/knda.txt.shuf.piece batch/knda $batch&); \
(python2.7 cut_sents.py parall/gujr.txt.shuf.piece batch/gujr $batch&); \
(python2.7 cut_sents.py parall/thai.txt.shuf.piece batch/thai $batch&); \
(python2.7 cut_sents.py parall/tibt.txt.shuf.piece batch/tibt $batch&); \
(python2.7 cut_sents.py parall/khmr.txt.shuf.piece batch/khmr $batch&); \
(python2.7 cut_sents.py parall/romn.txt.shuf.piece batch/romn $batch&); \
(python2.7 cut_sents.py parall/deva.txt.shuf.piece batch/deva $batch&); \
(python2.7 cut_sents.py parall/guru.txt.shuf.piece batch/guru $batch&); \
(python2.7 cut_sents.py parall/mlym.txt.shuf.piece batch/mlym $batch&); \
(python2.7 cut_sents.py parall/mymr.txt.shuf.piece batch/mymr $batch&)) 


