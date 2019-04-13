from bs4 import BeautifulSoup
import pickle, os
import grequests

header = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
}

def soup(response, fhandle):
    fhandle.write(response)

urls=['http://www.tipitaka.org/beng/cscd/', 'http://www.tipitaka.org/guru/cscd/', 'http://www.tipitaka.org/khmr/cscd/', 'http://www.tipitaka.org/mymr/cscd/', 'http://www.tipitaka.org/sinh/cscd/', 'http://www.tipitaka.org/thai/cscd/', 'http://www.tipitaka.org/tibt/cscd/', 'http://www.tipitaka.org/cyrl/cscd/', 'http://www.tipitaka.org/deva/cscd/', 'http://www.tipitaka.org/gujr/cscd/', 'http://www.tipitaka.org/knda/cscd/', 'http://www.tipitaka.org/mlym/cscd/', 'http://www.tipitaka.org/romn/cscd/', 'http://www.tipitaka.org/taml/cscd/', 'http://www.tipitaka.org/telu/cscd/']

names=['beng', 'guru', 'khmr', 'mymr', 'sinh', 'thai', 'tibt', 'cyrl', 'deva', 'gujr', 'knda', 'mlym', 'romn', 'taml', 'telu']

xmls = pickle.load(open('xmls', 'rb'))

if __name__ == "__main__":
    paths = []
    rqs = []
    mems = {}
    path_to_id = {}
    i = 0
    for name, url in zip(names, urls):
        dir_name = name+'/'
        os.mkdir(name)
        for xml in xmls:
            path_web = url+xml
            path_local = dir_name+xml
            paths.append((path_web, path_local))
            rqs.append(grequests.get(path_web))
            path_to_id[path_web] = i
            i+=1

    num_paralls = 32

    while(len(rqs)>0):
        print('---------------- num reqs = ', len(rqs))
        failed_urls = []

        def exception_handler(request, exception):
            #print("Request failed")
            failed_urls.append(request.url)

        res = grequests.imap(rqs, stream=False, size=num_paralls, exception_handler=exception_handler)
        count = 1
        for r in res:
            try:
                if r is not None:
                    #print(r.status_code == 200)
                    if r.status_code != 200:
                        failed_urls.append(r.url)
                        continue
                    i = path_to_id[r.url]
                    try:
                        fhandle = open(paths[i][1], 'w')#'wb')
                    except:
                        failed_urls.append(r.url)
                        continue
                    else:
                        txt = BeautifulSoup(r.text, "lxml", fromEncoding=r.encoding)
                        [s.extract() for s in txt('note')]
                        txt = txt.find_all("p")
                        txt = '\n'.join([ ''.join(t.find_all(text=True)) for t in txt])#.encode('utf-16')
                        soup(txt, fhandle)
                        fhandle.close()
                    finally:
                        del r
                else:
                    print('request None')
                    #mems[i] = txt
                if count%100==0:
                    print(i)
                    #exit(0)
                count += 1
            except:
                pass
        rqs = []
        for path_web in failed_urls:
            #print('retry '+path_web)
            rqs.append(grequests.get(path_web))

        num_paralls = max(int(num_paralls * 0.8), 8)
