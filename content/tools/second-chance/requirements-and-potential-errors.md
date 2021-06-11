---
title: "Second Chance requirements and potential errors"
weight: 61
meta_title: "Requirements and potential errors - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: '.'
aliases:
    - /tools/second-chance/how-does-it-work
---

## Requirements

### Customer email address

Second Chance emails can only be sent if the customer's email address is included in the transaction request.

### Transaction status         

Second Chance emails cannot be activated or sent to the customer while the status of the original transaction is **Uncleared**, or once it is **Completed**.

### Payment methods     

Second Chance emails can't be sent for the following payments methods because they follow a different payment flow:

- [Klarna](/payment-methods/billing-suite/klarna)
- [AfterPay](/payment-methods/billing-suite/afterpay)
- [Betaal per Maand](/payment-methods/billing-suite/betaalpermaand)
- [Pay After Delivery](/payment-methods/billing-suite/pay-after-delivery)
- [Bank transfer](/payment-methods/banks/bank-transfer)
- [Direct Debit](/payment-methods/banks/sepa-direct-debit)

### Customer consent

Under the [GDPR](/faq/gdpr/), you must obtain documented consent from the customer to send Second Chance emails. 

### Valid payment link
Payment links in Second Chance emails have the same lifetime as the original payment link, which is set to 30 days by default. 

For more information, see [Adjusting payment link lifetimes](/faq/api/lifetime-of-a-payment-link).

## Potential errors

### External plugins 
Second Chance emails can create conflicts with external warehouse systems. In some cases, this can be resolved using a [cron job](/faq/general/multisafepay-glossary/#cron). However, this is not always a stable solution. 

For example, when a customer cancels an order in the webshop, they can still pay for it using Second Chance within 30 days or a specified time frame. For more information, see [Adjusting payment link lifetimes](/faq/api/adjusting-payment-link-lifetimes/). 

If a cancelled order is subsequently paid for, MultiSafepay reopens the order in the webshop. A warehouse system may have already released the reservation on the order when it received **Cancelled** status, or may consider the **Cancelled** status permanent. As result, the items the customer ordered may no longer be available or in stock. 

### ERP systems
Second Chance emails can cause issues when running an enterprise resource planning (ERP) system. 

