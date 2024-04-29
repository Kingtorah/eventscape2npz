# eventscape2npz
Processing eventscape simulation dataset integrated into npz format

Eventscape is a simulated dataset containing semantic segmentation, depth map, original RGB image event data and corresponding timestamps.
The dataset format is:
Semantic label: png;
Depth map: npy;
rgb: png;
Event: npz(x,y,t,p);
and their respective frame formats

## EventScape

This work uses the EventScape dataset which can be downloaded here:

* [Training Set (71 Gb)](http://rpg.ifi.uzh.ch/data/RAM_Net/dataset/Town01-03_train.zip)
* [Validation Set (12 Gb)](http://rpg.ifi.uzh.ch/data/RAM_Net/dataset/Town05_val.zip)
* [Test Set (14 Gb)](http://rpg.ifi.uzh.ch/data/RAM_Net/dataset/Town05_test.zip)


<p align="center">
    <img src="doc/event_scape_s01_preview_w.gif" alt="Video to Events" width="800"/>
</p>


