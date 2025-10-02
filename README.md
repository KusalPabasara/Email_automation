# Email Automation Setup

## 📌 Introduction
This project automates the process of sending emails with attachments.  
Before running the script, you **must prepare the required files and directories** as described below.

---

## 📝 Step 1: Create the Data File

You need to create either a `.xlsx` **or** `.txt` file that contains the following columns:

- **Name** (optional if script uses it)
- **Email** (recipient email address)
- **Attachment Path** (full or relative path to the file in the attachments folder)

### Example (`emails.xlsx`):

| Name     | Email                | Attachment Path                  |
|----------|----------------------|----------------------------------|
| John Doe | johndoe@email.com    | attachments/report1.pdf          |
| Jane Doe | janedoe@email.com    | attachments/invoice2.pdf         |

### Example (`emails.txt`):
