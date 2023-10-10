#(1) AINP99起動
!apt update
!apt -y install python3.10
!curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10
!python3.10 -m pip install torch==1.13.1+cu116 torchvision==0.14.1+cu116 torchaudio==0.13.1 --extra-index-url https://download.pytorch.org/whl/cu116 -U
!python3.10 -m pip install -q xformers==0.0.16
!python3.10 -m pip install -q triton==2.0.0
%cd /notebooks/stable-diffusion-webui
!python3.10 launch.py --enable-insecure-extension-access --share --gradio-queue

#(1) AUTO　INPインストール
%cd /notebooks
!rm -rf stable-diffusion-webui
!git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui

#(2) デルモのインストール（ここにインストールしたいデルモ追加）
%cd /notebooks/stable-diffusion-webui/models/Stable-diffusion
!wget -nc https://civitai.com/api/download/models/16859 -O BulueberryMix-1.0.safetensors
!wget -nc https://civitai.com/api/download/models/11745 -O Chilloutmix-Ni-pruned-fp32-fix.safetensors
!wget -nc https://civitai.com/api/download/models/63786 -O braBeautifulRealistic_brav5.safetensors
!wget -nc https://civitai.com/api/download/models/60643 -O XXMix_9realistic.safetensors
!wget -nc https://huggingface.co/jtamph/magicmixRealistic/resolve/main/majicmixRealistic_v4.safetensors -O majicmixRealistic_v4.safetensors
!wget -nc https://huggingface.co/sazyou-roukaku/chilled_remix/resolve/main/chilled_remix_v1vae.safetensors -O chilled_remix_v1vae.safetensors

%cd /notebooks/stable-diffusion-webui/embeddings
!wget -nc https://civitai.com/api/download/models/60938 -O negative_hand-neg.pt
!wget -nc https://huggingface.co/datasets/Nerfgun3/bad_prompt/resolve/main/bad_prompt_version2.pt -O bad_prompt.pt

%cd /notebooks/stable-diffusion-webui/models/Lora
!wget -nc https://civitai.com/api/download/models/52340 -O GirlfriendMix2.safetensors

%cd /notebooks/stable-diffusion-webui/models/ControlNet
!wget -nc https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11p_sd15_canny_fp16.safetensors -O control_v11p_sd15_canny_fp16.safetensors
!wget -nc https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11p_sd15_openpose_fp16.safetensors -O control_v11p_sd15_openpose_fp16.safetensors


#(４) AUTO INPアップデート（アップデートが必要な時のみ実行）
%cd /notebooks/stable-diffusion-webui
!git checkout master
!git pull
