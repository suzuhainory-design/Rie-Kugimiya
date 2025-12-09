# 故障排除指南

## 常见问题和解决方案

### 1. 500 Internal Server Error

**症状**: 发送消息后收到"API error: 500"

**可能原因**:
- ❌ API密钥无效或过期
- ❌ 模型名称错误
- ❌ 网络连接问题
- ❌ API额度用尽（OpenAI/Anthropic）
- ❌ 账户余额不足（DeepSeek）
- ❌ Provider配置错误

**解决步骤**:

1. **检查API密钥**
   ```
   - OpenAI: 应该以 sk- 开头
   - Anthropic: 应该以 sk-ant- 开头
   - 确认密钥未过期
   ```

2. **验证模型名称**
   ```
   DeepSeek常用模型:
   - deepseek-chat (推荐，通用对话)
   - deepseek-coder (代码相关)

   OpenAI常用模型:
   - gpt-3.5-turbo
   - gpt-4
   - gpt-4-turbo

   Anthropic常用模型:
   - claude-3-5-sonnet-20241022
   - claude-3-opus-20240229
   ```

3. **检查网络连接**
   ```bash
   # 测试DeepSeek连接（国内推荐）
   curl https://api.deepseek.com/v1/chat/completions \
     -H "Authorization: Bearer YOUR_API_KEY" \
     -H "Content-Type: application/json" \
     -d '{"model":"deepseek-chat","messages":[{"role":"user","content":"hi"}]}'

   # 测试OpenAI连接
   curl https://api.openai.com/v1/models \
     -H "Authorization: Bearer YOUR_API_KEY"

   # 测试Anthropic连接
   curl https://api.anthropic.com/v1/messages \
     -H "x-api-key: YOUR_API_KEY"
   ```

4. **查看服务器日志**
   - 启动服务器时会显示详细错误信息
   - 查看控制台输出的完整traceback

### 2. 404 Not Found

**症状**: 静态文件无法加载，显示404错误

**可能原因**:
- ❌ 前端文件路径配置错误
- ❌ 缺少前端文件

**解决步骤**:

1. **验证前端文件存在**
   ```bash
   # 检查文件
   ls frontend/
   # 应该看到: index.html, chat.js, styles.css
   ```

2. **重启服务器**
   ```bash
   # Ctrl+C 停止当前服务器
   # 然后重新启动
   python run.py
   ```

3. **检查路径**
   ```python
   # 在服务器启动时应该看到:
   # Frontend directory: D:\...\frontend
   # Exists: True
   ```

### 3. 401 Unauthorized

**症状**: "Authentication failed"

**原因**: API密钥无效

**解决方案**:
1. 重新生成API密钥
2. 确保复制完整的密钥（没有多余空格）
3. 清除浏览器localStorage后重新配置

### 4. CORS错误

**症状**: 浏览器控制台显示CORS错误

**解决方案**:
```python
# src/api/main.py 中已经配置了CORS
# 如果仍有问题，确保从 localhost:8000 访问
# 不要使用 127.0.0.1:8000
```

### 5. 导入错误

**症状**: `ModuleNotFoundError` 或 `ImportError`

**解决方案**:
```bash
# 1. 确认在项目根目录
cd D:\Files\Develop Projects\AI\Rie_Kugimiya

# 2. 重新安装依赖
pip install -r requirements.txt

# 3. 检查 __init__.py 文件存在
ls src/__init__.py
ls src/api/__init__.py
ls src/behavior/__init__.py
ls src/utils/__init__.py

# 4. 使用虚拟环境
.venv\Scripts\python run.py
```

### 7. 配置丢失

**症状**: 每次刷新都需要重新配置

**原因**: localStorage未保存

**解决方案**:
1. 检查浏览器是否允许localStorage
2. 不要使用无痕/隐私模式
3. 检查浏览器设置中的Cookie/本地数据设置

## 调试工具

### 1. 运行测试脚本

```bash
# 测试所有组件
python test_api_simple.py

# 应该看到所有 [OK]
```

### 2. 调试模式启动

```bash
# 使用调试脚本启动
python run_debug.py

# 会显示详细的日志信息
```

### 3. 手动测试API

```bash
# 测试健康检查
curl http://localhost:8000/api/health

# 测试聊天接口
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{
    "llm_config": {
      "provider": "openai",
      "api_key": "sk-your-key",
      "model": "gpt-3.5-turbo",
      "system_prompt": "You are helpful."
    },
    "messages": [
      {"role": "user", "content": "Hello"}
    ]
  }'
```

### 4. 查看浏览器控制台

```
1. 按 F12 打开开发者工具
2. 切换到 Console 标签
3. 发送消息
4. 查看错误信息
```

## 性能问题

### 响应慢

**原因**: LLM API响应时间较长

**改善方案**:
1. 使用更快的模型（如gpt-3.5-turbo而不是gpt-4）
2. 缩短system prompt
3. 检查网络连接

### 播放节奏不自然

**原因**: 分段间隔范围设置过小或过大

**解决方案**:
```python
# 在 BehaviorConfig 中调整
config = BehaviorConfig(
    min_pause_duration=0.6,
    max_pause_duration=2.8
)
```

## 获取帮助

如果以上方法都无法解决问题：

1. **收集信息**:
   - 错误消息的完整内容
   - 浏览器控制台的错误日志
   - 服务器控制台的输出
   - 操作系统和Python版本

2. **运行诊断**:
   ```bash
   python test_api_simple.py > diagnosis.txt 2>&1
   ```

3. **查看日志**:
   - 服务器启动日志
   - API调用日志
   - 浏览器Network标签

4. **检查配置**:
   - requirements.txt中的依赖版本
   - Python版本 (需要3.10+)
   - 环境变量设置

## 快速诊断清单

```
□ Python 3.10+ 已安装
□ 依赖包已安装 (pip install -r requirements.txt)
□ 所有 __init__.py 文件存在
□ frontend/ 目录包含所有文件
□ API密钥有效且正确复制
□ 模型名称拼写正确
□ 网络连接正常
□ 防火墙未阻止8000端口
□ 浏览器JavaScript已启用
□ 从 localhost:8000 访问（不是127.0.0.1）
```

## 重新开始

如果问题仍然存在，尝试完全重置：

```bash
# 1. 停止服务器 (Ctrl+C)

# 2. 清除浏览器数据
# 浏览器设置 -> 清除浏览数据 -> localhost

# 3. 重新安装依赖
pip uninstall -r requirements.txt -y
pip install -r requirements.txt

# 4. 重启服务器
python run.py

# 5. 清除浏览器缓存后访问
http://localhost:8000
```
