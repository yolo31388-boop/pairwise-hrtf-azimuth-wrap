# pairwise-hrtf-azimuth-wrap

## 领域

游戏、图形与多媒体

## 主题

HRTF 方位回绕

## 说明

四元数插值、方位展开与跨界淡化。

初始状态下 `media/hrtf_azimuth_wrap.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
