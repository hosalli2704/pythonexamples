F1 = open('out3.txt', 'w')
F2 = open('out4.csv', 'w')
F1.write('IP address\tUsername \tTimestamp \tAccess request\tResult status code\tBytes transferred\tReferrer URL\tUser Agent ')
F2.writelines(['IP address,', 'Username,', 'Timestamp,', 'Access_request,',' Result_status_code,', 'Bytes_transferred,','Referrer_URL','User_Agent\n'])
F3 = open(r'log.txt')

for line in F3:
    if line[:3].isdigit():
       # print(line)
        sp = line.split()
       # print(sp)
        ip_address = sp[0]
        username = sp[1] + sp[2]
        timestamp = sp[3]
        accessrequest = sp[4]
        result = sp[5]
        byte = sp[6]
        url = sp[7]
        agent = sp[8]
        #F1.writelines(['\n' + ip_address + '\t' ,  username + '\t', timestamp + '\t', accessrequest + '\t', result + '\t', byte + '\t', url + '\t', agent +'\n'])
        print(ip_address, username, timestamp, accessrequest, result ,byte ,url ,agent, sep= '\t', file=F1)
        print(ip_address, username, timestamp, accessrequest, result, byte, url, agent, sep='\t', file=F2)