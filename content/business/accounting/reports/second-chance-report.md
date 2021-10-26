---
title: "Second Chance report"
weight: 6
meta_title: "Reports - Second Chance report - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
read_more: '.'
---

The Second Chance report provides an overview of all transactions:

- By payment method or country
- Declined
- Retried and completed 
- Retried and completed with a different payment method
- Completed with [Second Chance](/features/second-chance/) 

Supported format: Excel

## Report contents

- Report created: the date the report was generated
- Merchant ID: your MultiSafepay account number
- Date from: the start date of the reporting period
- Date till: the end date of the reporting period

{{< details title="By payment method or country" >}}
  
| Column | Description | 
| --- | --- |
| Paymentmethod | The payment method | 
| Country | The country where the transaction took place |
| Completed | The number of completed transactions |
| Declined | The number of declined transactions |
| Retry completed | The number of transactions that were completed after retrying |
| Retry completed diff paymentmethod | The number of transactions completed after retrying with a different payment method |
| Perc completed | The percentage of all transactions that were successfully completed |

{{< /details >}}

{{< details title="Other sections" >}}
  
| Column | Description | 
| --- | --- |
| Created | The time the transaction was created |
| Maintransaction | MultiSafepay's transaction reference number |
| Paymenttype | The payment method |
| Country | The country where the transaction took place |
| Email | The customer's email address | All |
| Merchant ID | Your unique identifier for the order |
| **Declined:** | |
| Reason| Any reason why the transaction was declined |
| **Retried and completed:** ||
| Result | Any additional information about the transaction  |
| **Different payment method:** ||
| Original | The original payment method |
| Retry | The payment method used to retry |
| Result | Any additional information about the transaction  |
| **Completed with Second Chance:** ||
| Amount | The amount paid |
| Totals | The total number of transactions, and total amount paid |

{{< /details >}}

## Requesting reports

To request a Second Chance report, email your account manager at <sales@multisafepay.com>
