---
title : "Recurring payment errors"
weight: 56
meta_title: "Recurring payments errors - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: '.'
aliases:
    - /tools/recurring-payments/error-response
---
Responses to recurring payment transaction request may contain a 1000 error. Possible reasons for this include:

### MultiSafepay Control settings
MultiSafepay has blocked the transaction due to potential fraud or other settings in your MultiSafepay Control, e.g.:

- Recurring payments are not enabled in your MultiSafepay Control.
- The payment method is disabled or not available. 

To check the settings in your MultiSafepay Control, email the Integration Team at <integration@multisafepay.com>  

### Frequency limit
The same recurring ID or customer data was used within 24 hours.

For more information, see [Activating recurring payments](/tools/recurring-payments/activating-recurring-payments/)
For support, email the Integration Team at <integration@multisafepay.com>

### Fraud
In rare cases, the customer's data may have been picked up by our automatic fraud filter, e.g.:

- The bank account is blocked.
- The credit card is marked as stolen.
- Fraud has occurred at the customer's address. 













