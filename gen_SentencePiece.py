import os

fs = ['beng.txt.shuf' ,'deva.txt.shuf' ,'guru.txt.shuf' ,'knda.txt.shuf' ,'mymr.txt.shuf' ,'sinh.txt.shuf' ,'telu.txt.shuf' ,'tibt.txt.shuf' ,'cyrl.txt.shuf' ,'gujr.txt.shuf' ,'khmr.txt.shuf' ,'mlym.txt.shuf' ,'romn.txt.shuf' ,'taml.txt.shuf' ,'thai.txt.shuf']


cmds = []
#os.mkdir('model')

for f in fs:
    cmd0 = 'spm_train --input=%s --model_prefix=%s  --vocab_size=%d --model_type=%s'%('parall/'+f, 'model/'+f, 32000, 'unigram')
    cmd1 = 'spm_encode --model=%s --output_format=piece < %s > %s'%('model/'+f+'.model', 'parall/'+f, 'parall/'+f+'.piece')
    cmd = cmd0 + '&&' + cmd1
    cmds.append(cmd)
print('&'.join(cmds))
os.system('&'.join(cmds))

