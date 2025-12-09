# 快速参考卡

## 🚀 一分钟启动

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 启动服务器
python run.py

# 3. 打开浏览器
http://localhost:8000
```

## 🔑 API密钥获取

| Provider | 注册地址 | 推荐度 |
|----------|---------|-------|
| **DeepSeek** 🌟 | https://platform.deepseek.com/ | ⭐⭐⭐⭐⭐ (国内首选) |
| **OpenAI** | https://platform.openai.com/ | ⭐⭐⭐⭐ (需国外手机) |
| **Anthropic** | https://console.anthropic.com/ | ⭐⭐⭐⭐ (需国外手机) |

## 📝 配置示例

### DeepSeek (推荐国内用户)
```
Provider: deepseek
API Key: sk-...
Model: deepseek-chat
```

### OpenAI
```
Provider: openai
API Key: sk-...
Model: gpt-3.5-turbo
```

### Anthropic
```
Provider: anthropic
API Key: sk-ant-...
Model: claude-3-5-sonnet-20241022
```

## 🧪 测试命令

```bash
# 测试所有组件
python test_api_simple.py

# 测试DeepSeek集成
python test_deepseek.py

# 调试模式启动
python run_debug.py
```

## 📚 文档导航

| 文档 | 用途 | 链接 |
|------|------|------|
| 快速开始 | 新手入门 | [START_HERE.md](START_HERE.md) |
| DeepSeek指南 | DeepSeek配置 | [DEEPSEEK_GUIDE.md](DEEPSEEK_GUIDE.md) |
| 故障排除 | 遇到问题 | [TROUBLESHOOTING.md](TROUBLESHOOTING.md) |
| API示例 | 代码参考 | [API_EXAMPLES.md](API_EXAMPLES.md) |
| 实现细节 | 技术文档 | [IMPLEMENTATION.md](IMPLEMENTATION.md) |

## ⚡ 常用命令

```bash
# 启动服务器
python run.py
.venv\Scripts\python run.py

# 测试API
curl http://localhost:8000/api/health

# 运行测试
python test_api_simple.py
pytest tests/ -v
```

## 🎯 常用模型

### DeepSeek
- `deepseek-chat` - 通用对话 ⭐⭐⭐⭐⭐
- `deepseek-coder` - 代码生成 ⭐⭐⭐⭐

### OpenAI
- `gpt-3.5-turbo` - 快速便宜 ⭐⭐⭐⭐
- `gpt-4` - 高质量 ⭐⭐⭐⭐⭐
- `gpt-4-turbo` - 平衡选择 ⭐⭐⭐⭐⭐

### Anthropic
- `claude-3-5-sonnet-20241022` - 推荐 ⭐⭐⭐⭐⭐
- `claude-3-opus-20240229` - 最强 ⭐⭐⭐⭐⭐

## ⚙️ 行为参数

```python
{
    "behavior_settings": {
        "enable_segmentation": true,     # 消息分段
        "enable_typo": true,              # 错别字
        "enable_recall": true,            # 撤回重发
        "base_typo_rate": 0.08,           # 8%错别字率
        "typo_recall_rate": 0.4           # 40%撤回率
    }
}
```

## 🐛 常见错误

| 错误 | 原因 | 解决 |
|------|------|------|
| 500 | API密钥错误 | 检查密钥是否正确 |
| 401 | 认证失败 | 确认密钥格式 |
| 404 | 模型不存在 | 检查模型名拼写 |
| 超时 | 网络问题 | 检查网络连接 |

## 💰 费用参考

| Provider | 输入 (1K tokens) | 输出 (1K tokens) |
|----------|-----------------|-----------------|
| DeepSeek | ~¥0.001 | ~¥0.002 |
| OpenAI GPT-3.5 | ~$0.0005 | ~$0.0015 |
| OpenAI GPT-4 | ~$0.03 | ~$0.06 |
| Claude Sonnet | ~$0.003 | ~$0.015 |

## 🔗 项目地址

```
项目路径: D:\Files\Develop Projects\AI\Rie_Kugimiya
前端URL: http://localhost:8000
API URL: http://localhost:8000/api/chat
健康检查: http://localhost:8000/api/health
```

## 📞 获取帮助

1. 查看 [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
2. 运行测试: `python test_api_simple.py`
3. 检查文档: [文档列表](#-文档导航)

## 🎨 推荐配置

### 国内用户（首选）
```json
{
    "provider": "deepseek",
    "model": "deepseek-chat",
    "system_prompt": "你是可爱的虚拟角色"
}
```

### 国外用户
```json
{
    "provider": "openai",
    "model": "gpt-3.5-turbo",
    "system_prompt": "You are a cute virtual character"
}
```

### 高质量对话
```json
{
    "provider": "anthropic",
    "model": "claude-3-5-sonnet-20241022",
    "system_prompt": "You are Rie..."
}
```

---

**打印此页** 作为快速参考！
