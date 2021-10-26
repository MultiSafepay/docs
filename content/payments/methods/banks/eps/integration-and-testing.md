---
title: "Integration and testing"
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "EPS - Integration and testing - MultiSafepay Docs"
short_description: "Integrating and testing EPS in your ecommerce platform"
layout: 'child'
logo: '/logo/Payment_methods/eps.svg'
url: '/payment-methods/eps/integration-testing/'
aliases:
    - /payment-methods/eps/eps-testing
    - /payments/methods/banks/eps/integration-and-testing/
---

To process EPS payments via our API, see API reference – [EPS](/api/#eps).

For the EPS logo, see MultiSafepay GitHub – [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons).

{{< details title="View credentials and testing process" >}}

You can test EPS using the Giropay gateway in your MultiSafepay test account. 

In your live MultiSafepay account, EPS only appears if you provide the country code for Austria `AT`.

Test credentials: You will need a test BIC.

Sample statuses:

| Status    | Description              |
| --------- | ------------------------ |
| **Completed** | Transaction was completed |
| **Declined**  | Transaction was declined |

{{< /details >}}