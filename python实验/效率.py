import datetime, time

def get_time_stamp1():
    #算毫秒级
    b = datetime.datetime.now()
    print(b)
    a = (i for i in range(20000000))
    c = datetime.datetime.now()
    print(c)

    print('ms',int(c.strftime('%f'))-int(b.strftime('%f')))


def get_time_stamp():
    ct = time.time()
    local_time = time.localtime(ct)
    data_head = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    data_secs = (ct - int(ct)) * 1000
    time_stamp = "%s.%03d" % (data_head, data_secs)
    print(time_stamp)
    stamp = ("".join(time_stamp.split()[0].split("-"))+"".join(time_stamp.split()[1].split(":"))).replace('.', '')
    print(stamp)


get_time_stamp()
# for i in a:
#     print(i)