# Base Image
FROM ncbihackathon/ncbihackathonbase

# Metadata
LABEL base.image="bioconductor:latest"
LABEL version="1"
LABEL software="NCBI Hackathon Image with Bioconductor and Extra R packages"
LABEL software.version="0.0.1"
LABEL description="NCBI Hackathons Image with Bioconductor and Extra R packages"

USER root

RUN conda install bedtools=2.25.0
RUN pip3 install panda>=0.17.1 scikit-learn>=0.17 numexpr>=2.4.6
# RUN rm -f /usr/bin/python 
# RUN conda install python=3.5
# RUN ln -s /usr/bin/python /usr/bin/python3



