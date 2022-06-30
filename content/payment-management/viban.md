---
title: 'Virtual IBANs'
category: 6278c92bf4ad4a00361431b0
order: 100
hidden: false
slug: 'virtual-ibans'
excerpt: "Collect bank transfers and direct debits in your own bank account."
---
A virtual international bank account number (VIBAN) in your company name removes MultiSafepay branding from the customer experience for [Bank Transfer](/docs/bank-transfer/) and [SEPA Direct Debit](/docs/sepa-direct-debit/), and helps you better manage payments. 

A VIBAN isn't connected to an actual bank account and simply routes incoming funds to MultiSafepay's account to collect. However, MultiSafepay's name no longer appears in payment instructions or on customer bank statements.   

# How it works

For bank transfers, customers receive your VIBAN details in payment instructions instead of MultiSafepay's IBAN, in both [payment pages](/docs/payment-pages/) and emails (including for the [direct flow](/docs/bank-transfer#payment-flow)). Your company name appears on the customer's bank statement. Customers don't see MultiSafepay's name at any point and enjoy a cohesive experience with your brand.

For direct debits, there is no change for customers when completing payment. However, your company name appears on bank statements, which increases brand recognition and trust, and can reduce [chargebacks](/docs/sepa-direct-debit#chargebacks).

You can apply for a VIBAN for your MultiSafepay account, or for a specific site.

VIBANs can only be used for transactions in EUR.

# Activation

Email a request for a VIBAN including required information to <sales@multisafepay.com>

<details id="required-information">
<summary>Required information</summary>
<br>

Include in the request:

- Whether you want to use in your dashboard the:
    - Refunds tool
    - Matching tool
- The company name you want to appear on bank statements
- Whether you want to use the VIBAN to:
    - Receive funds only
    - Refund/pay out funds only
    - Receive **and** refund/pay out funds

</details>

# Integration

Once activated, no integration is required.
<br>

---

# User guide

## Refunds

You can also make [refunds](/docs/refunds/) using your VIBAN, and manage them from your MultiSafepay dashboard. Your company name appears on bank statements instead of MultiSafepay's name.

You need to request this functionality when applying for your VIBAN.

## Matching payments

Most incoming payments are automatically matched to the relevant order in your account. However, if the customer accidentally provides incorrect information or pays the wrong amount, MultiSafepay matches them manually. See Bank Transfer – [Matching payments](/docs/bank-transfer#matching-payments). 

With a VIBAN, you can resolve unmatched payments yourself in your MultiSafepay dashboard. You need to request this functionality when applying for your VIBAN.

Once activated, an alert appears on your dashboard home page when you have unmatched payments to resolve. A new section appears under **Transactions**, called **Unmatched payments**. With this tool, you can perform the following actions: 

| Unmatched payment | Action | Outcome |
|---|---|---|
| Correct amount | Match to order | The <<glossary:order status>> changes to **Completed**. <br> An explanation appears on the **Transaction details** page under **Notes**.|
| Amount too high | Match and refund the excess | The order status changes to **Completed**. <br> A new refund order linked to the original order is created for the excess amount, and an explanation appears on the **Transaction details** page under **Notes**. |
|  | Partially match and reserve the excess | The order status changes to **Completed**. <br> The excess amount is reserved for future orders. |
|  | Match and keep the excess | The order status changes to **Completed**. <br> A new order (status **Completed**) linked to the original order is created to credit the excess to your account balance. <br> - An explanation appears on the **Transaction details** page under **Notes**. |
| Amount too low | Match and make up deficit from your account balance | The order status changes to **Completed**. <br> The deficit is debited from your balance as a transaction fee. <br> - An explanation appears on the **Transaction details** page under **Notes**. |
|  | Match and collect deficit | The order status changes to **Completed**. <br> A new Bank Transfer order (linked to the original order) is created with a payment link for the customer to pay the outstanding amount. |
| Refund requested | Refund in full | A refund order linked to the original order is created and the payment is refunded. |
| Lump payment | Match the payment to multiple orders | Divide the payment across multiple orders and their status changes to **Completed**. <br> If there is any excess after all relevant orders are matched, you can refund, reserve, or keep the excess (see above). <br> If there are not enough funds for all relevant orders, you can make up the deficit from your account balance or create a new order for the outstanding amount (see above).| 
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)