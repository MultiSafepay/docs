---
title : "Adding websites"
weight: 3
meta_title: "MultiSafepay Control - Adding websites - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: '.'
aliases:
    - /faq/getting-started/how-many-websites-can-i-add-to-my-multisafepay-account/
    - /tools/multisafepay-control/add-website
---
You can add an unlimited number of websites to your MultiSafepay Control, but they must all be operated by the same legal entity linked to that MultiSafepay account.

To process payments from a website operated by a separate legal entity, you must sign up for an additional MultiSafepay account.

To add a website to your MultiSafepay Control, follow these steps:

1. Log in to your [live](https://merchant.multisafepay.com) or [test](https://testmerchant.multisafepay.com) MultiSafepay Control.

2. Navigate to **Settings** > **Website settings**.

3. Click the **Quick add website** button.

4. From the **Category** dropdown menu, select what type of products or services your website sells.

5. In the **Description** field, enter the website name. This is displayed on the MultiSafepay payment page and, depending on the payment method, on the customer's bank statement.

6. In the **Base URL** field, add the website's URL. This must be the URL where you receive payments.

7. In the **Notification URL** field, provide a [notification URL](/faq/api/how-does-the-notification-url-work) for MultiSafepay to send status updates to, if required.

8. Click **Save**.

Adding a website automatically generates the following details you need to connect to the MultiSafepay platform using our API:

- API key
- Site ID
- Secure code



