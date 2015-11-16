from SimpleCV import Image
from pybrain.tools.xml import NetworkReader

net = NetworkReader.readFrom("classification_net")


def get_net_input(right, left):
    motion = left.findMotion(right, window=right.width / 5)
    data = []
    for i in range(27):
        if i < len(motion):
            data.append(motion[i].dx)
        else:
            data.append(0)
    return data


def is_cross_view(right, left):
    return net.activate(get_net_input(right, left)) < 0.5


def split(url):
    image = Image(url)
    image = image.scale(200.0/image.width)
    left = image.crop(0, 0, image.width/2, image.height)
    right = image.crop(image.width/2, 0, image.width/2, image.height)

    return right, left
