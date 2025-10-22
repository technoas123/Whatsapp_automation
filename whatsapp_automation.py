import pandas as pd
import pywhatkit as kit
import time

# Read the contact list
data = pd.read_excel("contacts.xlsx", engine="openpyxl")

# CORRECTED: Remove {link} from message template
group_link = "https://chat.whatsapp.com/BCjtXjrM9Hg3Zlu46rSMsY"
message_template = "Hello {name},\n njn ECE 4rth year Ahammed aan, Makethon nte group leek ii link vech join cheyyuka.....!\nJoin here: https://chat.whatsapp.com/BCjtXjrM9Hg3Zlu46rSMsY"

# Set your country code (e.g., +91 for India)
country_code = "+91"

# Loop through all contacts
for i, row in data.iterrows():
    name = str(row["Name"])
    phone = str(row["Phone"])

    # Skip if phone is missing or invalid
    if pd.isna(phone) or not phone.isdigit():
        continue

    # Now this will work since we only use {name}
    message = message_template.format(name=name)
    full_number = country_code + phone

    print(f"📤 Sending to {name} ({full_number})...")

    try:
        # Send message instantly (0 hour, 0 minute means send now)
        kit.sendwhatmsg_instantly(full_number, message, wait_time=40, tab_close=True)

        # Wait extra time between sends to allow WhatsApp to load properly
        time.sleep(15)  # Increased from 8 → 15 seconds

    except Exception as e:
        print(f"⚠️ Failed for {name}: {e}")
        time.sleep(10)