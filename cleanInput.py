import csv

from getConfig import getConfig

def getRows(fileName):
    l=[]
    count=0
    with open(fileName, 'r') as f:
        for line in f:
            count+=1
            if count > 8:
                row = line.split("\t")
                if row[0] == '#close':
                    break
                else:
                    l.append(row)
    return l

def main():
    cfg = getConfig()
    inputFile = cfg['dataLoc']+ "conn.log.labeled"
    data = getRows(inputFile)
    print("Read {:,.0f} rows from {}\n".format(len(data), inputFile))
    
    # Replace provide column names with more decriptive
    cols = ['ts', 'uid', 'id.orig_h', 'id.orig_p', 'id.resp_h', 'id.resp_p', 'proto', 'service',
            'duration', 'orig_bytes', 'resp_bytes', 'conn_state', 'local_orig', 'local_resp',
            'missed_bytes', 'history', 'orig_pkts', 'orig_ip_bytes', 'resp_pkts', 'resp_ip_bytes',
            'label']

    outputFile = cfg['dataLoc'] + 'clean.csv'
    benign = 0
    mal = 0
    with open(outputFile,'w') as f1:
        writer = csv.writer(f1, delimiter=',', lineterminator='\n',)
        writer.writerow(cols)
        for row in data:
            if "Benign" in row[-1]:
                benign +=1
                row[-1] = 'Benign'
            elif "Malicious" in row[-1]:
                mal +=1
                row[-1] = 'Malicious'
            else:
                print(row[-1])
            writer.writerow(row)

    print("Number benign:    {:,.0f}".format(benign))
    print("Number malicious: {:,.0f}".format(mal))

if __name__ == '__main__':
    main()