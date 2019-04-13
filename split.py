import glob
import os

if not os.path.isdir('corpus'):
    os.mkdir('corpus')

#f_dict = {}

for i,f in enumerate(glob.glob(r'batch_align_align/*.*')):
    lines = open(f,'r').readlines()
    fnames, block_id = f.split('/')[1].split('.')
    f = []
    print('processing %s'%fnames, block_id)
    for fname in fnames.split('_'):
        f.append(open('corpus/%s.%s'%(fname,block_id), 'w'))
    c = 0
    for line in lines:
        l = line.strip()
        if len(l) < 15:continue
        ls = l.split('\t')
        if len(ls) < 15:
            c += 1
            if c%100 ==0 :print(line,ls,len(ls))
            continue
        if len(ls) > 15:
            print('>', line,ls,len(ls))
            continue
        if '<p>' not in ls:
            for i,s in enumerate(ls):
                #if s == '<p>':
                #continue
                #s = ''
                f[i].write(s+'\n')

for n in fnames.split('_'):
    os.system('cat corpus/%s.* > corpus/%s.all &'%(n,n) )


