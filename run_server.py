#!/usr/bin/env python3
"""
Stable GasFill Server Launcher
No auto-reload, minimal dependencies
"""

import os
import sys
from pathlib import Path

def main():
    """Main function to start server"""
    print("🚀 Starting GasFill Server (Stable Mode)")
    print("=" * 50)
    
    # Set environment variables to prevent auto-reload issues
    os.environ["PYTHONUNBUFFERED"] = "1"
    os.environ["UVICORN_LOG_LEVEL"] = "info"
    
    # Change to the correct directory
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    try:
        # Direct import and execution
        from python_server import app
        import uvicorn
        
        print("✅ Server modules loaded successfully")
        print("📊 Starting on http://127.0.0.1:5002")
        print("🔄 Health: http://127.0.0.1:5002/api/health")
        print("📚 Docs: http://127.0.0.1:5002/api/docs")
        print("-" * 50)
        
        # Start with minimal configuration
        uvicorn.run(
            app,
            host="127.0.0.1",
            port=5002,
            reload=False,
            log_level="info",
            access_log=False,  # Disable access logs for stability
            workers=1
        )
        
    except KeyboardInterrupt:
        print("\n🛑 Server stopped")
    except Exception as e:
        print(f"❌ Error: {e}")
        print(f"💡 Try: pip install fastapi uvicorn pydantic pyjwt")
        sys.exit(1)

if __name__ == "__main__":
    main()