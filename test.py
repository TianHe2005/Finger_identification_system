# This Python file uses the following encoding: utf-8
import sys
import cv2
import os
from cv2 import xfeatures2d
import tempfile
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
import PyQt5.QtCore
from PyQt5 import QtCore
from form import Ui_Widget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import pymysql
from pymysql.cursors import DictCursor
import hashlib

def getCon():
    # 连接到MySQL数据库
    con = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',  # 数据库用户名
        password='123456',  # 数据库密码
        database='zhiwen',  # 数据库名称
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    return con

def encrypt_id(id):

    # 创建一个md5对象
    md5_obj = hashlib.md5()
    # 更新md5对象以hash密码字符串, 注意这里需要将密码转换为bytes
    md5_obj.update(id.encode('utf-8'))
    # 获取加密后的字符串
    encrypted_id = md5_obj.hexdigest()
    return encrypted_id

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.widget11)
        self.ui.pushButton_2.clicked.connect(self.widget22)
        self.ui.pushButton_3.clicked.connect(self.luruzhiwen)
        self.ui.pushButton_4.clicked.connect(self.zhuce)
        self.ui.pushButton_5.clicked.connect(self.xuanze)
        self.ui.pushButton_6.clicked.connect(self.denglu)

    def widget11(self):
        self.ui.widget.show()
        self.ui.widget_2.close()
    def widget22(self):
        self.ui.widget.close()
        self.ui.widget_2.show()

    def luruzhiwen(self):
        # 打开文件对话框选择图片
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Select Image File", "",
                                                  "Images (*.png *.xpm *.jpg *.jpeg *.bmp);;All Files (*)",
                                                  options=options)

        if fileName:
            # 使用QPixmap加载图片并显示在标签上
            pixmap = QPixmap(fileName)
            self.ui.label_3.setPixmap(pixmap)
    def zhuce(self):
            username = self.ui.lineEdit.text()
            pixmap = self.ui.label_3.pixmap()
            if pixmap.isNull():
                QMessageBox.warning(self, 'No Image', 'No image to save.')
                return
            maxid = int(get_max_id())
            print(maxid)
            id1 = maxid+1
            print(id1)
            id2 = encrypt_id(str(id1))
            image_path = os.path.join('res', f'{id1}.png')
            if not os.path.exists('res'):
                os.makedirs('res')
            con = None
            try:
                pixmap.save(image_path, 'PNG')
                con = getCon()
                with con.cursor() as cursor:
                    sql = "INSERT INTO user (id,id2,username) VALUES (%s,%s, %s)"
                    cursor.execute(sql, (id1, id2, username))
                    con.commit()
                    QMessageBox.information(self, "注册成功", f"{username}注册成功！")
            except Exception as e:
                QMessageBox.critical(self, "错误", f"保存数据时发生错误：{str(e)}")
            finally:
                if con:
                    con.close()

    def xuanze(self):
        # 打开文件对话框选择图片
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Select Image File", "",
                                                  "Images (*.png *.xpm *.jpg *.jpeg *.bmp);;All Files (*)",
                                                  options=options)

        if fileName:
            # 使用QPixmap加载图片并显示在标签上
            pixmap = QPixmap(fileName)
            self.ui.label_2.setPixmap(pixmap)  # 直接设置原图

    def denglu(self):
        pixmap2 = self.ui.label_2.pixmap()
        if pixmap2.isNull():
            QMessageBox.warning(self, 'No Image', 'No image to process.')
            return

        # 创建临时文件并保存 QPixmap
        with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_file:
            temp_file_path = temp_file.name
            pixmap2.save(temp_file_path, 'PNG')

        try:
            # 获取匹配到的模板ID
            ID = getID(temp_file_path, model_base)
            # 获取ID对应的名字
            result = getName(ID)
            print(f'识别结果为：{result}')
            QMessageBox.information(self, "登录成功", f"登录成功账号为：{result}")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"登录时发生错误：{str(e)}")
        finally:
            # 删除临时文件
            if os.path.exists(temp_file_path):
                os.remove(temp_file_path)


    def insert_into_database(self, username, id):
            id2 = encrypt_id(str(id))
            con = None
            try:
                con = getCon()
                with con.cursor() as cursor:
                    sql = "INSERT INTO user (id,username) VALUES (%s, %s)"
                    cursor.execute(sql, (id2,username))
                    con.commit()
            except Exception as e:
                QMessageBox.critical(self, "错误", f"保存数据时发生错误：{str(e)}")
            finally:
                if con:
                    con.close()

def get_max_id():
        con = None
        try:
            con = getCon()
            with con.cursor() as cursor:
                sql = "SELECT MAX(id) AS max_id FROM user"
                cursor.execute(sql)
                result = cursor.fetchone()
                max_id = result['max_id'] if result['max_id'] is not None else 0
                return max_id
        except Exception as e:
            print(f"数据库错误: {e}")
            return 0
        finally:
            if con:
                con.close()


def preprocess_image(image):
    # 转换为灰度图像
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 高斯模糊去噪
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    return blurred




def match(src, model):
    src = cv2.imread(src)
    model = cv2.imread(model)  # 用来匹配识别的指纹模板

    src = preprocess_image(src)
    model = preprocess_image(model)

    sift = xfeatures2d.SIFT_create(nfeatures=0, nOctaveLayers=3, contrastThreshold=0.04, edgeThreshold=10, sigma=1.6)
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

    # src：需要匹配的指纹，model_base：被匹配的指纹模板，通常为文件夹
def getID(src, model_base):
    max_right = 0
    best_name = ''
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
            best_name = file[0]
    ID = best_name
    # 若低于100，即判断指纹模板都不符合
    if max_right < 100:
        ID = 9999
    print(ID)
    return ID


def getName(ID):
    con = None
    id2 = encrypt_id(str(ID))
    try:
        con = getCon()

        with con.cursor() as cursor:
            sql = "SELECT username FROM user WHERE id2=%s"
            cursor.execute(sql, id2)
            result = cursor.fetchone()
            if result:
                name = str(result['username'])
                return name
            else:
                return "未知用户"
    except Exception as e:
            print(f"数据库查询错误: {e}")
            return "未知用户"
    finally:
        if con:
            con.close()





if __name__ == "__main__":
    PyQt5.QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    model_base = './res'
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
