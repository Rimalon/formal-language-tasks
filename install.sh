#!/bin/bash

conda --version
if [[ $? -ne 0 ]]; then
  wget -O conda_install.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
  bash conda_install.sh -b -p $HOME/miniconda
  source "$HOME/miniconda/etc/profile.d/conda.sh"
  conda env create -f environment.yml
  conda activate formal-language-env
fi
  conda env create -f environment.yml
  conda activate formal-language-env