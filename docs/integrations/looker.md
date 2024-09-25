---
title: Looker
description: Integrating Looker with Dexter.
---

Dexter uses the [Looker API] to integrate with Looker.

In order to setup the integration, you'll need the following data:

- Looker API path and port
- API credentials

### Looker API path and port

Your Looker admin can specify an API path by entering it in the API Host URL field on the Admin > API page in the following format:

```
https://<instance_name>.cloud.looker.com
```

Your Looker admin may also use the API Host URL field to assign an API path that is different from your Looker server machine name. This is common when your Looker installation is behind a load balancer, for example. In this case, contact your Looker admin for your API path.

If your Looker admin has not specified the API Host URL field, Looker uses the default API path. For Looker instances hosted on Google Cloud, Microsoft Azure, and instances hosted on Amazon Web Service (AWS) that were created on or after 07/07/2020, the default Looker API path uses port 443. For Looker instances hosted on AWS that were created before 07/07/2020, the default Looker API path uses port 19999. The default API URL is in the following format:

```
https://<instance_name>.cloud.looker.com:<port>
```

See [Getting started with the Looker API] for more information.

### Authentication

Dexter authenticates with Looker using API credentials (client ID and client secret). You can create API credentials on the [Users page] in the Admin section of your Looker instance. If you're not a Looker admin, ask your Looker admin to create the API credentials for you.

API credentials are always bound to a Looker user account. API requests execute "as" the user associated with the API credentials. Calls to the API will only return data that the user is allowed to see, and modify only what the user is allowed to modify. You may create a user dedicated to the Dexter integration or use an existing user.

See [Looker API authentication] for more information.

[Looker API]: https://cloud.google.com/looker/docs/api-intro
[Looker API authentication]: https://cloud.google.com/looker/docs/api-auth
[Getting started with the Looker API]: https://cloud.google.com/looker/docs/api-getting-started#looker_api_path_and_port
[Users page]: https://cloud.google.com/looker/docs/admin-panel-users-users
