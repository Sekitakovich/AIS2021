from PIL import Image
from pyzbar.pyzbar import decode


class QRcode(object):
    '''

    '''
    def __init__(self):
        pass

    def read(self, *, file: str):
        result = []
        src = Image.open(file)
        dst = decode(image=src)
        for d in dst:
            result.append(dst[0].data)
        pass


if __name__ == '__main__':
    def main():
        ooo = QRcode()
        ooo.read(file='chart.png')
        pass


    main()
