from cluster import Cluster, calculate_convergence, chunks
from Pixel import Pixel

from PIL import Image
import random
import numpy as np

class Management:
    def __init__(self, file_image: str, nbr_cluster: int, nbr_convergence: float, display_state=False):
        """

        :param file_image:  path to the image
        :param nbr_cluster:  number of color in the new image
        :param nbr_convergence: the number of convergence between each cluster
        :param display_state: display state every x steps
        """

        self.file_image = file_image
        self.nbr_cluster = nbr_cluster
        self.nbr_convergence = nbr_convergence
        self.pixels = []
        self.clustering = []
        self.size = ()
        self.display_state = display_state

        with Image.open(self.file_image) as im:
            px = im.convert('RGB')
            self.size = im.size
            for y in range(0, self.size[0] - 1):
                for x in range(0, self.size[1] - 1):
                    self.pixels.append(Pixel((y, x), px.getpixel((y, x))))
            im.show()

    def __create_cluster(self):
        for nbr in range(0, self.nbr_cluster):
            idx = random.randint(0, (self.size[0] * self.size[1]) - 1)
            self.clustering.append(Cluster(self.pixels.pop(idx)))

    def __verify_end(self):
        if self.display_state:
            self.__display_img()
            input("wait next state")
        for idx, cluster in enumerate(self.clustering):
            if not cluster.calculate_mediane(self.nbr_convergence):
                self.restore_all()
                return False
        return True

    def choice_cluster(self, pixel):
        truple = []
        idx = (85, 85444444442025852.5)

        for cluster in self.clustering:
            truple.append(calculate_convergence(cluster.copy_pixel, pixel.pixel))

        for index, convergence in enumerate(truple):
            if convergence < idx[1]:
                idx = (index, convergence)
        self.clustering[idx[0]].pixels.append(pixel)

    def __display_img(self):

        new_pixel = list(chunks(self.pixels, self.size[1]))
        new_img = [[(-1, -1, -1) for a in range(0, self.size[1])] for i in range(0, self.size[0])]
        count = 1
        print("start creation matrice of imgae")
        for idx, lines in enumerate(new_pixel):
            print(f"loading image .... { float(((idx + (self.size[0] * count)) / (self.size[1] * self.size[0])) * 100)}%")
            for index, pixel in enumerate(lines):
                for indexx, cluster in enumerate(self.clustering):
                    if pixel in cluster.pixels:
                        new_img[pixel.position[0]][pixel.position[1]] = cluster.copy_pixel
                if new_img[pixel.position[0]][pixel.position[1]][0] == -1:
                    new_img[pixel.position[0]][pixel.position[1]] = (0, 0, 0)
            count += 1
        print("loading picture ... 100%")
        new_img.remove([(-1, -1, -1) for a in range(0, self.size[1])])
        array = np.array(new_img, dtype=np.uint8)
        new_image = Image.fromarray(array)
        print("transpose image...")
        new_image.transpose(Image.FLIP_LEFT_RIGHT)
        print("rotate image...")
        new_image = new_image.rotate(270)
        new_image = new_image.resize((new_image.size[1], new_image.size[0]))
        new_image.show()

    def run(self):
        self.__create_cluster()
        tour = 0
        while 1:
            print(f"========================{tour}=============================")
            for pixel in self.pixels:
                self.choice_cluster(pixel)
            if self.__verify_end() or self.nbr_cluster == 1:
                for cluster in self.clustering:
                    print(f", position ({cluster.position}), color: {cluster.old_pixel}")
                self.__display_img()
                break
            self.restore_all()
            tour += 1

    def restore_all(self):
        for cluster in self.clustering:
            cluster.pixels = []

