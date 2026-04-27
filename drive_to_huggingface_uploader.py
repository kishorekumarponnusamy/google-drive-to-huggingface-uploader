# =========================
# Mount Google Drive
# =========================

from google.colab import drive
drive.mount('/content/drive')


# =========================
# Install and import packages
# =========================

!pip install huggingface_hub

from huggingface_hub import login, HfApi, upload_file
import os


# =========================
# Login to Hugging Face
# =========================

login()


# =========================
# Hugging Face repository settings
# =========================

username = "your_huggingface_username"
repo_name = "your_model_repository_name"
repo_id = f"{username}/{repo_name}"

private_repo = True
repo_type = "model"


# =========================
# Create Hugging Face repository
# =========================

api = HfApi()

try:
    api.create_repo(
        repo_id=repo_id,
        private=private_repo,
        repo_type=repo_type,
        exist_ok=True
    )
    print(f"Repo ready: {repo_id}")
except Exception as e:
    print(f"Repo creation failed: {e}")


# =========================
# Upload model folder
# =========================

model_folder = "/content/drive/MyDrive/your_model_folder"
model_folder_name_in_repo = "model_name_in_repo"

if os.path.exists(model_folder):
    for file_name in os.listdir(model_folder):
        file_path = os.path.join(model_folder, file_name)

        if os.path.isfile(file_path):
            path_in_repo = f"{model_folder_name_in_repo}/{file_name}"

            try:
                print(f"Uploading: {path_in_repo}")
                upload_file(
                    path_or_fileobj=file_path,
                    path_in_repo=path_in_repo,
                    repo_id=repo_id,
                    repo_type=repo_type
                )
                print(f"Uploaded: {path_in_repo}")
            except Exception as e:
                print(f"Failed to upload {path_in_repo}: {e}")
else:
    print(f"Model folder not found: {model_folder}")


# =========================
# Upload single model file
# =========================

model_file = "/content/drive/MyDrive/your_model_file.pt"
model_file_folder_in_repo = "model_name_in_repo"

if os.path.exists(model_file):
    file_name = os.path.basename(model_file)
    path_in_repo = f"{model_file_folder_in_repo}/{file_name}"

    try:
        print(f"Uploading: {path_in_repo}")
        upload_file(
            path_or_fileobj=model_file,
            path_in_repo=path_in_repo,
            repo_id=repo_id,
            repo_type=repo_type
        )
        print(f"Uploaded: {path_in_repo}")
    except Exception as e:
        print(f"Failed to upload {path_in_repo}: {e}")
else:
    print(f"Model file not found: {model_file}")
