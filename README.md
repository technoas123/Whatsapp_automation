# WhatsApp Group Invite Automation

A Python script to automate sending WhatsApp group invitations to multiple contacts from an Excel file. This tool helps streamline the process of inviting people to your WhatsApp groups without manual messaging.

##  Features

- **Bulk Messaging**: Send personalized invitations to multiple contacts
- **Excel Integration**: Read contacts from Excel files
- **Personalization**: Custom messages with contact names
- **Error Handling**: Robust error handling and logging
- **Progress Tracking**: Real-time progress updates
- **Detailed Reporting**: Success/failure reports with statistics
- **Rate Limiting**: Prevents spam detection with configurable delays

##  Prerequisites

- Python 3.7 or higher
- WhatsApp Web account
- Chrome browser installed
- Active internet connection

##  Installation

1. **Clone or download the script**
```bash
git clone <this-repo-url>
cd whatsapp-automation
```

2. **Install required packages**
```bash
pip install pandas pywhatkit openpyxl
```

3. **Prepare your contacts file**
   - Create an Excel file named `contacts.xlsx`
   - Ensure it has two columns: `Name` and `Phone`
   - Save it in the same directory as the script

##  File Structure

```
whatsapp-automation/
├── whatsapp_automation.py    # Main script
├── contacts.xlsx            # Contacts file (you create this)
└── README.md
```

##  Excel File Format

Your `contacts.xlsx` should look like this:

| Name | Phone |
|------|-------|
| John Doe | 9876543210 |
| Jane Smith | 9123456789 |
| Bob Johnson | 9988776655 |

**Note**: Phone numbers should be without country code (script adds +91 automatically)

## ⚙️ Configuration

### Message Template
Edit the `MESSAGE_TEMPLATE` in the script to customize your invitation:

```python
MESSAGE_TEMPLATE = """Hello {name},

njn ECE 4rth year Ahammed aan, Makethon nte group leek ii link vech join cheyyuka.....!

Join here: https://chat.whatsapp.com/BCjtXjrM9Hg3Zlu46rSMsY"""
```

### Key Settings
You can modify these variables in the `main()` function:
- `COUNTRY_CODE`: Country code (default: "+91" for India)
- `WAIT_TIME_BETWEEN_MESSAGES`: Delay between messages (default: 15 seconds)
- `EXCEL_FILE`: Your contacts file name (default: "contacts.xlsx")

##  Usage

1. **Prepare your environment:**
   - Ensure you're logged into WhatsApp Web in your browser
   - Keep your browser open
   - Have stable internet connection

2. **Run the script:**
```bash
python whatsapp_automation.py
```

3. **Follow the prompts:**
   - The script will check dependencies
   - Ask for confirmation to start
   - Show real-time progress

4. **Monitor the process:**
   - Watch progress in terminal
   - Check logs in `logs/` directory
   - Review reports in `reports/` directory

## 📈 Output

The script generates:

### Console Output
```
 WhatsApp Automation Script Starting...
 All dependencies check passed!
  Make sure you are logged into WhatsApp Web in your default browser
Press Enter to start sending messages...

 Reading contacts from contacts.xlsx
 Found 50 contacts to process
 Processing 1/50: John Doe
 Sending message to John Doe (+919876543210)
 Successfully sent message to John Doe
 Waiting 15 seconds before next message...
```


##  Important Notes

### Legal & Ethical Usage
- ✅ **DO**: Use for legitimate group invitations
- ✅ **DO**: Get consent where appropriate
- ✅ **DO**: Respect privacy and communication preferences
- ❌ **DON'T**: Use for spam or unsolicited messages
- ❌ **DON'T**: Violate WhatsApp's Terms of Service

### Technical Limitations
- Requires active WhatsApp Web session
- May need re-authentication if session expires
- Rate limiting to prevent account flags
- Dependent on browser automation stability

### Best Practices
1. **Test with small groups first**
2. **Keep message delays reasonable** (15-30 seconds)
3. **Verify your contacts list** before running
4. **Monitor the process** for any issues
5. **Keep your browser visible** during execution

##  Troubleshooting

### Common Issues

**QR Code Not Scanning**
- Refresh WhatsApp Web page
- Ensure browser is updated
- Check internet connection

**Messages Not Sending**
- Verify phone number formats
- Check if contacts exist in WhatsApp
- Ensure message content is allowed

**Script Crashes**
- Check `logs/whatsapp_automation.log`
- Verify Excel file format
- Ensure all dependencies installed

**Browser Not Opening**
- Set default browser in system settings
- Check if browser is properly installed
- Verify no firewall blocking

### Debug Mode
Check the generated log files in `logs/` directory for detailed error information.

##  Security & Privacy

- No data is stored permanently
- Phone numbers are processed locally
- No external API calls
- All operations happen in your local environment

##  License

This project is for educational and legitimate automation purposes. Users are responsible for complying with WhatsApp's Terms of Service and applicable laws.

##  Contributing

Feel free to:
- Report bugs
- Suggest enhancements
- Submit pull requests
- Share your use cases

##  Support

If you encounter issues:
1. Check the troubleshooting section above
2. Examine the log files in `logs/` directory
3. Verify your Excel file format
4. Ensure all dependencies are installed

---

** If this project helped you, please give it a star!**

