import os
import cv2

"""===============计算两个指纹间匹配点的个数===================="""


def match(src, model):
    src = cv2.imread(src)  # 需要匹配的指纹
    model = cv2.imread(model)  # 用来匹配识别的指纹模板
    sift = cv2.SIFT_create()  # 建立SIFT生成器
    # 特征点, 特征点描述符
    (kps1, des1) = sift.detectAndCompute(src, None)  # 检测SIFT特征点，并计算描述符
    (kps2, des2) = sift.detectAndCompute(model, None)  # 检测SIFT特征点，并计算描述符
    # cv2.FlannBasedMatcher() 是一个特征点匹配器，用于在两组特征点之间找到最佳匹配。
    flann = cv2.FlannBasedMatcher()
    matches = flann.knnMatch(des1, des2, k=2)
    right = 0
    # m，n为匹配到的两个最近的特征点
    for m, n in matches:
        ## 当最近距离跟次近距离的比值小于0.8值时，right + 1,即匹配对的数量加1
        if m.distance < 0.8 * n.distance:
            right += 1

    return right


"""============获取指纹编号================"""


# src：需要匹配的指纹，model_base：被匹配的指纹模板，通常为文件夹
def getID(src, model_base):
    max_right = 0
    name = ''
    # 遍历指纹模板下的每一张指纹模板图片
    for file in os.listdir(model_base):
        # 将路径连接起来，得到file的绝对路径
        model = os.path.join(model_base, file)
        # 传入函数一，得到匹配正确的right数量
        result = match(src, model)
        # 打印出来
        print(f'文件名：{model}, right:{result}')
        # 得到匹配对的right值最大的指纹编号
        if result > max_right:
            max_right = result
            name = file[0]
    ID = name
    # 若低于100，即判断指纹模板都不符合
    if max_right < 100:
        ID = 9999

    return ID


"""==========根据指纹编号，获取对应姓名=============="""


def getName(ID):
    nameID = {0: '张三', 1: '李四', 2: '王五', 3: '赵六', 4: '朱老七', 5: '钱八', 6: '曹九', 7: '王二麻子', 8: 'andy',
              9: 'Anna', 9999: '报警！'}
    name = nameID.get(int(ID))
    return name

"""==============主函数===================="""
if __name__ == '__main__':
    src = './src.png'                 #匹配指纹
    model_base = './res'     #指纹模板
    ID = getID(src, model_base)       #获取匹配到的模板ID
    result = getName(ID)              #获取ID对应名字
    print(f'识别结果为：{result}')
