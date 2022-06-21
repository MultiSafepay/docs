---
title: 'Second Chance reminders'
category: 6278c92bf4ad4a00361431b0
order: 800
hidden: false
slug: 'second-chance'
excerpt: 'Boost conversion by sending customers reminders about abandoned payments.'
---
Second Chance is a MultiSafepay service that automatically emails customers a payment link when they initiate but don't complete a transaction. This helps boost conversion and impulse purchases. The first email is sent 1 hour after the customer initiates the payment, and a second after 24 hours.

Second Chance emails are also sent for manually generated [payment links](/payment-links/) if the customer doesn't click the link to complete payment.

# Requirements

- Under the [GDPR](/gdpr), you must obtain documented consent from the customer to send Second Chance emails.
- You must include the customer's email address in the transaction API request.
- Second Chance emails cannot be activated or sent to the customer while the status of the original transaction is **Uncleared**, or once it is **Completed**.
- Payment links in Second Chance emails have the same lifetime as the original payment link, which is set to 30 days by default. 

# Activation

<details id="how-to-activate-second-chance">
<summary>How to activate Second Chance</summary>
<br>

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Settings** > **Website settings**.
3. Select the relevant site.
4. Under **Website functionality**, select the **Enable Second Chance** checkbox.

</details>

# Integration

To integrate, see API recipe – [Send payment reminders](https://docs-api.multisafepay.com/recipes/send-payment-reminders).
<br>

---

# User guide

## Customization

The Second Chance email template is completely customizable.

<details id="how-to-customize-templates">
<summary>How to customize templates</summary>
<br>

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Settings** > **Email templates**.
3. Select the relevant site.
4. Click **Add new template**.
5. From the **Type** list, select **Second Chance email (to consumer)**.
6. From the **Language** list, select the relevant language.
7. Click **Load default template**.

For how to customize the template, see [Customer emails](/customer-emails/).

</details>

## Payment methods

<details id="supported-payment-methods">
<summary>Supported payment methods</summary>
<br>

The following payments methods are not supported because they follow a different payment flow:

- [AfterPay](/afterpay)
- [Bank Transfer](/bank-transfer)
- [Betaal per Maand](/betaal-per-maand)
- [SEPA Direct Debit](/sepa-direct-debit)
- [Klarna](/klarna)
- [Pay After Delivery](/pay-after-delivery)

</details>

## Potential errors

- Second Chance emails can cause issues when running an enterprise resource planning (ERP) system.
- If you have another order for the same total amount with the same customer email address completed in the last 120 minutes, Second Chance emails are suppressed.

<details id="errors-in-external-plugins">
<summary>Errors in external plugins</summary>
<br>

Second Chance emails can create conflicts with external warehouse systems. In some cases, this can be resolved using a cron job. However, this is not always a stable solution.

For example, when a customer cancels an order in the webshop, they can still pay for it using Second Chance within 30 days or a specified time frame. For more information, see API reference - [Create order](https://docs-api.multisafepay.com/reference/createorder) > `days_active` parameter.

If a cancelled order is subsequently paid for, MultiSafepay reopens the order in the webshop. A warehouse system may have already released the reservation on the order when it received **Cancelled** status, or may consider the **Cancelled** status permanent. As result, the items the customer ordered may no longer be available or in stock.

</details>

## Reports

For an overview of all Second Chance emails that resulted in successful payment, see [Second Chance report](/second-chance-report/).
<br>

---

> 💬  Support
> Email <support@multisafepay.com>
[Top of page](#)