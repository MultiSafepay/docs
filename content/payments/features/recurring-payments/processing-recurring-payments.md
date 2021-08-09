---
title : "Processing recurring payments"
weight: 52
meta_title: "Processing recurring payments - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: '.'
aliases:
    - /tools/recurring-payments/recurring-payments-how-does-it-work/
---
To process recurring payments, follow these steps:

**Step 1:** Ensure the payment gateway is configured for the payment method:

- SEPA Direct Debit: `DIRDEB`
- Credit cards: `VISA`, `MASTERCARD`, or `AMEX`

**Step 2:** The customer initiates the first payment using their selected payment method:

- SEPA Direct Debit: iDEAL, SOFORT Banking
- Credit cards: Visa, Mastercard, American Express

**Step 3:** When the payment is complete, make a `GET /orders` request to [retrieve the transaction details](/api/#retrieve-an-order).

```
GET - /orders/{order_id}

  "success": true,
  "data": {
    "transaction_id": "",
```

**Step 4:** If the transaction is declined, the reason is included in the response, e.g. insufficient funds. MultiSafepay does not provide automated retries. Contact the customer, or wait and then try to charge the customer again.

**Step 5:** If the transaction was successful, the response contains a `recurring_id`. 

```
"payment_details": {
  "recurring_id": "",
```

**Step 6:** To process each [recurring payment](/api/#recurring-payment), make a `POST /orders` request including the `recurring_id` in the `gateway` information.

- You must provide the payment gateway, customer's details, transaction amount, and order description. 
- You do **not** need to provide the customer's bank account number or credit card details again. Recurring payments are processed using the same payment details as the initial transaction. 
- Request type: `Direct`

```
POST - /orders

  "type": "direct", 
  "order_id": "XXXX", 
  "recurring_id": "XXXX" 
```

**Note:** MultiSafepay automatically uses the `Site Description` and `Order ID` to identify the transaction on the customer's bank statement.
