"""feature_engineer skill 的单件 pipeline。
这件 skill 只做特征工程 —— 输入原始特征,输出变换后的特征矩阵。
不做训练、不做校准(那些是别的 skill 的事)。"""
from skill import feature_engineer


def run(X):
    """输入原始特征矩阵,输出变换后的特征矩阵(27 维)。"""
    return feature_engineer.engineer(X)
