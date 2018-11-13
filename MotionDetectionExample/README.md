This is a working motion detector example.

It works by capturing multiple frames to build a background model which
can be compared to the current frame.

If a large enough section of the current frame (defined in config) differs from the 
backgound model, we can assume there was motion in the room.

The example was edited to exclude dropbox upload upon detection.
