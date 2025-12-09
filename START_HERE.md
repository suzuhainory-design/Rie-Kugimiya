# 🚀 START HERE - 从这里开始

## 快速启动 (2分钟)

### 第一步：安装依赖

打开终端（命令提示符/PowerShell），进入项目目录：

```bash
cd "D:\Files\Develop Projects\AI\Rie_Kugimiya"

# 安装依赖
pip install -r requirements.txt
```

### 第二步：启动服务器

```bash
# 如果使用虚拟环境
.venv\Scripts\python run.py

# 或者直接运行
python run.py
```

看到以下信息表示启动成功：
```
🎭 Rie Kugimiya Virtual Character System
📍 URL: http://localhost:8000
```

### 第三步：打开浏览器

访问: **http://localhost:8000**

### 第四步：配置API

1. 在配置页面选择Provider
   - **国内用户推荐**: DeepSeek (快速、便宜、中文好)
   - **国外用户**: OpenAI 或 Anthropic
2. 输入你的API Key
3. 选择模型
   - DeepSeek: `deepseek-chat`
   - OpenAI: `gpt-3.5-turbo`
   - Anthropic: `claude-3-5-sonnet-20241022`
4. 点击 "Save & Start Chat"

### 第五步：开始聊天！

输入消息，观察：
- ✨ 微信式分段播放
- ✨ 消息分段显示
- ✨ 自然停顿
- ✨ 偶尔的错别字和撤回

---

## 遇到问题？

### ❌ 500错误
→ 检查API密钥是否正确
→ 查看 [TROUBLESHOOTING.md](TROUBLESHOOTING.md#1-500-internal-server-error)

### ❌ 404错误
→ 确认前端文件存在
→ 重启服务器

### ❌ 其他问题
→ 运行测试: `python test_api_simple.py`
→ 查看完整故障排除: [TROUBLESHOOTING.md](TROUBLESHOOTING.md)

---

## 📚 文档导航

| 文档 | 内容 | 适合 |
|------|------|------|
| **START_HERE.md** (本文档) | 快速开始 | 首次使用 |
| [QUICKSTART.md](QUICKSTART.md) | 详细使用指南 | 日常使用 |
| [TROUBLESHOOTING.md](TROUBLESHOOTING.md) | 故障排除 | 遇到问题 |
| [IMPLEMENTATION.md](IMPLEMENTATION.md) | 技术实现细节 | 开发/扩展 |
| [API_EXAMPLES.md](API_EXAMPLES.md) | API使用示例 | 集成开发 |
| [SETUP.md](SETUP.md) | 安装和配置 | 深度定制 |
| [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) | 项目总结 | 了解全貌 |

---

## ✅ 验证安装

运行测试脚本确保一切正常：

```bash
python test_api_simple.py
```

应该看到所有 `[OK]`。

---

## 🎯 下一步

### 基础使用
1. 尝试不同的对话主题
2. 观察情感检测（发"哈哈"、"难过"等）
3. 查看错别字和撤回行为

### 进阶定制
1. 修改system prompt调整角色性格
2. 调整行为参数（错别字概率等）
3. 查看 [IMPLEMENTATION.md](IMPLEMENTATION.md) 了解架构

### 开发扩展
1. 集成自己的ML模型
2. 添加新的情绪类型
3. 自定义分段策略

---

## 💡 快速参考

### 启动命令
```bash
python run.py              # 正常启动
python run_debug.py        # 调试模式
python test_api_simple.py  # 运行测试
```

### 常用API
```python
# 使用behavior系统
from src.behavior import BehaviorCoordinator
coordinator = BehaviorCoordinator()
segments = coordinator.process_message("你好！")
```

### 配置位置
- **后端配置**: `src/behavior/models.py` → `BehaviorConfig`
- **前端配置**: 浏览器localStorage（自动保存）
- **服务器配置**: `src/utils/config.py`

---

## 🆘 需要帮助？

1. **快速问题**: 查看 [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
2. **使用指南**: 查看 [QUICKSTART.md](QUICKSTART.md)
3. **技术细节**: 查看 [IMPLEMENTATION.md](IMPLEMENTATION.md)
4. **运行测试**: `python test_api_simple.py`

---

**准备好了吗？** 运行 `python run.py` 开始体验！
