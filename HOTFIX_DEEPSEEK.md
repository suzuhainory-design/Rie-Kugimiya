# DeepSeek API端点修复

## 🐛 问题描述

**错误**: `401 Unauthorized` when calling DeepSeek API

**原因**: API端点路径错误
- ❌ 错误: `https://api.deepseek.com/chat/completions`
- ✅ 正确: `https://api.deepseek.com/v1/chat/completions`

## ✅ 已修复

### 修改文件: `src/api/llm_client.py`

**修复前**:
```python
response = await self.client.post(
    f"{base_url}/chat/completions",  # ❌ 缺少 /v1/
    ...
)
```

**修复后**:
```python
response = await self.client.post(
    f"{base_url}/v1/chat/completions",  # ✅ 添加 /v1/
    ...
)
```

## 🔄 如何应用修复

### 方法1: 重启服务器（推荐）

如果服务器正在运行：
```bash
# 1. 停止服务器 (Ctrl+C)
# 2. 重新启动
python run.py
```

修复会自动生效！

### 方法2: 查看修改

```bash
# 查看修改后的文件
cat src/api/llm_client.py | grep -A 5 "_deepseek_chat"
```

## ✅ 验证修复

### 测试1: 运行测试脚本
```bash
python test_deepseek.py
```

应该看到所有 `[OK]`

### 测试2: 手动测试API
```bash
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{
    "llm_config": {
      "provider": "deepseek",
      "api_key": "YOUR_REAL_API_KEY",
      "model": "deepseek-chat",
      "system_prompt": "你是助手"
    },
    "messages": [
      {"role": "user", "content": "你好"}
    ]
  }'
```

### 测试3: 直接测试DeepSeek API
```bash
curl https://api.deepseek.com/v1/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek-chat",
    "messages": [{"role": "user", "content": "hi"}]
  }'
```

## 📝 相关文档更新

已同步更新以下文档：
- ✅ `DEEPSEEK_GUIDE.md` - 添加端点说明
- ✅ `TROUBLESHOOTING.md` - 更新测试命令
- ✅ `src/api/llm_client.py` - 修复代码

## 🎯 现在可以正常使用了

**步骤**:
1. 确保服务器已重启
2. 打开浏览器: `http://localhost:8000`
3. 配置:
   - Provider: `DeepSeek`
   - API Key: 你的密钥
   - Model: `deepseek-chat`
4. 开始聊天！

## 💡 为什么会有这个问题？

DeepSeek使用OpenAI兼容的API格式，标准端点包含 `/v1/` 前缀：
- ✅ OpenAI: `https://api.openai.com/v1/chat/completions`
- ✅ DeepSeek: `https://api.deepseek.com/v1/chat/completions`
- ❌ 之前缺少了 `/v1/` 导致401错误

## 🔍 如何确认修复生效

启动服务器后，在服务器日志中不应该再看到401错误。成功的请求会返回正常的聊天响应。

## 📞 仍然遇到问题？

如果仍然有401错误：
1. **检查API密钥**: 确保是有效的DeepSeek密钥（以 `sk-` 开头）
2. **检查余额**: 登录 https://platform.deepseek.com/ 确认有余额
3. **检查模型名**: 确认使用 `deepseek-chat` 或 `deepseek-coder`
4. **查看完整错误**: 检查服务器终端的完整错误消息

---

**版本**: v1.1.1 (Hotfix)
**修复时间**: 2024-12-09
**影响范围**: 仅DeepSeek provider
