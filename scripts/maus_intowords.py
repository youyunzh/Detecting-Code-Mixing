from pydub import AudioSegment
import sys
import os
import subprocess

# song = AudioSegment.from_wav("testwav/alfred1.wav")[:13444]
#
# song.export("01.wav",format="wav")

def main():
    sentence_wav_dir = sys.argv[1]
    trans_sen_dir = sys.argv[2]
    new_wav_dir=sys.argv[3]
    subprocess.call("mkdir -p " + new_wav_dir, shell=True)

    fileList = os.listdir(trans_sen_dir)

    for file in fileList:
        fileid=file[:-9]
        with open(trans_sen_dir+file) as f:

            startpoints=[]
            endpoints=[]
            text=[]
            line =f.readline()
            while "intervals [1]" not in line:
                line=f.readline()

            while "item [2]" not in line:
                toks = line.strip("\n").split()
                if toks[0]=='xmin':
                    startpoints.append(float(toks[-1]))
                elif toks[0]=='xmax':
                    endpoints.append(float(toks[-1]))
                elif toks[0]=='text':
                    if toks[-1]=="\"\"":
                        startpoints=startpoints[:-1]
                        endpoints=endpoints[:-1]
                    else:
                        text.append(toks[-1])
                line = f.readline()

        audio = AudioSegment.from_wav(sentence_wav_dir+fileid+".wav")


        # print(startpoints,endpoints)

        for t in range(len(startpoints)):
            newword=audio[startpoints[t]*1000:1000*endpoints[t]]

            newword.export(new_wav_dir+fileid +text[t]+".wav", format="wav")









if __name__ == '__main__':
    main()