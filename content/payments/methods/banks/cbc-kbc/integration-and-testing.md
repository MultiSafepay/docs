---
title: "Integrating and testing CBC/KBC"
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "CBC/KBC - Integration and testing - MultiSafepay Docs"
short_description: "Integrating and testing in your ecommerce platform"
layout: 'child'
logo: '/logo/Payment_methods/cbc.svg'
url: '/payment-methods/cbc-kbc/integration-testing/'
aliases:
    - /payment-methods/cbc/cbc-testing
    - /payments/methods/banks/kbc/integration-and-testing/
    - /payments/methods/banks/cbc-kbc/integrating-testing
---

To process CBC/KBC payments via our API, see API reference – [CBC/KBC](/api/#cbckbc).

For the CBC and KBC logos, see MultiSafepay GitHub – [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons).

{{< details title="View credentials and testing process" >}}

Test credentials: [API key](/account/site-id-api-key-secure-code/)

**Test a CBC/KBC order**

1. To test a CBC/KBC order, make a [direct](/api/#cbckbc---direct) or [redirect](/api/#cbckbc---redirect) API request.
2. On the Test platform page, from the **Test scenario** list, select **Completed**.
3. Click **Test**.  
  The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Completed**.

**Test cancelling an order**

To test cancelling an order:

1. Make a [direct](/api/#cbckbc---direct) or [redirect](/api/#cbckbc---redirect) API request.
2. On the Test platform page, from the **Test scenario** list, select **Cancelled**.
3. Click **Test**.  
  The order status changes to **Void**.

**Test refunding an order**

To test refunding an order:

1. Create an order. 
2. In your MultiSafepay test account, go to **Order summary**, and then click **Refund order**.
3. Under **Refund**, enter in the:
    - **Account holder name** field the account holder name of the account you want to refund to. 
    - **IBAN** field the IBAN of the account you want to refund to.
    - **Reason/Description** field the reason for the refund. 
    - **Amount** field the amount to refund.
4. Click **Continue**.
5. Under **Refund confirmation**, check that the description and amount are correct, and then click **Confirm**.
  {{< br >}} A new order is created for the refund. The order status for the refund changes to **Reserved**.
6. Under **Related transactions**, select the **ID** of the refund order.
7. Under **Order summary**, click **Accept**.
8. In the **Add transaction comment** field, add a comment, and then click **Add**.
  The order status changes to **Completed**.

---

**Note:** 

- You can't test refunding via the API.
- In the live environment, you can't accept refund orders. These are done automatically.

{{< /details >}}