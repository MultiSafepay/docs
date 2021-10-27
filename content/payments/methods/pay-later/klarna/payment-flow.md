---
title: 'Klarna payment flow'
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "Klarna payment flow - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
logo: '/logo/Payment_methods/Klarna.svg'
url: '/payment-methods/klarna/payment-flow/'
aliases:
    - /payments/methods/billing-suite/klarna/payment-flow/
---

The table below shows a successful payment flow from start to finish.  

{{< details title="About order and transaction statuses" >}}

- Order status: the progression of the customer's order with you, independent of the payment
- Transaction status: the progression towards settlement in your MultiSafepay balance

For more information, see [About MultiSafepay statuses](/payments/multisafepay-statuses/).

{{< /details >}}

|        | Flow      | Order status | Transaction status |
|------|---|---|------|
| 1. | The customer selects Klarna at checkout and is redirected to the Klarna payment page to initiate a transaction. {{< br >}} See also [Reservation and invoice numbers](/payments/methods/billing-suite/klarna/user-guide/reservation-and-invoice-number/). | Uncleared   | Initialized  |
| 2. | Klarna authorizes the payment. Settlement is now guaranteed, but not received until after you ship the order. | Completed  | Uncleared  |
| 3. | Ship the order within 28 days, or [extend the shipping period](/payments/methods/billing-suite/klarna/user-guide/extending-shipping-period/). {{< br >}} You **must**: {{< br >}} - Ship the order to receive payment. {{< br >}} - Manually [change the order status to Shipped](/payments/methods/billing-suite/klarna/user-guide/changing-order-status-to-shipped/). {{< br >}} See also [Supported addresses](/payments/methods/billing-suite/klarna/user-guide/supported-addresses/). | Shipped | Uncleared |
| 4. | Klarna invoices the customer. {{< br >}} See also [Customizing invoices](/payments/methods/billing-suite/klarna/user-guide/customizing-invoices/). | | |
| 5. | Klarna settles the funds with MultiSafepay, and we add them to your MultiSafepay balance within 21 days. | Shipped    | Completed  |

## Unsuccessful statuses
You can cancel payments before the funds are captured. After the funds are captured you can only process a refund.

| Description                      | Order status      | Transaction status |
|------|----|----|
| Klarna did not authorize the transaction. For more information, email <klarna@multisafepay.com> {{< br >}} **Or** {{< br >}} The customer or merchant cancelled the payment.    | Void   | Cancelled |
| You did not [change the order status to **Shipped**](/payment-methods/klarna/changing-order-status-to-shipped/) within 28 days. {{< br >}} If you have already shipped the order but didn't change the status: {{< br>}} - In your MultiSafepay account, go to **Transaction overview**, and select the expired transaction. {{< br >}} - Click **Payment link**, and then click **Duplicate this order**. {{< br >}} - Click **Generate payment link**. {{< br >}} - Send the payment link to the customer. {{< br >}} Alternatively, you can [create a new Klarna order](/api/#klarna), [change the status to **Shipped**](/payment-methods/klarna/changing-order-status-to-shipped/), and send the payment link to the customer. | Expired    | Expired    |


## Refund statuses

| Description  | Order status      | Transaction status |
|-----|----|------|
| The customer requests a refund. | Initialized    | Completed   |
| The refund is successfully processed.  | Completed      | Completed   |

{{< details title="Get support" >}} 

**Merchants**: email MultiSafepay at <klarna@multisafepay.com>

**Customers**:

- See Klarna – [Contact customer service](https://www.klarna.com/international/contact-customer-service).
- Email the Support Team at <support@multisafepay.com>


{{< /details >}}
