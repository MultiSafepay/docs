---
title: "Payment methods"
category: 62962dcdbccb9a001d4bbc81
order: 206
hidden: false
parentDoc: 62b0845857c8ab006af6a4f7
slug: 'payment-methods'
excerpt: 'Activate payment methods for your account.'
---
Some payment methods you can activate yourself in your dashboard, but for some you need to apply to MultiSafepay first. Other methods with specific requirements follow their own activation flow.  

| Activation flow | Payment methods |
|---|---|
| [Apply to MultiSafepay](#apply-to-multisafepay) then activate in dashboard | Credit and debit cards and wallets (**except** PayPal), Dotpay, in3, Pay After Delivery, SEPA Direct Debit |
| [Activate in dashboard](#activate-in-dashboard) | Banking methods, E-Invoicing   |
| [Own flow](#own-flow) | AfterPay, Betaal per Maand, Klarna, Edenred, gift cards, Paysafecard, PayPal |

> ℹ️ Ready-made integrations
> If you use a [ready-made integration](/docs/our-integrations/), first check that the payment method is supported. 
> Once the method is activated, also enable it in your <<glossary:backend>>.

# Apply to MultiSafepay 

1. Email a request to <risk@multisafepay.com> 
    
    <details id="required-information-for-cards-apple-google"> 
    <summary>Required information for cards, Apple Pay, and Google Pay</summary>
    <br>
    
    For cards, Apple Pay, and Google Pay, include in the request your: 
    - Average, minimum, and maximum transaction amount 
    - Annual turnover 
    </details>

    <details id="required-information-for-sepa-direct-debit"> 
    <summary>Required information for SEPA Direct Debit</summary>
    <br>

    For SEPA Direct Debit, include in the request the following information:
    - Monthly and annual SEPA Direct Debit transaction volume
    - Minimum and maximum transaction amount
    - Type of products sold using this payment method
    - Whether you want to accept [recurring payments](/docs/recurring-payments/)
    - Whether any subscriptions are monthly, quarterly, or annual
    - Any additional information we request
    We send you an agreement to sign and email back to us.
    </details>
2. We check your eligibilty and if approved, activate the payment method for your account. 
3. Once approved, activate the method in your dashboard as below.

# Activate in dashboard

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Settings**. 
3. To enable the payment method for:
    - All sites, go to **Payment methods**.
    - A specific site, go to **Website settings**, and click the relevant site.
4. Select the checkbox for the relevant payment method, and then click **Save changes**.

> **Support:** If the payment method isn't visible in your dashboard, email <integration@multisafepay.com>

# Own flow

## AfterPay
<details id="how-to-activate-afterpay"> 
<summary>How to activate AfterPay</summary>
<br>

1. To check you are eligible for AfterPay, email <sales@multisafepay.com>
2. For new AfterPay clients, apply directly to AfterPay:
    - The Netherlands: [Offerte](https://www.afterpay.nl/nl/zakelijk/offerte)
    - Belgium: [Offerte aanvragen](https://www.afterpay.be/be/footer/zakelijke-partners/offerte-aanvragen)
3. For existing AfterPay clients, to activate AfterPay for your MultiSafepay account, email AfterPay Sales at <sales@afterpay.nl>  
</details>

## Betaal per Maand

<details id="how-to-activate-betaal-per-maand">
<summary>How to activate Betaal per Maand</summary>
<br>

You must:

- Have a [MultiSafepay account](/docs/getting-started-guide/)
- Be registered with a Dutch Chamber of Commerce (no exceptions)
- Have an annual turnover of more than 500,000 EUR (unless agreed otherwise with Betaal per Maand)
- Sell products or services to European citizens with a residential or delivery address in the Netherlands (no exceptions)
- Connect to MultiSafepay via our API or [ready-made integrations](/docs/our-integrations/)

1. Email a request to <sales@multisafepay.com>
2. In the request, let us know if you already have a Santander account. If you don't, we'll submit an application for you. 
3. We check your eligibility and type of connection. 
4. Once approved, we activate the payment method for your account.

</details>

## Edenred
<details id="how-to-activate-edenred">
<summary>How to activate Edenred</summary>
<br>

1. Fill out the Edenred – [Registreer mijn website](https://registreermijnwebsite.edenred.be/) form, selecting the relevant checkbox for each voucher you want to offer.
2. Sign a contract with Edenred. They'll give you an Edenred Merchant ID.
3. Email your Edenred Merchant ID to <sales@multisafepay.com>
4. We activate the payment method for your account.
</details >

## Gift cards
<details id="how-to-activate-gift-cards">
<summary>How to activate gift cards</summary>
<br>

1. To check your eligibility, email <sales@multisafepay.com> 
2. Send a request to the **card issuer**, providing your company details and MultiSafepay account ID.
3. The issuer connects you to the card via either:
    - [Intersolve](https://intersolve.nl/contact) (majority of gift cards)
    - [Fashioncheque](https://www.fashioncheque.com/nl/customerservice)
    - [123TCS](https://www.123tcs.com/#Contact)
4.  The issuer sends us the connection details and we activate the card for your account.
</details>

### Klarna
How to activate with a Klarna:

<details id="test-account"> 
<summary>Test account</summary>
<br>

1. At [Klarna.com](https://www.klarna.com/nl/), sign up for a test account, selecting the **Playground** environment. 
2. Under **Settings**, click **Generate new Klarna API credentials** to generate a user name and password.
3. Email these credentials to <sales@multisafepay.com> 
4. MultiSafepay connects to Klarna. 

We recommend testing Klarna payments via the Klarna Portal to experience the full functionality. You can also test from your **test** MultiSafepay dashboard with more limited functionality.

</details>

<details id="live-account"> 
<summary>Live account</summary>
<br>

1. Sign up for a live Klarna account:
    - Via the Klarna website, selecting the **Production** environment, **or**  
    - Email your Klarna account manager or <verkoop@klarna.com>
2. Specify MultiSafepay as your payment service provider and the countries you want to activate Klarna for.
3. Sign an agreement with Klarna, including pricing.
4. We activate Klarna for your MultiSafepay account. 
5. If using a ready-made integration, activate Klarna in your <<glossary:backend>>.

For questions, see Klarna – [Klantenservice](https://www.klarna.com/nl/klantenservice).

> **Support:** If the payment method isn't visible in your dashboard, email <integration@multisafepay.com>
</details>

## PayPal
<details id="how-to-configure-your-paypal-account">
<summary>How to configure your PayPal account</summary>
<br>

To configure your PayPal account, follow these steps:

1. Sign in to your business account at [Paypal.com](https://www.paypal.com).
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
3. From the list, select **Western European languages (including English)**.
4. Click **More options**.
5. From the **Encoding** list, select **UTF-8**.
6. Select the **Yes** checkbox, and then click **Save**.

<blockquote class="callout callout_info">
    <h3 class="callout-heading false">
        <span class="callout-icon">💬</span>
        <p>Support</p>
    </h3>
    <p>- MultiSafepay – <a href="mailto:integration@multisafepay.com">integration@multisafepay.com</a></p>
    <p>- PayPal – <a href="https://www.paypal.com/us/smarthelp/contact-us">Contact us</a></p>
</blockquote>

> ⚠️ Known error
> If your PayPal business account isn't yet fully verified or approved, you might get a PayPal error 10002: Restricted account.

</details>

<details id="how-to-configure-your-multisafepay-account">
<summary>How to configure your MultiSafepay account</summary>
<br>

To configure your MultiSafepay account for PayPal, follow these steps:

1. Sign in to your business account at [Paypal.com](https://www.paypal.com).
2. Mouse over your account name in the top-right corner, and then select **Account settings**.
3. On the **Business information** tab, copy your PayPal Merchant ID.
4. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com), and then go to **Settings**. 
5. To activate PayPal for:
    - All your sites:
        - Go to **Payment methods**, and then select **PayPal**.
        - In the **PayPal Merchant ID** field, paste your ID, and click **Save changes**.
    - A specific site:
        - Go to **Website settings**, and click the relevant site.
        - Under **Payment methods**, select the **PayPal** checkbox, and click **Save changes**.

> ℹ️ **Notes** 
> - You can link each site to a separate PayPal business account, or all sites can use your main PayPal business account.
> - If PayPal isn't visible as a payment method in your dashboard, email <integration@multisafepay.com> 

> ✅ Success
> Your account is now configured!  

We strongly recommend [testing transactions](/docs/testing/) before processing live payments. 
</details>

<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)