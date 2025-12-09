# DeepSeek 快速检查清单

## ✅ 使用前检查

### 1. 账户设置
- [ ] 已在 https://platform.deepseek.com/ 注册
- [ ] 已生成API密钥
- [ ] 已复制完整密钥（包括 `sk-` 前缀）
- [ ] 账户有余额（至少¥1）

### 2. 服务器设置
- [ ] 已安装依赖: `pip install -r requirements.txt`
- [ ] 服务器正在运行: `python run.py`
- [ ] 可以访问: http://localhost:8000

### 3. 配置设置
- [ ] Provider 选择: `DeepSeek`
- [ ] API Key 已填写（无空格）
- [ ] Model 填写: `deepseek-chat`
- [ ] System Prompt 已设置

### 4. 测试
- [ ] 点击 "Save & Start Chat"
- [ ] 发送测试消息: "你好"
- [ ] 收到正常回复（无401错误）

## 🐛 遇到401错误？

### 立即检查（按顺序）

#### 第1步: API密钥
```bash
# 你的密钥看起来像这样吗？
sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# 检查：
# ✓ 以 sk- 开头
# ✓ 没有空格
# ✓ 完整复制
```

#### 第2步: 账户余额
```
登录: https://platform.deepseek.com/
查看右上角余额
如果是 ¥0.00 → 需要充值
```

#### 第3步: 手动测试API
```bash
curl https://api.deepseek.com/v1/chat/completions \
  -H "Authorization: Bearer 你的密钥" \
  -H "Content-Type: application/json" \
  -d '{"model":"deepseek-chat","messages":[{"role":"user","content":"hi"}]}'
```

**成功**: 返回JSON，包含 `"content":`
**失败**: 返回错误，说明API配置有问题

#### 第4步: 检查服务器日志
在运行 `python run.py` 的终端查看：
```
✓ 成功: 不应该看到 401 错误
✗ 失败: 看到 HTTPStatusError: 401
```

#### 第5步: 重新配置
1. 刷新浏览器 (Ctrl+Shift+R)
2. 清除配置 (F12 → Application → Storage → Clear)
3. 重新填写配置
4. 再次测试

## 📱 快速修复方案

### 方案A: 重新生成密钥（推荐）
```
1. 访问: https://platform.deepseek.com/api_keys
2. 创建新API Key
3. 立即复制
4. 粘贴到配置中
5. 保存并测试
```

### 方案B: 充值账户
```
1. 访问: https://platform.deepseek.com/
2. 点击"充值"
3. 充值至少 ¥10
4. 等待到账
5. 重新测试
```

### 方案C: 使用官方SDK测试
```python
# test_api.py
from openai import OpenAI

client = OpenAI(
    api_key="你的密钥",
    base_url="https://api.deepseek.com"
)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": "你好"}]
)

print(response.choices[0].message.content)
```

```bash
pip install openai
python test_api.py
```

如果这个成功了，说明密钥有效，问题在我们的配置。

## 💡 成功案例

### 配置示例（已验证有效）

**Provider**: `deepseek`

**API Key**: `sk-1234567890abcdef...`（你的真实密钥）

**Model**: `deepseek-chat`

**System Prompt**:
```
你是Rie，一个可爱活泼的虚拟角色。
说话风格自然随意，偶尔使用表情符号。
```

点击保存，发送 "你好"，应该收到类似：
```
你好呀！有什么我可以帮你的吗？(ﾟ▽ﾟ)/
```

## ⚠️ 常见错误

### ❌ 错误1: 密钥包含空格
```
错误: " sk-abc123..."
正确: "sk-abc123..."
```

### ❌ 错误2: 模型名称错误
```
错误: "DeepSeek-Chat"
正确: "deepseek-chat"
```

### ❌ 错误3: Base URL错误
```
错误需要填: 不需要填（除非用代理）
保持空白: ✓
```

### ❌ 错误4: 使用了错误的密钥
```
错误: 使用OpenAI的密钥
正确: 使用DeepSeek的密钥
```

## 📊 费用参考

测试预算建议：
- 最低充值: ¥10
- 100条对话约: ¥0.2-0.5
- ¥10够用几千条消息

## 🎯 下一步

检查全部通过后：
1. ✅ 开始正常使用
2. ✅ 调整 System Prompt 优化角色
3. ✅ 在 behavior_settings 中调整行为参数
4. ✅ 享受流畅的中文对话体验！

## 📞 需要帮助？

按顺序查看：
1. 本检查清单（当前文档）
2. [DEBUG_DEEPSEEK_401.md](DEBUG_DEEPSEEK_401.md) - 详细调试
3. [DEEPSEEK_GUIDE.md](DEEPSEEK_GUIDE.md) - 完整指南
4. [TROUBLESHOOTING.md](TROUBLESHOOTING.md) - 通用问题

---

**快速检查**: 密钥 → 余额 → 手动测试 → 重新配置

**大部分401错误都是密钥或余额问题！**
