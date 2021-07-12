---
title: 'Second Chance'
weight: 70
meta_title: "Second Chance - MultiSafepay Docs"
layout: 'single'
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
logo: '/svgs/Second Chance.svg'
short_description: 'Reach out to your customers with a friendly payment reminder and stimulate impulse purchases.'
aliases:
    - /tools/second-chance/about-second-chance/
    - /tools/second-chance/what-is-second-chance
    - /tools/second-chance/requirements-and-potential-errors/
    - /tools/second-chance/how-to-enable-second-chance
    - /tools/second-chance/activating-second-chance/
    - /tools/second-chance/customizing-second-chance/
    - /tools/second-chance/how-to-personalize-the-second-chance-e-mail
    - /tools/second-chance/how-does-it-work
---

Second Chance is an email service to remind customers about payments they initiated but didn't complete. The first email is sent 1 hour after the customer initiated the payment, and a second after 24 hours. The emails contain a link to a payment page complete the payment. 

When enabled in your MultiSafepay account, Second Chance emails are sent to customers automatically. This helps increase conversion and boost impulse purchases.

## Activating Second Chance
To activate Second Chance, follow these steps:

1. Sign in to your [MultiSafepay account](https://merchant.multisafepay.com).
2. Select the website you want to enable the Second Chance for.
3. Under **Website functionality** tile, enable **Second Chance**.

## Customizing Second Chance
Second Chance emails are completely customizable using a Second Chance [email template](https://docs.multisafepay.com/tools/email-template/body-and-html).

To edit the email template, follow these steps:

1. Sign in to your [MultiSafepay account](https://merchant.multisafepay.com).
2. Go to **Settings**.
3. Download the standard Second Chance email and customize it as required.

**Note:** The email template contains a piece of formatted text. For technical support, contact your web developer.

## Requirements

{{< details title="Customer email address" >}}

Second Chance emails can only be sent if the customer's email address is included in the transaction request.

{{< /details >}}

{{< details title="Transaction status" >}}         

Second Chance emails cannot be activated or sent to the customer while the status of the original transaction is **Uncleared**, or once it is **Completed**.

{{< /details >}}

{{< details title="Payment methods" >}}

Second Chance emails can't be sent for the following payments methods because they follow a different payment flow:

- [Klarna](/payment-methods/billing-suite/klarna)
- [AfterPay](/payment-methods/billing-suite/afterpay)
- [Betaal per Maand](/payment-methods/billing-suite/betaalpermaand)
- [Pay After Delivery](/payment-methods/billing-suite/pay-after-delivery)
- [Bank transfer](/payment-methods/banks/bank-transfer)
- [Direct Debit](/payment-methods/banks/sepa-direct-debit)

{{< /details >}}

{{< details title="Customer consent" >}}

Under the [GDPR](/faq/gdpr/), you must obtain documented consent from the customer to send Second Chance emails. 

{{< /details >}}

{{< details title="Valid payment link" >}}

Payment links in Second Chance emails have the same lifetime as the original payment link, which is set to 30 days by default. 

For more information, see [Adjusting payment link lifetimes](/developer/api/adjusting-payment-link-lifetimes).

{{< /details >}}

## Potential errors

{{< details title="External plugins" >}}

Second Chance emails can create conflicts with external warehouse systems. In some cases, this can be resolved using a [cron job](/faq/general/multisafepay-glossary/#cron). However, this is not always a stable solution. 

For example, when a customer cancels an order in the webshop, they can still pay for it using Second Chance within 30 days or a specified time frame. For more information, see [Adjusting payment link lifetimes](/developer/api/adjusting-payment-link-lifetimes/). 

If a cancelled order is subsequently paid for, MultiSafepay reopens the order in the webshop. A warehouse system may have already released the reservation on the order when it received **Cancelled** status, or may consider the **Cancelled** status permanent. As result, the items the customer ordered may no longer be available or in stock. 

{{< /details >}}

{{< details title="ERP systems" >}}

Second Chance emails can cause issues when running an enterprise resource planning (ERP) system. 

{{< /details >}}