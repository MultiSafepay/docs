---
title: "Account users"
category: 627bbcf80c1c9c0050320b60
order: 1
hidden: false
parentDoc: 62b0845857c8ab006af6a4f7
slug: 'account-users'
---

Your MultiSafepay account can have an unlimited number of authorized users. All users on one account share the same [security code](/docs/sites#site-id-api-key-and-security-code). You can block users, but not delete them.

# User permission profiles

| User                  | Permissions                                                                                                                                                                  |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Administrator         | Access all functionalities                                                                                                                                                   |
| Payment links manager | View all transactions <br /> Generate payment links                                                                                                                          |
| Balance hidden        | Cannot view the account balance                                                                                                                                              |
| Orders manager        | Create refunds <br /> View all transactions <br /> Generate payment links                                                                                                    |
| Reports manager       | View all transactions and the account balance <br /> Create and download reports <br /> Generate payment links                                                               |
| Websites manager      | View all transactions <br /> Add and edit websites and payment pages <br /> Add and edit terminal groups and POS terminals <br /> Style emails <br /> Resend offline actions |
| Captures manager      | View all transactions <br /> Accept or decline uncleared transactions                                                                                                        |

# How to add and block users

<details id="how-to-add-users">
  <summary>How to add users</summary>

  <br />

  1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style={{ fontSize: '12px', color: '#8b929e' }} />.
  2. Go to **Settings** > **Account users**.
  3. Click **Add new user**.
  4. Enter the new user's:
     * Username
     * Full name
     * Password
     * Email address
  5. From the **Status** list, select **Active**.
  6. Under **Rights** on the right side of the page, select the appropriate user permissions check boxes.
  7. Click **Add user** in the top-right corner.\
     ✅   The user appears under **Account users** with status **Active**.
</details>

<details id="how-to-block-users">
  <summary>How to block users</summary>

  <br />

  1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style={{ fontSize: '12px', color: '#8b929e' }} />.
  2. Go to **Settings** > **Account users**, and then click the relevant user profile.
  3. On the **User profile** pages, from the **Status** list, select **Blocked**.
  4. Click **Save changes**.\
     ✅   The user's status under **Account users** changes to **Blocked**.
</details>

<br />

***

# User guide

## Two-factor authentication

Two-factor authentication (2FA) is an optional, additional layer of security for your MultiSafepay account. It is supported in every country.

When enabled, users must verify their identity with a password, and a 6-digit token generated in the user's MultiSafepay mobile app for **every** sign in.

* You can only connect a mobile device to **one** user, and each user to only **one** mobile device.
* After 5 unsuccessful token inputs, the user's account is blocked and can only be unblocked by an administrator.
* If a user loses their 2FA device, disable and re-enable 2FA on their account.

### 1. Download the MultiSafepay app

* For Android devices – <a href="https://play.google.com/store/apps/details?id=com.multisafepay.control" target="_blank">Google Play</a> <i class="fa fa-external-link" style={{ fontSize: '12px', color: '#8b929e' }} />
* For Apple iOS devices – <a href="https://apps.apple.com/app/multisafepay-control/id929955963" target="_blank">App Store</a> <i class="fa fa-external-link" style={{ fontSize: '12px', color: '#8b929e' }} />

### 2. Enable 2FA

Only administrators can enable 2FA.

<details id="how-to-enable-2fa">
  <summary>How to enable 2FA</summary>

  <br />

  1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style={{ fontSize: '12px', color: '#8b929e' }} />.
  2. Go to **Settings** > **Account users**.
  3. Click the name of the user you want to enable 2FA for.
  4. On the **User details** page, from the **Two-factor authentication** list, select **Enabled**.
  5. Click **Save changes**.
</details>

### 3. Configure 2FA

Users must then configure 2FA the first time they sign in to the dashboard after 2FA is enabled.

<details id="how-to-configure-2fa">
  <summary>How to configure 2FA</summary>

  <br />

  1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style={{ fontSize: '12px', color: '#8b929e' }} /> on your laptop or PC.\
     A dialog requesting a 6-digit token appears.
  2. In the MultiSafepay app,  tap **More** in the bottom-right corner.
  3. Tap **Authenticator**.
  4. Copy the 6-digit token (remains visible for 30 seconds) from your mobile device to the 2FA dialog on your computer or laptop.
</details>

<br />

***

<HTMLBlock>{`
<blockquote class="callout callout_info">
    <h3 class="callout-heading false">
        <span class="callout-icon">💬</span>
        <p>Support</p>
    </h3>
    <p>Email <a href="mailto:support@multisafepay.com">support@multisafepay.com</a></p>
</blockquote>
`}</HTMLBlock>

[Top of page](#)