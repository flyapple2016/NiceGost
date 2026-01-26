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
      "domain": [
        "ai.google.dev",
        "aistudio.google.com",
        "api.githubcopilot.com",
        "api.groq.com",
        "api.together.xyz",
        "bard.google.com",
        "challenges.cloudflare.com",
        "console.groq.com",
        "ping0.cc",
        "openwrt.ai",
        "copilot-proxy.githubusercontent.com",
        "gemini.google.com",
        "generativelanguage.googleapis.com",
        "sydney.bing.com"
      ],
      "domain_suffix": [
        "a.nel.cloudflare.com",
        "ai.com",
        "algolia.net",
        "arkoselabs.com",
        "auth0.com",
        "browser-intake-datadoghq.com",
        "chat.com",
        "chatgpt.com",
        "fastly.net",
        "featureassets.org",
        "featuregates.org",
        "gpt3sandbox.com",
        "gravatar.com",
        "grok.com",
        "grokipedia.com",
        "i0.wp.com",
        "immersivetranslate.com",
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
        "openaiapi-site.azureedge.net",
        "openaicom-api-bdcpf8c6d2e9atf6.z01.azurefd.net",
        "openaicom.imgix.net",
        "openaicomproductionae4b.blob.core.windows.net",
        "prodregistryv2.org",
        "production-openaicom-storage.azureedge.net",
        "segment.io",
        "sentry.io",
        "sora.com",
        "static.cloudflareinsights.com",
        "statsig.com",
        "statsigapi.net",
        "statsigcdn.com",
        "stripe.com",
        "x.ai",
        "withpersona.com"
      ],
      "domain_keyword": [
        "anthropic",
        "chatgpt",
        "claude",
        "openai"
      ],
      "ip_cidr": [
        "24.199.123.28/32",
        "64.23.132.171/32"
      ]
    }
  ]
}

