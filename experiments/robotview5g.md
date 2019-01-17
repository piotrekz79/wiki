<!-- TITLE: Robotview 5G -->
<!-- SUBTITLE: Using the RobotView5G QoE VNF -->
![5 Ginfire Logo 3](/uploads/5-ginfire-logo-3.png "5 Ginfire Logo 3")
# Description of the QoE VNF
In the experiment for the QoE assessment, we have used a special tool with No-Reference QoE algorithms. No-Reference (NR) metrics evaluate the quality of digital images without access to non-distorted reference images or any features representing the reference images. Instead of making comparisons, No-Reference techniques try to identify or predict impairments such as blockiness or jerkiness by analysing the characteristics of the underlying network transport and/or by analysing the video itself. The advantage of NR models is their applicability on the client side. Moreover, this technique can be used in real-time. Most of the existing NR models are of the distortion-specific kind and assume that the assessed image is afflicted by a particular kind of distortion. Other approaches use natural scene statistics or employ learning-based classification methods.
The QoE tool can be used as a separate processing module that can provide QoE metrics to video streams provided over the network. We have created a separate QoE tool VNF and added it to the 5GinFIRE catalogue, enabling other experimenters to gather QoE data of videos in real-time. The QoE tool VNF can be run on MEC nodes and can receive video using various streaming protocols (RTP, RTSP, …). The QoE tool VNF performs real-time video analysis and writes the results to a log file. The QoE tool has the possibility to be run with a user interface however for the VNF version we have prepared it in the headless mode.

![Robotview Pic 1](/uploads/robot-view-5-g/robotview-pic-1.jpg "Robotview Pic 1")
Two instances of the QoE tool graphical user interface, showing difference of quality, as indicated by the measured parameters' values.

### QoE parameters
Measurements of the quality of experience has been done using a no reference software module. The module calculated values of some low level video metrics. These were presented individually, but also an aggregated value of objective QoE has been measured, based on these individual metrics.
**Spatial activity**
This metric resembles the amount of spatial details in the image. Too strong compression would result in diminished value of this parameter.
**Temporal activity**
This metric corresponds with an amount of temporal activity in the video. The higher the values, the bigger the change from frame to frame.
**Blockiness**
This value detects distortions characteristic to video compression algorithms operating on (macro)blocks. When such an algorithm is allocated too little bandwidth, the produced video characterizes with blocking artefacts this metric is intended to detect. The lower the value, the stronger the effect.
**Blockloss**
This parameter indicates the amount of outdated content present in the picture in the form of distinct blocks. These can appear when data loss is present.
**Noise**
This metric detects noise, randomly modifying single pixels. Such noise is characteristic to digital video cameras working in dark conditions.
**Slicing**
Slicing effect relates to distinct horizontal stripes of within the video. It can appear when parts of the video are encoded by separate threads, especially in low bit rate or packet loss situations. This metric detects such impairments.

# Connecting to the VNF machine
1.	Connect to the VPN where the VNF machine is deployed
2.	Connect to the jump machine over SSH.
3.	From the jump machine’s shell, connect to the VNF machine over SSH. Current credentials are as follows:
	user name: ubuntu
	password: 5ginfire

# Running an experiment
The VNF machine already contains the compiled software. If there is a need to recompile the code, there are scripts provided for that as well:
1.	On the VNF machine’s shell, move to the running scripts’ directory:
cd /home/ubuntu/qoe-tool/application/scripts
2.	In order to run a measurement of 30s period of a single video file, call
./run-vnf.sh
The script requires the following parameters:
* RTSP-URL - an URL of an RTSP stream to measure.
* frame width
* frame height
* IP address for live status output - IP address where a netcat server is listening to the progress of the experiment. This server is required running in order to have the experiment run correctly. An exemplary call starting such a server on port 54340 is as follows:
nc -kl 54340
If live progress monitoring is not required, the server can be run as a detached shell application on the VNF machine itself and the address can be supplied as 127.0.0.1
port for live status output - port on which the netcat server is listening to progress of the experiment.
experiment id - an extra string that is inserted into the result file names
extra initial delay in seconds before the measurement starts
An exemplary call to run a single experiment is as follows:
./run-vnf.sh rtsp://10.68.32.6:8554/ 1920 1080 10.68.32.6 54340 test-experiment 1
3.	In the same directory, there are also other scripts:
* run-vnf-locally.sh - this script allows to run a single preconfigured experiment. Please examine the file content for details.
* run-experiment-series-1080.sh - this script allows to run a series of experiment. It assumes that several video streams are served consecutively. Please examine the file content for details.
The application has been tested with RTSP H.264 video streams. An exemplary call to serve such a stream, from an H.264 video file, with command-line vlc application, is as follows:
cvlc "video-file-name.mkv" :sout=#rtp{sdp=rtsp://:8554/} :sout-all :sout-keep

