import kagglehub

# Download latest version
path = kagglehub.dataset_download("shakilrana/brats-2023-adult-glioma")

print("Path to dataset files:", path)