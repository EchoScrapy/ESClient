# ESClient

`ESCaptcha` is the Python client package for EchoSolutions. It provides CapSolver-style task creation and result polling for the solvers supported by the server.

Server repository: [EchoScrapy/EchoSolutions](https://github.com/EchoScrapy/EchoSolutions)

## Installation

```bash
python -m pip install git+https://github.com/EchoScrapy/ESClient.git
```

For local development:

```bash
python -m pip install .
```

## Usage

Set the client key and server URL, then create a task and poll for its solution:

```python
import os
from ESCaptcha.client import SolverClient
from ESCaptcha.tasks import ReCaptchaV3TaskProxyLess

client = SolverClient(
    api_key=os.environ["SOLVER_API_KEY"],
    base_url=os.environ.get("SOLVER_BASE_URL", "http://127.0.0.1:8000"),
)

task = ReCaptchaV3TaskProxyLess(
    url="https://example.com/page",
    site_key="SITE_KEY",
    action="submit",
)

task_id = client.create_task(task.to_dict())
solution = client.get_task_result(task_id)
print(solution["gRecaptchaResponse"])
```

Task classes are available in `ESCaptcha.tasks` for reCAPTCHA v3, ImageToText, AWS WAF, Tencent Slider, Geetest v3/v4, Cloudflare JSD, and FriendlyCaptcha v1/v2. Use `FriendlyCaptchaV1TaskProxyLess` for the v1 `frc-captcha-solution` field and `FriendlyCaptchaTaskProxyLess` for v2 `frc-captcha-response`. Both return `solution["token"]`. The server determines which task types are supported.

`get_task_result()` raises `SolverClientError` when the server reports a failed task instead of waiting until the polling timeout.
