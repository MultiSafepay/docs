---
title: "Integration and testing"
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "ING Home Pay - Integration and testing - MultiSafepay Docs"
short_description: "Integrating and testing ING Home Pay in your ecommerce platform"
layout: 'child'
logo: '/logo/Payment_methods/ING_Homepay.svg'
url: '/payment-methods/ing-home-pay/integration-testing/'
aliases:
    - /payment-methods/ing-home-pay/ing-home-pay-testing
    - /payments/methods/banks/ing-home-pay/integration-and-testing/
---

To integrate ING Home'Pay using our API, see API reference - [ING Home'Pay](/api/#ing-home-pay).

For the ING Home'Pay logo, see MultiSafepay GitHub – [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons).

{{< details title="View credentials and testing process" >}}

Test credentials: [API key](/account/site-id-api-key-secure-code/)

**Test an ING Home'Pay order**

1. To test an ING Home'Pay order, send a [direct](/api/#ing-homepay---direct) or [redirect](/api/#ing-homepay---redirect) API request.
2. On the Test platform page, from the **Test scenario** list, select **Completed**, and then click **Test**.  
  The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Completed**.

**Test declining an order**

To test declining an order:

1. Send a [direct](/api/#ing-homepay---direct) or [redirect](/api/#ing-homepay---redirect) API request.
2. On the Test platform page, from the **Test scenario** list, select **Cancelled**, and then click **Test**.  
  The transaction status changes to **Declined**.

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

- You can't test:
  - Cancelling orders
  - Refunding via the API
- In the live environment, you can't accept refund orders. These are done automatically.
{{< /details >}}