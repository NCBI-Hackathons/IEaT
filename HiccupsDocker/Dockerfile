FROM biocontainers/biocontainers:latest

# Metadata
LABEL base.image="biocontainers:latest"
LABEL version="1"
LABEL software="NCBI Hackathon Base Image"
LABEL software.version="0.0.1"
LABEL description="Base image for NCBI Hackathons Projects"
LABEL website="https://github.com/NCBI-Hackathons/HackathonDockerImages/Docker/base"
LABEL documentation="https://github.com/NCBI-Hackathons/HackathonBaseImages/blob/master/Docker/README.md"
LABEL license="https://github.com/NCBI-Hackathons/HackathonDockerImages/LICENSE"
LABEL tags="NCBI, Hackathon"

# Maintainer
MAINTAINER Roberto Vera Alvarez <r78v10a07@gmail.com>

USER root

RUN apt-get update && \
    apt-get install -y \
        libncurses5-dev \
        libncursesw5-dev \
		libbz2-dev \
		lzma lzma-dev liblzma-dev \
		libcurl4-gnutls-dev \
		python3 python3-pip \
		nodejs npm \
		liblwp-protocol-https-perl \
		r-base r-base-dev && \
    apt-get clean && \
    apt-get purge && \
    conda install bedtools=2.25.0 && \
	pip3 install numpy pysam scipy pandas==0.17.1 scikit-learn==0.17 numexpr==2.4.6 && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


# Update the repository sources list
# Install base packages: java, git, wget
RUN apt-get update && apt-get install -y \
    default-jdk \
    gawk \
    gcc \
    git \
    libz-dev \
    locales \
    make \
    unzip \
    bzip2 \
    libbz2-dev \	
&& rm -rf /var/lib/apt/lists/*

# GAWK has the 'and' function, needed for chimeric_blacklist
RUN echo 'alias awk=gawk' >> ~/.bashrc

# Need to be sure we have this for stats
RUN locale-gen en_US.UTF-8

WORKDIR /opt/

# Install BWA
ADD https://github.com/lh3/bwa/archive/v0.7.17.zip .
RUN unzip v0.7.17.zip 
RUN cd bwa-0.7.17/ && make
RUN ln -s bwa-0.7.17/bwa bwa

# Install Samtools
ADD https://github.com/samtools/samtools/releases/download/1.6/samtools-1.6.tar.bz2 .
RUN bunzip2 samtools-1.6.tar.bz2 
RUN tar xf samtools-1.6.tar 
RUN cd samtools-1.6 && ./configure --without-curses --disable-bz2 --disable-lzma && make && make install

# Install Juicer
ADD https://github.com/theaidenlab/juicer/archive/1.6.2.zip .
RUN unzip 1.6.2.zip
RUN cd juicer-1.6.2 && chmod +x CPU/* CPU/common/* 

# Install Juicer tools
ADD http://hicfiles.tc4ga.com.s3.amazonaws.com/public/juicer/juicer_tools.1.7.6_jcuda.0.8.jar /opt/juicer-1.6.2/CPU/common
RUN ln -s /opt/juicer-1.6.2/CPU/common/juicer_tools.1.7.6_jcuda.0.8.jar /opt/juicer-1.6.2/CPU/common/juicer_tools.jar
RUN ln -s juicer-1.6.2/CPU scripts

# Version number contained in image
# ADD VERSION .

# For sorting, LC_ALL is C
ENV LC_ALL C
ENV PATH=/opt:/opt/scripts:/opt/scripts/common:$PATH


USER biodocker

WORKDIR /data/

