class ScreenControl:

    def getResolution(self) -> list:
        """
        获取屏幕分辨率
        :return: 分辨率
        """
        pass

    def getScreenColor(self, x: int, y: int) -> tuple:
        """
        获取屏幕指定像素颜色, 返回RGB形式
        :param x: 距离屏幕左边的像素
        :param y: 距离屏幕上面的像素
        :return: RGB颜色
        """
        pass

    def isColor(self, x: int, y: int, rgbColor = (255, 255, 255)) -> bool:
        """
        返回指定像素颜色是否与指定的颜色一直
        :param x: 距离屏幕左边的像素
        :param y: 距离屏幕上面的像素
        :param rgbColor: 要匹配的颜色
        :return: 布尔值
        """
        pass

    def takeAScreenshot(self, savePath: str) -> 'ScreenControl':
        """
        截取整个屏幕
        :param savePath: 保存路径
        :return: Display
        """
        pass

    def zoneTakeAScreenshot(
            self,
            left: int,
            top: int,
            width: int,
            height: int,
            savePath: str
    ) -> 'ScreenControl':
        """
        截取指定区域
        :param left: 距离屏幕左边的位置
        :param top: 距离屏幕上面的像素
        :param width: 截取的宽度
        :param height: 截取的高度
        :param savePath: 保存路径
        :return: Display
        """
        pass

    def getScreenFullText(
            self,
            left: int,
            top: int,
            width: int,
            height: int,
            language: list,
            zone: bool
    ) -> str:
        """
        识别屏幕文字
        :param left: 距离屏幕左边的位置
        :param top: 距离屏幕上面的像素
        :param width: 截取的宽度
        :param height: 截取的高度
        :param language: 语言
        :param zone: 是否区域截屏
        :return: 识别的文字
        """
        pass

