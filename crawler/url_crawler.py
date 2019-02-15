from scapy.all import *

f = open("url.txt", 'w')

def find_url(packet):
    ls = []
    ls.append("\n".join(packet.sprintf("{Raw:%Raw.load%}\n").split(r"\r\n")))
    for http_packet in ls:
        if http_packet.find('GET') != -1:
            request = http_packet.split(' ')
            f.write(request[0]+" "+request[1]+'\n')
        elif http_packet.find('POST') != -1:
            request = http_packet.split(' ')
            f.write(request[0]+" "+request[1]+'\n')
        elif http_packet.find('PUT') != -1:
            request = http_packet.split(' ')
            f.write(request[0]+" "+request[1]+'\n')
        elif http_packet.find('DELETE') != -1:
            request = http_packet.split(' ')
            f.write(request[0]+" "+request[1]+'\n')
        else:
            pass

def sniffing(filter):
    sniff(prn = find_url)