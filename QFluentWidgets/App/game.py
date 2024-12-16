import random


class PoKe:

    def __init__(self):
        self.__color = ['♠', '♣', '♥', '♦']
        self.__points = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4 + ['BigJoker', 'MinJoker']

    def setPoKeNumber(self, number: int):
        self.__points *= number
        return self

    def disruptedPoKe(self):
        for index in range(len(self.__points)):
            randomIndex = random.randint(0, len(self.__points) - 1)
            self.__points[randomIndex], self.__points[index] = self.__points[index], self.__points[randomIndex]
        # print(f"Length: {len(self.__points)}  {self.__points}")
        return self

    def getColor(self):
        return self.__color[random.randint(0, len(self.__color) - 1)]

    def getPoint(self):
        return self.__points.pop(random.randint(0, len(self.__points) - 1))

    def getColorAndPoint(self):
        return f"{self.getPoint()}{self.getColor()}"

    def jinHuaPlay(self, number: int, isCustomPlayerName=False, playerName: list[str] = None):
        try:
            result = {}
            for i in range(number):
                if isCustomPlayerName:
                    result[f"{playerName[i]}"] = [self.getColorAndPoint() for _ in range(3)]
                else:
                    result[f"Player{i+1}"] = [self.getColorAndPoint() for _ in range(3)]
            return '\n'.join([f"{key}: {result[key]}" for key in result.keys()])
        except Exception as e:
            return f"Error: {e}"


if __name__ == '__main__':
    print(
        PoKe()
        .disruptedPoKe()
        .jinHuaPlay(2)
    )