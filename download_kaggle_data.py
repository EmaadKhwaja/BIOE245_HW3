#!/usr/bin/env python
import os
from kaggle.api.kaggle_api_extended import KaggleApi

def main():
    api = KaggleApi()
    api.authenticate()

    # Set the path for the data download
    path = os.path.join(os.getcwd(), 'lgg-mri-segmentation')
    os.makedirs(path, exist_ok=True)

    # Download the dataset
    api.dataset_download_files('mateuszbuda/lgg-mri-segmentation', path=path, unzip=True)

if __name__ == '__main__':
    main()
