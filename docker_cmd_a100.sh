img="nvcr.io/nvidia/pytorch:23.01-py3"



sudo docker run --gpus all  --privileged=true   --workdir /git --name "chatglm"  -e DISPLAY --ipc=host -d --rm  -p 6327:4352  \
-v /localhome/local-vili/git/ChatGLM-6B:/git/ChatGLM-6B \
 -v /localhome/local-vili/git/datasets:/git/datasets \
 $img sleep infinity


sudo docker exec -it chatglm  /bin/bash


