#  IEat (Interacting Enhancers and Targets)
A tool that combines Gro-Seq and Chip-Seq data to predict enhancer and promoter interactions. We present one workflow derivative of [TargetFinder](https://github.com/shwhalen/targetfinder) and [ChromHMM](http://compbio.mit.edu/ChromHMM/) as a searchable example.

### Problem
Biologists are manually searching for enhancer promoter interacting pairs because it is difficult to build a predictor specific to each experimental system.

### Approach
![Minimal Workflow](https://raw.githubusercontent.com/NCBI-Hackathons/enhancertargets/master/img/MinWorkflow.png)

### Use cases
 - Experimentalists with data that is similar to [MCF-7 cell line](https://en.wikipedia.org/wiki/MCF-7) can directly query our model [Here](https://www.google.com)
- Experimentalists looking to build their own model but who cannot meet provide the data demanded by other methods can follow our minimalist approach

### Installation
```
git clone https://github.com/NCBI-Hackathons/enhancertargets.git
cd enhancertargets 
docker build . -t enhancer
docker run -it -v `pwd`:/data enhancer
```
### Data Preparation
Run `./generate_region.sh`

### Machine Learning

http://scikit-learn.org/stable/tutorial/statistical_inference/supervised_learning.html
