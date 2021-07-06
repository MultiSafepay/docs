---
title: 'Integration and testing in3'
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "Integration and testing in3 - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Integration and testing in3 in your ecommerce platform"
layout: 'child'
logo: '/svgs/in3.svg'
---

To integrate in3 using our API, see API Reference – [in3](/api/#in3).

For the in3 logo, see MultiSafepay GitHub – [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons).

{{< details title="View credentials and testing process" >}}

Test credentials: [API key](.com/tools/multisafepay-control/get-your-api-key/)

To test in3 transactions, follow these steps:

1. Send a [Direct or redirect](/faq/api/difference-between-direct-and-redirect/) API request.
2. The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Uncleared**.
3. To change the order status to **Shipped**, either:
    - Send an [Update an order](/api/#update-an-order) API request, or 
    - Change the status in your MultiSafepay Test Control.
{{< br >}}The transaction status remains **Uncleared**.
4. No invoice is generated in the test control so you can't change the transaction (financial) status to **Completed**. Alternatively, in your live MultiSafepay Control, you can initiate the invoice process by changing the order status to **Shipped**, because the order is captured in in3.

You can also test in3 transactions by entering the following details on the in3 checkout page:
| Date of birth    | Postal code | House number |
| ------------------- | ------------------- | ----------------- |
| 01-01-1999 | 1234AB | 1 |
| 01-01-2000 | 1111AB | 1 |

Sample statuses:

- **Approved**
- **Declined**

{{< /details >}}
