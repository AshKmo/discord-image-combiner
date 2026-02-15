# discord image combiner
This Python script generates an image that looks like one image when in Discord's light theme and another when in dark theme.

## how to use
```
pip install -r requirements.txt
python main.py light-theme-image.png dark-theme-image.png out.png
```

The images used as inputs must be of equal width and height, and each pixel must be either fully transparent or fully opaque. Colours will be ignored, since that is the point.
