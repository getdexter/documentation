---
title: Jira
description: Integrating Jira with Dexter.
---

Dexter uses the [Jira Cloud API] to integrate with Jira.

In order to setup the integration, you'll need the following data:

- Account name
- Account email
- API Token

### Account name

You'll find the account name in the URL you use for Jira:

```
https://<account name>.atlassian.net
```

### Account email

The agent email is the same email you use to login to Jira and to create the API Token.

### API Token

Dexter uses basic auth to authenticate with the Jira Cloud API. You can create an API token from your Atlassian account:

1. Log in to https://id.atlassian.com/manage-profile/security/api-tokens
1. Click Create API token
1. From the dialog that appears, enter a memorable and concise Label for your token and click Create

[Jira Cloud API]: https://developer.atlassian.com/cloud/jira/software/rest/intro/#introduction
