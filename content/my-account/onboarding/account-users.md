---
title: "Account users"
category: 62962dcdbccb9a001d4bbc81
order: 202 
hidden: false
parentDoc: 62a206ee0298c80058af3aed
---

Your MultiSafepay account can have an unlimited number of authorized users. All users on one account share the same secure code. You can disable but not delete users.

<details id="user-permission-profiles">
<summary>User permission profiles</summary>

| User | Permissions |
|---|---|
| Administrator | Access all functionalities |
| Basic | View all transactions <br> Generate payment links |
| DisableBalance | Cannot view the account balance |
| Refund | Create refunds <br> View all transactions <br> Generate payment links |
| Reporting | View all transactions and the account balance <br> Create and download reports <br> Generate payment links |
| Technical | View all transactions <br> Add and edit websites and payment pages <br> Edit email templates <br> Resend offline actions |
| Uncleared | View all transactions <br> Accept or decline uncleared transactions |

</details>

## Adding users

<details id="adding-users-to-your-account">
<summary>Adding users to your account</summary>

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Settings** > **User management**.
3. Click **Add new user** in the top right corner.
4. Enter the new user's:  
    - User name
    - Full name
    - Password
    - Email address
5. From the **Status** list, select **Active**.
6. Under **Rights** on the right side of the page, select the appropriate user permissions check boxes. See [User permissions overview](#user-permissions-overview) below.
7. Click **Add user** in the top-right corner.

</details >

## Two-factor authentication
    
 Two-factor authentication (2FA) is an optional, additional layer of security for data in your MultiSafepay account. It is supported in every country.

When enabled, users must verify their identity with a password, and a 6-digit token generated in the user's MultiSafepay mobile app for **every** sign in.

- You can only connect a mobile device to **one** user, and each user to only **one** mobile device.
- After 5 unsuccessful token inputs, the user's account is blocked and can only be unblocked by an administrator. 
- If a user loses their 2FA device, disable and re-enable 2FA on their account.

> 📘 Download the MultiSafepay app
> 
> - Android devices from [Google Play](https://play.google.com/store/apps/details?id=com.multisafepay.control)
> - Apple iOS devices from the [App Store](https://apps.apple.com/app/multisafepay-control/id929955963)


### Enabling 2FA

Only administrators can enable 2FA.

<details id="Enabling-2fa">
<summary>Enabling 2FA</summary>

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **User management**.
3. Click the name of the user you want to enable 2FA for.
4. On the **User details** page, from the **Two-factor** list, select **Enable**.
5. Click **Save changes**.

</details>

### Configuring 2FA

Users must then configure 2FA the first time they sign in to the dashboard after 2FA is enabled.

<details id="configuring-2fa">
<summary>Configuring 2FA</summary>

1.  Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com) on your laptop or PC.  
A dialog requesting a 6-digit token appears.
2. In the MultiSafepay app,  tap **More** in the bottom-right corner.
3. Tap **Authenticator**.
4. Copy the 6-digit token (remains visible for 30 seconds) from your mobile device to the 2FA dialog on your computer or laptop.

</details >

## Support

Email <support@multisafepay.com>