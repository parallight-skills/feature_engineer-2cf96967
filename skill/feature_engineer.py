"""特征工程 skill —— 把原始 6 个特征变换成更可学的特征。
加原始 + 平方项 + 两两交互项(共 27 维),挖出藏在非线性/交互里的信号。
竞技反事实增量 +0.20 ~ +0.30(主杠杆,最贵的那件)。"""


def engineer(X):
    out = []
    for row in X:
        # 1. 原始特征 (6 个)
        feats = list(row)
        # 2. 平方项 (6 个): x_i² —— 捕捉单变量非线性(如倒 U 型)
        feats += [x * x for x in row]
        # 3. 两两交互项 (C(6,2)=15 个): x_i * x_j —— 捕捉两变量的联合效应
        n = len(row)
        for i in range(n):
            for j in range(i + 1, n):
                feats.append(row[i] * row[j])
        out.append(feats)
    return out
