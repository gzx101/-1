from PIL import Image
import matplotlib.pyplot as plt

def flip_left_right(img):
    """
    图片左右翻转函数
    :param img: 输入PIL Image图片对象
    :return: 左右翻转后的图片对象
    """
    # 左右翻转：transpose(Image.FLIP_LEFT_RIGHT)
    flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    return flipped_img


def show_two_images(original_img, flipped_img):
    """同时显示原图和翻转后的图片"""
    # 创建1行2列画布
    plt.figure(figsize=(10, 5))

    # 子图1：原始图片
    plt.subplot(1, 2, 1)
    plt.imshow(original_img)
    plt.title("Original Image")
    plt.axis("off")

    # 子图2：翻转后的图片
    plt.subplot(1, 2, 2)
    plt.imshow(flipped_img)
    plt.title("Flipped Left‑Right Image")
    plt.axis("off")

    plt.show()