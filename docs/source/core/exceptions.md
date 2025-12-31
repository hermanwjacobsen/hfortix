# Exceptions

Documentation for the exception hierarchy.

```{note}
For complete exception documentation, see the [API Reference](/api-reference/exceptions.rst).
```

## Overview

All HFortix exceptions inherit from `FortinetError`.

## Exception Hierarchy

```text
FortinetError (Base exception)
├── APIError (Base for all API errors)
│   ├── HTTPError (Base for HTTP errors)
│   │   ├── BadRequestError (400)
│   │   ├── UnauthorizedError (401)
│   │   ├── ForbiddenError (403)
│   │   ├── ResourceNotFoundError (404)
│   │   ├── MethodNotAllowedError (405)
│   │   ├── RateLimitError (429)
│   │   └── ServerError (500+)
│   ├── DuplicateEntryError (FortiOS: object exists)
│   ├── EntryInUseError (FortiOS: object in use)
│   └── ValidationError (Invalid input)
├── ConnectionError (Network/connection issues)
├── TimeoutError (Request timeout)
└── ConfigurationError (Invalid configuration)
```

## See Also

- [API Reference - Exceptions](/api-reference/exceptions.rst)
- [Error Handling Guide](/fortios/user-guide/error-handling.md)
