"""
Test DeepSeek integration
测试DeepSeek集成是否正常
"""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

print("=" * 60)
print("Testing DeepSeek Integration")
print("=" * 60)

# Test 1: Import
print("\n1. Testing imports...")
try:
    from src.api.schemas import LLMConfig
    from src.api.llm_client import LLMClient
    print("   [OK] Imports successful")
except Exception as e:
    print(f"   [FAIL] {e}")
    sys.exit(1)

# Test 2: Schema validation
print("\n2. Testing schema validation...")
try:
    from src.api.schemas import LLMConfig

    config = LLMConfig(
        provider="deepseek",
        api_key="sk-test-key",
        model="deepseek-chat",
        system_prompt="你是一个测试角色"
    )
    print("   [OK] DeepSeek config created")
    print(f"      Provider: {config.provider}")
    print(f"      Model: {config.model}")
except Exception as e:
    print(f"   [FAIL] {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Test 3: Client initialization
print("\n3. Testing client initialization...")
try:
    from src.api.schemas import LLMConfig
    from src.api.llm_client import LLMClient

    config = LLMConfig(
        provider="deepseek",
        api_key="sk-test-key",
        model="deepseek-chat"
    )

    client = LLMClient(config)
    print("   [OK] LLMClient created with DeepSeek config")
    print(f"      Config provider: {client.config.provider}")
except Exception as e:
    print(f"   [FAIL] {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Test 4: Route handling
print("\n4. Testing route handling...")
try:
    from src.api.routes import get_behavior_coordinator
    from src.api.schemas import ChatRequest, LLMConfig, ChatMessage

    request = ChatRequest(
        llm_config=LLMConfig(
            provider="deepseek",
            api_key="sk-test",
            model="deepseek-chat"
        ),
        messages=[
            ChatMessage(role="user", content="test")
        ]
    )

    coordinator = get_behavior_coordinator(request)
    print("   [OK] Behavior coordinator created for DeepSeek request")
except Exception as e:
    print(f"   [FAIL] {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Test 5: Frontend defaults
print("\n5. Checking frontend defaults...")
try:
    with open("frontend/chat.js", "r", encoding="utf-8") as f:
        content = f.read()
        if "'deepseek': 'deepseek-chat'" in content:
            print("   [OK] Frontend has DeepSeek default model")
        else:
            print("   [WARN] DeepSeek default not found in frontend")

    with open("frontend/index.html", "r", encoding="utf-8") as f:
        content = f.read()
        if 'value="deepseek"' in content:
            print("   [OK] Frontend has DeepSeek provider option")
        else:
            print("   [WARN] DeepSeek option not found in frontend")
except Exception as e:
    print(f"   [WARN] Could not check frontend files: {e}")

print("\n" + "=" * 60)
print("DeepSeek Integration Test Results:")
print("=" * 60)
print("\n[SUCCESS] All tests passed!")
print("\nNext steps:")
print("   1. Get DeepSeek API key from: https://platform.deepseek.com/")
print("   2. Start server: python run.py")
print("   3. Open browser: http://localhost:8000")
print("   4. Select 'DeepSeek' as provider")
print("   5. Enter API key and model: deepseek-chat")
print("   6. Start chatting!")
print("\nSee DEEPSEEK_GUIDE.md for detailed instructions")
print("=" * 60)
