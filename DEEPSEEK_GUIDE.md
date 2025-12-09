# DeepSeek API 使用指南

## 📝 DeepSeek 简介

DeepSeek 是一个国内的AI模型提供商，提供高性价比的大语言模型服务。
- 🚀 **响应快速** - 国内访问速度快
- 💰 **价格实惠** - 相比国外API更便宜
- 🔌 **兼容OpenAI** - 使用OpenAI兼容的API格式
- 🇨🇳 **中文友好** - 对中文支持优秀

## 🔑 获取API密钥

### 1. 注册账号
访问: https://platform.deepseek.com/

### 2. 获取API Key
1. 登录后进入控制台
2. 点击 "API Keys"
3. 创建新的API Key
4. 复制密钥（格式类似: `sk-...`）

### 3. 充值（如需要）
- DeepSeek采用按量计费
- 需要先充值才能使用

## ⚙️ 配置步骤

### 方式一：Web界面配置

1. 启动服务器：
   ```bash
   python run.py
   ```

2. 打开浏览器: `http://localhost:8000`

3. 在配置页面：
   - **Provider**: 选择 `DeepSeek`
   - **API Key**: 粘贴你的API密钥
   - **Model**: 选择模型（见下方）
   - **System Prompt**: 设置角色提示词

4. 点击 "Save & Start Chat"

### 方式二：API调用

```python
import httpx
import asyncio

async def chat_with_deepseek():
    response = await httpx.AsyncClient().post(
        "http://localhost:8000/api/chat",
        json={
            "llm_config": {
                "provider": "deepseek",
                "api_key": "sk-your-api-key",
                "model": "deepseek-chat",
                "system_prompt": "你是一个可爱的虚拟角色。"
            },
            "messages": [
                {"role": "user", "content": "你好！"}
            ]
        }
    )
    return response.json()

result = asyncio.run(chat_with_deepseek())
print(result)
```

## 🎯 可用模型

### deepseek-chat
- **用途**: 通用对话
- **特点**: 平衡性能和成本
- **推荐**: ⭐⭐⭐⭐⭐ 日常使用首选

```json
{
  "model": "deepseek-chat"
}
```

### deepseek-coder
- **用途**: 代码生成和编程
- **特点**: 专注于代码理解和生成
- **推荐**: ⭐⭐⭐⭐ 编程相关对话

```json
{
  "model": "deepseek-coder"
}
```

## 💡 使用示例

### 基础对话

```bash
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{
    "llm_config": {
      "provider": "deepseek",
      "api_key": "sk-your-key",
      "model": "deepseek-chat",
      "system_prompt": "你是Rie，一个可爱活泼的虚拟角色。"
    },
    "messages": [
      {"role": "user", "content": "介绍一下你自己"}
    ]
  }'
```

### 带行为设置

```python
{
    "llm_config": {
        "provider": "deepseek",
        "api_key": "sk-your-key",
        "model": "deepseek-chat",
        "system_prompt": "你是一个傲娇的虚拟角色。"
    },
    "messages": [
        {"role": "user", "content": "今天天气真好"}
    ],
    "behavior_settings": {
        "enable_segmentation": true,
        "enable_typo": true,
        "enable_recall": true,
        "base_typo_rate": 0.05,
        "typo_recall_rate": 0.3
    }
}
```

### 代码生成对话

```json
{
    "llm_config": {
        "provider": "deepseek",
        "api_key": "sk-your-key",
        "model": "deepseek-coder",
        "system_prompt": "你是一个编程助手，擅长Python。"
    },
    "messages": [
        {"role": "user", "content": "写一个快速排序算法"}
    ]
}
```

## 🔧 高级配置

### 自定义Base URL

如果使用代理或自定义端点：

```json
{
    "provider": "deepseek",
    "api_key": "sk-your-key",
    "base_url": "https://your-proxy.com",  // 不含 /v1
    "model": "deepseek-chat"
}
```

**注意**：
- 默认base_url是 `https://api.deepseek.com`
- 实际请求会自动添加 `/v1/chat/completions`
- 如果使用代理，只需提供base_url（不含/v1）

### 优化中文对话

```json
{
    "system_prompt": "你是Rie Kugimiya，一个可爱的日本声优虚拟角色。\n性格：活泼、傲娇、关心他人\n说话风格：口语化、偶尔使用颜文字\n注意：回复要自然简短，不要太正式"
}
```

## 📊 性能对比

| 特性 | OpenAI GPT-3.5 | DeepSeek Chat | Anthropic Claude |
|------|---------------|---------------|------------------|
| 中文理解 | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| 响应速度（国内） | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ |
| 价格 | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ |
| 代码能力 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |

## ⚠️ 注意事项

### 1. API密钥安全
- ❌ 不要在代码中硬编码密钥
- ✅ 使用环境变量或配置文件
- ✅ 定期轮换密钥

### 2. 费用控制
- 监控API使用量
- 设置预算告警
- 合理设置max_tokens限制

### 3. 网络问题
- DeepSeek服务器在国内，访问速度快
- 如遇超时，检查网络连接
- 可以增加timeout设置

## 🐛 常见问题

### Q1: API返回401错误
**A**: 检查API密钥是否正确，是否已充值

### Q2: 响应速度慢
**A**: DeepSeek国内访问通常很快，检查本地网络

### Q3: 中文乱码
**A**: 确保代码使用UTF-8编码

### Q4: 余额不足
**A**: 登录平台充值: https://platform.deepseek.com/

### Q5: 模型名称错误
**A**: 确认使用 `deepseek-chat` 或 `deepseek-coder`

## 💰 费用参考

DeepSeek定价（参考官网最新价格）：
- **输入**: ~¥0.001 / 1K tokens
- **输出**: ~¥0.002 / 1K tokens

示例成本：
- 100条对话（每条~100字）≈ ¥0.2
- 非常经济实惠！

## 🔗 相关链接

- 官网: https://www.deepseek.com/
- 控制台: https://platform.deepseek.com/
- 文档: https://platform.deepseek.com/api-docs/
- 定价: https://platform.deepseek.com/api-docs/pricing/

## 📞 技术支持

遇到问题：
1. 查看 [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
2. 检查 DeepSeek 官方文档
3. 运行测试: `python test_api_simple.py`

---

**推荐使用场景**：
- ✅ 国内用户首选
- ✅ 中文对话为主
- ✅ 预算有限
- ✅ 需要快速响应

开始使用DeepSeek，享受高性价比的AI对话体验！
