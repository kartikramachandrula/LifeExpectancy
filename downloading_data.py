import kagglehub

def download_datasets():
    datasets = [
        "mjshri23/life-expectancy-and-socio-economic-world-bank",
        "mahdiehhajian/life-expectancy-around-the-world",
        "iamsouravbanerjee/life-expectancy-at-birth-across-the-globe"
    ]
    
    paths = []
    for dataset in datasets:
        path = kagglehub.dataset_download(dataset)
        paths.append(path)
        print("Path to dataset files:", path)

    return paths