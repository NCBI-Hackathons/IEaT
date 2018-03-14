#  IEat (Interacting Enhancers and Targets)
We present a catalog of errors incurred while exploring [TargetFinder](https://github.com/shwhalen/targetfinder) (by Pollard Lab) and JEME

Biologists are manually searching for enhancer promoter interacting pairs because it is [difficult]() to build a predictor specific to each experimental system. 


### Installation
```
git clone https://github.com/NCBI-Hackathons/enhancertargets.git
cd enhancertargets
docker build . -t jeme
docker run -it -v `pwd`:/data jeme
```
