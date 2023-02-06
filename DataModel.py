class DataModel:
    def __init__(self, xdata: list, ydata: list):
        self.xdata = xdata
        self.ydata = ydata

    def joinData(self) -> dict:
        new_dict: dict = {self.xdata[i]: self.ydata[i] for i in range(len(self.xdata))}
        return new_dict
