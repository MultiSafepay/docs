---
title: 'Email styling'
category: 627bbcf80c1c9c0050320b60
order: 4
hidden: false
parentDoc: 62b0845857c8ab006af6a4f7
slug: 'email-styling'
---

You can style emails to customers, payment pages, and success pages to match your brand's look and feel.

# Emails to customers

Use our pre-formatted and/or pre-written templates and populate them with your content.

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>. 
2. Go to **Settings** > **Email styling**, and then click the relevant website.  
3. On the **Email templates** page, click **Add new**.   
5. From the **Type** list, select the template type.  

    <details id="template-types">
    <summary>Template types</summary>
    <br>

    **Bank transfer details email (to customer)**  
    For sending customers MultiSafepay's bank details for <<glossary:redirect>> [bank 
    transfers](/docs/bank-transfer/). 

    **Chargeback email (to merchant)**  
    For notifying you when a customer requests a [chargeback](/docs/chargebacks/).

    Make sure you add an email addresses for us to send these emails to in your dashboard, under 
    **Account information** > **Chargebacks email**. 

    **Manual capture completed (to customer)**  
    For notifying customers that you have manually captured reserved funds for an [uncleared transaction](/docs/uncleared/). 

    **Manual capture completed (to merchant)**  
    For confirming that you have manually captured reserved funds for an [uncleared transaction](/docs/uncleared/).  

    **Partial and/or full capture completed (to customer)**  
    For notifying customers that you have partially or fully captured reserved funds for an [uncleared transaction](/docs/uncleared/). 

    **Partial and/or full capture completed (to merchant)**  
    For confirming that you have partially or fully captured reserved funds for an [uncleared transaction](/docs/uncleared/).

    **Refund complete email (to customer)**  
    For notifying customers that you have processed their refund. 

    **Second Chance email (to customer)**  
    For sending customers a friendly reminder to complete a payment. 

    Make sure you have enabled [Second Chance](/docs/second-chance/) in your MultiSafepay dashboard.

    **Transaction completed email (to customer)**  
    For sending payment confirmation to customers. 

    **Transaction completed email (to merchant)**  
    For notifying you that a customer has successfully completed a payment.

    ---

    </details>

6. From the **Language** list, select the email language.  

    <details id="supported-languages">
    <summary>Supported languages</summary>
    <br>

    - Dutch
    - English
    - French
    - German
    - Italian
    - Spanish

    ---

    </details>

    **⚠️ Note:** The language you set here is overridden by the `customer.locale` parameter in [create order](/reference/createorder/) requests. 

    <details id="locale-example">
    <summary>Locale example</summary>
    <br>

    ```json
    {
    "customer": {
        "first_name": "John",
        "last_name": "Doe",
        "house_number": "39",
        "address1": "Kraanspoor",
        "address2": "",
        "city": "Amsterdam",
        "zip_code": "1033 SC",
        "state": "Noord-Holland",
        "country": "NL",
        "locale": "nl_NL", // Set the language and country code
        "phone": "0208500500",
        "email": "example@multisafepay.com",
        "gender": "M",
        "birthday": "1980-12-31",
        "user_agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
        "referrer": "http://test.com",
        "ip_address": "123.123.123.123",
        "forwarded_ip": "",
        "reference": ""
    }
    }
    ```

    </details>

    <details id="locale-codes">
    <summary>Locale codes per language and country</summary>
    <br>

    | Code | Language & country |
    |---|---|
    | `cs_CZ` | Czech |
    | `de_AT` | German (Austria) |
    | `de_DE` | German (Germany) |
    | `en_US` | American English |
    | `fi_FI` | Finnish |
    | `fr_BE` | French (Belgium) |
    | `fr_FR` | French (France) |
    | `it_IT` | Italian |
    | `nl_BE` | Dutch (Belgium) |
    | `nl_NL` | Dutch (Netherlands) |
    | `pl_PL` | Polish |
    | `es_ES` | Spanish |
    | `sv_SE` | Swedish |
    | `zh_CN` | Chinese |

    </details>

