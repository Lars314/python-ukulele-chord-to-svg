# The MIT License (MIT)
#
# Copyright (c) 2017 G. Völkl
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


# ------------------------------------------------------------------------------
# Originally written by gkvoelkl on GitHub:
# https://github.com/gkvoelkl/python-ukulele-chord-to-svg
#
# Modified by Lars314 to their personal preferences. List of changes:
#   - Added debug parameter to turn on print statements for debugging purposes
#   - Expanded diagram to include 5 frets instead of 4
#   - Added grey fretmarker circles on 5th, 7th, 10th, 12th, and 15th frets
#   - Added black box to mark the nut, as long as the starting fret is 1
#   - Lowered closed string markers 1px to center them between frets
#   - Shifted the fretboard 2px right to fix starting fret labels >=10
#   - Raised the chord name 2px so that letters like "j" don't overlap with
#     open string circles
# ------------------------------------------------------------------------------


class Chord:
    """

    """

    def __init__(self, name, frets, starting_fret=1, fingers="", subtexts="", debug=False):
        self.name = name
        self.starting_fret = starting_fret
        self.frets = frets
        self.fingers = fingers
        self.subtexts = subtexts
        self.debug = debug

    def to_svg(self):
        """

        :rtype: str
        """
        return """
        <svg width="84" height="154" viewBox="0 0 84 144" style="font-family: sans-serif; font-size: 11px;" 
           xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
        """ + self._to_svg() + "</svg>"

    def _to_svg(self):
        closed_string_visible = []
        open_string_visible = []
        fret_y = []
        finger = []
        subtext = []

        for i in range(4):
            if int(self.frets[i]) > 0:
                closed_string_visible.append("visible")
                open_string_visible.append("hidden")
            else:
                closed_string_visible.append("hidden")
                open_string_visible.append("visible")

            fret = int(self.frets[i])
            if self.starting_fret != 1:
                fret = fret - self.starting_fret + 1
            fret_y.append((fret - 1) * 20)
            if self.fingers != "":
                if self.fingers[i] != "_":
                    finger.append(self.fingers[i])
                else:
                    finger.append("")
            else:
                finger.append("")

            if self.subtexts != "":
                if self.subtexts[i] != "_":
                    subtext.append(self.subtexts[i])
                else:
                    subtext.append("")
            else:
                subtext.append("")

        if self.starting_fret != 1:
            starting_fret_visible = "visible"
            nut_visible = "hidden"
            offset_from_nut = 0
            
            # fretMarker5
            if self.starting_fret > 5:
                marker5_y_offset = 0
                marker5_visible = "hidden"
            else:
                marker5_y_offset = (6-self.starting_fret)*20 - 7
                marker5_visible = "visible"
                
            # fretMarker7
            if self.starting_fret > 7 or self.starting_fret < 3:
                marker7_y_offset = 0
                marker7_visible = "hidden"
            else:
                marker7_y_offset = (8-self.starting_fret)*20 - 7
                marker7_visible = "visible"
                
            # fretMarker10
            if self.starting_fret > 10 or self.starting_fret < 6:
                marker10_y_offset = 0
                marker10_visible = "hidden"
            else:
                marker10_y_offset = (11-self.starting_fret)*20 - 7
                marker10_visible = "visible"
                
            # fretMarker12
            if self.starting_fret > 12 or self.starting_fret < 8:
                marker12_y_offset = 0
                marker12_visible = "hidden"
            else:
                marker12_y_offset = (13-self.starting_fret)*20 - 7
                marker12_visible = "visible"
                
            # fretMarker15
            if self.starting_fret > 15 or self.starting_fret < 11:
                marker15_y_offset = 0
                marker15_visible = "hidden"
            else:
                marker15_y_offset = (16-self.starting_fret)*20 - 7
                marker15_visible = "visible"
            
        else:
            starting_fret_visible = "hidden"
            nut_visible = "visible"
            offset_from_nut = 10
            
            marker5_y_offset = 93
            marker5_visible = "visible"
            marker7_y_offset = 0
            marker7_visible = "hidden"
            marker10_y_offset = 0
            marker10_visible = "hidden"
            marker12_y_offset = 0
            marker12_visible = "hidden"
            marker15_y_offset = 0
            marker15_visible = "hidden"
            
        if self.debug:
            print("Marker 5 offset: {0}".format(marker5_y_offset))
            print("Marker 5 visible: {0}".format(marker5_visible))
            print("Marker 7 offset: {0}".format(marker7_y_offset))
            print("Marker 7 visible: {0}".format(marker7_visible))
            print("Marker 10 offset: {0}".format(marker10_y_offset))
            print("Marker 10 visible: {0}".format(marker10_visible))
            print("Marker 12 offset: {0}".format(marker12_y_offset))
            print("Marker 12 visible: {0}".format(marker12_visible))
            print("Marker 15 offset: {0}".format(marker15_y_offset))
            print("Marker 15 visible: {0}".format(marker15_visible))


        svg = """
      <text id="chordName" x="44" y="9" text-anchor="middle" style="font-size: 16px;">{name}</text>
      <text id="startingFret" x="0" y="40" style="font-size: 9px; visibility: {starting_fret_visible};">{starting_fret}</text>
      <g id="nut" transform="translate(11, 26)">
        <rect height="10" width="62" x="2" fill="black" style="visibility: {nut_visible};"></rect>
      </g>
      <g id="svgChord" transform="translate(11,24)">
        <g id="strings" transform="translate(2,{strings_y_offset})">
          <rect height="100" width="2" x="0" fill="black"></rect>
          <rect height="100" width="2" x="20" fill="black"></rect>
          <rect height="100" width="2" x="40" fill="black"></rect>
          <rect height="100" width="2" x="60" fill="black"></rect>
        </g>
        <g id="frets" transform="translate(2,{frets_y_offset})">
          <rect height="2" width="62" y="0" fill="black"></rect>
          <rect height="2" width="62" y="20" fill="black"></rect>
          <rect height="2" width="62" y="40" fill="black"></rect>
          <rect height="2" width="62" y="60" fill="black"></rect>
          <rect height="2" width="62" y="80" fill="black"></rect>
          <rect height="2" width="62" y="100" fill="black"></rect>
        </g>
        <g id="fretMarkers" transform="translate(2, {fretmarkers_y_offset})">
          <circle id="fret5Marker" cx="31" cy="{marker5_y_offset}" r="3" fill="grey" fill-opacity="0.6" style="visibility: {marker5_visible};"></circle>
          <circle id="fret7Marker" cx="31" cy="{marker7_y_offset}" r="3" fill="grey" fill-opacity="0.6" style="visibility: {marker7_visible};"></circle>
          <circle id="fret10Marker" cx="31" cy="{marker10_y_offset}" r="3" fill="grey" fill-opacity="0.6" style="visibility: {marker10_visible};"></circle>
          <circle id="fret12Marker1" cx="11" cy="{marker12_y_offset}" r="3" fill="grey" fill-opacity="0.6" style="visibility: {marker12_visible};"></circle>
          <circle id="fret12Marker2" cx="51" cy="{marker12_y_offset}" r="3" fill="grey" fill-opacity="0.6" style="visibility: {marker12_visible};"></circle>
          <circle id="fret15Marker" cx="31" cy="{marker15_y_offset}" r="3" fill="grey" fill-opacity="0.6" style="visibility: {marker15_visible};"></circle>
        </g>
        <g id="closedStrings" transform="translate(3,{closedStrings_y_offset})">
          <g id="closedString0" transform="translate(0,{fret_y[0]})" style="visibility: {closed_string_visible[0]};">
            <circle r="6"></circle>
            <text fill="white" id="finger0" y="4" text-anchor="middle" >{finger[0]}</text>
          </g>
          <g id="closedString1" transform="translate(20,{fret_y[1]})" style="visibility: {closed_string_visible[1]};">
            <circle r="6"></circle>
            <text fill="white" id="finger1" y="4" text-anchor="middle">{finger[1]}</text>
          </g>
          <g id="closedString2" transform="translate(40,{fret_y[2]})" style="visibility: {closed_string_visible[2]};">
            <circle r="6"></circle>
            <text fill="white" id="finger2" y="4" text-anchor="middle">{finger[2]}</text>
          </g>
          <g id="closedString3" transform="translate(60,{fret_y[3]})" style="visibility: {closed_string_visible[3]};">
            <circle r="6"></circle>
            <text fill="white" id="finger3" y="4" text-anchor="middle">{finger[3]}</text>
          </g>
        </g>
        <g id="openStrings" transform="translate(3,-5)">
          <circle id="openString0" cx="0" r="4" fill="none" stroke="black" stroke-width="1" style="visibility: {open_string_visible[0]};"></circle>
          <circle id="openString1" cx="20" r="4" fill="none" stroke="black" stroke-width="1" style="visibility: {open_string_visible[1]};"></circle>
          <circle id="openString2" cx="40" r="4" fill="none" stroke="black" stroke-width="1" style="visibility: {open_string_visible[2]};"></circle>
          <circle id="openString3" cx="60" r="4" fill="none" stroke="black" stroke-width="1" style="visibility: {open_string_visible[3]};"></circle>
        </g>
        <g id="subText" transform="translate(3,98)">
          <text id="subText0" x="0" text-anchor="middle">{subtext[0]}</text>
          <text id="subText1" x="20" text-anchor="middle">{subtext[1]}</text>
          <text id="subText2" x="40" text-anchor="middle">{subtext[2]}</text>
          <text id="subText3" x="60" text-anchor="middle">{subtext[3]}</text>
        </g>
      </g>
        """.format(name=self.name,
                   open_string_visible=open_string_visible,
                   starting_fret_visible=starting_fret_visible,
                   starting_fret=self.starting_fret,
                   nut_visible=nut_visible,
                   strings_y_offset=2+offset_from_nut,
                   frets_y_offset=2+offset_from_nut,
                   fretmarkers_y_offset=offset_from_nut,
                   marker5_y_offset=marker5_y_offset,
                   marker5_visible=marker5_visible,
                   marker7_y_offset=marker7_y_offset,
                   marker7_visible=marker7_visible,
                   marker10_y_offset=marker10_y_offset,
                   marker10_visible=marker10_visible,
                   marker12_y_offset=marker12_y_offset,
                   marker12_visible=marker12_visible,
                   marker15_y_offset=marker15_y_offset,
                   marker15_visible=marker15_visible,
                   closedStrings_y_offset=13+offset_from_nut,
                   closed_string_visible=closed_string_visible,
                   fret_y=fret_y,
                   finger=finger, subtext=subtext)
        return svg


class Chords:
    def __init__(self, chordlist):
        self._chordlist = chordlist

    def to_svg(self):
        result = """<svg width="100%" height="100%" style="font-family: sans-serif; font-size: 11px;" 
                 xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
        """
        for i in range(len(self._chordlist)):
            result += '<g transform="translate({},24)">'.format(i * 80)
            result += self._chordlist[i]._to_svg()
            result += '</g>'
        result += "</svg>"
        return result


def write_chord(filename, name, frets, starting_fret=1, fingers="", subtexts=""):
    """
    Convenient way to write an svg file
    :param filename: name of svg file
    :param name: chord name
    :param frets: fret positions
    :param starting_fret: number of starting fret
    :param fingers: position of fingers
    :param subtexts: text under the chord
    :return:
    """

    with open(filename, 'w') as f:
        f.write(Chord(name, frets, starting_fret, fingers, subtexts).to_svg())


#write_chord('pic/dm7.svg','Dm7','7988',fingers='1423',starting_fret=6)

