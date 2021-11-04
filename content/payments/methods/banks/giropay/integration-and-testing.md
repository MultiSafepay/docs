---
title: "Integration and testing"
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "Giropay - Integration and testing - MultiSafepay Docs"
short_description: "Integrating and testing Giropay in your ecommerce platform"
layout: 'child'
logo: '/logo/Payment_methods/Giropay.svg'
url: '/payment-methods/giropay/integration-testing/'
aliases:
    - /payment-methods/giropay/giropay-testing
    - /payments/methods/banks/giropay/integration-and-testing/
---

To process Giropay payments via our API, see API reference – [Giropay](/api/#giropay).

For the Giropay logo, see MultiSafepay GitHub – [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons).

{{< details title="View credentials and testing process" >}}

Test credentials:

- [API key](/account/site-id-api-key-secure-code/)

**Test a Giropay order**

1. To test a Giropay order, send a [redirect](/api/#giropay) API request.
2. On the Giropay page, in the **BIC** field, enter any BIC code. For example, `NOLADE22XXX`.
3. Click **Confirm**.
4. On the Test platform page, from the **Test scenario** list, select **Completed**, and then click **Test**.
5. The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Completed**.

**Test cancelling an order**

To test cancelling an order:

1. Send a [redirect](/api/#eps) API request.
2. On the Giropay page, in the **BIC** field, enter any BIC code. For example, `NOLADE22XXX`.
3. Click **Confirm**.
4. On the Test platform page, from the **Test scenario** list, select **Cancelled**, and then click **Test**.  
  The transaction status changes to **Void**.

**Test refunding an order**

To test refunding an order:

1. Create an order.
2. In your MultiSafepay test account, go to **Order summary**, and then click **Refund order**.
3. Under **Refund**, in the **Account holder name** field, enter the account holder name of the account you want to refund to. 
4. In the **IBAN** field, enter the IBAN of the account you want to refund to.
5. In the **Reason/Description** field, enter a reason for the refund. 
6. In the **Amount** field, enter the amount to refund, and then click **Continue**.
7. Under **Refund confirmation**, check that the description and amount are correct, and then click **Confirm**.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
8. Under **Related transactions**, select the **ID** of the refund order.
9. Under **Order summary**, click **Accept**.
10. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

**Test refunding an order with an API request**

To test refunding an order with an API request:

1. Create an order. 
2. Send a [refund](/api/#refund-an-order) API request.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
3. In your MultiSafepay test account, go to **Related transactions**, and then select the **ID** of the refund order.
4. Under **Order summary**, click **Accept**.
5. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

---

**Note:** 

- In the live environment you can't accept a refund order. This is done automatically.
{{< /details >}}