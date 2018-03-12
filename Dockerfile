# Base Image
FROM ncbihackathon/ncbihackathonbase

# Metadata
LABEL base.image="bioconductor:latest"
LABEL version="1"
LABEL software="NCBI Hackathon Image with Bioconductor and Extra R packages"
LABEL software.version="0.0.1"
LABEL description="NCBI Hackathons Image with Bioconductor and Extra R packages"

RUN conda install bedtools=2.25.0

