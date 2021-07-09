---
title: 'Activating E-invoicing'
breadcrumb_title: 'Activation'
weight: 20
meta_title: "Activating E-invoicing - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Activating E-invoicing and setting up your collection flow"
layout: 'child'
logo: '/logo/Payment_methods/Klarna.svg'
---


1. Before applying for E-invoicing, check your eligibility with your account manager at <sales@multisafepay.com>

2. Email your application to your account manager at <sales@multisafepay.com>

3. MultiSafepay activates E-invoicing in your MultiSafepay account.

## Setup

To set up E-invoicing in your MultiSafepay account, follow these steps:

{{< details title="1. Create an action" >}}

Create an action in the form of an email, text message, or letter. Multiple actions form a collection flow. 

1. Sign in to your [MultiSafepay account](https://merchant.multisafepay.com).
2. Go to **E-invoicing** > **Action**.
3. Click **Add new template**.
4. Select the relevant delivery option(s): **Email address**, **SMS**, or **Letter**.
5. For each delivery option, provide a description, e.g. "NL 1st invoice".
6. Select a language.
7. The default **From address** is `noreply@multisafepay.com`. When you edit this address, we recommend also adding a DNS record to your domain to avoid your messages being marked as spam. For more information, see your MultiSafepay account.
8. Enter a **From name**.
9. Enter a **Subject line**, e.g. "Invoice from Amazing Socks Ltd."
10. **Plain body** indicates unformatted text. Design your preferred layout.
11. Design and create the **Body HTML**.  
 - [Customize the email template](/payment-methods/billing-suite/e-invoicing/user-guide/customizing-e-invoices/) as required.  
 - For how to use the @@ tokens, see [Email template tokens](/tools/multisafepay-control/email-template-token).
12. Create an action for every step in the collection flow. 

**Example plain body:**

``` shell
Date: @CURRENTDATE@ 
Order number: @DESCRIPTION@

Subject: Your order from @SITENAME@

Dear @FIRSTNAME@ @LASTNAME@,

Thank you for your order at @SITENAME@.

Order details:
@CONTENT@

Please pay the invoice by @DUE_DATE@.

Use the following payment link:
@PAYLINK@ 

Or

For bank transfers, use the following information:
IBAN: @BANKTRANSFERIBAN@
BIC: ​@BANKTRANSFERBIC@
Name: @BANKTRANSFERHOLDER@
Payment reference:​ @BANKTRANSFERID@

The payment reference is important so that we can link your payment to the correct order. 

Kind regards, 
@Your name@ 
Finance

__
For questions about your order, call customer service on 0208500500 or email example@email.nl
```

{{< /details >}}

{{< details title="2. Create a collection flow" >}}

To create a collection flow, follow these steps:

1. in your MultiSafepay account, go to **E-invoicing** > **Workflows**.
2. Click **Create new**.
3. Under **Settings**, select a template. 
4. In the **Description** field, enter a name for the collection flow, e.g. "B2B Netherlands".
5. From the **Drag and drop**, select an action to start creating the flow. Start with the first invoice and build up the payment flow towards the customer. You can design the collection flow as required.
6. If you use a debt collection agency and want to pass invoices to them automatically, enable **Debt collector**.
7. To accept or decline transactions manually, enable **Manual approval before execution**.
8. To add an additional amount on top of the original amount, enable **Increase transaction fee**. Format the amount in cents, e.g. &euro; 1.00 = 100.
9. To add an additional percentage instead of a fixed amount, enable **Increase transaction fee %**.
10. To specify how many days the payment link is valid for, enter a number in the **Days active** field.
11. To set **When** to send the invoice, either:
 - Under **X days after previous step**, set the number of days, **or** 
 - Under **Day of month**, set a specific date (1 to 28 only). This is mostly for repeated invoices.
12. You can also specify:
 - A **Day of the week**
 - An **Execution time** 
14. Click **Save**. 
15. Repeat steps 5 to 14 for every action you add to the collection flow.
16. Click **Save flow**.

{{< /details >}}

{{< details title="3. Activate the collection flow" >}}

To activate your collection flow, follow these steps to link it to a specific website in your MultiSafepay account:

1. in your MultiSafepay account, go to **Settings** > **Website settings**.
2. Click the relevant website to open the **Website settings** page.
3. From the **E-Invoicing workflow** dropdown menu, select your preferred flow.

{{< /details >}}

Once the collection flow is activated, you can start using E-invoicing as a payment method.
