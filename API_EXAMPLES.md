# API Examples

This document provides practical examples of using the Rie Kugimiya API.

## Basic Chat Request

### Minimal Configuration

```bash
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{
    "llm_config": {
      "provider": "openai",
      "api_key": "your-api-key-here",
      "model": "gpt-3.5-turbo",
      "system_prompt": "You are Rie Kugimiya, a cute and sassy character."
    },
    "messages": [
      {"role": "user", "content": "你好！"}
    ]
  }'
```

### With Behavior Settings

```bash
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{
    "llm_config": {
      "provider": "openai",
      "api_key": "your-api-key-here",
      "model": "gpt-3.5-turbo",
      "system_prompt": "You are Rie."
    },
    "messages": [
      {"role": "user", "content": "今天天气怎么样？"}
    ],
    "behavior_settings": {
      "enable_segmentation": true,
      "enable_typo": true,
      "enable_recall": true,
      "base_typo_rate": 0.1,
      "typo_recall_rate": 0.5
    }
  }'
```

## Provider-Specific Examples

### OpenAI

```python
import httpx
import asyncio

async def chat_with_openai():
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://localhost:8000/api/chat",
            json={
                "llm_config": {
                    "provider": "openai",
                    "api_key": "sk-...",
                    "model": "gpt-3.5-turbo",
                    "system_prompt": "You are a helpful assistant."
                },
                "messages": [
                    {"role": "user", "content": "Hello!"}
                ]
            }
        )
        return response.json()

result = asyncio.run(chat_with_openai())
print(result)
```

### DeepSeek (推荐国内用户)

```python
async def chat_with_deepseek():
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://localhost:8000/api/chat",
            json={
                "llm_config": {
                    "provider": "deepseek",
                    "api_key": "sk-...",
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
```

### Anthropic (Claude)

```python
async def chat_with_claude():
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://localhost:8000/api/chat",
            json={
                "llm_config": {
                    "provider": "anthropic",
                    "api_key": "sk-ant-...",
                    "model": "claude-3-5-sonnet-20241022",
                    "system_prompt": "You are Rie, a virtual character."
                },
                "messages": [
                    {"role": "user", "content": "你好！"}
                ]
            }
        )
        return response.json()

result = asyncio.run(chat_with_claude())
```

### Custom OpenAI-Compatible API

```python
async def chat_with_custom():
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://localhost:8000/api/chat",
            json={
                "llm_config": {
                    "provider": "custom",
                    "api_key": "your-key",
                    "base_url": "https://your-api.com/v1",
                    "model": "your-model-name",
                    "system_prompt": "You are Rie."
                },
                "messages": [
                    {"role": "user", "content": "Hello!"}
                ]
            }
        )
        return response.json()
```

## Response Format

### Typical Response

```json
{
  "actions": [
    {
      "type": "send",
      "duration": 0.0,
      "text": "你好呀！",
      "message_id": "3b4f1c4824f342958eba8b1b64f7d339",
      "target_id": null,
      "metadata": {
        "emotion": "happy",
        "segment_index": 0,
        "total_segments": 2
      }
    },
    {
      "type": "pause",
      "duration": 0.9,
      "text": null,
      "message_id": null,
      "target_id": null,
      "metadata": {
        "reason": "segment_interval",
        "emotion": "happy"
      }
    },
    {
      "type": "send",
      "duration": 0.0,
      "text": "今天过得怎么样？",
      "message_id": "a81c8d0e3e324ce1b0579b71349f3355",
      "target_id": null,
      "metadata": {
        "emotion": "happy",
        "segment_index": 1,
        "total_segments": 2
      }
    }
  ],
  "raw_response": "你好呀！今天过得怎么样？",
  "metadata": {
    "emotion": "happy",
    "segment_count": 2
  }
}
```

### Response with Typo and Recall

