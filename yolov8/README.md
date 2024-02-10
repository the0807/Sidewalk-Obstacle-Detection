# Sidewalk-Obstacle-Detection
sidewalk obstacle detection using YOLOv8

## Dataset
<div style="display:flex; flex-direction:row;">
  • AI Hub
</div>
<div style="display:flex; flex-direction:row;">
  &nbsp&nbsp 인도보행 영상 (bbox - 약 30,000장)
</div>
<br>
<div style="display:flex; flex-direction:row;">
Change annotation format to match YOLOv8 using xmltotxt
</div>

## Environment
<div style="display:flex; flex-direction:row;">
  GPU: Nvidia Quadro RTX 5000
</div>
<div style="display:flex; flex-direction:row;">
  Ubuntu 20.04
</div>
<div style="display:flex; flex-direction:row;">
  CUDA 11.6
</div>
<div style="display:flex; flex-direction:row;">
  PyTorch 1.13.1
</div>

## Train
<div style="display:flex; flex-direction:row;">
  epoch: 500
</div>
<div style="display:flex; flex-direction:row;">
  batch: 32
</div>
<div style="display:flex; flex-direction:row;">
  use the default for others
</div>

## Result
![results](https://github.com/the0807/Sidewalk-Obstacle-Detection/assets/73097985/5ce80c1f-38bc-475f-8a24-21334fcb01b2)
![test1](https://github.com/the0807/Sidewalk-Obstacle-Detection/assets/73097985/65f696d6-8b42-4a75-8fe2-e5fcb837912e) | ![test2](https://github.com/the0807/Sidewalk-Obstacle-Detection/assets/73097985/2c1b2be1-698f-40cb-827d-6254e157683a)| ![test3](https://github.com/the0807/Sidewalk-Obstacle-Detection/assets/73097985/175f7094-304e-47ce-afcd-25e66c64dc18)
|:---:|:---:|:---:|
