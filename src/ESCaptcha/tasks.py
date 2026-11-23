from dataclasses import dataclass, asdict
from typing import Optional, Dict, Any


@dataclass
class BaseTask:
    type: str

    def to_dict(self) -> Dict[str, Any]:
        return {k: v for k, v in asdict(self).items() if v is not None}


@dataclass
class ImageToTextTask(BaseTask):
    body: str

    def __init__(self, body: str):
        super().__init__('ImageToTextTask')
        self.body = body


@dataclass
class ReCaptchaV2TaskProxyLess(BaseTask):
    websiteURL: str
    websiteKey: str

    def __init__(self, url: str, site_key: str):
        super().__init__('ReCaptchaV2TaskProxyLess')
        self.websiteURL = url
        self.websiteKey = site_key


@dataclass
class ReCaptchaV3TaskProxyLess(BaseTask):
    websiteURL: str
    websiteKey: str
    pageAction: Optional[str] = None
    engine: Optional[str] = None

    def __init__(self, url: str, site_key: str, action: Optional[str] = None,
                 engine: Optional[str] = None):
        super().__init__('ReCaptchaV3TaskProxyLess')
        self.websiteURL = url
        self.websiteKey = site_key
        self.pageAction = action
        self.engine = engine


@dataclass
class HCaptchaTaskProxyLess(BaseTask):
    websiteURL: str
    websiteKey: str

    def __init__(self, url: str, site_key: str):
        super().__init__('HCaptchaTaskProxyLess')
        self.websiteURL = url
        self.websiteKey = site_key


@dataclass
class TurnstileTaskProxyLess(BaseTask):
    websiteURL: str
    websiteKey: str

    def __init__(self, url: str, site_key: str):
        super().__init__('TurnstileTaskProxyLess')
        self.websiteURL = url
        self.websiteKey = site_key


@dataclass
class FunCaptchaTaskProxyLess(BaseTask):
    websiteURL: str
    websitePublicKey: str

    def __init__(self, url: str, pub_key: str):
        super().__init__('FunCaptchaTaskProxyLess')
        self.websiteURL = url
        self.websitePublicKey = pub_key


@dataclass
class GeeTestTaskProxyLess(BaseTask):
    websiteURL: str
    gt: str
    challenge: str

    def __init__(self, url: str, gt: str, challenge: str):
        super().__init__('GeeTestTaskProxyLess')
        self.websiteURL = url
        self.gt = gt
        self.challenge = challenge


@dataclass
class GeeTestV4TaskProxyLess(BaseTask):
    websiteURL: str
    captchaId: str
    riskType: str
    voice: Optional[bool] = None
    proxy: Optional[str] = None

    def __init__(self, url: str, captcha_id: str, risk_type: str = 'slide',
                 voice: Optional[bool] = None, proxy: Optional[str] = None):
        super().__init__('GeeTestV4TaskProxyLess')
        self.websiteURL = url
        self.captchaId = captcha_id
        self.riskType = risk_type
        self.voice = voice
        self.proxy = proxy


@dataclass
class AmazonWafTaskProxyLess(BaseTask):
    websiteURL: str
    websiteKey: str
    proxy: Optional[str] = None

    def __init__(self, url: str, site_key: str, proxy: Optional[str] = None):
        super().__init__('AmazonWafTaskProxyLess')
        self.websiteURL = url
        self.websiteKey = site_key
        self.proxy = proxy


@dataclass
class TencentSliderTaskProxyLess(BaseTask):
    websiteURL: str
    appid: str
    proxy: Optional[str] = None

    def __init__(self, url: str, appid: str, proxy: Optional[str] = None):
        super().__init__('TencentSliderTaskProxyLess')
        self.websiteURL = url
        self.appid = appid
        self.proxy = proxy


@dataclass
class CloudflareJsdTaskProxyLess(BaseTask):
    websiteURL: str
    proxy: Optional[str] = None

    def __init__(self, url: str, proxy: Optional[str] = None):
        super().__init__('CloudflareJsdTaskProxyLess')
        self.websiteURL = url
        self.proxy = proxy


class TaskFactory:
    @staticmethod
    def serialize(task: BaseTask) -> dict:
        if not isinstance(task, BaseTask):
            raise TypeError('Task must inherit BaseTask')
        return task.to_dict()
