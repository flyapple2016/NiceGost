import json
import urllib.request

AD_URLS = [
    "https://raw.githubusercontent.com/KaringX/karing-ruleset/sing/ACL4SSR/BanEasyListChina.json",
    "https://raw.githubusercontent.com/KaringX/karing-ruleset/sing/ACL4SSR/BanAD.json",
    "https://raw.githubusercontent.com/KaringX/karing-ruleset/sing/ACL4SSR/BanProgramAD.json",
    "https://raw.githubusercontent.com/KaringX/karing-ruleset/sing/ACL4SSR/BanADCompany.json",
    "https://raw.githubusercontent.com/217heidai/adblockfilters/main/rules/adblocksingboxlite.json",
    "https://raw.githubusercontent.com/qq5460168/666/master/Singbox.json",
]

LIST_URLS = [
    "https://raw.githubusercontent.com/KaringX/karing-ruleset/sing/ACL4SSR/ProxyGFWlist.json",
    "https://raw.githubusercontent.com/KaringX/karing-ruleset/sing/ACL4SSR/Telegram.json",
    "https://raw.githubusercontent.com/KaringX/karing-ruleset/sing/ACL4SSR/Ruleset/AI.json",
    "https://raw.githubusercontent.com/KaringX/karing-ruleset/sing/ACL4SSR/Ruleset/Github.json",
    "https://raw.githubusercontent.com/KaringX/karing-ruleset/sing/ACL4SSR/Ruleset/Spotify.json",
    "https://raw.githubusercontent.com/KaringX/karing-ruleset/sing/ACL4SSR/Ruleset/TikTok.json",
    "https://raw.githubusercontent.com/KaringX/karing-ruleset/sing/ACL4SSR/Ruleset/YouTube.json",
]

AI_LOCAL_JSON = {
    "version": 3,
    "rules": [
        {
            "domain_keyword": [
                "anthropic",
                "claude",
                "openai"
            ],
            "domain": [
                "ai.google.dev",
                "aistudio.google.com",
                "api.githubcopilot.com",
                "api.groq.com",
                "api.together.xyz",
                "bard.google.com",
                "console.groq.com",
                "copilot-proxy.githubusercontent.com",
                "gemini.google.com",
                "generativelanguage.googleapis.com",
                "sydney.bing.com"
            ],
            "domain_suffix": [
                "ai.com",
                "algolia.net",
                "api.statsig.com",
                "auth0.com",
                "browser-intake-datadoghq.com",
                "cdn.auth0.com",
                "chat.com",
                "chat.openai.com.cdn.cloudflare.net",
                "chatgpt.com",
                "chatgpt.livekit.cloud",
                "client-api.arkoselabs.com",
                "events.statsigapi.net",
                "fastly.net",
                "featuregates.org",
                "gpt3sandbox.com",
                "gravatar.com",
                "host.livekit.cloud",
                "i0.wp.com",
                "identrust.com",
                "intercom.io",
                "intercomcdn.com",
                "jsdelivr.net",
                "launchdarkly.com",
                "livekit.cloud",
                "oaistatic.com",
                "oaiusercontent.com",
                "observeit.net",
                "openai.com",
                "openai.com.cdn.cloudflare.net",
                "openai-api.arkoselabs.com",
                "openaiapi-site.azureedge.net",
                "openaicom.imgix.net",
                "openaicom-api-bdcpf8c6d2e9atf6.z01.azurefd.net",
                "openaicomproductionae4b.blob.core.windows.net",
                "production-openaicom-storage.azureedge.net",
                "segment.io",
                "sentry.io",
                "sora.com",
                "static.cloudflareinsights.com",
                "statsigapi.net",
                "stripe.com",
                "turn.livekit.cloud",
                "livekit.cloud"
            ]
        }
    ]
}

def download(url):
    with urllib.request.urlopen(url) as resp:
        return json.load(resp)

def get_ai_data():
    return AI_LOCAL_JSON

def merge_rules(urls, extra_local_data=None):
    merged = {
        "domain_keyword": set(),
        "domain_suffix": set(),
        "domain": set(),
        "ip_cidr": set(),
    }

    for url in urls:
        try:
            data = download(url)
            for rule in data.get("rules", []):
                for key in merged:
                    if key in rule:
                        merged[key].update(rule[key])
        except Exception as e:
            print(f" {url}: {e}")
            continue

    if extra_local_data:
        try:
            for rule in extra_local_data.get("rules", []):
                for key in merged:
                    if key in rule:
                        merged[key].update(rule[key])
        except Exception as e:
            print(f"{e}")

    result = {"version": 3, "rules": [{}]}
    obj = result["rules"][0]
    for key in merged:
        items = sorted(merged[key])
        if items:
            obj[key] = items
    return result

if __name__ == "__main__":
    ads_merged = merge_rules(AD_URLS)
    with open("ads.json", "w", encoding="utf-8") as f:
        json.dump(ads_merged, f, ensure_ascii=False, indent=2)

    list_merged = merge_rules(LIST_URLS, extra_local_data=get_ai_data())
    with open("list.json", "w", encoding="utf-8") as f:
        json.dump(list_merged, f, ensure_ascii=False, indent=2)

    print("======")
    for k, v in ads_merged["rules"][0].items():
        print(f" {k}: {len(v)} ")

    print("\n=== ===")
    for k, v in list_merged["rules"][0].items():
        print(f" {k}: {len(v)} ")
