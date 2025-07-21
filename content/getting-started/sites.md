---
title: "Websites"
category: 627bbcf80c1c9c0050320b60
order: 12
hidden: false
parentDoc: 62b0845857c8ab006af6a4f7
slug: 'sites'
---

To set up your account, you must add at least one website (e.g. a website, app, or other application), for which we generate an API key. 

You can add an unlimited number of websites to your MultiSafepay account, but they must all be operated by the same legal entity linked to that account.

To process payments from a website operated by a separate legal entity, you must sign up for an additional MultiSafepay account.

<details id="how-to-add-a-website">
<summary>How to add a website</summary>
<br>

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>. 
2. Go to **Websites**.
3. Click **Add new website**.
   - From the **Category** list, select what type of products or services your website sells.
   - From the **Subcategory** list, select the specific products or services based on the chosen category.
   - In the **Description** field, enter the website name.  
     **⚠️ Note:** This is displayed on MultiSafepay payment pages and the customer’s bank statement.
   - In the **Base URL** field, add the website’s URL. This must be the URL where you receive payments.
   - If you want to receive [status updates](/docs/payment-statuses/) via webhook, in the **Webhook URL** field, enter a URL for us to send them to.
4. Click **Save**. You will be redirected to the panel of your new **website**, where you can manage different functionalities. Here, you will also find the **Website ID**, **API key**, and **Security code**.
5. Optionally, provider your **Customer support phone** and **Customer support email**. 
6. To learn how to style your payment page for this website, see Payment pages – [Styling](/docs/payment-pages/#styling).
   </details>

<details id="how-to-connect-to-backend">
<summary>How to connect a website to your backend</summary>
<br>

To connect a website to your <<glossary:backend>>, enter the required details: 

- Most [ready-made integrations](/docs/our-integrations/): Your [website ID, API key, and security code](#site-id-api-key-and-security-code), and account ID (top-right corner of your dashboard)  
- [API integrations](/docs/api-integration/): Your [website API key](#site-id-api-key-and-security-code)

To validate the connection, [place a test order](/docs/testing/).

</details>

***

# User guide

## Block/unblock a website

To block or unblock a website:

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Go to **Websites**, and then click the relevant website.
3. On the **Website** panel, from the **Status** list select:
   - **Blocked**, to block the website.
   - **Active**, to unblock the website.
4. Click **Save changes**.

✅ On the **Websites** overview page, the website's status changes to **Blocked**.

***

## Delete/restore a website

To delete a website:

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Go to **Websites**.
3. On the row of the relevant website, click ❌   **Disable payments** > **Delete**.

✅ The website profile disappears from the **Websites** page.

To restore a website:

1. On the **Websites** overview page, click **Show deleted websites**. 
2. From the list of websites, click **Restore website** > **Yes**.
3. To return to the **Websites** overview page, deselect the **Show deleted websites** checkbox.

✅   The website profile reappears on the **Websites** page.

***

## Disable/enable payments for a website

You can temporarily disable payments for a website, and then re-enable them.

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Go to **Websites**.
3. On the row of the relevant website:
   - To disable payments, click ❌   **Disable payments** > **Yes**. <br> On the **Websites** page, the website's status changes to **Blocked**.
   - To enable payments, click ✅   **Enable payments** > **Yes**. <br> On the **Websites** page, the website's status changes to **Active**.

***

## Logos and icons

For MultiSafepay logos, see our GitHub repository – <a href="https://github.com/MultiSafepay/MultiSafepay-logos" target="_blank">MultiSafepay logos</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

For the logos and icons of all MultiSafepay payment methods, see our GitHub repository – <a href="https://github.com/MultiSafepay/MultiSafepay-icons" target="_blank">MultiSafepay icons</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

<details id="how-to-generate-logo-png">
<summary>How to generate a PNG of logos</summary>
<br>

To generate a portable network graphic (PNG) of a payment method logo to display on your website, follow these steps:

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

## Website ID, API key, and Security code

To view the ID, API key, and security code for a website:

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">live</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> or <a href="https://testmerchant.multisafepay.com" target="_blank">test</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> MultiSafepay dashboard.
2. Go to **Websites**, and then click on the relevant website.
3. You can find the website ID, API key, and security code in the top-right corner of the page.

## Terminal group ID and API key

To view the ID and API key for a terminal group:

4. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">live</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> or <a href="https://testmerchant.multisafepay.com" target="_blank">test</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> MultiSafepay dashboard.
5. Go to **Devices** > **Terminals**.
6. Click on **Manage groups**. 
7. A list of all available terminal groups will be displayed, showing the ID and API key for each group.

## Specify company name

You can specify how your company name appears on customer bank statements (if supported by the bank) and on [payment pages](/docs/payment-pages/), or choose to display an alias instead. Customers may prefer this if you offer adult products.

<details id="how-to-display-company-name">
<summary>How to display your company name</summary>
<br>

To set how your company name displays, follow these steps:

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Go to **Websites**, and then click the relevant website.
3. In the **Website name** field, enter the name to display (maximum 35 characters).
4. Click **Save**.

</details>

***

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]


[Top of page](#)