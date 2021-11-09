---
title: 'Integration and testing Pay After Delivery'
breadcrumb_title: 'Integration and testing'
weight: 40
meta_title: "Integration and testing Pay After Delivery - MultiSafepay Docs"
short_description: "Integration and testing Pay After Delivery in your ecommerce platform"
layout: 'child'
logo: '/logo/Payment_methods/Pay_After_Delivery.svg'
url: '/payment-methods/pay-after-delivery/integration-testing/'
aliases:
    - /payments/methods/billing-suite/pay-after-delivery/integration-and-testing/
---

## Integration and testing
To process Pay After Delivery payments via our API, see API reference – [Pay After Delivery](/api/#pay-after-delivery).

For the Pay After Delivery logo, see MultiSafepay GitHub – [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons).

{{< details title="View credentials and testing process" >}}

Test credentials: [API key](/account/site-id-api-key-secure-code/)

**Test a Pay After Delivery order**

1. To test a Pay After Delivery order, send a [direct](api/#pay-after-delivery---direct) or [redirect](api/#pay-after-delivery---redirect) API request.
2. If you send a redirect API request, click **Pay After Delivery**.
3. Enter in the:
    - **Birthdate** field any date of birth. Format: DD-MM-YYYY.
    - **Bank account** field any bank account number.
    - **E-mail address** field any email address.
    - **Phone number** field any phone number.
4. Click **Confirm**.
  The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Uncleared**.

**Test declining an order**  

To decline an order, in your test account under **Order summary**, click **Decline**. The transaction and order statuses change to **Void**.

**Test cancelling an order**

To test cancelling an order:

1. Create an order.
2. In your MultiSafepay test account, go to **Order summary**, click **Order status**.
3. From **Change status to**, select **cancelled**, in the **memo** field enter a reason, and then click **Ok**.  
  The transaction status changes to **Void** and the order status changes to **Cancelled**.

---

**Note:** 
You can't test:  
  - Processing refunds
  - Changing the statuses of orders to shipped

{{< /details >}}
