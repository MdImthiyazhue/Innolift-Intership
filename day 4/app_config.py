# Day 4 - Task 4
# App Configuration using Tuple

# Tuple containing fixed application settings
APP_CONFIG = ("v1.0.3", "en", 30)
# (Version, Language, Session Timeout in Minutes)

print("===== APPLICATION CONFIGURATION =====")

print(f"Version           : {APP_CONFIG[0]}")
print(f"Language          : {APP_CONFIG[1]}")
print(f"Session Timeout   : {APP_CONFIG[2]} minutes")

# The following line would cause an error because tuples are immutable.
# APP_CONFIG[0] = "v1.0.4"