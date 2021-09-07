---
title : "Recurring Payments errors"
weight: 56
meta_title: "Recurring Payments errors - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: '.'
aliases:
    - /tools/recurring-payments/error-response
---
Responses to Recurring Payments requests may contain a 1000 error. Possible reasons for this include:

### MultiSafepay account settings
MultiSafepay has blocked the transaction due to potential fraud or other settings in your MultiSafepay account, e.g.:

- Recurring Payments is not enabled in your MultiSafepay account.
- The selected payment method is disabled or not available. 

To check the settings in your MultiSafepay account, email the Integration Team at <integration@multisafepay.com>  

### Frequency limit
The same `recurring_id` or customer data was used within 24 hours.

For more information, see [Activating Recurring Payments](/tools/recurring-payments/activating-recurring-payments/)

For support, email the Integration Team at <integration@multisafepay.com>

### Fraud
In rare cases, the customer's data may have been picked up by our automatic fraud filter, e.g.:

- The bank account is blocked.
- The credit card is marked as stolen.
- Fraud has occurred at the customer's address. 













