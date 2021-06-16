---
title: 'Klarna payment flow'
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "Klarna payment flow - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
logo: '/logo/Payment_methods/Klarna.svg'
---

The table below shows the Klarna payment flow from start to finish.  

In your MultiSafepay Control > **Transaction overview** > **Transaction details** page under **Status history**, there are two statuses that change as the flow progresses: 

- Order status: indicates the status of the customer's order with the merchant independent of the payment
- Transaction status: indicates the status of the payment

|                       | Flow      | Order status | Transaction status |
|--------------------------------|-----------|---|-----------------------------------------------------------------------------------------|
|  1. | The customer initiates a transaction on the Klarna payment page. {{< br >}} See also [Reservation and invoice numbers](/payment-methods/billing-suite/klarna/faq/reservation-and-invoice-number/). | Uncleared   | Initialized  |
| | The transaction is successful, but Klarna hasn't received payment yet. | Completed  | Uncleared  |
| 2. | Klarna confirms the transaction. | | |
| 3. | Ship the order within 28 days, or [extend the shipping period](/payment-methods/billing-suite/klarna/faq/extending-shipping-period/). {{< br >}} See also [Supported addresses](/payment-methods/billing-suite/klarna/faq/supported-addresses/). | | |
| 4. | [Change the order status to Shipped](/payment-methods/billing-suite/klarna/faq/changing-order-status--to-shipped/).  | | | 
| 5. | MultiSafepay sends a capture to Klarna. | Shipped    | Uncleared  |
| 6. | Klarna sends the customer an invoice. Your payout is now guaranteed. {{< br >}} See also [Customizing invoices](/payment-methods/billing-suite/klarna/faq/customizing-invoices/). | | |
| 7. | Klarna pays the funds to MultiSafepay. | Shipped    | Completed  |
| 8. | MultiSafepay adds the funds to your MultiSafepay balance.| | |

## Other statuses

| Description                      | Order status      | Transaction status |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Klarna has rejected the transaction. See Klarna&nbsp;–&nbsp;[Contact customer service](https://www.klarna.com/international/contact-customer-service). {{< br >}} **Or** {{< br >}} The customer or merchant cancelled the transaction.    | Void   | Cancelled   |
| The transaction was not completed or the [order status did not change to Shipped]((/payment-methods/billing-suite/klarna/faq/changing-order-status-to-shipped/)), and the transaction expired. {{< br >}} Expired transactions cannot be reactivated but still appear in your MultiSafepay Control **Transaction overview**. Create a new order, if required.  | Expired    | Expired    |

## Refund statuses

For how to process refunds, see [Processing refunds](/payment-methods/billing-suite/klarna/#processing-refunds).

| Description                      | Order status      | Transaction status |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| The customer requests a refund. | Initialized    | Completed   |
| The refund is successfully processed.  | Completed      | Completed   |
