import pandas as pd
import numpy as np
import data
import pdb


class DecisionTree:
    space = "　　　"
    lineflag = False

    def __init__(self, X, Y, version=2):
        self.X = X
        self.Y = Y
        self.version = version
        if self.version == 1:
            self.infoFunc = self.compEntropy
        elif self.version == 2:
            self.infoFunc = self.compGini

    def comp_entropy(self, Y):
        probs = [np.sum(Y == y)/len(Y) for y in np.unique(Y)]
        return np.sum(probs*np.log2(probs))

    def comp_gini(sef, y):
        probs = [np.sum(Y == y)/len(Y) for y in np.unique(Y)]
        return 1 - np.sum(np.square(probs))

    def select_x(self, X, Y):
        all_info: float = self.infoFunc(Y)
        # 各説明変数の平均情報量および利得の記録
        col_infos = []
        gains = []
        # 説明変数のループ
        for col in X.columns:

            # 説明変数を限定した平均情報エントロピーまたはジニ不純度の計算
            colInfo = np.sum([np.sum(X[col] == value)/len(X) *
                              self.infoFunc(Y[X[col] == value]) for value in np.unique(X[col])])
            col_infos.append(colInfo)
            # 利得の計算およgainsに記録
            gains.append(all_info-colInfo)
        return np.argmax(gains), all_info

     # value: 説明変数の値
    def delCol(self, X, Y, col, value):
        # 説明変数colの削除
        subX = X[X[col] == value]
        subX = subX.drop(col, axis=1)

        # 目的変数から値を削除
        subY = Y[X[col] == value]

        return subX, subY
    # -------------------

    # -------------------
    # 5. 決定木の作成
    # X: 入力データ（データ数×カラム数のdataframe）
    # Y: 出力データ（データ数×１のnumpy.ndarray）
    # layer:
    def train(self, X=[], Y=[], layer=0):
        if not len(X):
            X = self.X
        if not len(Y):
            Y = self.Y

        # 葉ノードの標準出力
        if self.infoFunc(Y) == 0:
            print(f" --> {Y[0][0]}")
            return Y[0][0]
        else:
            print("\n", end="")

        # 説明変数の選択
        colInd, allInfo = self.selectX(X, Y)

        # 説明変数名の取得
        col = X.columns[colInd]

        # 説明変数colの値ごとに枝を分岐
        for value in np.unique(X[col]):

            # 説明変数colの削除
            subX, subY = self.delCol(X, Y, col, value)

            # -----------
            # 分岐ノードの標準出力
            if self.lineFlag:
                print(f"{self.space*(layer-1)}｜")
            self.lineFlag = True

            if layer > 0:
                print(f"{self.space*(layer-1)}＋― ", end="")

            print(
                f"{col} ({round(allInfo,2)}) = '{value}' ({round(self.infoFunc(subY),2)})", end="")
            # -----------

            # 分岐先の枝で決定木を作成
            self.train(subX, subY, layer+1)
    # -------------------
