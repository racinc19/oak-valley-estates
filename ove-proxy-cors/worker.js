const OVE_PROXY = 'https://ove-proxy.racinc19.workers.dev';
const CORS_HEADERS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type',
};

export default {
  async fetch(req, env, ctx) {
    if (req.method === 'OPTIONS') {
      return new Response(null, { headers: CORS_HEADERS });
    }
    const url = new URL(req.url);
    const target = OVE_PROXY + url.pathname + url.search;
    const opts = { method: req.method, headers: req.headers };
    if (req.method === 'POST' && req.body) {
      opts.body = req.body;
    }
    const res = await fetch(target, opts);
    const headers = new Headers(res.headers);
    Object.entries(CORS_HEADERS).forEach(([k, v]) => headers.set(k, v));
    return new Response(res.body, { status: res.status, headers });
  },
};