AD_LOCAL_JSON = {
  "version": 3,
  "rules": [
    {
      "domain_suffix": [
        "couchcoaster.jp",
        "delivery.dmkt-sp.jp",
        "ehg-youtube.hitbox.com",
        "m-78.jp",
        "nichibenren.or.jp",
        "nicorette.co.kr",
        "stats.chinaz.com",
        "google-analytics.com",
        "googlesyndication.com",
        "ads.youtube.com",
        "api.mobula.sdk.duapps.com",
        "dianjoy.com",
        "jisucn.com",
        "c0563.com",
        "switchadhub.com",
        "123juzi.net",
        "leadboltmobile.net",
        "antivirus.baidu.com",
        "1kxun.mobi",
        "ads.feedly.com",
        "ads.twitter.com",
        "analytics.twitter.com",
        "scribe.twitter.com",
        "syndication.twitter.com",
        "feixin2.com",
        "flashtalking.com",
        "600ad.com",
        "cooguo.com",
        "ironsrc.com",
        "supersonic.com",
        "chengadx.com",
        "chartbeat.com",
        "celtra.com",
        "ads.linkedin.com",
        "pagead-tpc.l.google.com",
        "youtube.2cnt.net",
        "xiaozhen.com",
        "ad.wretch.cc",
        "mobgi.com",
        "innity.com",
        "media.cheshi.com",
        "dotmore.com.tw",
        "nexage.com",
        "analytics.yahoo.com",
        "gemini.yahoo.com",
        "wqmobile.com",
        "sezvc.com",
        "mobileadtrading.com",
        "ads.genieessp.com",
        "airpush.com",
        "inter1ads.com",
        "collector.githubapp.com",
        "vungle.com",
        "sysdig.com",
        "applovin.com",
        "adcolony.com",
        "revsci.net",
        "badad.googleplex.com",
        "admob.com",
        "doubleclick.com",
        "ads.google.com",
        "pagead.l.google.com",
        "clickzs.com",
        "juicyads.com",
        "c.algovid.com",
        "adxmi.com",
        "mzy2014.com",
        "sitemeter.com",
        "pubmatic.com",
        "istreamsche.com",
        "startappexchange.com",
        "appboy.com",
        "disqusads.com",
        "taboola.com",
        "adroll.com",
        "jimdo.com",
        "dkeyn.com",
        "bjxiaohua.com",
        "haoghost.com",
        "sanya1.com",
        "baoyatu.cc",
        "138lm.com",
        "ugvip.com",
        "maysunmedia.com",
        "staticxx.facebook.com",
        "domob.org",
        "mediaplex.com",
        "fastclick.com",
        "pyerc.com",
        "medialytics.io",
        "adsco.re",
        "voicefive.com",
        "scorecardresearch.com",
        "xyrkl.com",
        "vpon.com",
        "ads.gmodules.com",
        "googlecommerce.com",
        "doubleclick.net",
        "6dad.com",
        "pica-juicy.picacomic.com",
        "criteo.net",
        "cloudmobi.net",
        "chartboost.com",
        "ad-locus.com",
        "adlocus.com",
        "adfurikun.jp",
        "extend.tv",
        "smaato.com",
        "axonix.com",
        "ard.yahoo.co.jp",
        "yads.yahoo.co.jp",
        "zemanta.com",
        "propellerads.com",
        "adjust.io",
        "trafficmp.com",
        "glispa.com",
        "doubleverify.com",
        "pixel.wp.com",
        "bttrack.com",
        "ereg.adobe.com",
        "hl2rcv.adobe.com",
        "adobe-dns.adobe.com",
        "hlrcv.stage.adobe.com",
        "3dns-3.adobe.com",
        "activate-sjc0.adobe.com",
        "na2m-pr.licenses.adobe.com",
        "activate-sea.adobe.com",
        "leadboltads.net",
        "leadbolt.com",
        "jizzads.com",
        "lmlicenses.wip4.adobe.com",
        "sape.ru",
        "adhigh.net",
        "apsalar.com",
        "bayimob.com",
        "mobfox.com",
        "ad4game.com",
        "mookie1.com",
        "awempire.com",
        "inmobi.com",
        "ads.yahoo.com",
        "beap-bc.yahoo.com",
        "partnerads.ysm.yahoo.com",
        "ads.cdn.tvb.com",
        "mobadme.jp",
        "unimhk.com",
        "ad.unimhk.com",
        "tribalfusion.com",
        "bat.bing.com",
        "zedo.com",
        "sitescout.com",
        "clicktracks.com",
        "everesttech.net",
        "tellapart.com",
        "optimix.asia",
        "scupio.com",
        "2cnt.net",
        "ssl-youtube.2cnt.net",
        "bepolite.eu",
        "adition.com",
        "voiceads.com",
        "hyperpromote.com",
        "popads.net",
        "yengo.com",
        "criteo.com",
        "geo2.adobe.com",
        "e.nexac.com",
        "miidi.net",
        "cacafly.com",
        "addthis.com",
        "i-mobile.co.jp",
        "sharethis.com",
        "vidoomy.com",
        "focuscat.com",
        "adsrvr.org",
        "kochava.com",
        "applift.com",
        "meetrics.net",
        "dxpmedia.com",
        "somecoding.com",
        "atas.io",
        "dumedia.ru",
        "adhood.com",
        "adserver.unityads.unity3d.com",
        "mopub.com",
        "adservice.com",
        "adadvisor.net",
        "smartadserver.com",
        "ader.mobi",
        "bidvertiser.com",
        "gosquared.com",
        "adotmob.com",
        "mixpanel.com",
        "mobilityware.com",
        "a3p4.net",
        "amobee.com",
        "appier.net",
        "nend.net",
        "adform.net",
        "kmd365.com",
        "adbana.com",
        "adhouyi.com",
        "adirects.com",
        "drdwy.com",
        "tansuotv.com",
        "sycbbs.com",
        "zcdsp.com",
        "fastapi.net",
        "tapjoy.com",
        "quantserve.com",
        "dl-vip.pcfaster.baidu.co.th",
        "o2omobi.com",
        "datouniao.com",
        "admaji.com",
        "microad-cn.com",
        "intentiq.com",
        "publicidad.tv",
        "similarweb.com",
        "zhjfad.com",
        "stickyadstv.com",
        "buysellads.com",
        "steelhousemedia.com",
        "lm.licenses.adobe.com",
        "powerlinks.com",
        "localytics.com",
        "smartnews-ads.com",
        "moatads.com",
        "pubnub.com",
        "iskyworker.com",
        "segment.com",
        "channeladvisor.com",
        "uberads.com",
        "iperceptions.com",
        "adsunion.com",
        "bloggerads.net",
        "amazon-adsystem.com",
        "viglink.com",
        "leadboltapps.net",
        "tapjoyads.com",
        "appsflyer.com",
        "activate.adobe.com",
        "btyou.com",
        "ad-brix.com",
        "ad-stir.com",
        "na1r.services.adobe.com",
        "hitslink.com",
        "inner-active.mobi",
        "pixels.asia",
        "histats.com",
        "startapp.com",
        "applifier.com",
        "publicidad.net",
        "youtube.112.2o7.net",
        "connexity.net",
        "krux.net",
        "madmini.com",
        "ueadlian.com",
        "ylunion.com",
        "mgid.com",
        "quantcount.com",
        "branch.io",
        "js-apac-ss.ysm.yahoo.com",
        "analytics.query.yahoo.com",
        "log.outbrain.com",
        "trafficjunky.com",
        "trafficjunky.net",
        "admedia.com",
        "ws.progrss.yahoo.com",
        "brucelead.com",
        "liveadvert.com",
        "inmobi.net",
        "revdepo.com",
        "1.letvlive.com",
        "2.letvlive.com",
        "rubiconproject.com",
        "acuityplatform.com",
        "sitetag.us",
        "92x.tumblr.com",
        "its-dori.tumblr.com",
        "coremetrics.com",
        "mathtag.com",
        "eqads.com",
        "adap.tv",
        "adss.yahoo.com",
        "instabug.com",
        "bidtheatre.com",
        "boxshows.com",
        "heyzap.com",
        "advertising.com",
        "overture.com",
        "adtech.de",
        "adtechjp.com",
        "adtechus.com",
        "flurry.com",
        "millennialmedia.com",
        "mydas.mobi",
        "p3p.yahoo.com",
        "mng-ads.com",
        "adv.sec.intl.miui.com",
        "51taifu.com",
        "adriver.ru",
        "exoclick.com",
        "yadro.ru",
        "marketgid.com",
        "thoughtleadr.com",
        "am15.net",
        "sponsorpay.com",
        "moogos.com",
        "marketo.com",
        "statcounter.com",
        "ad-channel.wikawika.xyz",
        "ad-display.wikawika.xyz",
        "stats.developingperspective.com",
        "effectivemeasure.net",
        "cpx24.com",
        "xtgreat.com",
        "guohead.com",
        "vamaker.com",
        "coinhive.com",
        "adinfuse.com",
        "clickadu.com",
        "plugrush.com",
        "pingdom.net",
        "ad-delivery.net",
        "beintoo.com",
        "blismedia.com",
        "casalemedia.com",
        "ujian.cc",
        "eyereturn.com",
        "ad.duapps.com",
        "hosting.miarroba.info",
        "effectivemeasure.com",
        "hot-mob.com",
        "azabu-u.ac.jp",
        "edigitalsurvey.com"
      ]
    }
  ]
}

