import json
import urllib.request

AD_URLS = [
    "https://raw.githubusercontent.com/KaringX/karing-ruleset/sing/ACL4SSR/BanEasyListChina.json",
    "https://raw.githubusercontent.com/KaringX/karing-ruleset/sing/ACL4SSR/BanAD.json",
    "https://raw.githubusercontent.com/KaringX/karing-ruleset/sing/ACL4SSR/BanProgramAD.json",
    "https://raw.githubusercontent.com/KaringX/karing-ruleset/sing/ACL4SSR/BanADCompany.json",
    "https://raw.githubusercontent.com/217heidai/adblockfilters/main/rules/adblocksingbox.json",
]

LIST_URLS = [
    "https://raw.githubusercontent.com/KaringX/karing-ruleset/sing/ACL4SSR/ProxyGFWlist.json",
    "https://raw.githubusercontent.com/KaringX/karing-ruleset/sing/ACL4SSR/Telegram.json",
]

def download(url):
    with urllib.request.urlopen(url) as resp:
        return json.load(resp)

def merge_rules(urls):
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
            continue

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
    list_merged = merge_rules(LIST_URLS)
    with open("list.json", "w", encoding="utf-8") as f:
        json.dump(list_merged, f, ensure_ascii=False, indent=2)

    for k, v in ads_merged["rules"][0].items():
        print(f"  {k}: {len(v)} ")

    for k, v in list_merged["rules"][0].items():
        print(f"  {k}: {len(v)} ")
