# Enhancertargets
A tool that combines Gro-Seq and Chip-Seq data to predict enhancer and promoter interactions. We present one workflow derivative of [TargetFinder](https://github.com/shwhalen/targetfinder) as a searchable example.

### Problem
Biologists are manually searching for enhancer promoter interacting pairs because it is difficult to build a predictor specific to each experimental biology.

### Approach


### Use cases
 - Experimentalists with data that is similar to [MCF-7 cell line](https://en.wikipedia.org/wiki/MCF-7) can directly query our model [Here](https://www.google.com)
- Experimentalists looking to build their own model but who cannot meet provide the data demanded by other methods can follow our minimalist approach

### Installation
1. Install Docker
2. docker run image
3. Run python generate_enhancer.py
4. Train

### HackathonBaseImages
Docker and Server Images for Hackathons and Hackathon Products

``
git clone https://github.com/NCBI-Hackathons/enhancertargets.git
cd enhancertargets
docker build . -t enhancer
docker run -it -v `pwd`:/data enhancer
``

