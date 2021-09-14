---
title: 'Klarna payment flow'
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "Klarna payment flow - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
logo: '/logo/Payment_methods/Klarna.svg'
---

The table below shows a successful payment flow from start to finish.  

{{< details title="About order and transaction statuses" >}}

- Order status: the progression of the customer's order with you, independent of the payment
- Transaction status: the progression towards settlement in your MultiSafepay balance

For more information, see [About MultiSafepay statuses](/payments/multisafepay-statuses/).

{{< /details >}}

|        | Flow      | Order status | Transaction status |
|------|---|---|------|
| 1. | The customer selects Klarna in your checkout and is redirected to the Klarna payment page to initiate a transaction. {{< br >}} See also [Reservation and invoice numbers](/payments/methods/billing-suite/klarna/user-guide/reservation-and-invoice-number/). | Uncleared   | Initialized  |
| 2. | Klarna authorizes the payment. Settlement is now guaranteed, but not received until after you ship the order. | Completed  | Uncleared  |
| 3. | Ship the order within 28 days, or [extend the shipping period](/payments/methods/billing-suite/klarna/user-guide/extending-shipping-period/). {{< br >}} See also [Supported addresses](/payments/methods/billing-suite/klarna/user-guide/supported-addresses/). | | |
| 4. | **Important:** You **must** manually [change the order status to Shipped](/payments/methods/billing-suite/klarna/user-guide/changing-order-status--to-shipped/) in your MultiSafepay account.  | Shipped | Uncleared | 
| 5. | Klarna invoices the customer. {{< br >}} See also [Customizing invoices](/payments/methods/billing-suite/klarna/user-guide/customizing-invoices/). | | |
| 6. | Klarna settles the funds with MultiSafepay, and we add them to your MultiSafepay balance within 21 days. | Shipped    | Completed  |

## Unsuccessful statuses
You can cancel payments before the funds are captured. After the funds are captured you can only process a refund.

| Description                      | Order status      | Transaction status |
|------|----|----|
| Klarna has declined the payment. See Klarna&nbsp;–&nbsp;[Contact customer service](https://www.klarna.com/international/contact-customer-service). {{< br >}} **Or** {{< br >}} The customer or merchant cancelled the payment.    | Void   | Cancelled   |
| The payment was not completed within the 1-day period or the [order status did not change to Shipped]((/payments/methods/billing-suite/klarna/user-guide/changing-order-status-to-shipped/)), and the transaction expired. {{< br >}} Expired transactions cannot be reactivated but still appear in your MultiSafepay account **Transaction overview**. Create a new order, if required.  | Expired    | Expired    |

## Refund statuses

| Description  | Order status      | Transaction status |
|-----|----|------|
| The customer requests a refund. | Initialized    | Completed   |
| The refund is successfully processed.  | Completed      | Completed   |

{{< details title="Get support" >}}
&nbsp;  
For customers:

- See Klarna – [Contact customer service](https://www.klarna.com/international/contact-customer-service)
- Email the Support Team at <support@multisafepay.com>

For merchants, email MultiSafepay at <klarna@multisafepay.com>

{{< /details >}}
