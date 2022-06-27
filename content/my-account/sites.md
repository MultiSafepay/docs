---
title: "Sites"
category: 62962dcdbccb9a001d4bbc81
order: 210
hidden: false
parentDoc: 62b0845857c8ab006af6a4f7
slug: 'sites'
---

To set up your account, you must add at least one site (e.g. a website, app, or other application), for which we generate an API key. 

# How it works

You can add an unlimited number of sites to your MultiSafepay account, but they must all be operated by the same legal entity linked to that account.

To process payments from a site operated by a separate legal entity, you must sign up for an additional MultiSafepay account.

# Activation

<details id="how-to-add-a-site">
<summary>How to add a site</summary>
<br>

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com). 
2. Go to **Settings** > **Website settings**.
3. Click **Quick add site**.
    - From the **Category** list, select what type of products or services your site sells.
    - In the **Description** field, enter the site name.  
    **Note:** If relevant, this is displayed on MultiSafepay payment pages and the customer’s bank statement.
    - In the **Base URL** field, add the site’s URL. This must be the URL where you receive payments.
    - If you want to receive [status updates](/payment-statuses/) via webhook, in the **Notification URL** field, enter a URL for us to send them to.
4. Click **Save**.
    A **Website settings** page for the new site displays, which you can configure as needed. 
</details>

# Integration

To connect a site to your <<glossary:backend>>, enter the required details: 

- Most [ready-made integrations](/docs/our-integrations/): Your [site ID, API key, and secure code](#site-id-api-key-and-security-code), and account ID (top-right corner of your dashboard)  
- Self-made integrations: Your [site API key](#site-id-api-key-and-security-code)

The connection is finalized. To validate the connection, [place a test order](/docs/testing/).
<br>

___

# User guide

## Company name
You can specify how your company name appears on customer bank or credit card statements (if supported by the bank) and on [payment pages](/docs/payment-pages/), or choose to display an alias instead. Customers may prefer this if you offer adult products.

<details id="how-to-display-company-name">
<summary>How to display your company name</summary>
<br>

To set how your company name displays, follow these steps:

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Settings** > **Website settings**.
3. In the **Name** field, enter the name to display (maximum 35 characters).
4. Click **Save**.

</details>

## Deleting sites

<details id="how-to-delete-site">
<summary>How to delete a site</summary>
<br>

To delete a site from your account, follow these steps:

1. Sign in to your MultiSafepay dashboard.
2. Go to **Settings** > **Website settings**.
3. For the site you want to delete, click the green **Enabled** button in the right most column.
4. In the **Disable payments** dialog, click **Delete**.

</details>

## Site ID, API key, and security code

To view the site ID, API key, and secure code for a site:

1. Sign in to your [live](https://merchant.multisafepay.com) or [test](https://testmerchant.multisafepay.com) MultiSafepay dashboard.
2. Go to **Settings** > **Website settings**.
3. Click on the relevant site to view the **Website details** page.
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]