```json
{
  "actions": [
    {
      "type": "send",
      "duration": 0.0,
      "text": "你号！",
      "message_id": "d40e61c6d56f434aab786c6fbbd4f122",
      "target_id": null,
      "metadata": {
        "emotion": "neutral",
        "segment_index": 0,
        "total_segments": 1,
        "has_typo": true
      }
    },
    {
      "type": "pause",
      "duration": 1.2,
      "metadata": {
        "reason": "typo_recall_delay"
      }
    },
    {
      "type": "recall",
      "duration": 0.0,
      "message_id": null,
      "target_id": "d40e61c6d56f434aab786c6fbbd4f122",
      "metadata": {
        "reason": "typo_recall"
      }
    },
    {
      "type": "pause",
      "duration": 0.6,
      "metadata": {
        "reason": "typo_retype_wait"
      }
    },
    {
      "type": "send",
      "duration": 0.0,
      "text": "你好！",
      "message_id": "f96705410e7b49c585e453048a98b1ce",
      "target_id": null,
      "metadata": {
        "emotion": "neutral",
        "segment_index": 0,
        "total_segments": 1,
        "is_correction": true
      }
    }
  ],
  "raw_response": "你好！",
  "metadata": {
    "emotion": "neutral",
    "segment_count": 2
  }
}
```

## Behavior Configuration

### Disable All Behaviors (Direct LLM Output)

```json
{
  "llm_config": {...},
  "messages": [...],
  "behavior_settings": {
    "enable_segmentation": false,
    "enable_typo": false,
    "enable_recall": false,
    "enable_emotion_detection": false
  }
}
```

### High Typo Rate (Testing)

```json
{
  "llm_config": {...},
  "messages": [...],
  "behavior_settings": {
    "enable_typo": true,
    "base_typo_rate": 0.3,
    "typo_recall_rate": 0.8
  }
}
```

### Conservative Behavior

```json
{
  "llm_config": {...},
  "messages": [...],
  "behavior_settings": {
    "enable_segmentation": true,
    "enable_typo": true,
    "enable_recall": true,
    "base_typo_rate": 0.03,
    "typo_recall_rate": 0.2
  }
}
```

## Error Handling

### Invalid API Key

```json
{
  "detail": "HTTP error: 401"
}
```

### Invalid Model Name

```json
{
  "detail": "HTTP error: 404"
}
```

### Missing Required Fields

```json
{
  "detail": [
    {
      "loc": ["body", "llm_config", "api_key"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

## Health Check

```bash
curl http://localhost:8000/api/health
```

Response:
```json
{
  "status": "ok"
}
```

## JavaScript Frontend Example

```javascript
async function sendMessage(text) {
  const config = {
    provider: "openai",
    api_key: "sk-...",
    model: "gpt-3.5-turbo",
    system_prompt: "You are Rie."
  };

  const response = await fetch('http://localhost:8000/api/chat', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      llm_config: config,
      messages: [
        { role: 'user', content: text }
      ]
    })
  });

  const data = await response.json();

  // Play actions sequentially
  for (const action of data.actions) {
    if (action.duration > 0) {
      await sleep(action.duration * 1000);
    }

    switch (action.type) {
      case 'pause':
        // Nothing to render, the await above already handles timing.
        break;
      case 'send':
        appendMessage(action.text, { id: action.message_id });
        break;
      case 'recall':
        removeMessage(action.target_id);
        break;
    }
  }
}
```

## Batch Processing Example

```python
async def process_multiple_messages():
    messages = [
        "你好！",
        "今天天气真好",
        "你喜欢什么？"
    ]

    async with httpx.AsyncClient() as client:
        tasks = []
        for msg in messages:
            task = client.post(
                "http://localhost:8000/api/chat",
                json={
                    "llm_config": {...},
                    "messages": [{"role": "user", "content": msg}]
                }
            )
            tasks.append(task)

        responses = await asyncio.gather(*tasks)
        return [r.json() for r in responses]
```

## Tips

1. **Rate Limiting**: Be mindful of your LLM provider's rate limits
2. **Error Handling**: Always handle potential API errors
3. **Caching**: Consider caching config to avoid repeated API calls
4. **Timeouts**: Set appropriate timeouts for long-running requests
5. **Behavior Tuning**: Adjust behavior settings based on use case
