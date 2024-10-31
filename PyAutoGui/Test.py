import sys
import random
from PySide6.QtCore import Qt, QTimer, QPoint
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QMenu


class DesktopPet(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置无边框和透明背景
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # 准备桌宠图像帧
        self.frames = [
            QPixmap(
                r"C:\Users\Administrator\Downloads\Soft\MyFlowingFireflyWifie-beta-v0.4-window11-x64-nuitka\MyFlowingFireflyWife\data\assets\images\firefly\actions\left\0.png"),
            # 替换为桌宠的图像帧路径
            QPixmap(
                r"C:\Users\Administrator\Downloads\Soft\MyFlowingFireflyWifie-beta-v0.4-window11-x64-nuitka\MyFlowingFireflyWife\data\assets\images\firefly\actions\left\1.png"),
            # 替换为桌宠的图像帧路径
            QPixmap(
                r"C:\Users\Administrator\Downloads\Soft\MyFlowingFireflyWifie-beta-v0.4-window11-x64-nuitka\MyFlowingFireflyWife\data\assets\images\firefly\actions\left\2.png"),
            # 替换为桌宠的图像帧路径
            QPixmap(
                r"C:\Users\Administrator\Downloads\Soft\MyFlowingFireflyWifie-beta-v0.4-window11-x64-nuitka\MyFlowingFireflyWife\data\assets\images\firefly\actions\left\3.png"),
            # 替换为桌宠的图像帧路径
        ]
        self.current_frame = 0

        # 设置初始图像
        self.label = QLabel(self)
        self.label.setPixmap(self.frames[self.current_frame])
        self.resize(self.frames[self.current_frame].size())

        # 初始化动画参数，随机生成初始移动方向
        self.move_direction = QPoint(random.choice([-1, 1]), random.choice([-1, 1]))
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_position)
        self.timer.start(100)  # 每100毫秒更新位置并切换帧

    def update_position(self):
        # 切换图像帧，创建动画效果
        self.current_frame = (self.current_frame + 1) % len(self.frames)
        self.label.setPixmap(self.frames[self.current_frame])

        # 更新桌宠位置
        new_pos = self.pos() + self.move_direction

        # 边界检测，防止桌宠移动到屏幕外
        screen_rect = QApplication.primaryScreen().availableGeometry()
        if new_pos.x() < 0 or new_pos.x() + self.width() > screen_rect.width():
            self.move_direction.setX(-self.move_direction.x())
        if new_pos.y() < 0 or new_pos.y() + self.height() > screen_rect.height():
            self.move_direction.setY(-self.move_direction.y())

        # 移动到新位置
        self.move(new_pos)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # 停止动画
            self.timer.stop()
            self.drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()
        elif event.button() == Qt.RightButton:
            # 显示右键菜单
            self.show_context_menu(event.globalPosition().toPoint())

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            # 重新启动动画
            self.timer.start(100)
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            # 拖动窗口
            self.move(event.globalPosition().toPoint() - self.drag_position)
            event.accept()

    def show_context_menu(self, pos):
        # 创建右键菜单
        menu = QMenu(self)

        # 添加菜单选项
        move_action = menu.addAction(QIcon("move_icon.png"), "移动到随机位置")  # 可用图标替换路径
        quit_action = menu.addAction(QIcon("quit_icon.png"), "退出")  # 可用图标替换路径

        # 连接菜单选项的功能
        move_action.triggered.connect(self.move_to_random_position)
        quit_action.triggered.connect(self.close)

        # 设置菜单样式
        menu.setStyleSheet("""
            QMenu {
                background-color: #333333;  /* 菜单背景颜色 */
                color: #FFFFFF;  /* 文字颜色 */
                border: 1px solid #555555;
                border-radius: 8px;
            }
            QMenu::item {
                padding: 8px 20px;
                background-color: transparent;
            }
            QMenu::item:selected {
                background-color: #666666;  /* 选中项的背景颜色 */
                color: #FFFFFF;  /* 选中项的文字颜色 */
            }
            QMenu::icon {
                padding-left: 10px;  /* 图标与文字的距离 */
            }
        """)

        # 显示菜单
        menu.exec(pos)

    def move_to_random_position(self):
        # 移动桌宠到屏幕的随机位置
        screen_rect = QApplication.primaryScreen().availableGeometry()
        random_x = random.randint(0, screen_rect.width() - self.width())
        random_y = random.randint(0, screen_rect.height() - self.height())
        self.move(random_x, random_y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pet = DesktopPet()
    pet.show()
    sys.exit(app.exec())
