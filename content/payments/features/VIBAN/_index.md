---
title: 'Virtual IBANs'
weight: 95
meta_title: "Virtual IBANs - MultiSafepay Docs"
logo: '/svgs/Banks.svg'
layout: 'single'
short_description: "Collect bank transfers and direct debits in your own bank account."
url: '/features/virtual-ibans/'
---
A virtual international bank account number (VIBAN) in your company name removes MultiSafepay branding from the customer experience for [Bank Transfer](/payment-methods/bank-transfer/) and [SEPA Direct Debit]((/payment-methods/sepa-direct-debit/)), and helps you better manage payments. 

A VIBAN isn't connected to an actual bank account and simply routes incoming funds to MultiSafepay's account to collect. However, MultiSafepay's name no longer appears in payment instructions or on customer bank statements.   

## How it works

For bank transfers, customers receive your VIBAN details in payment instructions instead of MultiSafepay's IBAN, in both [payment pages](/payment-pages/) and emails (including for the [direct flow](/payment-methods/bank-transfer/payment-flow/)). Your company name appears on the customer's bank statement. Customers don't see MultiSafepay's name at any point and enjoy a cohesive experience with your brand.

For direct debits, there is no change for customers when completing payment. However, your company name appears on bank statements, which increases brand recognition and trust, and can reduce [chargebacks](/payment-methods/sepa-direct-debit/overview/#chargebacks).

You can apply for a VIBAN for your MultiSafepay account, or for a specific site.

VIBANs can only be used for transactions in EUR.

### Refunds

You can also make [refunds](/refunds/) using your VIBAN, and manage them from your MultiSafepay dashboard. Your company name appears on bank statements instead of MultiSafepay's name.

You need to request this functionality when applying for your VIBAN.

## Matching payments

Most incoming payments are automatically matched to the relevant order in your account. However, if the customer accidentally provides incorrect information or pays the wrong amount, MultiSafepay matches them manually. See [Resolving unmatched Bank Transfer payments](/bank-transfer/unmatched-payments/). 

With a VIBAN, you can resolve unmatched payments yourself in your MultiSafepay dashboard. You need to request this functionality when applying for your VIBAN.

Once activated, an alert appears on your dashboard home page when you have unmatched payments to resolve. A new section appears under **Transactions**, called **Unmatched payments**. With this tool, you can perform the following actions: 

| Unmatched payment | Action | Outcome |
|---|---|---|
| Correct amount | Match to order | The order status changes to **Completed**. {{< br >}} An explanation appears on the **Transaction details** page under **Notes**.|
| Amount too high | Match and refund the excess | The order status changes to **Completed**. {{< br >}} A new refund order linked to the original order is created for the excess amount, and an explanation appears on the **Transaction details** page under **Notes**. |
|  | Partially match and reserve the excess | The order status changes to **Completed**. {{< br >}} The excess amount is reserved for future orders. |
|  | Match and keep the excess | The order status changes to **Completed**. {{< br >}} A new order (status **Completed**) linked to the original order is created to credit the excess to your MultiSafepay balance: {{< br >}} - The order is flagged as `viban-fund-balance`. {{< br >}} - An explanation appears on the **Transaction details** page under **Notes**. |
| Amount too low | Match and make up deficit from your MultiSafepay balance | The order status changes to **Completed**. {{< br >}} A new order linked to the original order is created to debit the deficit from your balance: {{< br >}} - The order is flagged as `viban-charge-balance`. {{< br >}} - An explanation appears on the **Transaction details** page under **Notes**. |
|  | Match and collect deficit | The order status changes to **Completed**. {{< br >}} A new order linked to the original order is created for the outstanding amount. |
| Refund requested | Refund in full | A refund order linked to the original order is created and the payment is refunded. |
| Lump payment | Match the payment to multiple orders | Divide the payment across multiple orders and their status changes to **Completed**. {{< br >}} If there is any excess after all relevant orders are matched, you can refund, reserve, or keep the excess (see above). {{< br >}} If there are not enough funds for all relevant orders, you can make up the deficit from your MultiSafepay balance or create a new order for the outstanding amount (see above).| 

## Activation

Email a request for a VIBAN to <sales@multisafepay.com>

Include in the request:

- Whether you want to use in your dashboard the:
    - Refunds tool
    - Matching tool
- The company name you want to appear on bank statements
- Whether you want to use the VIBAN to:
    - Receive funds only
    - Refund/pay out funds only
    - Receive **and** refund/pay out funds