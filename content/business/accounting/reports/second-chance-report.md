---
title: "Second Chance report"
weight: 6
meta_title: "Reports - Second chance report - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
read_more: '.'
---

The Second Chance report provides an overview of:

- All transactions by payment type
- All transactions by country
- All declined transactions
- All transactions that were retried and completed
- All transactions that were retried and completed with a different payment method
- All paid transactions that were a result of [Second Chance](/features/second-chance/)

Supported formats: Excel or PDF

{{< details title="Report contents" >}}

- Report created: the date the report was generated
- Merchant ID: your MultiSafepay account number
- Date from: the start date of the reporting period
- Date till: the end date of the reporting period

By payment type:  

- Paymentmethod: the payment method
- Completed: the number of completed transactions
- Declined: the number of declined transactions
- Retry completed: the number of transactions that were completed after retry
- Retry completed diff paymentmethod: the number of transactions that were completed after retrying with a different payment method
- Perc completed: the percentage of all transactions that were successfully completed

By country:  

- Country: the country where the transaction took place
- Completed: the number of completed transactions
- Declined: the number of declined transactions
- Retry completed: the number of transactions that were completed after retry
- Retry completed diff paymentmethod: the number of transactions that were completed after retrying with a different payment method
- Perc completed: the percentage of all transactions that were successfully completed

Declined:  

- Created: the time the transaction was created
- Maintransaction: MultiSafepay's transaction reference number
- Paymenttype: the payment method
- Country: the country where the transaction took place
- Email: your customer email address
- Merchant id: your unique identifier for the order
- Reason: the reason why the transaction was declined, if applicable

Completed retry:  

- Created: the time the transaction was created
- Maintransaction: MultiSafepay's transaction reference number
- Paymenttype: the payment method
- Country: the country where the transaction took place
- Email: your customer email address
- Merchant id: your unique identifier for the order
- Result: additional information about the transaction, if applicable

Completed diff method:  

- Created: the time the transaction was created
- Maintransaction: MultiSafepay's transaction reference number
- Paymenttype: the payment method
- Country: the country where the transaction took place
- Email: your customer email address
- Merchant id: your unique identifier for the order
- Original: the original payment method
- Retry: the payment method used to retry
- Result: additional information about the transaction, if applicable

Second chance orders:  

- Created: the time the transaction was created
- Maintransaction: MultiSafepay's transaction reference number
- Amount: the amount paid
- Paymenttype: the payment method
- Country: the country where the transaction took place
- Email: your customer email address
- Merchant id: your unique identifier for the order
- Totals: the total number of transactions, and total amount paid

{{< /details >}}

## Generating a Second Chance report

To request a second chance report, email your account manager at <sales@multisafepay.com>

## See also

- [Second Chance](/features/second-chance/)