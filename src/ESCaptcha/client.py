import os
import time
import requests
from .exceptions import SolverClientError

class SolverClient:
    """Client that follows CapSolver's createTask/getTaskResult API format."""
    def __init__(self, api_key=None, base_url=None):
        self.api_key = api_key or os.getenv('SOLVER_API_KEY')
        self.base_url = (base_url or os.getenv('SOLVER_BASE_URL') or '').rstrip('/')
        if not self.api_key:
            raise SolverClientError('Missing API key. Set SOLVER_API_KEY or provide api_key.')
        if not self.base_url:
            raise SolverClientError('Missing base URL. Set SOLVER_BASE_URL or provide base_url.')

    def _post(self, endpoint: str, data: dict, timeout: int = 15):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        payload = {'clientKey': self.api_key, **data}
        try:
            resp = requests.post(url, json=payload, timeout=timeout)
        except Exception as e:
            raise SolverClientError(f'Request failed: {e}')
        try:
            j = resp.json()
        except Exception:
            raise SolverClientError(f'Non-JSON response: {resp.status_code} {resp.text}')
        if j.get('errorId', 0) != 0:
            raise SolverClientError(f"API error: {j.get('errorDescription')}")
        return j

    def create_task(self, task: dict) -> str:
        result = self._post('createTask', {'task': task})
        return result['taskId']

    def get_task_result(self, task_id: str, timeout: int = 120, interval: float = 1.0):
        elapsed = 0.0
        while elapsed < timeout:
            result = self._post('getTaskResult', {'taskId': task_id})
            status = result.get('status')
            if status == 'ready':
                return result.get('solution')
            if status == 'failed':
                solution = result.get('solution') or {}
                detail = solution.get('error') or solution.get('errorDescription') or 'Task failed'
                raise SolverClientError(detail)
            time.sleep(interval)
            elapsed += interval
        raise SolverClientError('Timeout waiting for task result')