def download(url):
    try:
        with urllib.request.urlopen(url) as resp:
            return json.load(resp)
    except Exception as e:
        return None

def parse_blocklist_txt(url):
    domains = set()
    try:
        with urllib.request.urlopen(url) as resp:
            content = resp.read().decode('utf-8', errors='ignore')
            for line in content.splitlines():
                line = line.strip()
                if not line or line.startswith(('!', '[', '#')):
                    continue
                if line.startswith('*://*.') and line.endswith('/*'):
                    domain = line[6:-2]
                    domains.add(domain)
                elif line.startswith('||') and line.endswith('^'):

                    domain = line[2:-1]
                    domains.add(domain)
                elif line.startswith('||') and line.endswith('/'):
                    domain = line[2:-1]
                    domains.add(domain)
                elif '.' in line and not line.startswith(('http', '*', '|', '!')):
                    domains.add(line)
    except Exception as e:
    return sorted(domains)

def get_ad_extra_domains():
    BLOCKLIST_TXT_URL = "https://raw.githubusercontent.com/obgnail/chinese-internet-is-dead/master/blocklist.txt"
    extra_suffix = parse_blocklist_txt(BLOCKLIST_TXT_URL)
    return extra_suffix

def merge_rules(urls, extra_local_data=None, extra_domains=None):
    merged = {
        "domain_keyword": set(),
        "domain_suffix": set(),
        "domain": set(),
        "ip_cidr": set(),
    }
    
    for url in urls:
        data = download(url)
        if data is None:
            continue
        for rule in data.get("rules", []):
            for key in merged:
                if key in rule:
                    merged[key].update(rule[key])
    
    if extra_local_data:
        for rule in extra_local_data.get("rules", []):
            for key in merged:
                if key in rule:
                    merged[key].update(rule[key])
    
    if extra_domains:
        merged["domain_suffix"].update(extra_domains)
    
    result = {"version": 3, "rules": [{}]}
    obj = result["rules"][0]
    for key in merged:
        items = sorted(merged[key])
        if items:
            obj[key] = items
            
    return result

if __name__ == "__main__":
    extra_ad_domains = get_ad_extra_domains()
    ads_merged = merge_rules(AD_URLS, extra_local_data=AD_LOCAL_JSON, extra_domains=extra_ad_domains)
    
    with open("ads.json", "w", encoding="utf-8") as f:
        json.dump(ads_merged, f, ensure_ascii=False, indent=2)
    
    list_merged = merge_rules(LIST_URLS, extra_local_data=AI_LOCAL_JSON)
    with open("list.json", "w", encoding="utf-8") as f:
        json.dump(list_merged, f, ensure_ascii=False, indent=2)
    
    print("===ads===")
    for k, v in ads_merged["rules"][0].items():
        print(f" {k}: {len(v)} ")
    
    print("\n===list===")
    for k, v in list_merged["rules"][0].items():
        print(f" {k}: {len(v)} ")
