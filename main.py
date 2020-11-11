from configs import config
from src import clocWrapper
from src import emailSender

repoURL = config.public["CLOC"]["repositoryURL"]

messageBody = f"Target repository: {repoURL}\n"
messageBody += clocWrapper.cloneGit(repoURL)
print(messageBody)

recipientEmail = config.public["email"]["recipient"]
if recipientEmail != "":
    messageSubject = "GitHub CLOC Scan Results"
    emailSender.send(recipientEmail, messageSubject, messageBody)
    