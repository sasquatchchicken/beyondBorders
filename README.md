# beyondBorders


**automatic-telegram.py** stands as a Python script meticulously crafted to unveil potential vulnerabilities within web applications through strategic manipulation of cookies. Developed as a response to the discovery of a vulnerability during a bug bounty exploration, this script harnesses the power of Selenium with Python. Its orchestration of actions unravels security risks, specifically targeting access controls and session management.

## Key Features
**Geolocation Diversity:** Generates a random UUID with a non-US IPv4 address, adding an extra layer of obfuscation to malicious activities.

**Headless Browser Automation:** Utilizes Selenium to launch a headless browser, navigating to the target URL without a graphical interface.

**Dynamic Cookie Manipulation:** Crafts and injects a payload into 'browserID' and 'country' cookies, potentially compromising access controls.

## Usage

    python automatic-telegram.py

### Demonstration
**Geolocation Information:** Displays the geolocation information based on the dynamically generated non-US IPv4 address.

**Headless Browser Action:** Utilizes a headless browser to navigate to the specified target URL and perform cookie manipulations.

**Cookie Management:** Deletes specified cookies and injects a crafted payload to 'browserID' and 'country' cookies.

### Threat Model Overview
#### Target Profile
The target is a web application susceptible to manipulation of cookies, with specific focus on the 'browserID' and 'country' cookies. This threat model assumes an advanced adversary seeking unauthorized access, compromising access controls, and potentially breaching user sessions.

#### Threat Actor
The threat actor in this scenario is a sophisticated attacker with an understanding of web security, utilizing advanced techniques to exploit vulnerabilities. The actor employs the "automatic-telegram.py" script to manipulate cookies and orchestrate unauthorized access to the target web application.

#### Tactics, Techniques, and Procedures (TTP)

***Tactic:*** Cookie Manipulation

***Technique 1:*** Dynamic Geolocation Diversity


Procedure: Generates a random UUID with a non-US IPv4 address for enhanced obfuscation.


***Technique 2:*** Headless Browser Automation


Procedure: Utilizes Selenium with Python to launch a headless browser, navigating to the target URL without a graphical interface.


***Technique 3:*** Dynamic Cookie Manipulation


Procedure: Crafts and injects a payload into 'browserID' and 'country' cookies, potentially compromising access controls.


***Tactic:*** Unauthorized Access

***Technique 4:*** Silent Overwriting


Procedure: Deletes specified cookies and silently overwrites them with a crafted payload, potentially leading to unauthorized access.

### Impact

***The impact of successful execution of the script includes:***

Unauthorized access to restricted areas within the web application.

Subversion of access controls, potentially allowing the adversary to perform actions beyond their authorized scope.

Compromise of user sessions, raising concerns about the integrity of user identification and activities.

***Threat Scenario***
The adversary employs "automatic-telegram.py" to exploit vulnerabilities within the target web application. The script strategically manipulates cookies, focusing on 'browserID' and 'country' cookies, with the ultimate goal of achieving unauthorized access and compromising access controls.

### Risk Assessment
***Impact:*** High - Critical

Unauthorized access may result in unauthorized actions or resource access, potentially compromising sensitive user information.

***Probability:*** Moderate to High

The likelihood of success depends on the effectiveness of existing security measures and the ability of the adversary to evade detection.

***In my case it was successful within the bounds of the bug bounty***

### Mitigation Strategies
***Enhanced Cookie Security Measures:***

Implement robust mechanisms to detect and prevent unauthorized modifications of cookies.

***Regular Session Management Audits:***

Conduct frequent and thorough reviews of session management mechanisms to identify and rectify potential vulnerabilities.

***Injection Vulnerability Mitigation:***

Strengthen input validation and sanitization practices to mitigate potential injection vulnerabilities.

***Access Controls Fortification:***

Regularly review and reinforce access control mechanisms to fortify defenses against unauthorized access.

### Conclusion
Threat actors leveraging this tool can exploit vulnerabilities, demanding a robust defense strategy to safeguard against unauthorized access and potential breaches of sensitive information. Advanced threat hunters should be vigilant, employing comprehensive mitigation strategies to counteract the threat posed by this TTP.
