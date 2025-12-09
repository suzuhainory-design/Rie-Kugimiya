"""Simple API test"""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

print("=" * 60)
print("Testing API Components")
print("=" * 60)

# Test 1: Import app
print("\n1. Testing FastAPI app import...")
try:
    from src.api.main import app
    print("   [OK] FastAPI app imported")
except Exception as e:
    print(f"   [FAIL] {e}")
    import traceback
    traceback.print_exc()

# Test 2: Import behavior
print("\n2. Testing behavior system import...")
try:
    from src.behavior import BehaviorCoordinator
    from src.behavior.models import BehaviorConfig
    print("   [OK] Behavior system imported")
except Exception as e:
    print(f"   [FAIL] {e}")
    import traceback
    traceback.print_exc()

# Test 3: Create coordinator
print("\n3. Testing behavior coordinator creation...")
try:
    from src.behavior import BehaviorCoordinator
    from src.behavior.models import BehaviorConfig

    config = BehaviorConfig()
    coordinator = BehaviorCoordinator(config=config)
    print("   [OK] BehaviorCoordinator created")
except Exception as e:
    print(f"   [FAIL] {e}")
    import traceback
    traceback.print_exc()

# Test 4: Process message
print("\n4. Testing message processing...")
try:
    from src.behavior import BehaviorCoordinator
    from src.behavior.models import BehaviorConfig

    config = BehaviorConfig(enable_typo=False)
    coordinator = BehaviorCoordinator(config=config)

    segments = coordinator.process_message("Hello, this is a test!")
    print(f"   [OK] Processed into {len(segments)} segment(s)")

    for i, seg in enumerate(segments[:3]):  # Show first 3
        print(f"      - Segment {i+1}: '{seg.text}' (pause: {seg.pause_before:.2f}s)")

except Exception as e:
    print(f"   [FAIL] {e}")
    import traceback
    traceback.print_exc()

# Test 5: Routes
print("\n5. Testing API routes...")
try:
    from src.api.routes import router
    print(f"   [OK] Router has {len(router.routes)} route(s)")
    for route in router.routes:
        if hasattr(route, 'path'):
            print(f"      - {route.path}")
except Exception as e:
    print(f"   [FAIL] {e}")
    import traceback
    traceback.print_exc()

# Test 6: Frontend files
print("\n6. Checking frontend files...")
frontend_files = ["frontend/index.html", "frontend/chat.js", "frontend/styles.css"]
for f in frontend_files:
    exists = os.path.exists(f)
    status = "[OK]" if exists else "[MISSING]"
    print(f"   {status} {f}")

print("\n" + "=" * 60)
print("Test completed!")
print("=" * 60)