7. Either click **Load default template**, or fill in the fields as required.

    <details id="from-address-field">
    <summary>From address field</summary>
    <br>

    In the **From address** field, enter the email address you want the email sent from, e.g. sales@yourcompany.com.
    
    **⚠️ Note:** If you enter a from address other than noreply@multisafepay.com, to avoid emails being marked as spam, we recommend adding the following DNS record to your domain: 

    ```
    v=spf1 ip4:213.189.0.0/23 ip4:185.99.128.0/22 mx
    ```

    ---

    </details>
        
    <details id="from-name-field">
    <summary>From name field</summary>
    <br>
    
    In the **From name** field, enter the name you want the email sent by, e.g. your company name.

    ---

    </details>

    <details id="subject-field">
    <summary>Subject field</summary>
    <br>
    
    In the **Subject** field, enter a subject.  

    ---

    </details>

8. Edit the text **either** in the **Body plain** field, **or** if you know HTML and CSS, you can fully customize the content and layout in the **Body HTML** field. To view the HTML/CSS code, click **Source**.

    <details id="how-to-add-links">
    <summary>How to add links</summary>
    <br>

    1. Click the **Link** icon.
    2. Select the link type: **URL**, **Anchor link**, or **Mailto link**.
    3. Fill in the additional fields as required, and then click **OK**. 
    
    ---

    </details>

    <details id="how-to-use-tokens">
    <summary>How to use tokens</summary>
    <br>

    To save time, you can use @tokens@ to auto-fill personalized details in emails.

    1. In the **Body HTML editor**, click the **Token** icon.
    2. Select a token from the list, and then click **OK**.
    <br>

    The table below describes all available tokens.

    | Token | Output |      
    |---|---| 
    | ACCOUNT                       | The `account_id` of a FastCheckout customer |   
    | ACCOUNTADDRESS                | The customer's address and street name   |  
    | ACCOUNTADDRESSAPARTMENT       | The customer's house number |
    | ACCOUNTCITY                   | The customer's city of residence |
    | ACCOUNTCOUNTRY                | The customer's country of residence |
    | ACCOUNT EMAIL                 | The customer's email address |
    | ACCOUNTFIRSTNAME              | The customer's first name |
    | ACCOUNTLASTNAME               | The customer's last name |
    | ACCOUNTNR                     | Your MultiSafepay account ID |
    | ACCOUNTZIPCODE                | The customer's ZIP code |
    | ADDRESS1                      | Your company address line 1 |
    | ADDRESS2                      | Your company address line 2 |
    | ADDRESS3                      | Your company address line 3 |
    | BANKHOLDERNAME                | The account holder name for a bank transfer |
    | BANKIBAN                      | The IBAN for a bank transfer |
    | BANKPAYMENTID                 | The payment reference for a bank transfer |
    | BANKTRANSFERBIC               | The BIC for a bank transfer |
    | BANKTRANSFERHOLDER            | The account holder name receiving a bank transfer |
    | BANKTRANSFERID                | The reference for a bank transfer |
    | BIRTHYDAY                     | The customer's date of birth |
    | CITY                          | Your company city of residence |
    | COMPANYNAME                   | Your company name given in your MultiSafepay account |
    | CONTENT                       | The items in the shopping cart |
    | COUNTRY                       | The <a href="https://www.iso.org/iso-3166-country-codes.html" target="_blank">ISO 3166</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> code for your company country |
    | COUNTRYCODE                   | The <a href="https://www.iso.org/iso-3166-country-codes.html" target="_blank">ISO 3166</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> code for your company country |
    | CURRENTDATE                   | Today's date |
    | DELIVERYINVOICEURL            | The invoice URL for delivery |
    | DELIVERYREASON                | The reason for delivery |
    | DELIVERYCARRIER               | The carrier used for delivery |
    | DELIVERYTRACKINGURL           | The track and trace URL for delivery |
    | DELIVERYTRACKINGCODE          | The track and trace code for delivery |
    | DELIVERYSHIPDATE              | The shipping date for delivery |
    | DESCRIPTION                   | The account ID to receive money |
    | DESTAMOUNT                    | The amount to be received |
    | DESTAMOUNTFORMATCUR           | The amount (and currency to be paid by the customer via bank transfer transactions |
    | DESTCURRENCY                  | The currency of the amount to be received |
    | DESTFORMATAMOUNTCUR           | The currency and amount to be paid out |
    | EMAIL                         | The customer's email address |
    | FINANCIAL EMAIL               | Your invoices email address |
    | FIRSTNAME                     | The customer's first name and email address set as sender for emails |
    | FROMNAME                      | The name of the sender's email account |
    | GENDER                        | The customer's gender |
    | LASTNAME                      | The customer's last name |
    | MERCHANTCITY                  | Your company city of residence |
    | MERCHANTCOUNTRY               | Your company country of residence  |
    | MERCHANTLOGOHTML              | The HTML code for your logo |
    | MERCHANTNAME                  | Your company's full name |
    | MERCHANTPHONESUPPORT          | Your customer service phone number |
    | MERCHANTPO                    | Your customer tracking number |
    | MERCHANTSUPPORT EMAIL         | Your customer service email address |
    | MERCHANTTRANSACTIONID         | Your transaction reference number |
    | ORDERSTATUS                   | The <<glossary:order status>> |
    | PAYLINK                       | The [payment link](/docs/payment-links/) |
    | PAYMENTMETHOD                 | The payment method  |
    | PHONE                         | Your company phone number  |
    | REFUNDDESTINATION             | The bank account number to receive a refund |
    | REPORT EMAIL                  | Your reports email address |
    | SITENAME                      | The website name |
    | SITEURL                       | The website URL |
    | STATE                         | The province or state |
    | STATUS                        | The <<glossary:transaction status>> |
    | SUBJECT                       | The email subject line |
    | TOTALAMOUNT                   | The total amount of the order |
    | TRANSACTIONID                 | The MultiSafepay transaction ID  |
    | TRANSCOMP EMAIL               | Your email address for completed transactions |
    | VARA                          | Var1 from your create order request |
    | VARB                          | Var2 from your create order request |
    | VARC                          | Var3 from your create order request |
    | VATNUMBER                     | Your company VAT number  |
    | ZIPCODE                       | Your company ZIP code |

    ---

    </details>
    <details id="how-to-add-your-logo">
    <summary>How to add your logo</summary>
    <br>

    To add your logo to emails to increase customers' recognition and trust, follow these steps:

    1. Sign in to your <a href="https://merchant.multisafepay.com/" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
    2. Go to **Settings** > **Files**.
    3. Under **Upload a new file**, select the relevant file, and then click **Choose file**. 
    4. Under **Upload queue**, click **Upload** or **Upload all**.
       The file appears under **File directory**.
    5. Go to **Settings** > **Email styling**, and then click the relevant website.
    6. At the end of the row of the relevant email, click the orange pen icon to edit the template.
    7. Click the **Image** icon in the first row of the editor.
    8. In the **Image properties** dialog, under **URL**, click **Browse server**.
    9. On the row of the relevant file, click the green **Use image** icon.
    10. In the **Image properties** dialog, edit the image's parameters as required: height, border, horizontal space, vertical space, and alignment.
    11. Click **OK**, and then click **Save**.
    
    ---

    </details>

    <details id="how-to-add-an-inline-frame">
    <summary>How to add an inline frame</summary>
    <br>

    Inline frames (Iframes) are HTML documents embedded inside another HTML document, which you can use to insert content from another source into the email template. 

    1. Go to the Body HTML editor on the email template page, and then click the **Iframe** icon. 
    2. In the **Iframe window**, enter the URL of the Iframe.
    3. Edit other parameters as required: width, height, alignment, name, and title.
    4. Click **OK**. 

    ---

    </details>

9.  Click **Save**.

<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)
