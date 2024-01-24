from datetime import datetime, timezone, timedelta
print((datetime.utcnow() + timedelta(hours=9)).strftime("%Y-%m-%d"))