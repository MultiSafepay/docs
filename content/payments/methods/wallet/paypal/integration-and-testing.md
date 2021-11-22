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

{{< details title="View credentials and testing process" >}}

Test credentials: [API key](/tools/multisafepay-control/get-your-api-key/)

**Test a PayPal order**

1. Send a [direct](/api/#paypal---direct) API request.
2. On the Test platform page, from the **Test scenario** list, select **Completed**.
3. Click **Test**.  
The payment is processed in your MultiSafepay test account as **Successful**, with order status **Completed**, and transaction status **Initialized**.

---

**Note**: Since MultiSafepay does not collect payments on behalf of PayPal, the transaction status remains **Initialized** and can't be changed to **Completed**.

---

**Change the order status**

You can change the order status to:

| Status    | Description              | Test scenario     |
| --------- | ------------------------ | ----------------- |
| **Completed** | Order was completed | Completed  |
| **Void** | Order was cancelled | Cancelled  |
| **Initialized**/ **Completed** | Payment blocked by PayPal, then accepted after 2 minutes | Initialized completed |

To change the order status, on the Test platform page, from the **Test scenario** list, select the relevant test scenario.

**Test refunding an order**

To refund an order:

1. Create an order. 
2. In your MultiSafepay test account, go to **Order summary**, and then click **Refund order**.
3. Under **Refund**, enter in the:
    - **Reason/Description** field the reason for the refund. 
    - **Amount** field the amount to refund.
4. Click **Continue**.
5. Under **Refund confirmation**, check that the description and amount are correct, and then click **Confirm**.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
6. Under **Related transactions**, select the **ID** of the refund order.
7. Under **Order summary**, click **Accept**.
8. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

Alternatively, send a [Refund](/api/#refund-an-order) API request.

---

**Note**:  

- You can't test sending redirect API requests.
- In the live environment, you can't accept refund orders. These are done automatically.

{{< /details >}}
