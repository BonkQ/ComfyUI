from beam import task_queue, Output, Image, env, Volume
import os
import sys
import requests

if env.is_remote():
    import folder_paths

    sys.path.append(os.getcwd())
    import main



# Import functions or execute code from workflow_api.py
# Step 1: Define environment setup and model loading
@task_queue(
    name="ComfyUI",
    cpu=4,
    memory="24Gi",
    gpu="RTX4090",
    image=Image(
        python_version="python3.10",
        python_packages="requirements.txt",
        # commands=["pip3 install opencv-python"],
    ),
    volumes=[Volume(name="model-weights", mount_path="./model-weights")],
    # keep_warm_seconds=0,
    # on_start=upload_models,
)
def run_workflow(**inputs):
    main()