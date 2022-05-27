---
title: "Managing websites"
weight: 1
meta_title: "Managing websites - MultiSafepay Docs"
read_more: "."
url: "/account/managing-websites/"
aliases:
    - /account/adding-websites/
    - /tools/multisafepay-account/delete-website
    - /tools/multisafepay-account/deleting-websites
    - /getting-started/set-up-your-account/user-guide/deleting-websites/
    - /account/deleting-websites/
    - /getting-started/set-up-your-account/user-guide/connecting-websites-to-your-backend/
    - /account/connecting-websites-to-backend/
    - /tools/multisafepay-control/get-your-api-key
    - /tools/multisafepay-control/retrieving-your-api-key
    - /getting-started/set-up-your-account/user-guide/retrieving-your-api-key/
    - /getting-started/set-up-your-account/user-guide/viewing-your-api-key/
    - /set-up-your-account/site-id-api-key-secure-code/
    - /developer/api/generating-your-api-key/
    - /faq/api/generate-your-api-key
    - /faq/api/generating-your-api-key
    - /account/site-id-api-key-secure-code
    - /tools/multisafepay-control/autowithdrawl-updates
    - /faq/general/descriptor-bank-statement
    - /tools/multisafepay-control/adding-descriptors-to-customer-bank-statements
    - /my-account/manage-your-balance/adding-descriptors-to-customer-bank-statements/
    - /account/displaying-company-names/
---

To set up your account, you must add at least one website, for which we generate an API key. 

You can add an unlimited number of websites to your MultiSafepay account, but they must all be operated by the same legal entity linked to that account.

To process payments from a website operated by a separate legal entity, you must sign up for an additional MultiSafepay account.

## Adding websites

1. Sign in to your MultiSafepay dashboard. 
2. Go to **Settings** > **Website settings**.
3. Click either:  
    {{< details title="Quick add website" >}}

1. From the **Category** list, select what type of products or services your website sells.
2. In the **Description** field, enter the website name.  
    **Note:** If relevant, this is displayed on MultiSafepay payment pages and the customer’s bank statement.
3. In the **Base URL** field, add the website’s URL. This must be the URL where you receive payments.
4. If you want to receive [status updates](/about-payments/multisafepay-statuses/) via webhook, in the **Notification URL** field, enter a URL for us to send them to.
5. Click **Save**.

{{< /details >}} 
    Or, for more advanced configuration:
{{< details title="Website wizard" >}}

1. Enter the website URL in the **Full website URL** field, or select it from the **Select existing site** list, and then click **Continue**.
2. From the **Website platform** list, select your ecommerce platform.  
    You are prompted to install the MultiSafepay ready-made integration for your ecommerce platform in your website. 
3. From the **Category** list, select the type of products and/or services you sell from this website, and then click **Continue**.
4. If you want to receive [status updates](/about-payments/multisafepay-statuses/) via webhook, in the **Notification URL** field, enter a URL for us to send them to.
5. In the **Description** field, enter your company name, and then click **Continue**.  
    **Note:** If relevant, this is displayed on MultiSafepay payment pages and the customer’s bank statement.  
    A template of your [payment page](/payment-pages/) is generated.
6. Customize the template as required.  
    - To toggle the view of the payment page, click:
        - **List view** to see all payment methods in a list
        - **Detail view** to display one detailed box for entering payment details and collapse all other payment methods
        - **API view code** to view the code
    - To replace the MultiSafepay logo in the top-left corner, after completing the wizard, upload your own logo under **Settings** > **Payment page templates**.
    - To hide the MultiSafepay logo in the top-left corner, on the lefthand side under **Settings**, select the **Hide main logo** checkbox.
    - On the lefthand side, under **Header**, **Body**, **Container**, **Cart**, **Payment form**, and **Buttons**, you can change the color of the background, text, lines, and links in different parts of the payment page.
    - To clear your changes and start again, click **Reset style**.
7. To set this payment page as your default template, select the **Set as default template** checkbox. 
8. In the **Save template as** field, enter a name for this template.  

Your account is now linked to your website. 
{{< /details >}} 

4. The **Website settings** page contains your:  
    - Site ID
    - Secure code
    - API key
5. Copy the API key to start building your integration. The API key also lets you monitor transactions, configure [payouts](/account/payouts/), generate reports, and more. 

**Note:** Website names are displayed on MultiSafepay payment pages and, for some payment methods, on the customer’s bank statement (if supported by their bank).

## Viewing the site ID, API key, and secure code

To view the site ID, API key, and secure code for a website:

1. Sign in to your [live](https://merchant.multisafepay.com) or [test](https://testmerchant.multisafepay.com) MultiSafepay dashboard.

2. Go to **Settings** > **Website settings**.

3. Click on the relevant website to view the **Website details** page.

## Connecting websites to your backend

To connect a website to your [backend](/glossaries/multisafepay-glossary/#backend), enter the required details: 

- Most [ready-made integrations](/integrations/ecommerce-integrations): Your site ID, API key, and secure code, and account ID (top-right corner of your dashboard)  

- Self-made integrations: The API key under **Website settings** in your account

The connection is finalized. To validate the connection, [place a test order](/integrations/testing/).

## Displaying your company name
You can specify how your company name appears on customer bank or credit card statements and on MultiSafepay payment pages, or choose to display an alias instead. Customers may prefer this if you offer adult products. 

To set how your company name displays, follow these steps:

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Settings** > **Website settings**.
3. In the **Name** field, enter the name to display (maximum 35 characters).
4. Click **Save**.

## Deleting websites

To delete a website from your account, follow these steps:

1. Sign in to your MultiSafepay dashboard.
2. Go to **Settings** > **Website settings**.
3. For the website you want to delete, click the green **Enabled** button in the right most column.
4. In the **Disable payments** dialog, click **Delete**.