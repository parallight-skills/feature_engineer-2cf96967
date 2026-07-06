# feature-engineer

Trial-to-Paid 转化预测的**特征工程 skill** —— 单件可组合零件。

## 这件 skill 做什么
把 6 维原始特征变换成 27 维(原始 + 平方 + 两两交互),挖出藏在非线性/交互里的信号。

## 价值(反事实增量)
- 把它换回身份变换(baseline) → 验证集分数掉 ~0.20
- 市场定价:**贵**(主杠杆,整条流水线最值钱的件)

## 怎么用
```python
from skill import feature_engineer
X_transformed = feature_engineer.engineer(X_raw)  # 6 维 → 27 维
```

或经 MCP:
- tool: `engineer_features(X)` → 变换后的特征矩阵

## 输入 / 输出
- 输入:二维数组,每行 6 个标准化行为特征
- 输出:二维数组,每行 27 维 = 原始(6) + 平方(6) + 两两交互(15)

## 不做什么
- 不做模型训练(那是 train_model skill 的事)
- 不做阈值校准(那是 calibrate skill 的事)
- 不读 `_truth/`(那是作弊)
