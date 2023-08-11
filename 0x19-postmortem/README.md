# Server error incident report

>By development team (codepraycode)

<img src="https://miro.medium.com/v2/resize:fit:720/format:webp/1*mCZbuIctkZslJgHp7wjVjw.png" alt="hero-img" align="center"/>

Earlier today, we experienced a break in operation as there was a critical exception on an endpoint in our server. We understand that this has caused issues for our users, and we apologize for every inconvenience.

## Issue Summary

From 8:30 AM (WAT) to 12:15 PM (WAT), requests to login responded with a response of 500 (Server error). Every of our users could not authenticate. The cause of this was a runtime exception in the logic that processes authentication, however , users whose session was still valid before the time of incident could still continue to use our services.

## Timeline (all in West African Time)

- 8:30 AM — The issues was first detected by monitoring system, and alert was sent to the team.

- 9:00 AM — The team got the alert, and attempted restarting the server, but that attempt didn’t resolve it.

- 9:15 AM — The team set the login page to “Under maintenance” and pushed to production, so users don’t get to attempt authenticating, but wait till maintenance is completed.

- 9:17 AM — The team began investigation and resolution of the issue.

- 10:15 AM — The team identified the issue as it had to do with recent database migration. The team resolved it, and began testing.

- 11:10 AM — Reviewed updates and integrated bug fixes.

- 11:12 AM — Restarted server again.

- 11:17 AM — 100% back online and working.

## Root cause

In the previous update pushed to production on 6th August, 2023 8:12 PM (WAT), there was a change in the database schema of User model, where a some fields were deprecated, which implies that some fields were deleted as they were deprecated due to the updated requirement, one of those fields was still been used in the logic for authentication which raised an exception, causing the server to respond with a response 500 (server error).

In resolving this issue, the team took down the login page, and replaced it with a maintenance screen, so as to keep users from authenticating, then we tested the endpoint so as to see the traceback of the exception, we traced it, and found the bug.

We then identified the deprecated field that was queried, removed it, and developed a patch to resolve it. we tested it, made sure it was working, integrated it, and pushed to production. We took down the maintenance screen and restored the login screen.

## Corrective and preventative measures must contain

We’ve conducted an internal review and analysis of our codes, and attempted to find out underlying issues that could have occurred due to the update pushed on the 6th August, 2023 8:12 PM(WAT).

- Conducted full code reviews.
- Updated all test cases, added more tests
- Setup error management mechanism so users don’t get to see the ugly side of bugs on their screens.
- Setup a mechanism for users to message us as soon as they see an issue.
- Designated a team member to watch out for bugs and alert the team (in person, by call, by chat system) on time, so as to begin resolution earlier.

We are committed to offering a clean, safe and reliable service to our users, we appreciate your patience and again apologize for the impact of the incident on you, thank you.

Sincerely,
