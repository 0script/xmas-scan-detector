from scapy.all import *
import sys
#import threading

MYIP=sys.argv[1]
FLAGS=[i.flags for i in [TCP(flags=_) for _ in (41,32,8,1)]]

def checkflags(packets):
    for i in packets:
        if i[IP].dst==MYIP:
            if i[TCP].flags in FLAGS:
                print('Possible xMax scan by {} on port {} with flags={}'.format(
                    i[IP].src,
                    i[TCP].dport,
                    i[TCP].flags))
    #time.sleep(1)

if __name__=='__main__':
    while True:
        capture=sniff(filter="tcp",count=10)
        checkflags(capture)
        #thread0=threading.Thread(target=checkflags,args=(capture,))