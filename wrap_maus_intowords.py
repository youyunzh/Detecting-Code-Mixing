import os
import subprocess
import sys

def main():
    sentence_wav_total_dir = sys.argv[1]
    trans_sen_total_dir = sys.argv[2]
    new_wav_total_dir = sys.argv[3]

    subprocess.call("mkdir -p " + new_wav_total_dir, shell=True)

    senfileList = os.listdir(sentence_wav_total_dir)
    transfileList = os.listdir(trans_sen_total_dir)
    # wavfileList = os.listdir(trans_sen_total_dir)
    for senfile in senfileList:
        if senfile[0] != '.':
            audioname=senfile
            groupfileList = os.listdir(sentence_wav_total_dir+senfile+"/")

            for groupfile in groupfileList:
                if groupfile[0]!='.':
                    subprocess.call("mkdir -p " + new_wav_total_dir+audioname+"/"+groupfile+"/", shell=True)
                    command="python maus_intowords.py "+sentence_wav_total_dir+audioname+"/"+groupfile+"/ "+ trans_sen_total_dir + audioname+"/"+groupfile+"_tg/ "+ new_wav_total_dir+audioname+"/"+groupfile+"/"
                    print(command)
                    subprocess.call(command, shell=True)






if __name__ == '__main__':
    main()