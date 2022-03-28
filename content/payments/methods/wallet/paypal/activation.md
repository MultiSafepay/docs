---
title: "Activating PayPal"
breadcrumb_title: 'Activation'
weight: 20
meta_title: "Activating PayPal - MultiSafepay Docs"
short_description: "Activating PayPal for your MultiSafepay account"
layout: 'child'
url: '/payment-methods/paypal/activation/'
aliases: 
    - /payment-methods/paypal/activate-paypal
    - /faq/errors-explained/paypal-error-10002
    - /faq/errors-explained/iframe-errors
    - /payments/methods/wallet/paypal/activation/
---

{{< blue-notice >}} If using a [ready-made integration](/integrations/ready-made/): 

- First check that the payment method is supported. 
- Once you have activated the method for your MultiSafepay account, you must also enable it in your [backend](/glossaries/multisafepay-glossary/#backend).  {{< /blue-notice >}}

The instructions below are for the PayPal interface in English. If your PayPal webpage is in another language, you can change the language easily by clicking the links at the bottom right of the page.

## Configuring your PayPal account

To configure your PayPal account, follow these steps:

1. Sign in to [Paypal.com](https://www.paypal.com) with your business account.
2. Mouse over your account name in the top-right corner, and then select **Account settings**.
3. On the **Account access** tab, under **API access**, click **Update**.
4. Under **Pre-built payment solution**, click **Grant API permission**.
5. In the **Third-party permission username** field, enter `paypal_api1.multisafepay.com`. 
7. Click **Lookup**.  
8. Select the checkboxes of the relevant permissions:  
    - Use Express Checkout to process payments.
    - Issue a refund for a specific transaction.
    - Process your customers' credit or debit card payments.
    - Obtain information about a single transaction.

To complete the configuration, change the language encoding setting of your PayPal account to **UTF-8**:

1. Click PayPal – [Profile language encoding](https://www.paypal.com/cgi-bin/customerprofileweb?cmd=_profile-language-encoding).
2. Next to **Language coding for PayPal buttons**, click **Edit**.
3. From the dropdown menu, select **Western European languages (including English)**.
4. Click **More options**.
5. From the **Encoding** dropdown menu, select **UTF-8**.
6. Select the **Yes** checkbox.
7. Click **Save**.

For support or if any steps are inaccurate, email the Integration Team at <integration@multisafepay.com>

{{< alert-notice >}} **Known issue:** If your PayPal business account isn't yet fully verified or approved, you might get a PayPal error 10002: Restricted account. {{< /alert-notice >}}

For support or if any steps are inaccurate, email the Integration Team at <integration@multisafepay.com>

For further support, see PayPal – [Contact us](https://www.paypal.com/us/smarthelp/contact-us).

## Configuring your MultiSafepay account

To configure your MultiSafepay account for PayPal, follow these steps:

1. Sign in to [Paypal.com](https://www.paypal.com) with your business account.
2. Mouse over your account name in the top-right corner, and then select **Account settings**.
3. On the **Business information** tab, copy your PayPal Merchant ID.
4. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
5. Go to **Settings**. 
6. To activate PayPal for:

- All your websites:
    - Go to **Payment methods**, and then select **PayPal**.
    - In the **PayPal Merchant ID** field, paste in your ID.

- A specific website:
    - Go to **Website settings**, and click the relevant website.
    - Under **Payment methods**, select the **PayPal** checkbox.

**Note:** You can link each website to a separate PayPal business account, or all websites can use your main PayPal business account.

7. Click **Save changes**.

**Note:** If PayPal is not visible as a payment method in your MultiSafepay dashboard, email the Integration Team at <integration@multisafepay.com> 

Your account is now configured. We strongly recommend [testing some transactions](/payment-methods/paypal/integration-testing/) before processing live payments.






