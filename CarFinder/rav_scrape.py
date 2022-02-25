import requests
from bs4 import BeautifulSoup
import re
import time

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/75.0.3770.80 Safari/537.36"
}

output = open("info.txt", "w")

print("Starting to scrape info...")
start = time.time()

page = requests.get("https://www.carcomplaints.com/Toyota/RAV4/", headers=headers)
parsed_page = BeautifulSoup(page.content, "html.parser")

for car in parsed_page.find_all("li"):
    if (car.get("class") == ["even"]) or (car.get("class") == ["odd"]):
        year = re.findall(r"\d\d\d\d", str(car))[0]
        problems = re.findall(r'class="count">\d+', str(car))[0]
        problems = problems[14:]
        output.write("\n"+str(year) + ": " + str(problems)+"\n")

        year_data = requests.get("https://www.carcomplaints.com/Toyota/RAV4/" + str(year) + "/", headers=headers)
        year_parsed = BeautifulSoup(year_data.content, "html.parser")

        for issue in year_parsed.find_all("li"):
            if ((issue.get("class") != None) and (issue.get("class") != ["menu"]) and (issue.get("class") != ["hidden"]) and (issue.get("class") != ["right"])):
                issueType = issue.get("class")[0]
                output.write("\t" + issueType+"\n")

                nhtsa = re.findall(r"ints: \d+", str(issue))
                if nhtsa == []:
                    nhtsa = 0
                else:
                    nhtsa = str(nhtsa[0])[6:]
                output.write("\t\tNHTSA Complaints: " + str(nhtsa)+"\n")

                issue_data = requests.get(
                    "https://www.carcomplaints.com/Toyota/RAV4/"+str(year)+"/"+str(issueType)+"/",
                    headers=headers,
                )
                issue_parsed = BeautifulSoup(issue_data.content, "html.parser")

                for badThing in issue_parsed.find_all("li"):
                    if re.findall(r'id="bar\d+"', str(badThing)):
                        if re.findall(r"[nN][hH][tT][sS][aA]", str(badThing)):
                            problem = re.findall(r"NHTSA: .+?<", str(badThing))[0][7:-1]
                            amount = re.findall(r"span>\d+", str(badThing))[0][5:]
                            output.write("\t\t\t" + problem + " - " + str(amount)+"\n")

                user_comp = re.findall(r"<span>\d+", str(issue))
                if user_comp == []:
                    user_comp = 0
                else:
                    user_comp = str(user_comp[0])[6:]
                output.write("\t\tUser Complaints: " + str(user_comp)+"\n")

                for badThing in issue_parsed.find_all("li"):
                    if re.findall(r'id="bar\d+"', str(badThing)):
                        if badThing.get("class") == []:
                            problem = re.findall(r"<strong>.+?<", str(badThing))[0][8:-1]
                            amount = re.findall(r"span>\d+", str(badThing))[0][5:]
                            output.write("\t\t\t" + problem + " - " + str(amount)+"\n")

output.close()
end = time.time()
print("Finished in "+ str(end-start)+ " seconds")
