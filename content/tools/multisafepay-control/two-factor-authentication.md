---
title : "Two-factor authentication"
weight: 100
meta_title: "MultiSafepay Control- 2FA - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
read_more: '.'
description_short: "Two-factor authentication (2FA) requires users to verify their identity with two pieces of evidence. This authentication method is used to add an additional layer of security to your data. At MultiSafepay, the first piece of evidence users are asked to provide is a password. The second piece of evidence is a 6-digit token, generated in the MultiSafepay app on the user's mobile device."
---

Two-factor authentication (2FA) requires users to verify their identity with two pieces of evidence. This authentication method is used to add an additional layer of security to your data. At MultiSafepay, the first piece of evidence users are asked to provide is a password. The second piece of evidence is a 6-digit token, generated in the MultiSafepay app on the user's mobile device.

## How to enable 2FA
Enabling 2FA is a two-step process. First, a user with administrator rights enables 2FA in the user settings. Then, users can individually configure 2FA on their own mobile devices. You can find more detailed steps below.

### Step 1: The administrator's steps
Please note that only a user with administrator rights can perform these steps:  
1. Open the [User Management](https://merchant.multisafepay.com/user-management) page in your MultiSafepay Control
2. Open a user's details by clicking their name
3. Click the drop-down list *Two-factor* and select *Enable*
4. Click *Save changes*

{{< screen src="/gifs/MCP_2FA-1.gif" alt="Enabling Two-factor authentication in MultiSafepay Control" align="center" caption="That's it. Don't forget to click 'Save changes'" >}}

### Step 2: The user's steps
The first time a user logs into MultiSafepay Control after 2FA is enabled, they are asked to configure 2FA. This is done by connecting their MultiSafepay account to their mobile device, following these steps:
1. Log into [MultiSafepay Control](https://merchant.multisafepay.com/) on your laptop or PC. An additional screen asking for a 6-digit token should appear
2. If you have not yet done so, [download](https://docs.multisafepay.com/tools/multisafepay-control-app/how-to-download-the-app/) the MultiSafepay Control app 
3. Log into the MultiSafepay Control app on your mobile device
4. Press *More* in the bottom-right corner
5. Press *Authenticator*
6. Copy the 6-digit token from your mobile device to the 2FA screen on your computer or laptop

{{< screen src="/gifs/MCP_2FA-3.gif" alt="Generating a 6-digit 2FA token the in MultiSafepay Control app" align="center" caption="The 6-digit token remains visible for 30 seconds">}}

### Step 3: Enjoy
Congratulations, 2FA is enabled and configured. You can now enjoy an extra layer of security for your data. 
Please keep in mind that upon every login a newly generated 6-digit token is required.

{{< br >}}
## Frequently asked questions
{{< br >}}

### Can I use one device for multiple users?
Currently one mobile device can only be connected to one user and only one user can be connected to one mobile device. This means there is a unique link between every one user and one device.

### Why can I not enable 2FA for my account?
To enable or disable 2FA, you must have administrator rights. If this doesn't answer your question, please [contact support](support@multisafepay.com)

### What happens after too many failed login attempts?
After 5 unsuccessful 6-digit token inputs, the account is blocked. Only users with administrator rights can unblock accounts. 

### Does every user need to use 2FA?
No, this is not required. 2FA provides an extra layer of security to your data. However, it is not mandatory to enable 2FA on every user account.

### Can I choose a different verification method?
No. Currently we implement 2FA through the use of a password and a 6-digit token. 

### In what countries is 2FA supported?
2FA is supported in every country. The MultiSafepay app is available for [iOS](https://apps.apple.com/nl/app/multisafepay-control/id929955963) and [Android](https://play.google.com/store/apps/details?id=com.multisafepay.control).

### What if a user loses their 2FA device?
If a user loses their 2FA device, disable and re-enable 2FA on their account. Follow [these steps](#how-to-enable-2fa) to do so (this requires administrator's rights). Once 2FA is disabled, the existing connection is broken. The user can now connect a new mobile device to their MultiSafepay Control. If you only have one MultiSafepay user account or in case any other problems arise, please contact support@multisafepay.com
