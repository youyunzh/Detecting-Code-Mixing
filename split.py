import subprocess
import sys
import os

def main():


    original_track_dir = sys.argv[1]
    track_list_dir = sys.argv[2]
    new_wav_dir=sys.argv[3]

    fileList = os.listdir(track_list_dir)
    ctdur=0

    for spfile in fileList:


        audioname=spfile[:-7]
        groupname=spfile[-3:]
        original_track = original_track_dir  +audioname+".wav"

        subprocess.call("mkdir -p "+ new_wav_dir+audioname, shell=True)
        subprocess.call("mkdir -p "+ new_wav_dir+audioname+"/"+groupname, shell=True)

        # create a template of the ffmpeg call in advance
        cmd_string = 'ffmpeg -i {tr} -c copy -ss {st} -to {en} {nm}.wav'

        # read each line of the track list and split into start, end, name
        with open(track_list_dir+spfile, 'r') as f:
            for line in f:
                # skip comment and empty lines
                if line.startswith('#') or len(line) <= 1:
                    continue

                # create command string for a given track
                start, end, name = line.strip().split()
                if int(end[-2:])>int(start[-2:]):
                    dur=int(end[-2:])-int(start[-2:])
                else:
                    dur=int(end[-2:])-int(start[-2:])+60

                if dur>=4:
                    ctdur+=1
                    command = cmd_string.format(tr=original_track, st=start, en=end, nm=new_wav_dir+audioname+'/'+groupname+'/'+name)
                # print("!!!!!"+command)
                # use subprocess to execute the command in the shell
                    subprocess.call(command, shell=True)
    # print(ctdur)
    return None


if __name__ == '__main__':
    main()