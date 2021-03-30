---
title : Add a bank account
layout : single
tags : hidden
---

## Introduction

Use seven request to perform actions on bank account details of Merchant Accounts affiliated to your Partner Account:
1. [Add bank account](#add-bank-account): Add a bank account to a Merchant Account
2. [List bank accounts](#list-bank-accounts): Retrieve a list of all bank accounts associated to a Merchant Account
3. [Get bank account](#get-bank-account): Retrieve a single bank account associated to a Merchant Account
5. [Create payment link](#create-payment-link): Create a payment link, to verify a bank account
6. [Add bank statement](#add-bank-statement): Add a bank statement, to verify a bank account
7. [List bank statements](#list-bank-statements): Retrieve a list of all bank statements associated to a bank account
8. [Get bank statement](#get-bank-statement): Retrieve a single bank statement


### The process

The requests above can be split into two steps:

- **Add bank accounts**: Use the first three requests to add and retrieve bank accounts associated to a Merchant Account. 
- **Verify bank accounts**: Use the last four requests to verify bank accounts. You can choose to verify through a payment link or by supplying a bank statement.

## Authentication
All seven bank account requests require a Partner Account API key. This is not the same as a [website API key](/tools/multisafepay-control/get-your-api-key/). Ask your Partner Manager for more information.

All URLs on this page are directed to our test API. To use the live API, change the subdomain `testapi` to `api` and use the according API key.

## Add bank account 

`METHOD` `URL`

Description in a couple sentences max.

### Path parameters
|Parameter|Description|
|-----|------|
|  |  |

### Query parameters
|Key|Description|
|-----|------|
|  |  |

{{< collapse title="Sample request" h3="." >}}
```
???
```
{{< /collapse >}}

{{< collapse title="Sample response" h3="." >}}
```
???
```
{{< /collapse >}}

---

## List bank accounts

`METHOD` `URL`

Description in a couple sentences max.

### Path parameters
|Parameter|Description|
|-----|------|
|  |  |

### Query parameters
|Key|Description|
|-----|------|
|  |  |

{{< collapse title="Sample request" h3="." >}}
```
???
```
{{< /collapse >}}

{{< collapse title="Sample response" h3="." >}}
```
???
```
{{< /collapse >}}

---

## Get bank account

`METHOD` `URL`

Description in a couple sentences max.

### Path parameters
|Parameter|Description|
|-----|------|
|  |  |

### Query parameters
|Key|Description|
|-----|------|
|  |  |

{{< collapse title="Sample request" h3="." >}}
```
???
```
{{< /collapse >}}

{{< collapse title="Sample response" h3="." >}}
```
???
```
{{< /collapse >}}

---

## Create payment link

`METHOD` `URL`

Description in a couple sentences max.

### Path parameters
|Parameter|Description|
|-----|------|
|  |  |

### Query parameters
|Key|Description|
|-----|------|
|  |  |

{{< collapse title="Sample request" h3="." >}}
```
???
```
{{< /collapse >}}

{{< collapse title="Sample response" h3="." >}}
```
???
```
{{< /collapse >}}

---

## Add bank statement

`METHOD` `URL`

Description in a couple sentences max.

### Path parameters
|Parameter|Description|
|-----|------|
|  |  |

### Query parameters
|Key|Description|
|-----|------|
|  |  |

{{< collapse title="Sample request" h3="." >}}
```
???
```
{{< /collapse >}}

{{< collapse title="Sample response" h3="." >}}
```
???
```
{{< /collapse >}}

---

## List bank statements

`METHOD` `URL`

Description in a couple sentences max.

### Path parameters
|Parameter|Description|
|-----|------|
|  |  |

### Query parameters
|Key|Description|
|-----|------|
|  |  |

{{< collapse title="Sample request" h3="." >}}
```
???
```
{{< /collapse >}}

{{< collapse title="Sample response" h3="." >}}
```
???
```
{{< /collapse >}}

---

## Get bank statement

`METHOD` `URL`

Description in a couple sentences max.

### Path parameters
|Parameter|Description|
|-----|------|
|  |  |

### Query parameters
|Key|Description|
|-----|------|
|  |  |

{{< collapse title="Sample request" h3="." >}}
```
???
```
{{< /collapse >}}

{{< collapse title="Sample response" h3="." >}}
```
???
```
{{< /collapse >}}

---

## Next steps
Now that you have created a Merchant Account and added one or multiple bank accounts, you can add UBOs and websites, using the unique Merchant Account `id` .

{{< two-buttons

href-1="/tools/api-onboarding/create-account" header-1="Previous" text-1="Create a Merchant Account" img-1="/svgs/arrow-thin-left.svg" alt-1="Left arrow" 

href-2="/tools/api-onboarding/add-ubo" header-2="Next" text-2="Add UBO details" img-2="/svgs/arrow-thin-right.svg" alt-2="Right arrow" >}}
