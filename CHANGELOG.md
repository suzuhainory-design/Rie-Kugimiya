# Changelog

All notable changes to this project will be documented in this file.

## [1.2.0] - 2024-12-09

### Added
- ✅ 播放序列数据结构（send/pause/recall），前端严格按时间轴展示
- ✅ 迷你分段模型HTTP接口，支持失败自动切回标点规则
- ✅ 单消息postfix处理（移除结尾逗号/句号）

### Changed
- ♻️ 移除所有打字动画/指示器，改为微信式一次性播放体验
- ♻️ API响应中的 `MessageAction` 精简为 `send/pause/recall` + `duration/message_id`
- ♻️ 前端 `chat.js`、文档、测试全面同步新设计

### Fixed
- 🛠️ 多文档存在的旧设计描述已更新，避免与现有实现冲突

## [1.1.0] - 2024-12-09

### Added
- ✨ **DeepSeek API支持**
  - 添加DeepSeek作为新的LLM provider选项
  - 国内用户友好的高性能选择
  - 支持 `deepseek-chat` 和 `deepseek-coder` 模型
- 📚 **DeepSeek完整文档** (`DEEPSEEK_GUIDE.md`)
  - 详细的配置指南
  - 使用示例和最佳实践
  - 常见问题解答
- 🧪 **DeepSeek集成测试** (`test_deepseek.py`)
  - 自动化测试DeepSeek集成
  - 验证所有组件正常工作

### Changed
- 🔧 前端Provider选择器增加DeepSeek选项
- 📝 更新所有文档提及DeepSeek
- 🌐 优化国内用户体验

### Fixed
- 🐛 改进错误处理，显示详细错误类型
- 🔍 前端错误消息更友好（区分401/404/500）
- 📋 添加缺失的`__init__.py`文件

## [1.0.0] - 2024-12-09

### Added
- 🎉 初始版本发布
- 🤖 多LLM支持（OpenAI、Anthropic、Custom）
- 🧠 完整的消息行为系统
  - 智能分段（规则基 + ML接口）
  - 情感检测（7种情绪状态）
  - 错别字注入（基于情绪的概率模型）
  - 撤回重发系统
  - 停顿预测
- 💻 现代化Web界面
  - （旧版本）打字动画效果
  - （旧版本）打字指示器
  - 撤回动画
  - 情绪颜色指示
- 📚 完整文档
  - 实现指南 (IMPLEMENTATION.md)
  - 安装指南 (SETUP.md)
  - API示例 (API_EXAMPLES.md)
  - 快速开始 (QUICKSTART.md)
  - 故障排除 (TROUBLESHOOTING.md)
- 🧪 测试套件
  - 单元测试
  - 集成测试
  - 组件测试脚本

### Technical
- FastAPI异步后端
- Pydantic数据验证
- HTTPX异步HTTP客户端
- 模块化架构设计
- ML模型接入接口

---

## Future Plans

### [1.2.0] - 数据处理
- [ ] LCCC数据集下载和预处理
- [ ] 训练数据生成
- [ ] 数据增强

### [1.3.0] - ML模型训练
- [ ] BiLSTM-CRF模型实现
- [ ] 分段模型训练
- [ ] 停顿预测模型训练

### [2.0.0] - 高级功能
- [ ] 对话历史分析
- [ ] 用户行为偏好学习
- [ ] 多语言支持扩展
- [ ] 语音合成集成
