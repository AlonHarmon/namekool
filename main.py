from prometheus_client import Counter
from nameko_prometheus import PromethusMetrics

from nameko.web.handlers import http

entered_messages = Counter('total_enterd_messgaes', 'total number of entered messages')
out_messages = Counter('total_out_messgaes', 'total number of out messages')


class Service:
    metrics = PromethusMetrics()

    @http('GET', '/metrics')
    def serve_metrics(self, request):
        return self.metrics.expose_metrics(request)
