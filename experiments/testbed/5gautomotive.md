<!-- TITLE: IT-Av Automotive experiment example: video-based assisted driving -->
<!-- SUBTITLE: A quick summary of IT-Av Automotive experiment example: video-based assisted driving -->

# Overview
The objective of the assisted overtaking is to gather all needed information in real-time for a driver to make a decision of overtaking or not the front vehicle, while the visibility of the road from the vehicle is not sufficient to take a decision. Important information can be used to take the decision, such as: video images from the road ahead. However, to 

The concrete scenario for video-camera-based assisted driving is presented in Figure X. Each vehicle contains an On Board Unit (OBU) that provides the communication between the vehicle and the infrastructure. The OBU also connects to an Android device, smartphone, through WiFi, providing visual information for the driver. 

Both rear and front vehicles may belong to different brands and have no agreement between them, both in terms of communication (vehicle to vehicle) and in terms of joint services. This means that the transmission of the video streaming from the camera in the front vehicle to the visual screen in the rear vehicle may need a 3rd party agreement to agree on the service to be established between the vehicles. Moreover, the video quality to be chosen in the camera will depend on the capabilities of the video screen. Therefore, a video transcoding system may be needed to adapt the video capabilities between both vehicles.

## System architecture
![Automotive](/uploads/automotive/automotive.png "Automotive"){.align-center}
# VNF description