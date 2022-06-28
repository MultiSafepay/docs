---
title: 'PayPal'
category: 6298bd782d1cf4006032e765
order: 507
hidden: false
parentDoc: 62a6ec51d7a8100053916d99
slug: 'paypal'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Payment_methods/PayPal.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

[PayPal](https://www.paypal.com/nl/home) is a leading global payment method that lets customers pay by credit card or create a digital wallet linked to multiple payment methods.

Read how PayPal can benefit your business on [multisafepay.com](https://www.multisafepay.com/solutions/payment-methods/paypal)

| Supports | Details |
|---|---|
| **Chargebacks**  |  [Yes](/docs/chargebacks/)  |
| **Countries**  | Worldwide  | 
| **Currencies**  | [Multiple](https://developer.paypal.com/docs/reports/reference/paypal-supported-currencies/) | 
| **Payment components** | [Yes](/docs/payment-components/) | 
| **Payment pages** | [Yes](/docs/payment-pages/) (current and deprecated versions) |
| **Refunds** | [Yes](/docs/refund-payments/): Full and partial (see guidance below) | 
| **Second Chance** | [Yes](/docs/second-chance/) | 

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/readmedocs-staging/static/diagrams/svg/paypal-payment-flow.svg" alt="PayPal payment flow" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;
  width: 100%;">

> ℹ️ **Note** 
> MultiSafepay does **not** collect funds for PayPal transactions.

# Payment statuses 

The table below sets out the <<glossary:order status>> and <<glossary:transaction status>> for payments and refunds.

| Description | Order status | Transaction status |
|---|---|---|
| The customer has been redirected to PayPal. | Initialized | Initialized |
| Awaiting the customer to pay in their PayPal account, **or** <br> PayPal is authorizing the transaction, **or** <br> You may need to enable the currency and then authorize the payment in your PayPal business account.  | Uncleared | Initialized |
| PayPal has collected payment. | Completed | Initialized |
| The customer cancelled the payment in PayPal. | Void   | Void/Cancelled   |
| The customer didn't complete payment within 14 days. | Expired | Expired |
| **Refunds:** Refund initiated. | Reserved | Initialized |
| **Refunds:** Refund complete.  | Completed | Initialized |
| Refund declined. | Declined | Declined |
| PayPal is authorizing the refund, **or** <br> There are not enough funds in your PayPal business account to process the refund. <br> For more information, see your PayPal business account. | Uncleared | Initialized   |

# Activation 

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

> 💬  Support 
> - MultiSafepay – <integration@multisafepay.com>
> - PayPal – [Contact us](https://www.paypal.com/us/smarthelp/contact-us)

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

# Integration

### API
- [Create order](https://docs-api.multisafepay.com/reference/createorder) > Wallet order. 
- Examples > PayPal direct/redirect.
- Transactions expire after 14 days.

### Ready-made integrations
Supported in all [ready-made integrations](/docs/our-integrations/).

### Testing
To test PayPal payments, see [Testing](/docs/testing#wallets).
<br>

---

# User guide

## PayPal Seller Protection

PayPal Seller Protection covers you in the event of claims, chargebacks, or <<glossary:reversals>> due to unauthorized purchases or items the customer didn't receive. You are covered for the full amount of all eligible transactions.

To be eligible, for specific countries, transaction requests must contain the correct `state` in the `customer_address`. 

- For a list of the countries, see PayPal API – [State codes](https://developer.paypal.com/api/rest/reference/state-codes/).
- For more information, see PayPal – [What is Seller Pretection](https://www.paypal.com/cs/smarthelp/article/what-is-the-seller-protection-policy-and-what-items-aren%E2%80%99t-covered-faq1156).

## Refunds

Refunds are only processed if there are enough funds in your PayPal business account. Otherwise, PayPal issues an [eCheck](https://www.paypal.com/us/smarthelp/article/what-is-an-echeck-faq1082). 

To avoid PayPal cancelling the refund, in your PayPal account, authorize PayPal to withdraw funds from another bank account instead. 

For support, contact PayPal – [Help Center Home](https://www.paypal.com/us/smarthelp/home).

## Your logo in PayPal's checkout

You can display your logo in the PayPal checkout to increase brand recognition and trust. 

<details id="how-to-display-your-logo-in-paypal-checkout">
<summary>How to display your logo in PayPal's checkout</summary>
<br>

To display your header or logo on the PayPal checkout page, follow these steps:

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Settings** > **Files**, and upload the relevant images. 
3. Go to **Payment methods** at the bottom right, and then select the relevant images from the **Logo** and **Header** list. 
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
