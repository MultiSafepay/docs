---
title: "Integration and testing"
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "PayPal - Integration and testing - MultiSafepay Docs"
short_description: "Integrating and testing PayPal in your ecommerce platform"
layout: 'child'
url: '/payment-methods/paypal/integration-testing/'
aliases:
    - /payment-methods/wallet/paypal/paypal-testing
    - /payments/methods/wallet/paypal/integration-and-testing/
---

To process PayPal payments via our API, see API reference – [PayPal](/api/#paypal).

For the PayPal logo, see MultiSafepay GitHub – [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons).

{{< details title="Credentials and testing process" >}}

Test credentials: [API key](/tools/multisafepay-control/get-your-api-key/)

**Test a PayPal order**

1. Send a [Direct](/api/#paypal---direct) API request.
2. On the Test Platform page, in the **Test Scenario** list, select **Completed**, and then click **Test**.
2. The payment is processed in your MultiSafepay test account as **Successful**, with order status **Completed**, and transaction status **Initialized**.

---

**Note**: Since MultiSafepay does not collect payments on behalf of PayPal, the transaction status remains **Initialized** and can't be changed to **Completed**.

---

**Change the order status**

You can change the order status to:

| Status    | Description              |
| --------- | ------------------------ |
| **Completed** | Order was completed |
| **Declined** | Order was declined |
| **Initialized**/ **Completed** | Payment blocked by PayPal, then accepted |
| **Initialized**/ **Declined** | Payment blocked by PayPal, then declined |
| **Cancelled** | Order was cancelled |

To change the order status, on the Test Platform page, in the **Test Scenario** list, select the desired order status.

**Test refunding an order**

To refund an order:

1. In your test account, under **Order summary**, click **Refund order**.
2. Under **Refund**, in the **Reason/Description** field, enter a reason for the refund. In the **Amount** field, enter the amount to refund, and then click **Continue**.
3. Under **Refund confirmation**, check the description and amount are correct, and then click **Confirm**.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
4. Under **Related transactions**, select the **ID** of the refund order.
5. Under **Order summary**, click **Accept**.
6. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

Alternatively, send a [Refund](/api/#refund-an-order) API request.

---

**Note**: You can't test sending a redirect API request.

{{< /details >}}
