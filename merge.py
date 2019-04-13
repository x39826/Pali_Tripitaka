# coding=utf-8
import os, sys

'''
y   28737 batch/beng.1.txt
y   28737 batch/cyrl.1.txt
y   28737 batch/deva.1.txt
y   28737 batch/gujr.1.txt
y   28737 batch/guru.1.txt
nn   28913 batch/khmr.1.txt
y   28737 batch/knda.1.txt
y   28737 batch/mlym.1.txt
nn   28913 batch/mymr.1.txt
y   28737 batch/romn.1.txt
nn   28913 batch/sinh.1.txt
y   28737 batch/taml.1.txt
y   28737 batch/telu.1.txt
nn   28913 batch/thai.1.txt
y   28737 batch/tibt.1.txt


   33148 batch/beng.1.txt
   33148 batch/cyrl.1.txt
   33148 batch/deva.1.txt
   33148 batch/gujr.1.txt
   33148 batch/guru.1.txt
nn   33626 batch/khmr.1.txt
   33148 batch/knda.1.txt
   33148 batch/mlym.1.txt
nn   33626 batch/mymr.1.txt
   33148 batch/romn.1.txt
nn   33626 batch/sinh.1.txt
   33148 batch/taml.1.txt
   33148 batch/telu.1.txt
nn   33626 batch/thai.1.txt
   33148 batch/tibt.1.txt

'''
def countf(filename):
    count = 0
    thefile = open(filename,'r')
    for line in thefile:
        count += 1
    thefile.close()
    return count

nn = [x for x in os.listdir('batch/')]
names = [x.split('.') for x in nn]
sizes = [countf('batch/'+x) for x in nn]
index = {}
chunks={}
for n in names:
    index[n[0]]=[]
for n,s in zip(names,sizes):
    index[n[0]].append(n[1])
    chunks[n[0]+n[1]]=s
N = len(names) / 15

#print index #zip(names,sizes)

def group(file_names, file_chunks):
    g = {}
    for fn, fc in zip(file_names, file_chunks):
        g[fc] = []
    for fn, fc in zip(file_names, file_chunks):
        g[fc].append(fn)
    return g

groups = []

for id in index[index.keys()[0]]:
    file_names = []
    file_chunks = []
    for n in index.keys():
        file_names.append('batch/%s.%s.txt'%(n,id))
        file_chunks.append(chunks[n+id])
    groups.append(group(file_names, file_chunks))

#print index.keys(), groups

def paste(file_names, output_name):
    fnames =  ' '.join(file_names)
    cmd = 'paste --delimiters=\'\\t\' ' + fnames + ' > %s'%output_name
    os.system(cmd)

def align(file_name1, file_name2, output_name):
    #generate ladder file
    cmd = './hunaligner dict %s %s > %s'%(file_name1, file_name2, output_name)
    os.system(cmd)

def concat(pairs, file_names, output_name):
    base = {}
    #cmd = 'cp %s %s.aligned'%(file_names[0], file_names[0])
    #os.system(cmd)
    parisN = len(pairs) 
    for i in range(parisN):
        for line in pairs[i]:
            a, b = int(line[0]), int(line[1])
            if a not in base:
                base[a] = [None]*parisN
            if base[a][i] is None:
                base[a][i] = []
            base[a][i].append(b)
    maxN = max(base.keys())
    fout = open('%s.aligned'%file_names[0], 'w')
    alllines = open(file_names[0],'r').readlines() + ['\n']

    base.keys().sort()
    for k in base.keys():
        fout.write(alllines[k])
    fout.close()
    fas = [open('%s.aligned'%n, 'w') for n in file_names[1:]]
    for i in range(parisN):
        alllines = open(file_names[i+1],'r').readlines() + ['\n']
        fout = fas[i]
        for j in base.keys():
            lines = base[j][i]
            if lines is None:
                fout.write('\n')
            else:
                try:
                    fout.write(' '.join([s.strip() for s in [alllines[t] for t in lines]]) + '\n')
                except:
                    print file_names, parisN
                    print 'align error',i,j
                    print [alllines[t] for t in lines]
    [f.close() for f in fas]
    file_names = ['%s.aligned'%n for n in file_names]
    paste(file_names, output_name)

def align_files(file_names, output_name):
    base = file_names[0]
    pairs = []
    for i in range(1, len(file_names)):
        other = file_names[i]
        file_ladder = output_name+'.ladder.%d'%i
        align(base, other, file_ladder)
        ladder = [s.split('\t')[:2] for s in open(file_ladder, 'r').readlines()]
        pairs.append(ladder)
    return pairs
#
#pairs = align_files(['batch/cyrl.3.txt', 'batch/beng.3.txt', 'batch/sinh.3.txt'], 't')
#concat(pairs, ['batch/cyrl.3.txt', 'batch/beng.3.txt', 'batch/sinh.3.txt'], 't')

def get_name(prefix, file_names):
    #prefix = file_names[0].split('/')[0] + '_align/'
    names = [y.split('.') for y in [x.split('/')[1] for x in file_names]]
    name = []
    number = names[0][1]
    for t in names:
        name.append(t[0] )
    name = '_'.join(name)
    name=prefix + name + '.' + number
    return name

def align_files_by_groups(file_groups):
    for file_group in file_groups:
        file_group.keys().sort()
        align_names = []
        output_names = []
        for chunk_size in file_group.keys():
            file_names = file_group[chunk_size]
            output_name = get_name('batch_align/',file_names)
            align_names.append(file_names[0])
            output_names.append(output_name)
            paste(file_names, output_name)
            print file_names, '---paste--->', output_name

        output_name = get_name('batch_align_align/',output_names)
        print output_names, '---concat--->',output_name
        pairs = align_files(align_names, output_name)
        concat(pairs, output_names, output_name)

#groups = [{33217: ['batch/mlym.50.txt', 'batch/deva.50.txt'], 33218: ['batch/cyrl.50.txt']}]
align_files_by_groups(groups[12:])

# file_group   {33217: ['batch/mlym.50.txt', 'batch/deva.50.txt', 'batch/telu.50.txt', 'batch/taml.50    .txt', 'batch/guru.50.txt', 'batch/gujr.50.txt', 'batch/tibt.50.txt', 'batch/beng.50.txt', 'batch/knda.50.txt    '], 33218: ['batch/cyrl.50.txt', 'batch/romn.50.txt'], 33669: ['batch/sinh.50.txt', 'batch/mymr.50.txt', 'bat    ch/khmr.50.txt', 'batch/thai.50.txt']}
align_files_by_groups(groups[:12])
