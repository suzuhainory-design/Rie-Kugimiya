# DeepSeek 401错误调试指南

## 🔍 401错误常见原因

### 1. API密钥问题（最常见）

**检查清单**:
- ✅ 密钥是否完整复制（包括 `sk-` 前缀）
- ✅ 密钥中没有多余的空格
- ✅ 密钥没有过期
- ✅ 使用的是DeepSeek的密钥（不是OpenAI的）

**获取新密钥**:
1. 访问: https://platform.deepseek.com/api_keys
2. 创建新的API Key
3. 立即复制（只显示一次！）

### 2. 账户余额不足

**检查步骤**:
1. 登录: https://platform.deepseek.com/
2. 查看右上角余额
3. 如果余额为0，需要充值

**充值方法**:
- 进入"充值"页面
- 支持支付宝/微信支付
- 最低充值金额参考官网

### 3. API端点验证

**手动测试API**:
```bash
# 替换 YOUR_API_KEY 为你的真实密钥
curl https://api.deepseek.com/v1/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek-chat",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant"},
      {"role": "user", "content": "Hello"}
    ]
  }'
```

**预期结果**:
- ✅ 成功: 返回JSON响应，包含 `choices` 数组
- ❌ 401: 返回错误消息，检查密钥

### 4. 网络问题

**测试连通性**:
```bash
# 测试能否访问DeepSeek
curl -I https://api.deepseek.com

# 应该返回 200 或 301/302
```

## 🛠️ 详细调试步骤

### 步骤1: 验证API密钥格式

打开浏览器开发者工具 (F12)，查看Network标签：

1. 发送一条消息
2. 找到 `/api/chat` 请求
3. 查看Request Headers中的payload
4. 确认 `api_key` 字段是否正确

### 步骤2: 查看服务器日志

服务器终端会显示详细错误：
```
Error in chat endpoint: {
  'error': "Client error '401 Unauthorized'",
  'type': 'HTTPStatusError',
  ...
}
```

### 步骤3: 使用官方SDK测试

创建测试文件 `test_deepseek_direct.py`:

```python
# pip install openai
import os
from openai import OpenAI

# 替换为你的真实API密钥
client = OpenAI(
    api_key="sk-your-real-key-here",
    base_url="https://api.deepseek.com"
)

try:
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": "Hello"},
        ],
        stream=False
    )
    print("✓ Success!")
    print(response.choices[0].message.content)
except Exception as e:
    print("✗ Error:", e)
```

运行:
```bash
python test_deepseek_direct.py
```

如果这个也失败，说明是API密钥或账户问题。

## 🔧 解决方案

### 方案1: 重新生成API密钥

1. 访问: https://platform.deepseek.com/api_keys
2. 删除旧密钥
3. 创建新密钥
4. 复制新密钥到配置中
5. 重新保存配置

### 方案2: 检查账户状态

```bash
# 使用API检查账户信息
curl https://api.deepseek.com/v1/user/balance \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### 方案3: 清除浏览器缓存

1. F12 打开开发者工具
2. Application → Storage → Clear site data
3. 刷新页面
4. 重新配置

### 方案4: 使用环境变量

创建 `.env` 文件:
```bash
DEEPSEEK_API_KEY=sk-your-real-key-here
```

更新配置读取环境变量（可选）。

## 📝 常见错误消息

### 错误1: "Invalid API key"
**原因**: 密钥格式错误或已失效
**解决**: 重新生成密钥

### 错误2: "Insufficient balance"
**原因**: 账户余额不足
**解决**: 充值账户

### 错误3: "Rate limit exceeded"
**原因**: 请求过于频繁
**解决**: 等待几分钟后重试

### 错误4: "Model not found"
**原因**: 模型名称错误
**解决**: 确认使用 `deepseek-chat` 或 `deepseek-coder`

## ✅ 验证修复

修复后测试：

```bash
# 1. 重启服务器
python run.py

# 2. 访问浏览器
http://localhost:8000

# 3. 配置DeepSeek
Provider: deepseek
API Key: sk-your-new-key
Model: deepseek-chat

# 4. 发送测试消息
"你好"

# 5. 检查响应
# 应该收到正常回复，没有401错误
```

## 🆘 仍然无法解决？

### 收集诊断信息

1. **API密钥格式**:
   ```
   是否以 sk- 开头？
   长度是否正确？
   ```

2. **账户状态**:
   ```
   余额是多少？
   是否已实名认证？
   ```

3. **错误信息**:
   ```
   完整的服务器错误日志
   浏览器控制台错误
   ```

4. **测试结果**:
   ```bash
   # 运行测试
   python test_deepseek_direct.py
   # 粘贴输出结果
   ```

### 联系支持

如果以上都无法解决：
- DeepSeek官方文档: https://platform.deepseek.com/api-docs/
- 查看项目TROUBLESHOOTING.md
- 检查是否有网络代理/防火墙阻止

## 💡 Pro Tips

1. **测试时先用小额充值**: 测试成功后再充值更多
2. **保存密钥**: 密钥只显示一次，立即保存到安全位置
3. **定期检查余额**: 避免使用中突然余额不足
4. **使用不同模型**: 如果 `deepseek-chat` 有问题，试试 `deepseek-coder`

---

**最后更新**: 2024-12-09
**相关文档**: DEEPSEEK_GUIDE.md, TROUBLESHOOTING.md
