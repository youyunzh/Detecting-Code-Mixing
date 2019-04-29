## Code-mixing Detection Using Acoustic Features
Author: Youyun Zhang & Xinyi Wu

Code-mixing is an interesting and underdeveloped field due to the limitation of CM data and its variousness in phenomenons. There are usually three types of models to detect a code-mixing speech: acoustic models, pronunciation models, and language models.
Most of the code-mixing detection model are build on language models (Vu & Schultz 2014, Yilmaz & Leeuwen 2018, see `doc/Final Report.pdf` for bib). We are interested in finding out whether using the acoustic features of an utterance can predict if code-mixing is happening.

Corpus: [Eppler Corpus (1999)](https://biling.talkbank.org/access/Eppler.html)

Segmentation Tool: [The Munich Automatic Segmentation System(MAUS)](
https://www.phonetik.uni-muenchen.de/forschung/Verbmobil/VM14.7eng.html
)

Required packages: `pyAudioAnalysis`, `contextlib`, `wave` 
To run: scripts/run.sh
Results and Analysis: doc/Final Report.pdf
