#!/usr/bin/env bash

#library used:
#ffmpeg; pydub; pyAudioAnalysis

#To read and transform the original transcript to the form [start_time] [end_time] [wav index]:
# template: python intochunk_groups.py [Corpus_transcipt] [output_directory] [if_split_into_different_langs_per_transcipt] [if_keep_annotated_text]
# 1 0: split_into_different_langs_per_transcipt & don't keep annotated text
# 0 1: don't split_into_different_langs_per_transcipt & keep annotated text - for the purpose of tracking what are the sentences
# 2 2: split into one sentence per file - for inputting into MAUS
python intochunk_groups.py Eppler_transcript/ Eppler_utterance_split/ 1 0
python intochunk_groups.py Eppler_transcript/ Eppler_utterance_split_anno/  0 1
python intochunk_groups.py Eppler_transcript/ new_sen_split/  2 2

# use library ffmpeg to split the original wav files according to the time constraints that we generate:
#python split.py [original_wav_directory] [splited_transcript_directory] [new_splited_wav_directory]
python split.py original_wav/ Eppler_utterance_split/ split_sen_wav_full/

#boot strap step: input sentence wav files(new_split_wav/) and its corresponding transcripts (new_sen_split/) into MAUS's webservice,
# put the output in MAUS_output_word_splited/

python wrap_maus_intowords.py split_sen_wav_full/ MAUS_output_word_splited/ Eppler_word_split_wav_4sec_up/

runipy -o prepare_data.ipynb

runipy -o build_gradientboosting.ipynb
runipy -o build_gradientboosting2.ipynb

runipy -o evaluate_system.ipynb

