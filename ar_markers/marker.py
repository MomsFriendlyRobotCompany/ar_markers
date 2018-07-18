from __future__ import print_function
try:
    import cv2
except ImportError:
    raise Exception('Error: OpenCv is not installed')

from numpy import mean, binary_repr, zeros
from numpy.random import randint
# from scipy.ndimage import zoom  # get rid of this! - replaced w/ cv2.Resize

from ar_markers.coding import encode, HAMMINGCODE_MARKER_POSITIONS

MARKER_SIZE = 7


class HammingMarker(object):
    def __init__(self, id, contours=None):
        self.id = id
        self.contours = contours

    def __repr__(self):
        return '<Marker id={} center={}>'.format(self.id, self.center)

    @property
    def center(self):
        if self.contours is None:
            return None
        center_array = mean(self.contours, axis=0).flatten()
        return (int(center_array[0]), int(center_array[1]))

    def generate_image(self):
        img = zeros((MARKER_SIZE, MARKER_SIZE))
        img[1, 1] = 255  # set the orientation marker
        for index, val in enumerate(self.hamming_code):
            coords = HAMMINGCODE_MARKER_POSITIONS[index]
            if val == '1':
                val = 255
            img[coords[0], coords[1]] = int(val)
        # return zoom(img, zoom=50, order=0)
        height, width = img.shape[:2]
        res = cv2.resize(img, (50*width, 50*height), interpolation=cv2.INTER_NEAREST)
        return res

    def draw_contour(self, img, color=(0, 255, 0), linewidth=5):
        cv2.drawContours(img, [self.contours], -1, color, linewidth)

    def highlite_marker(self, img, contour_color=(0, 255, 0), text_color=(255, 0, 0), linewidth=5, text_thickness=2):
        """
        This draws a bounding box around the marker on the image. NOTE: it returns
        a BGR image so the highlite is in color.

        Input:
          img: image with detected marker
          contour_color: bounding box color, default is Green (0,255,0)
          text_color: text color, default is Blue (255,0,0)
          linewidth: thickness of bonding box line
          text_thickness: thickness of marker number text

        Output:
          A color image with the marker drawn on it
        """
        # this is a grayscale, so make it a color image
        if len(img.shape) == 2:
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        self.draw_contour(img, color=contour_color, linewidth=linewidth)
        cv2.putText(img, str(self.id), self.center, cv2.FONT_HERSHEY_SIMPLEX, text_thickness, text_color)
        return img

    @classmethod
    def generate(cls):
        return HammingMarker(id=randint(4096))

    @property
    def id_as_binary(self):
        return binary_repr(self.id, width=12)

    @property
    def hamming_code(self):
        return encode(self.id_as_binary)
