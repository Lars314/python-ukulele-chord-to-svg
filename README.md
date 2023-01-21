
# Creating Ukulele Chord Diagrams in SVG with Python

With the Python modul __uchord__ you can create ukulele chord diagrams in SVG format.   

This project was originally made by gkvoelkl, you can find their version here: https://github.com/gkvoelkl/python-ukulele-chord-to-svg.

This version includes minor changes to match my personal preferences. These changes are: 
   - Added debug parameter to turn on print statements for debugging purposes
   - Expanded diagram to include 5 frets instead of 4
   - Added grey fretmarker circles on 5th, 7th, 10th, 12th, and 15th frets
   - Added black box to mark the nut, as long as the starting fret is 1
   - Lowered closed string markers 1px to center them between frets
   - Shifted the fretboard 2px right to fix starting fret labels >=10
   - Raised the chord name 2px so that letters like "j" don't overlap with
     open string circles

```python
import uchord

uchord.write_chord('c.svg','C','0003')
```

<img src="pic/c.svg" align="left"><br><br><br><br><br>

If you like it, use it. If you have some suggestions, tell me (gkvoelkl@nelson-games.de).

# Thanks

Special thanks to the project https://github.com/gkvoelkl/python-ukulele-chord-to-svg where I learned much about 
SVG and chord diagrams. I recycled all of the svg commands.
