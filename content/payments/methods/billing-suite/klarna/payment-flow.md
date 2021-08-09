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

The table below shows a successful payment flow from start to finish.  

{{< details title="About order and transaction statuses" >}}

- Order status: the progression of the customer's order with you, independent of the payment
- Transaction status: the progression towards settlement in your MultiSafepay balance

For more information, see [About MultiSafepay statuses](/api/multisafepay-statuses/).

{{< /details >}}

|                       | Flow      | Order status | Transaction status |
|--------------------------------|-----------|---|-----------------------------------------------------------------------------------------|
|  1. | The customer initiates a transaction on the Klarna payment page. {{< br >}} See also [Reservation and invoice numbers](/payments/methods/billing-suite/klarna/user-guide/reservation-and-invoice-number/). | Uncleared   | Initialized  |
| 2. | Klarna authorizes the payment. | Completed  | Uncleared  |
| 3. | Once authorized, MultiSafepay sends a capture to Klarna. |     |   |
| 4. | Ship the order within 28 days, or [extend the shipping period](/payments/methods/billing-suite/klarna/user-guide/extending-shipping-period/). {{< br >}} See also [Supported addresses](/payments/methods/billing-suite/klarna/user-guide/supported-addresses/). | | |
| 5. | [Change the order status to Shipped](/payments/methods/billing-suite/klarna/user-guide/changing-order-status--to-shipped/).  | Shipped | Uncleared | 
| 6. | Klarna invoices the customer. Settlement is now guaranteed. {{< br >}} See also [Customizing invoices](/payments/methods/billing-suite/klarna/user-guide/customizing-invoices/). | | |
| 7. | The customer completes the payment with Klarna. |     |   |
| 8. | Klarna settles the funds with MultiSafepay. | Shipped    | Completed  |
| 9. | MultiSafepay adds the funds to your MultiSafepay balance.| Completed | Completed |

## Unsuccessful statuses
You can cancel payments before the funds are captured. After the funds are captured you can only process a refund.

| Description                      | Order status      | Transaction status |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Klarna has declined the payment. See Klarna&nbsp;–&nbsp;[Contact customer service](https://www.klarna.com/international/contact-customer-service). {{< br >}} **Or** {{< br >}} The customer or merchant canceled the payment.    | Void   | Cancelled   |
| The payment was not completed or the [order status did not change to Shipped]((/payments/methods/billing-suite/klarna/user-guide/changing-order-status-to-shipped/)), and the transaction expired. {{< br >}} Expired transactions cannot be reactivated but still appear in your MultiSafepay account **Transaction overview**. Create a new order, if required.  | Expired    | Expired    |

## Refund statuses

| Description                      | Order status      | Transaction status |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| The customer requests a refund. | Initialized    | Completed   |
| The refund is successfully processed.  | Completed      | Completed   |


