
def funcion1(packet):
    try:
        if(packet['IP']['src']== '172.17.0.3'):
            packet['MDNS']['count.queries'] = 0
            print("\n contador modificado a :",packet['MDNS']['count.queries'])
            return packet
    except:
        return packet

def funcion3(packet):
    try:
        if(packet['IP']['src'] == '172.17.0.3'):
            packet['IP']['src'] == '192.168.1.4'
            return packet
    except:
        return packet 

def funcion4(packet):
    try:
        if(packet['IP']['src'] == '192.168.0.3'):
            if(packet['UDP']['length'] == 36 ):
                packet['MDNS']['qry.name']=''
                packet['UDP']['length'] = 24
                packet['IP']['len'] = 44
                return packet
    except:
        return packet


def funcion5(packet):
    try:
        if(packet['IP']['src'] == '172.17.0.2'):
            packet['MDNS']['count.queries'] = 69
            print("Count queries modificada a 69")
            packet['MDNS']['count.answers'] = 33
            print("\nCount answers modificada a 33")
        return packet
    except:
        return packet

def funcion5p2(packet):
    try:
        if(packet['IP']['src'] == '172.17.0.3'):
            packet['MDNS']['count.queries'] = 69
            print("Count queries modificada a 1")
            packet['MDNS']['count.answers'] = 33
            print("\nCount answers modificada a 1")
        return packet
    except:
        return packet
