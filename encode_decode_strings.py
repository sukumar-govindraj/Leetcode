string=["hello", "world", "encode", "decode"]

def encode(string):
    encode=''
    for s in string:
        encode+=f'{len(s)}#{s}'
    
    return encode


string='5#hello5#world6#encode6#decode'
def decode(string):
    res=[]
    i=0
    while i < len(string):
        j = string.find('#', i)
        length = int(string[i:j])

        res.append(string[j+1:j+1+length])

        i = j+1+length
    
    return res

print(decode(string)) 