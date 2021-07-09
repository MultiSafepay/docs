---
title : "Enabling two-factor authentication"
weight: 50
meta_title: "MultiSafepay account - Enabling two-factor authentication - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: '.'
description_short: "Two-factor authentication (2FA) requires users to verify their identity with two pieces of evidence. This authentication method is used to add an additional layer of security to your data. At MultiSafepay, the first piece of evidence users are asked to provide is a password. The second piece of evidence is a 6-digit token, generated in the MultiSafepay app on the user's mobile device."
aliases:
    - /tools/multisafepay-contro/two-factor-authentication
    - /tools/multisafepay-control/enabling-two-factor-authentication
---

Two-factor authentication (2FA) is an optional, additional layer of security for data in your MultiSafepay account. It is supported in every country.

When enabled, users must verify their identity with:

- A password
- A 6-digit token generated in the user's MultiSafepay mobile app for **every** Sign in

## Enabling 2FA

### Administrator 

To enable 2FA in your MultiSafepay account, you must have administrator rights. 

1. Sign in to your MultiSafepay account and go to [User management](https://merchant.multisafepay.com/user-management).

2. Click the name of the user you want to enable 2FA for to open the **User details** page.

3. From the **Two-factor** dropdown menu, select **Enable**.

4. Click **Save changes**.

{{< screen src="/gifs/MCP_2FA-1.gif" alt="Enabling Two-factor authentication in your MultiSafepay account" align="center" screen_size="desktop" >}}

For support, email the Support Team at <support@multisafepay.com>

### User

The first time the user logs in to MultiSafepay account after 2FA is enabled, they must configure 2FA.

1.  Sign in to [MultiSafepay account](https://merchant.multisafepay.com) on your laptop or PC. A dialog requesting a 6-digit token appears.

2. Open or [download](https://docs.multisafepay.com/tools/multisafepay-control-app/how-to-download-the-app) the MultiSafepay app and Sign in.

3. Tap **More** in the bottom-right corner.

4. Tap **Authenticator**.

5. Copy the 6-digit token from your mobile device to the 2FA dialog on your computer or laptop.

{{< screen src="/gifs/MCP_2FA-3.gif" alt="Generating a 6-digit 2FA token the in your MultiSafepay account app" align="center" caption="The 6-digit token remains visible for 30 seconds" screen_size="mobile" >}}

**Notes:** 

- You can only connect a mobile device to one user, and a user to only one mobile device.
- After 5 unsuccessful 6-digit token inputs, the user's account is blocked. Only administrators can unblock user accounts. 
- If a user loses their 2FA device, disable and re-enable 2FA on their account. 

For support, email the Support Team at <support@multisafepay.com>
