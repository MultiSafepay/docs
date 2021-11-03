---
title: "Integration and testing"
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "V Pay - Integration and testing - MultiSafepay Docs"
short_description: "Integrating and testing V Pay in your ecommerce platform"
layout: 'child'
---

V Pay payments are processed as credit card payments by Visa.

To process V Pay payments via our API, see API reference – [Credit cards](/api/#credit-cards).

**Note:** With our [ready-made integrations](/ecommerce-platforms/), you can also integrate V Pay using the [generic Visa gateway](/developer/general/generic-gateways/).

For the V Pay logo, see MultiSafepay GitHub – [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons).

{{< details title="Credentials and testing process" >}}

Test credentials:

- [API key](/account/site-id-api-key-secure-code/)

**Test a V-Pay order**  

1. Send a [redirect](/api/#visa) API request.
3. In the **Card number** field, enter `4111111111111111`.
4. In the **Card holder** field, enter any name.
5. From the **Expiry date** lists, select any future date.
6. In the **CVC/CVV** field, enter `123`, and then click **Confirm**.
7. On the 3D payment page, from the drop-down list, select **Authenticated (Y)**, and then click **Confirm**.
5. The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Completed**.

Use the following card numbers to test different transaction statuses.

| Card number         | Status    | Description              |
| ------------------- | --------- | ------------------------ |
| 4111111111111111 | **Completed** | Transaction was completed (3D enrolled) |
| 4012001038443335 | **Completed** | Transaction was completed (not 3D enrolled) |
| 4917300000000008 | **Uncleared** | Transaction is uncleared. After 3 minutes, this changes to Void. |
| 4462000000000003 | **Uncleared** | Transaction is uncleared. After 3 minutes, this changes to **Completed**. |
| 4012001037461114 | **Declined**  | Transaction was declined (3D authentication failed) |
| 4012001038488884 | **Declined**  | Transaction was declined (3D authentication was successful, but insufficient funds) |

---

**Note:** The reason a transaction is declined can be seen in your MultiSafepay test account under **Notes**.

---

**Test refunding an order**

To test refunding an order:

1. Create an order using card number: `4012001038443335`. 
2. In your MultiSafepay test account, go to **Order summary**, and then click **Refund order**.
3. Under **Refund**, in the **Reason/Description** field, enter a reason for the refund. 
4. In the **Amount** field, enter the amount to refund, and then click **Continue**.
5. Under **Refund confirmation**, check that the description and amount are correct, and then click **Confirm**.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
6. Under **Related transactions**, select the **ID** of the refund order.
7. Under **Order summary**, click **Accept**.
8. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

**Test refunding an order with an API request**

To test refunding an order with an API request:

1. Create an order using card number: `4012001038443335`. 
2. Send a [refund](/api/#refund-an-order) API request.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
3. In your MultiSafepay test account, go to **Related transactions**, and then select the **ID** of the refund order.
4. Under **Order summary**, click **Accept**.
5. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.
---

**Note:**

- You can't test cancelling an order. 
- In the live environment you can't accept a refund order. This is done automatically.

{{< /details >}}