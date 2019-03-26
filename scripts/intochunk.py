import sys

out=open(sys.argv[1],'w')
# out.write("File type = \"ooTextFile\"\nObject class = \"TextGrid\"\nxmin = 0\n")

outtext=''
size=1

alltoks=[]
for file in sys.argv[2:]:
    with open(file) as f:
        line=f.readline()

        while line.strip('\n'):
            # if line[0]=='*':
            # print(line)
            toks=line.strip('\n').split()
            for t in toks:
                alltoks.append(t)

            # if toks[1]=="[- eng]":

            # print(toks)
            # print(text)
            # print(toks[-1].split("_"))
            # xmin=float(toks[-1].split("_")[0][4:])/1000
            # xmax=float(toks[-1].split("_")[1][:-4])/1000
            #
            # outtext+="\t\tintervals ["+str(size)+"]:\n\t\t\txmin = "+str(xmin)+"\n\t\t\txmax = "+str(xmax)+"\n\t\t\ttext = "+text+"\n"

            line = f.readline()
# print(alltoks)
temptext=[]

lines=[]

for t in alltoks[1:]:
    if t[0]=='*' or t[0]=='%':

        lines.append(temptext)
        temptext=[]
        temptext.append(t)
    else:
        temptext.append(t)

# print(lines)

# for l in lines:
for l in lines:
    print(l)
    # print(l[0][0])


    if l[0][0]=="*":
        text = " ".join(l[:-1])
        # decoded_xmin = l[-1].decode('utf-8')
        # print(l[-1].split("_")[0][1])
        # print(l[-1].split("_")[1])
        try:
            xmin=float(l[-1].split("_")[0][1:])

            xmax=float(l[-1].split("_")[1][:-1])

            # start_misec=int((xmin%1000)*60/1000)
            start_sec=(int(xmin/1000))%60
            start_min=int((int(xmin/1000))/60)

            # end_misec=int((xmax%1000)*60/1000)
            end_sec=(int(xmax/1000))%60
            end_min=int((int(xmax/1000))/60)

            print(start_min)
            print(start_sec)
            print(end_sec)
            # print(start_misec)


            start="00:"
            end="00:"
            if start_min<10:
                start+="0"+str(start_min)+":"
            else:
                start += str(start_min) + ":"
            if start_sec<10:
                start+="0"+str(start_sec)
            else:
                start += str(start_sec)

            if end_min<10:
                end+="0"+str(end_min)+":"
            else:
                end += str(end_min) + ":"

            if end_sec < 10:
                end += "0" + str(end_sec)
            else:
                end += str(end_sec)



        except:
            continue
        # print(l[-1].split("_"))
        # print(xmin)
        # print(xmax)
        # print(text)
        #
        # outtext += "\t\tintervals [" + str(size) + "]:\n\t\t\txmin = " + str(xmin) + "\n\t\t\txmax = " + str(
        #     xmax) + "\n\t\t\ttext = " + text + "\n"

        out.write(start+" "+end+" "+str(size)+"\n")
        size += 1

#
# out.write("xmax = "+str(xmax)+"\ntiers? <exists>\nsize = 1\nitem []:\n\titem [1]:\n\t\tclass = \"IntervalTier\"\n\t\tname = \"MAU\"\n\t\txmin = 0\n\t\txmax = "+str(xmax)
          # +"\n\t\tintervals: size = "+str(size)+'\n')

# out.write(outtext)