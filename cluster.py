from Pixel import Pixel

import math


def chunks(list_in, n):
    # For item i in a range that is a length of l,
    for i in range(0, len(list_in), n):
        # Create an index range for l of n items:
        yield list_in[i:i + n]


def calculate_convergence(pixel1, pixel2):
    return math.sqrt(pow(pixel1[0] - pixel2[0], 2) + pow(pixel1[1] - pixel2[1], 2) + pow(pixel1[2] - pixel2[2], 2))


class Cluster(Pixel):
    def __init__(self, position, color):
        super().__init__(position, color)
        self.pixels = list()
        self.copy_pixel = color
        self.old_pixel = self.pixel

    def __init__(self, pixel: Pixel):
        super().__init__(pixel.position, pixel.pixel)
        self.pixels = list()
        self.copy_pixel = pixel.pixel
        self.old_pixel = self.pixel

    def calculate_mediane(self, convergence_limit: float):
        idx = 1
        for index, pixel in enumerate(self.pixels):
            idx = index
            if index == 0:
                self.copy_pixel = pixel.pixel
                continue
            self.copy_pixel = (self.copy_pixel[0] + pixel.pixel[0], self.copy_pixel[1] + pixel.pixel[1], self.copy_pixel[2] + pixel.pixel[2])
        self.copy_pixel = (int(self.copy_pixel[0] / idx), int(self.copy_pixel[1] / idx), int(self.copy_pixel[2] / idx))
        end = False if calculate_convergence(self.copy_pixel, self.old_pixel) > convergence_limit else True
        print(calculate_convergence(self.copy_pixel, self.old_pixel))
        self.old_pixel = self.copy_pixel
        return end
