#  IEaT (Interacting Enhancers and Targets)

<img src="https://orig00.deviantart.net/605a/f/2012/333/0/c/panda_eating_watermelon_by_audiessy-d5ko3ut.png" alt="I EaT" width="200">

A docker for running [JEME](https://github.com/yiplabcuhk/JEME) (by Yip Lab) analysis.

Some biologists manually searching for enhancer promoter interacting pairs because it is [difficult](https://github.com/NCBI-Hackathons/enhancertargets/blob/master/TroubleShooting.md) to [build a predictor](https://docs.google.com/presentation/d/1smCxGFrgfo06YGImBy1E2dL7s6jyneLsxz3GwmQHQYE/edit?usp=sharing) specific to each experimental system. Some tools like JEME exist, but they are opaque. We will explore JEME methods with docker.

### Gather Data
Test JEME with their [published data](https://www.dropbox.com/sh/wjyqyog3p5d33kh/AABUY-OSsV8CQD4TFPRGzp8Na?dl=0)
(Dropbox has data transfer limits, and wget does not cooperate)

### Setup
- First, build JEME file structure.
```
git clone https://github.com/yiplabcuhk/JEME
cd JEME/JEME_code/Roadmap/1_first_step_modeling/1MB_intervals
###   Move each data folders to /1MB_intervals. ###
```

- Next, build the JEME docker.
```
git clone https://github.com/NCBI-Hackathons/IEaT.git
cd IEaT/JemaWekaDocker
docker build . -t jeme
```
- Navigate to the data and run docker.
```
cd ../../JEME/JEME_code/Roadmap/1_first_step_modeling/1MB_intervals
docker run -it -v `pwd`:/data jeme
```
- Run JEME, one script at a time
```
./1_batch_generate.sh
```


