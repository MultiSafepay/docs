---
title: "Sites"
category: 627bbcf80c1c9c0050320b60
order: 12
hidden: false
parentDoc: 62b0845857c8ab006af6a4f7
slug: 'sites'
---

To set up your account, you must add at least one site (e.g. a website, app, or other application), for which we generate an API key. 

You can add an unlimited number of sites to your MultiSafepay account, but they must all be operated by the same legal entity linked to that account.

To process payments from a site operated by a separate legal entity, you must sign up for an additional MultiSafepay account.

<details id="how-to-add-a-site">
<summary>How to add a site</summary>
<br>

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>. 
2. Go to **Sites**.
3. Click **Add new site**.
    - From the **Category** list, select what type of products or services your site sells.
    - In the **Description** field, enter the site name.  
    **⚠️ Note:** If relevant, this is displayed on MultiSafepay payment pages and the customer’s bank statement.
    - In the **Base URL** field, add the site’s URL. This must be the URL where you receive payments.
    - If you want to receive [status updates](/docs/payment-statuses/) via webhook, in the **Webhook URL** field, enter a URL for us to send them to.
4. Click **Save**.
    A **Sites** page for the new site appears, including the site ID, API key, and security code. 
5. Optionally, provider your **Customer support phone** and **Customer support email**. 
6. To style your payment page for this site, see Payment pages – [Styling](/docs/payment-pages/#styling).
</details>

<details id="how-to-connect-to-backend">
<summary>How to connect a site to your backend</summary>
<br>

To connect a site to your <<glossary:backend>>, enter the required details: 

- Most [ready-made integrations](/docs/our-integrations/): Your [site ID, API key, and security code](#site-id-api-key-and-security-code), and account ID (top-right corner of your dashboard)  
- [API integrations](/docs/api-integration/): Your [site API key](#site-id-api-key-and-security-code)

To validate the connection, [place a test order](/docs/testing/).

</details>
<br>

___

# User guide

## Block/unblock a site

<details id="how-to-block-unblock-a-site">
<summary>How to block/unblock a site</summary>
<br>

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Go to **Sites**, and then click the relevant site.
3. On the **Sites** page, from the **Status** list:
  - To block, select **Blocked**.
  - To unblock, select **Active**.
4. Click **Save changes**. 
   ✅ &nbsp; On the **Sites** page, the site's status changes to **Blocked**.

</details>

## Delete/restore a site

<details id="how-to-delete-restore-a-site">
<summary>How to delete/restore a site</summary>
<br>

To delete a site:

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Go to **Sites**.
3. On the row of the relevant site, click ❌ &nbsp; **Disable payments** > **Delete**. 
   ✅ &nbsp; The site profile disappears from the **Sites** page.

To restore the site:

1. On the **Sites** page, select the **Show deleted sites** checkbox. 
2. On the row of the relevant site, click the trash can icon **Restore site** > **Yes**.
3. To return to the **Sites** overview page, deselect the **Show deleted sites** checkbox.
   ✅ &nbsp; The site profile reappears on the **Sites** page.

</details>

## Disable/enable payments for a site

You can temporarily disable payments for a site, and then re-enable them.

<details id="how-to-disable-enable-payments-for-a-site">
<summary>How to disable/enable payments for a site</summary>
<br>

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Go to **Sites**.
3. On the row of the relevant site:
   - To disable payments, click ❌ &nbsp; **Disable payments** > **Yes**. <br> On the **Sites** page, the site's status changes to **Blocked**.
   - To enable payments, click ✅ &nbsp; **Enable payments** > **Yes**. <br> On the **Sites** page, the site's status changes to **Active**.

</details>

## Logos and icons

For MultiSafepay logos, see our GitHub repository – <a href="https://github.com/MultiSafepay/MultiSafepay-logos" target="_blank">MultiSafepay logos</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

For the logos and icons of all MultiSafepay payment methods, see our GitHub repository – <a href="https://github.com/MultiSafepay/MultiSafepay-icons" target="_blank">MultiSafepay icons</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

<details id="how-to-generate-logo-png">
<summary>How to generate a PNG of logos</summary>
<br>

To generate a portable network graphic (PNG) of a payment method logo to display on your site, follow these steps:

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Go to **Settings** > **Logo designer**.
3. Select a layout template.
4. From the **Select elements** window, select the logos you want to include.
5. Under **Result logo**, check the preview. 
6. Under **Order icons**, you can:  
    - Drag and drop logos to change the order in which they display.
    - Remove logos by clicking **Remove**.
7. When you are happy with the preview, to generate the PNG image, click **Download**. 

</details>

## Site ID, API key, and security code

To view the ID, API key, and security code for a website:

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">live</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> or <a href="https://testmerchant.multisafepay.com" target="_blank">test</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> MultiSafepay dashboard.
2. Go to **Websites**, and then click on the relevant website.
3. You can find the website ID, API key, and security code in the top-right corner of the page.

To view the ID and API key for a terminal group:

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">live</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> or <a href="https://testmerchant.multisafepay.com" target="_blank">test</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> MultiSafepay dashboard.
2. Go to **Devices** > **Terminals**.
3. Click on **Manage groups**. 
4. A list of all available terminal groups will be displayed, showing the ID and API key for each group.


## Specify company name

You can specify how your company name appears on customer bank statements (if supported by the bank) and on [payment pages](/docs/payment-pages/), or choose to display an alias instead. Customers may prefer this if you offer adult products.

<details id="how-to-display-company-name">
<summary>How to display your company name</summary>
<br>

To set how your company name displays, follow these steps:

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Go to **Sites**, and then click the relevant site.
3. In the **Site name** field, enter the name to display (maximum 35 characters).
4. Click **Save**.

</details>

<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)