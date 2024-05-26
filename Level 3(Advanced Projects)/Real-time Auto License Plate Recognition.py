Object Detection on Live Camera Stream (Jetson)


Features:
*Compatible with various pre-trained models: Supports a range of models like ssd-mobilenet-v2 (default), ssd_resnet50_v1.5, etc. (refer to JetPack documentation for available options).
*Customizable detection overlay: Choose to display bounding boxes (box), class labels (labels), confidence scores (conf), or a combination of these.
*Threshold control: Set a minimum confidence threshold (--threshold) to filter out low-confidence detections.
*Flexible input and output: Accepts input from different sources (e.g., webcam, video file) using URIs and outputs to various destinations (e.g., display, video recording).


Requirements:
*NVIDIA Jetson device
*JetPack SDK installed (https://developer.nvidia.com/embedded/jetpack)
*Python 3.x


Command Line Arguments:
*'input_URI: URI of the input stream (e.g., camera, video file)
*'output_URI: URI of the output stream (e.g., display, file)
*'--network: Pre-trained model to load (default: ssd-mobilenet-v2)
*'--overlay: Detection overlay flags (default: box,labels,conf)
*'--threshold: Minimum detection threshold (default: 0.5)


Troubleshooting:
*Ensure your Jetson device has the latest JetPack installed.
*Check the Jetson Inference documentation for additional setup and configuration help.
*Verify that your input URI and output URI are correctly specified and accessible.




import jetson.inference
import jetson.utils
import argparse
import sys
# Parse the command line
parser = argparse.ArgumentParser(description="Locate objects in a live camera stream using an object detection DNN.", 
                                 formatter_class=argparse.RawTextHelpFormatter, 
                                 epilog=jetson.inference.detectNet.Usage() +
                                        jetson.utils.videoSource.Usage() +
                                        jetson.utils.videoOutput.Usage() +
                                        jetson.utils.logUsage())
parser.add_argument("input_URI", type=str, default="", nargs='?', help="URI of the input stream")
parser.add_argument("output_URI", type=str, default="", nargs='?', help="URI of the output stream")
parser.add_argument("--network", type=str, default="ssd-mobilenet-v2", help="Pre-trained model to load (see below for options)")
parser.add_argument("--overlay", type=str, default="box,labels,conf", 
                    help="Detection overlay flags (e.g. --overlay=box,labels,conf)\nValid combinations are: 'box', 'labels', 'conf', 'none'")
parser.add_argument("--threshold", type=float, default=0.5, help="Minimum detection threshold to use")

is_headless = ["--headless"] if sys.argv[0].find('console.py') != -1 else [""]

try:
    opt = parser.parse_args()
except:
    parser.print_help()
    sys.exit(0)

# Load the object detection network
net = jetson.inference.detectNet(opt.network, sys.argv, opt.threshold)

# Create video sources & outputs
input = jetson.utils.videoSource(opt.input_URI, argv=sys.argv)
output = jetson.utils.videoOutput(opt.output_URI, argv=sys.argv + is_headless)

# Process frames until the user exits
while True:
    # Capture the next image
    img = input.Capture()

    # Detect objects in the image (with overlay)
    detections = net.Detect(img, overlay=opt.overlay)

    # Print the detections
    print("detected {:d} objects in image".format(len(detections)))

    for detection in detections:
        print(detection)

    # Render the image
    output.Render(img)

    # Update the title bar
    output.SetStatus("{:s} | Network {:.0f} FPS".format(opt.network, net.GetNetworkFPS()))

    # Print out performance info
    net.PrintProfilerTimes()

  # Exit on input/output EOS
    if not input.IsStreaming() or not output.IsStreaming():
    break
