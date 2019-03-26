import sys
import os
import re
import subprocess

def intogroup(l):
    text = " ".join(l[:-1])


    codemix = 0
    for t in l:
        if "@s" in t:
            codemix = 1
            break

    try:
        xmin = float(l[-1].split("_")[0][1:])

        xmax = float(l[-1].split("_")[1][:-1])


        if codemix:
            xmax+=1000

        # start_misec=int((xmin%1000)*60/1000)
        start_sec = (int(xmin / 1000)) % 60
        start_min = int((int(xmin / 1000)) / 60)

        # end_misec=int((xmax%1000)*60/1000)
        end_sec = (int(xmax / 1000)) % 60
        end_min = int((int(xmax / 1000)) / 60)

        # print(start_min)
        # print(start_sec)
        # print(end_sec)
        # print(start_misec)

        start = "00:"
        end = "00:"
        if start_min < 10:
            start += "0" + str(start_min) + ":"
        else:
            start += str(start_min) + ":"
        if start_sec < 10:
            start += "0" + str(start_sec)
        else:
            start += str(start_sec)

        if end_min < 10:
            end += "0" + str(end_min) + ":"
        else:
            end += str(end_min) + ":"

        if end_sec < 10:
            end += "0" + str(end_sec)
        else:
            end += str(end_sec)


    except:
        return 0


    return start, end


def main():

    eppler_trans_dir = sys.argv[1]

    outdir=sys.argv[2]
    subprocess.call("mkdir -p " + outdir , shell=True)

    ifgrouped_lang=int(sys.argv[3])

    ifannotated=int(sys.argv[4])

    out_eng = ''
    out_ger = ''
    out_mix = ''

    fileList = os.listdir(eppler_trans_dir)



    for cha_file in fileList:
        outname=cha_file[:-4]
        alltoks=[]

        size=1
        with open(eppler_trans_dir+cha_file) as f:
            line=f.readline()

            while line.strip('\n'):
                if line[0]!='@' or ('@s' in line):
                    toks=line.strip('\n').split()
                    for t in toks:
                        alltoks.append(t)

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


        if ifannotated==2 and ifgrouped_lang==2:


        #     subprocess.call("mkdir -p " + outdir + outname + "/ger/" , shell=True)
        #                                 out = open(outdir + outname + "/ger/"  + str(size) + ".txt", 'w')
        #                                 out.write(text)
        #     out_eng = open(outdir + outname + "_sp_eng", 'w')
        #     out_ger = open(outdir + outname + "_sp_ger", 'w')
        #     out_mix = open(outdir + outname + "_sp_mix", 'w')
            out_eng = open(outdir + outname + "_sp_eng", 'w')
            out_ger = open(outdir + outname + "_sp_ger", 'w')
            out_mix = open(outdir + outname + "_sp_mix", 'w')
            for l in lines:
                # print(l)
                # print(l[0][0])
                text=''
                for t in l[1:]:
                    if t == "eng]":
                        continue
                    elif re.search('[a-zA-Z]', t):
                        text += t + ' '

                if l:
                    if l[0][0] == "*":
                        codemix = 0
                        for t in l:
                            if "@s" in t:
                                codemix = 1
                                break

                        if codemix:
                            result = intogroup(l)
                            if result:
                                # out_mix.write(result[0] + " " + result[1] + " " + str(size)  +" "+ " ".join(l) +"\n")
                                subprocess.call("mkdir -p " + outdir + outname + "/mix/", shell=True)
                                out = open(outdir + outname + "/mix/" + str(size) + ".txt", 'w')
                                out.write(text)
                                out.close()
                                out_mix.write(result[0] + " " + result[1] + " " + str(size) + " " + text + "\n")
                                size += 1
                                continue
                            else:
                                continue

                        if "eng]" in l:

                            result = intogroup(l)
                            if result:
                                # out_eng.write(result[0] + " " +result[1] + " " + str(size)+" "+ " ".join(l)  + "\n")
                                subprocess.call("mkdir -p " + outdir + outname + "/eng/", shell=True)
                                out = open(outdir + outname + "/eng/" + str(size) + ".txt", 'w')
                                out.write(text)
                                out.close()
                                out_eng.write(result[0] + " " + result[1] + " " + str(size) + " " + text + "\n")
                                size += 1
                            else:
                                continue
                        else:
                            result = intogroup(l)
                            if result:
                                subprocess.call("mkdir -p " + outdir + outname + "/ger/", shell=True)
                                out = open(outdir + outname + "/ger/" + str(size) + ".txt", 'w')
                                out.write(text)
                                out.close()
                                # out_ger.write(result[0] + " " + result[1] + " " + str(size) +" "+ " ".join(l) + "\n")
                                out_ger.write(result[0] + " " + result[1] + " " + str(size) + " " + text + "\n")
                                size += 1
                            else:
                                continue



        elif not ifgrouped_lang:
            if ifannotated:
                out = open(outdir + outname + "_sp_anno", 'w')
            else:
                out = open(outdir + outname+"_sp", 'w')
            for l in lines:
                text =''
                if ifannotated:
                    text=" ".join(l)

                if l:
                    result = intogroup(l)
                    if result:
                        out.write(result[0] + " " + result[1] + " " + str(size) + " " + text + "\n")
                        size += 1
                    else:
                        continue





        else:

            if not ifannotated:
                out_eng = open(outdir + outname + "_sp_eng", 'w')
                out_ger = open(outdir + outname + "_sp_ger", 'w')
                out_mix = open(outdir + outname + "_sp_mix", 'w')
            else:
                out_eng = open(outdir + outname + "_sp_eng_anno", 'w')
                out_ger = open(outdir + outname + "_sp_ger_anno", 'w')
                out_mix = open(outdir + outname + "_sp_mix_anno", 'w')

            for l in lines:
                # print(l)
                # print(l[0][0])
                text = ''
                if ifannotated:
                    text = " ".join(l)

                if l:
                    if l[0][0]=="*":
                        codemix = 0
                        for t in l:
                            if "@s" in t:
                                codemix = 1
                                break

                        if codemix:
                            result = intogroup(l)
                            if result:
                                # out_mix.write(result[0] + " " + result[1] + " " + str(size)  +" "+ " ".join(l) +"\n")
                                out_mix.write(result[0] + " " + result[1] + " " + str(size) +" " +text+"\n")
                                size += 1
                                continue
                            else:
                                continue

                        if "eng]" in l:

                            result = intogroup(l)
                            if result:
                                # out_eng.write(result[0] + " " +result[1] + " " + str(size)+" "+ " ".join(l)  + "\n")
                                out_eng.write(result[0] + " " +result[1] + " " + str(size)+" "+text+  "\n")
                                size += 1
                            else:
                                continue
                        else:
                                result = intogroup(l)
                                if result:
                                    # out_ger.write(result[0] + " " + result[1] + " " + str(size) +" "+ " ".join(l) + "\n")
                                    out_ger.write(result[0] + " " + result[1] + " " + str(size) +" " +text + "\n")
                                    size += 1
                                else:
                                    continue







if __name__ == '__main__':
    main()