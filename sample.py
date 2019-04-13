import glob
import os

if not os.path.isdir('sample'):
    os.mkdir('sample')

#f_dict = {}

file_size = 85706
files = []

for i,f in enumerate(glob.glob(r'Data/*.*')):
    fname, block_id = f.split('/')[1].split('.')
    files.append(fname)
    print('processing %s'%fname)
    #'''
    lines = open(f,'r').readlines()
    f = []
    for i in range(14):
        f.append(open('sample/%s.%s'%(fname,i+1), 'w'))
    c = 0
    for line in lines:
        f[int(c/file_size)].write(line)
        c+=1
    #'''
#exit(0)

def make_pair(fs,ft, n1, n2, id, t=0):
    f1 = 'sample/%s.%s'%(n1,id)
    f2 = 'sample/%s.%s'%(n2,id)
    src = f1+'.src.%d.tmp'%t
    tgt = f2+'.tgt.%d.tmp'%t
    cmd1 = 'sed \'s/^/<t_%s> &/g\' %s > %s'%(n2,f1,src)
    cmd2 = 'sed \'s/^/<f_%s> &/g\' %s > %s'%(n1,f2,tgt)
    #print(cmd1, cmd2)
    #return '%s & %s'%(cmd1,cmd2)
    return '%s && %s && cat %s >> %s && cat %s >> %s && rm %s && rm %s'%(cmd1,cmd2,src,fs,tgt,ft,src,tgt)
    #return '((%s & %s)  && (cat %s >> %s & cat %s >> %s))'%(cmd1,cmd2,src,fs,tgt,ft)
    #os.system('(%s & %s)  && (cat %s >> %s & cat %s >> %s)&'%(cmd1,cmd2,src,fs,tgt,ft) )
'''
a = make_pair('s', 't','tibt','guru',1)
b = make_pair('s', 't','tibt','guru',2)
cmds=[a,b]
cmd = '&'.join(cmds)
os.system(cmd)
print(files)
exit(0)
'''

N= len(files) - 1

idx = [i + 1 for i in range(N)]
num_samples = 6
Fs = ['sample/sample.%d.src'%i for i in range(num_samples)]
Ft = ['sample/sample.%d.tgt'%i for i in range(num_samples)]

import random, time
random.seed(time.time())

for t in range(num_samples):
    fs = Fs[t]
    ft = Ft[t]
    random.shuffle(idx)
    cmds = []
    cmds_ = []
    c = 0
    for i in range(N + 1):
        n1 = files[i]
        for j in range(N + 1):
            if j == i:continue
            id = (i * N + j) % (N +1) - 1
            n2 = files[j]
            cmd = make_pair(fs,ft,n1,n2,idx[id],t)
            cmds.append(cmd)
            c+=1
            if c==N:
                c = 0
                cmds_.append('(' + ' && '.join(cmds) + ')')
                cmds = [] 
            #print(t,i,j,n1,n2,idx[id])
    print('{' +' && '.join(cmds_) + '}')
    os.system('{' + ' && '.join(cmds_) + '}')
    #os.system('(cat sample/*.src.%d.tmp > %s & cat sample/*.tgt.%d.tmp > %s)'%(t,fs,t,ft))






