---
title : " Using email template tokens"
weight: 8
meta_title: "MultiSafepay Control - Using email template tokens - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: '.'
aliases:
    - /tools/multisafepay-control/email-template-token
---

In MultiSafepay email templates, you can use the following tokens between @@:

| Tags                          |     Result    |      
| ----------------------------- | ------------- | ------
| ACCOUNT                       | Account_id of FastCheckout customer |   
| ACCOUNTADDRESS                | Customer address and street name   |  
| ACCOUNTADDRESSAPARTMENT       | Customer house number |
| ACCOUNTCITY                   | Customer city of residence |
| ACCOUNTCOUNTRY                | Customer country of residence |
| ACCOUNT EMAIL                 | Customer email address |
| ACCOUNTFIRSTNAME              | Customer first name |
| ACCOUNTLASTNAME               | Customer last name |
| ACCOUNTNR                     | Your MultiSafepay AccountID |
| ACCOUNTZIPCODE                | Customer zip code |
| ADDRESS1                      | Your company address line 1 |
| ADDRESS2                      | Your company address line 2 |
| ADDRESS3                      | Your company address line 3 |
| BANKHOLDERNAME                | Account holder used by the customer to process bank transfer transactions |
| BANKIBAN                      | IBAN used by the customer to process bank transfer transactions |
| BANKPAYMENTID                 | Reference used by the customer to process bank transfer transactions |
| BANKTRANSFERBIC               | BIC used by the customer to process bank transfer transactions |
| BANKTRANSFERHOLDER            | Account holder name of IBAN to receive the money |
| BANKTRANSFERID                | Reference used with the bank transfer |
| BIRTHYDAY                     | Customer date of birth |
| CITY                          | Your company city of residence |
| COMPANYNAME                   | Your company name given in your MultiSafepay Control |
| CONTENT                       | Shopping cart info |
| COUNTRY                       | [ISO 3166](https://www.iso.org/iso-3166-country-codes.html) code for your company country |
| COUNTRYCODE                   | [ISO 3166](https://www.iso.org/iso-3166-country-codes.html) code for your company country |
| CURRENTDATE                   | Today's date |
| DESCRIPTION                   | AccountID to receive money |
| DESTAMOUNT                    | Amount to be received |
| DESTAMOUNTFORMATCUR           | Amount including currency to be paid by the customer via bank transfer transactions |
| DESTCURRENCY                  | Currency of amount to be received |
| DESTFORMATAMOUNTCUR           | Currency and amount to be paid out |
| EMAIL                         | Customer email address |
| FINANCIAL EMAIL               | Email address for financial email |
| FIRSTNAME                     | Customer first name and email address set as sender for emails |
| FROMNAME                      | Name of the sender's email account |
| GENDER                        | Customer gender |
| LASTNAME                      | Customer last name |
| MERCHANTCITY                  | Your company city of residence |
| MERCHANTCOUNTRY               | Your company country of residence  |
| MERCHANTLOGOHTML              | HTML code for your logo |
| MERCHANTNAME                  | Your company full name |
| MERCHANTPHONESUPPORT          | Your customer service phone number |
| MERCHANTSUPPORT EMAIL         | Your customer service email address |
| MERCHANTTRANSACTIONID         | Your reference number |
| PAYLINK                       | Link to the MultiSafepay payment page for this transaction |
| PAYMENTMETHOD                 | Payment method used for this transaction |
| PHONE                         | Your company phone number given in your MultiSafepay Control |
| REFUNDDESTINATION             | Bank account number to receive the refund |
| REPORT EMAIL                  | Email address to receive report emails |
| SITENAME                      | Nname of your webshop given in your MultiSafepay Control |
| SITEURL                       | URL of your webshop given in your MultiSafepay Control |
| STATE                         | Province or state within the country |
| STATUS                        | Status of the transaction |
| SUBJECT                       | Subject of the email |
| TOTALAMOUNT                   | Total of the order |
| TRANSACTIONID                 | MultiSafepay PSP ID |
| TRANSCOMP EMAIL               | Email address to receive transaction completed mails |
| VARA                          | var1 from your transaction request |
| VARB                          | var2 from your transaction request |
| VARC                          | var3 from your transaction request |
| VATNUMBER                     | Your VAT number given in your MultiSafepay Control |
| ZIPCODE                       | Your company zip code |
