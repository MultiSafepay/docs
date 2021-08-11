---
title: "Activating PayPal"
breadcrumb_title: 'Activation'
weight: 20
meta_title: "Activating PayPal - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Activating PayPal to use in your MultiSafepay account"
layout: 'child'
aliases: 
    - /payment-methods/paypal/activate-paypal
    - /faq/errors-explained/paypal-error-10002
    - /faq/errors-explained/iframe-errors
---
## Configuring your PayPal account
{{< details title="Changing the language of the PayPal interface" >}}

The instructions below are for the PayPal interface in English. If your PayPal webpage is in another language, you can change the language easily by clicking the links at the bottom right of the page.

{{< /details >}}

To configure your PayPal account, follow these steps:

1. Sign in to [Paypal.com](https://www.paypal.com) with your business account.
2. Mouse over your account name in the top-right corner, and then select **Account settings**.
3. On the **Account access** tab, under **API access**, click **Update**.
4. Under **Pre-built payment solution**, click **Grant API permission**.
5. In the **Third-party permission username** field, enter `paypal_api1.multisafepay.com`. 
7. Click **Lookup**.  

Here you can:

- Use Express Checkout to process online and mobile payments.
- Process refunds.
- Process credit and debit card payments.
- Obtain information about a specific transaction.
- Obtain authorization for pre-approved payments and initiate pre-approved transactions.

To complete the configuration, change the language encoding setting of your PayPal account to **UTF-8**. Follow these steps:

1. Click PayPayl – [Profile language encoding](https://www.paypal.com/cgi-bin/customerprofileweb?cmd=_profile-language-encoding).
2. From the dropdown menu, select **Western European languages (including English)**.
3. Click **More options**.
4. From the **Encoding** dropdown menu, select **UTF-8**.
5. Select the **Yes** checkbox.
6. Click **Save**.

For support or if any steps are inaccurate, email the Integration Team at <integration@multisafepay.com>

{{< alert-notice >}} **Known issue:** If your PayPal business account isn't yet fully verified or approved, you might get a PayPal error 10002: Restricted account. {{< /alert-notice >}}

For further support, see PayPal – [Contact us](https://www.paypal.com/us/smarthelp/contact-us).

## Configuring your MultiSafepay account

To configure your MultiSafepay account for PayPal, follow these steps:

1. Sign in to [Paypal.com](https://www.paypal.com) with your business account.
2. Mouse over your account name in the top-right corner, and then select **Account settings**.
3. On the **Business information** tab, copy your PayPal Merchant ID.
4. Sign in into your [MultiSafepay account](https://merchant.multisafepay.com).
5. Go to **Settings** > **Payment methods**, and then select **PayPal**.
6. In the **PayPal Merchant ID** field, paste in your ID.
7. Click **Save changes**.

If PayPal is not visible as a payment method in your MultiSafepay account, email the Integration Team at <integration@multisafepay.com> 

If you offer a different selection of payment methods on different websites, you also need to activate PayPal for each site:

1. Go to **Settings** > **Website settings**.
2. Click the relevant website to open the **Website settings** page.
3. Under **Payment methods**, select the **PayPal** checkbox.
4. Click **Save.**

**Note:** You can link each website to a separate PayPal business account, or all websites can use your main PayPal business account.

Your account is now configured. We strongly recommend testing some transactions before processing live payments.

## Displaying your logo in the PayPal checkout
To display your header or logo on the PayPal checkout page, follow these steps:

1. Sign in into your [MultiSafepay account](https://merchant.multisafepay.com).
2. Go to **Settings** > **Files**, and upload the relevant images. 
3. Go to **Payment methods** at the bottom right, and then select the relevant images from the **Logo** and **Header** dropdown menu. 
4. Click **Save**.




