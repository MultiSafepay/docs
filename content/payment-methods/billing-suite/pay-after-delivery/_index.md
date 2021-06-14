---
title: 'Pay After Delivery'
weight: 170
meta_title: "Payment methods Pay After Delivery - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
layout: 'single'
faq: '.'
logo: '/logo/Payment_methods/Pay_After_Delivery.svg' 
short_description: "MultiSafepay's own post-payment solution for Dutch merchants"
aliases:
    - /support-tab/magento2/payment-methods/pay-after-delivery
    - /payment-methods/billing-suite/pay-after-delivery/activate-pay-after-delivery 
    - /payment-methods/billing-suite/pay-after-delivery/how-does-pay-after-delivery-work
    - /payment-methods/billing-suite/pay-after-delivery/pay-after-delivery-testing
    - /payment-methods/billing-suite/pay-after-delivery/refund-pay-after-delivery
    - /payment-methods/billing-suite/pay-after-delivery/what-is-pay-after-delivery
---

## About Pay After Delivery
Pay After Delivery is MultiSafepay's own online post-payment method that lets customers pay for orders after receiving them, increasing customer confidence and conversion. Customers are only charged for the items they keep from the order. MultiSafepay bears the full risk, based on the customer's history, and guarantees payout of the transaction.

|   |   |  | 
|---|---|---| 
| **Payment type**   | Post-payment method   | | 
| **API flow**  | `Direct`/`Redirect`  | [More information](/faq/api/difference-between-direct-and-redirect) | 
| **Countries**  | Netherlands  |  | 
| **Currencies**  | EUR  |  |
| **Refunds**  | Full and partial  | [More information](/payment-methods/billing-suite/pay-after-delivery/faq/processing-refunds/) |
| **Recurring payments** | No  | [More information](/tools/recurring-payments) |
| **Chargebacks**  | No  | [More information](/faq/chargebacks)  |

### Product rules

{{< details title="Gift cards" >}}
&nbsp;  
Post-payment methods do not generally support entering [gift card](/payment-methods/prepaid-cards/gift-cards) details **after** the order is placed (for a whole or partial payment). This is because, as the collecting party, Pay After Delivery requires very precise order specifications. 

{{< /details >}}

{{< details title="Multiple order rules" >}}
&nbsp;  
If you supply multiple order rules with the same `merchant-item-id`and the customer requests a partial refund, this creates a conflict. 

To successfully process partial refunds for the same product with different specifications (e.g. size, color) via the shopping cart, each `merchant-item-id` must be unique.

**Example:** For different-sized products, differentiate the `merchant-item-id` with `-size`: 1001311-xxl, 1001311-m, 1001311-s.

{{< /details >}}

- Minimum and maximum order amounts apply. For more information, email your account manager at <sales@multisafepay.com>

- The delivery and invoice addresses must be the **same** to prevent fraud. For&nbsp;more information, see MultiFactor – [Shipping policies](https://www.multifactor.nl/voorwaarden/shipping-policies).

- You cannot [adjust payment link lifetimes](/faq/api/lifetime-of-a-payment-link).

## Payment flow

The table below shows a successful Pay After Delivery payment flow from start to finish.

In your MultiSafepay Control > **Transaction overview** > **Transaction details** page under **Status history**, there are two statuses that change as the flow progresses:

- Order status: indicates the status of the customer’s order with the merchant independent of the payment
- Transaction status: indicates the status of the payment

|   | Flow  | Order status  | Transaction status  | 
|---|---|---|---|
|  1. | The customer agrees with the terms and conditions and initiates a transaction.  | Uncleared  | Uncleared  |
| 2.  | MultiSafepay approves or declines the transaction within 2 business days.  |   |   |
|   | The transaction is successful.  | Completed | Uncleared  |
| 3.  | Ship the order. {{< br >}} The order can no longer be cancelled. {{< br >}} See also [Closing transactions](/payment-methods/billing-suite/pay-after-delivery/faq/closing-transactions).  | Shipped  | Uncleared  |
| 4.  | [Change the order status to Shipped](/payment-methods/billing-suite/pay-after-delivery/faq/changing-order-status-to-shipped/).   |   |   |
| 5.  | MultiSafepay sends Pay After Delivery a capture, and Pay After Delivery confirms the transaction.   |   |   |
| 6.  | MultiFactor emails the customer an invoice containing a payment link within 24 hours of changing to **Shipped** status. {{< br >}} Your payout is now guaranteed. |   |   |
| 7.  | The customer has 14 days to pay the invoice. {{< br >}} See also [Failure to pay](#failure-to-pay) below.  |   |   |
| 8.  | MultiSafepay adds the funds to your MultiSafepay balance within 30 days of changing to **Shipped** status.  | Shipped  | Completed  |

### Failure to pay

If the customer fails to pay within the initial 14 day period, MultiFactor emails them reminders with new payment links, each valid for 6 days: 

- The first and second reminders are free. 
- With the third, we add a fee of 7.50 EUR to the invoice. 
- With the fourth, we add a fee of 12.50 EUR to the invoice. 

If the customer still fails to pay, the amount of the total invoice is transferred to a debt collection agency. 

To stop sending reminders, credit the invoice for a zero amount. 

### Other statuses

| Description  | Order status  | Transaction status  | 
|---|---|---|
| The transaction has been cancelled.  | Void  | Cancelled  |
| The customer did not complete the transaction within 90 days of initiating it and the transaction has expired.  | Expired  | Expired  |

### Refund statuses

For how to process refunds, see [Processing refunds](/payment-methods/billing-suite/pay-after-delivery/faq/processing-refunds/).

| Description                      | Order status     | Transaction status  |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| The customer has requested a refund. | Initialized    | Initialized   |  
|  The refund is successfully processed. | Completed      | Completed | 

## Activation
To check your eligibility for Pay After Delivery, email your account manager at <sales@multisafepay.com>

To activate Pay After Delivery, phone +31 20 8500 502 or email your account manager at <sales@multisafepay.com> 

## Integration and testing
To integrate Pay After Delivery using our API, see API Reference – [Pay After Delivery](/api/#pay-after-delivery).

{{< details title="View credentials and testing process" >}}

Test addresses:

- Kraanspoor 39C, 1033SC Amsterdam
- Vlierweg 12D, 1032LG Amsterdam

Sample statuses:

| Status    | Description              |
| --------- | ------------------------ |
| **Completed** | Transaction was completed |
| **Declined** | Transaction was declined |

{{< /details >}}

