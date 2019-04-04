#print("www.tacoma.uw.edu")
#print("")

#UW Websites
uw_websites={}
uw_websites["Academics"]="http://www.tacoma.uw.edu/about-uw-tacoma/uw-tacoma-academic-listings"
#print(uw_websites)
#print("")

uw_websites["UW Home"]="http://www.tacoma.uw.edu"
#print(uw_websites)
#print("")

uw_websites["Job at UWT"]="https://www.tacoma.uw.edu/human-resources/employment"
#print(uw_websites)
#print("")

uw_websites["Admissions"]="http://www.tacoma.uw.edu/admissions-home"
#print(uw_websites)
#print("")

uw_websites["Global Affairs"]="http://www.tacoma.uw.edu/global-affairs/global-affairs-home"
#print(uw_websites)
#print("")

uw_websites["About UW Tacoma"]="https://www.tacoma.uw.edu/about-uw-tacoma/about-university-washington-tacoma"
#print(uw_websites)
#print("")

uw_websites["Transfer Students"]="https://www.tacoma.uw.edu/admissions/transfer-admission"
#print(uw_websites)
#print("")
print("Here are the possible websites you can see:\nUW Home"
      "\nAcademics\nJob at UWT\nAdmissions\nGlobal Affairs\nAbout UW Tacoma"
      "\nTransfer Students")
print("")

website=str(input("What website would you like to see? "))

print(uw_websites[website])
