---
title: "Adding websites"
weight: 10
meta_title: "Account - Adding websites - MultiSafepay Docs"
read_more: '.'
url: '/account/adding-websites/'
---

To set up your test account, you must first add at least one website and generate an [API key](/account/site-id-api-key-secure-code/). 

## Website requirements

You can add an unlimited number of websites to your MultiSafepay account, but they must all be operated by the same legal entity linked to that account.

To process payments from a website operated by a separate legal entity, you must sign up for an additional MultiSafepay account.

## Adding websites

1. Sign in to your [MultiSafepay test account](https://testmerchant.multisafepay.com). 
2. Go to **Settings** > **Website settings**.
3. Click either:  
    {{< details title="Quick add website" >}}

1. From the **Category** dropdown menu, select what type of products or services your website sells.
2. In the **Description** field, enter the website name.  
    **Note:** This is displayed on the MultiSafepay payment page and, depending on the payment method, on the customer’s bank statement.
3. In the **Base URL** field, add the website’s URL. This must be the URL where you receive payments.
4. In the **Notification URL** field, provide a notification URL for MultiSafepay to send status updates to, if required.
5. Click **Save**.

{{< /details >}} 
    Or, for more advanced configuration:
{{< details title="Website wizard" >}}

1. Enter the website URL in the **Full website URL** field, or select it from the **Select existing site** dropdown, and then click **Continue**.
2. From the **Website platform** dropdown, select your ecommerce platform.  
    You are prompted to install the MultiSafepay plugin for your ecommerce platform in your website. 
3. From the **Category** dropdown, select the type of products and/or services you sell from this website, and then click **Continue**.
4. If you want to receive [transaction status](/payments/multisafepay-statuses/) updates via webhook, in the **Notification URL** field, enter a URL for us to send them to.
5. In the **Description** field, enter your company name, and then click **Continue**.  
    **Note:** This name appears on payment pages and customer bank statements (if supported by their bank).  
    A template of your MultiSafepay payment page is generated.
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

Your test account is now linked to your website. 
{{< /details >}} 

4. The **Website settings** page contains your:  
    - Site ID
    - Secure code
    - API key
5. Copy the API key to start building your integration. The API key also lets you monitor transactions, configure [payouts](/account/payouts/), generate reports, and more. 

**Note:** Website names are displayed on MultiSafepay payment pages and, for some payment methods, on the customer’s bank statement (if supported by their bank).