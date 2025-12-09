"""
Quick API test script
"""
import sys
import os

# Fix Windows console encoding
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

# Add project root to path
sys.path.insert(0, os.path.dirname(__file__))

def test_imports():
    """Test all imports"""
    print("Testing imports...")

    try:
        from src.api.main import app
        print("✓ FastAPI app imported")
    except Exception as e:
        print(f"✗ Failed to import app: {e}")
        return False

    try:
        from src.behavior import BehaviorCoordinator
        print("✓ BehaviorCoordinator imported")
    except Exception as e:
        print(f"✗ Failed to import BehaviorCoordinator: {e}")
        return False

    try:
        from src.api.schemas import ChatRequest, ChatResponse
        print("✓ Schemas imported")
    except Exception as e:
        print(f"✗ Failed to import schemas: {e}")
        return False

    return True

def test_behavior_system():
    """Test behavior system"""
    print("\nTesting behavior system...")

    try:
        from src.behavior import BehaviorCoordinator
        from src.behavior.models import BehaviorConfig

        config = BehaviorConfig()
        coordinator = BehaviorCoordinator(config=config)
        print("✓ BehaviorCoordinator created")

        # Test processing a simple message
        actions = coordinator.process_message("你好，今天天气真好！")
        print(f"? Message processed: {len(actions)} actions")

        for i, action in enumerate(actions[:5]):
            snippet = (action.text or "")[:20]
            print(f"  Action {i+1}: type={action.type} text='{snippet}' duration={action.duration}")

        return True
    except Exception as e:
        print(f"✗ Behavior system error: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_api_routes():
    """Test API route creation"""
    print("\nTesting API routes...")

    try:
        from src.api.routes import router, get_behavior_coordinator
        print("✓ Routes imported")

        # Check routes
        print(f"✓ Router has {len(router.routes)} routes")
        for route in router.routes:
            print(f"  - {route.path} [{', '.join(route.methods)}]")

        return True
    except Exception as e:
        print(f"✗ Routes error: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_frontend_files():
    """Check frontend files exist"""
    print("\nChecking frontend files...")

    frontend_files = [
        "frontend/index.html",
        "frontend/chat.js",
        "frontend/styles.css"
    ]

    all_exist = True
    for file in frontend_files:
        if os.path.exists(file):
            print(f"✓ {file}")
        else:
            print(f"✗ Missing: {file}")
            all_exist = False

    return all_exist

if __name__ == "__main__":
    print("=" * 60)
    print("Rie Kugimiya API Test Suite")
    print("=" * 60)

    results = []

    results.append(("Imports", test_imports()))
    results.append(("Behavior System", test_behavior_system()))
    results.append(("API Routes", test_api_routes()))
    results.append(("Frontend Files", test_frontend_files()))

    print("\n" + "=" * 60)
    print("Test Results:")
    print("=" * 60)

    for name, passed in results:
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"{status}: {name}")

    all_passed = all(r[1] for r in results)

    if all_passed:
        print("\n✓ All tests passed! Server should work correctly.")
        print("\nRun the server with:")
        print("  python run.py")
        print("or")
        print("  .venv/Scripts/python run.py")
    else:
        print("\n✗ Some tests failed. Check errors above.")

    sys.exit(0 if all_passed else 1)
