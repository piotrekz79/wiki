<!-- TITLE: Ehealth 5G Experiment example-->
<!-- SUBTITLE: Ehealth 5G Experiment example -->

# Ehealth 5G Experiment example

In our example scenario we assume that some medical work with eHealth devices is taking place and we want to process their video streams and save as video files. We use Edge Cloud to collect high resoultion video stream and process it before uploading to Core Cloud where it is written to a file and additional information about the video is collected.

![Detector Scheme](/uploads/ehealth/detector-scheme.png "Detector Scheme")

## Components description

## Video resizer - detector_edge01_vnfd
This VNF contains ffmpeg and ffserver software.
It is configured to pull video stream, transcode, resize and restream it.

## Scene detect - detector_edge02_vnfd
This VNF contains simple python script based on OpenCV.
Application functionality:
- pulling video frames from video resizer
- detecting scene change in video by comparing the colors between each two frames
- serving frames together with detection information

## Video and metadata archive - detector_core_vnfd
The detector_core VNF contains python script used to receive frames with metadata and save them to files.

## Experiment - detector_example_nsd
This NSD consist of three VNFs described above.

# Recreating the experiment.
0. Request setup of selected eHealth device ([our equipment](https://5ginfire.eu/ehealth/)) or video server with already recorded video.
1. Request deployment of detector_example_nsd from 5GinFire portal, place edge VNFs in eHealth5G Tesbed edge and core VNF in eHealth5G Testbed core in
frastructures.
2. After successful deployment, run start_edge01.sh [video stream URL] in detector_edge01 VNF, then start_edge02.sh [edge01 ip address] in detector_edge02 VNF and finally start_core.sh [edge02 ip address] in detector_core VNF.
3. Files video-[date].avi and video-[date].metadata will be created in detector_core VNF.


