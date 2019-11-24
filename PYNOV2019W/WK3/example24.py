import psutil


def get_mem_detais():
    resp = psutil.virtual_memory()
   
    tm = resp.total
    fm = resp.available
    um = resp.used
    return tm, fm, um

def get_used():
    resp = get_mem_detais()
    return resp[2]

def get_free():
    resp = get_mem_detais()
    return resp[1]

def get_total():
    resp = get_mem_detais()
    return resp[0]


output = get_free()
print(output)
# you can convert that object to a dictionary 


#dict(psutil.virtual_memory()._asdict())
