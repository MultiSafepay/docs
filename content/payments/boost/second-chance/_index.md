---
title: 'Second chance'
weight: 70
meta_title: "Second chance - MultiSafepay Docs"
layout: 'single'
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
logo: '/svgs/Second Chance.svg'
short_description: 'Send customers a friendly reminder to complete payments'
aliases:
    - /tools/second-chance/about-second-chance/
    - /tools/second-chance/what-is-second-chance
    - /tools/second-chance/requirements-and-potential-errors/
    - /tools/second-chance/how-to-enable-second-chance
    - /tools/second-chance/activating-second-chance/
    - /tools/second-chance/customizing-second-chance/
    - /tools/second-chance/how-to-personalize-the-second-chance-e-mail
    - /tools/second-chance/how-does-it-work
    - /tools/email-template
---

Second Chance is a MultiSafepay service that automatically emails customers a payment link when they initiate but don't complete a transaction. This helps increase conversion and boost impulse purchases. The first email is sent 1 hour after the customer initiates the payment, and a second after 24 hours.  

{{< details title="Requirements" >}}

- Under the [GDPR](/security-and-legal/gdpr), you must obtain documented consent from the customer to send Second Chance emails. 

- You must include the customer's email address in the transaction API request.

- Second Chance emails cannot be activated or sent to the customer while the status of the original transaction is **Uncleared**, or once it is **Completed**.

- Payment links in Second Chance emails have the same lifetime as the original payment link, which is set to 30 days by default. For more information, see [Adjusting payment link lifetimes](/developer/api/adjusting-payment-link-lifetimes).

- The following payments methods are not supported because they follow a different payment flow:
    - [Klarna](/payments/methods/billing-suite/klarna)
    - [AfterPay](/payments/methods/billing-suite/afterpay)
    - [Betaal per Maand](/payments/methods/billing-suite/betaalpermaand)
    - [Pay After Delivery](/payments/methods/billing-suite/pay-after-delivery)
    - [Bank transfer](/payments/methods/banks/bank-transfer)
    - [Direct Debit](/payments/methods/banks/sepa-direct-debit)

{{< /details >}}

## Activating Second Chance
To activate Second Chance, follow these steps:

1. Sign in to your [MultiSafepay account](https://merchant.multisafepay.com).
2. Go to **Settings** > **Website settings**.
3. Select the relevant website.
4. Under **Website functionality**, select the **Enable Second Chance** checkbox.

## Customizing the emails
The Second Chance email template is completely customizable. Follow these steps:

1. Sign in to your [MultiSafepay account](https://merchant.multisafepay.com).
2. Go to **Settings** > **Email templates**.
3. Select the relevant website. 
4. Click **Add new template**.
5. From the **Type** dropdown menu, select **Second Chance email (to consumer)**.
6. From the **Language** dropdown menu, select the relevant language.
7. Click **Load default template**. 

For how to customize the template, see [Email templates](/payments/boost/email-template/).



## Potential errors

{{< details title="External plugins" >}}

Second Chance emails can create conflicts with external warehouse systems. In some cases, this can be resolved using a [cron job](/faq/general/multisafepay-glossary/#cron). However, this is not always a stable solution. 

For example, when a customer cancels an order in the webshop, they can still pay for it using Second Chance within 30 days or a specified time frame. For more information, see [Adjusting payment link lifetimes](/developer/api/adjusting-payment-link-lifetimes/). 

If a cancelled order is subsequently paid for, MultiSafepay reopens the order in the webshop. A warehouse system may have already released the reservation on the order when it received **Cancelled** status, or may consider the **Cancelled** status permanent. As result, the items the customer ordered may no longer be available or in stock. 

{{< /details >}}

{{< details title="ERP systems" >}}

Second Chance emails can cause issues when running an enterprise resource planning (ERP) system. 

{{< /details >}}

{{< details title="Other orders" >}}
&nbsp;  
If you have another order for the same total amount with the same customer email address completed in the last 120 minutes, Second Chance emails are suppressed.

{{< /details >}}
